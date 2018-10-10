""" Cisco_IOS_XR_ipv4_dhcpd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-dhcpd\: DHCP IPV4 configuration

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class BaseAction(Enum):
    """
    BaseAction (Enum Class)

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
    Dhcpv4AuthUsername (Enum Class)

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
    Dhcpv4LimitLease1 (Enum Class)

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
    Dhcpv4MatchOption (Enum Class)

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
    Ipv4dhcpdBroadcastFlagPolicy (Enum Class)

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
    Ipv4dhcpdFmt (Enum Class)

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
    Ipv4dhcpdFmtSpecifier (Enum Class)

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

    .. data:: l3_interface = 9

    	L3 Interface

    .. data:: host_name = 10

    	Hostname

    """

    physical_chassis = Enum.YLeaf(1, "physical-chassis")

    physical_slot = Enum.YLeaf(2, "physical-slot")

    physical_sub_slot = Enum.YLeaf(3, "physical-sub-slot")

    physical_port = Enum.YLeaf(4, "physical-port")

    physical_sub_port = Enum.YLeaf(5, "physical-sub-port")

    inner_vlan_id = Enum.YLeaf(6, "inner-vlan-id")

    outer_vlan_id = Enum.YLeaf(7, "outer-vlan-id")

    l2_interface = Enum.YLeaf(8, "l2-interface")

    l3_interface = Enum.YLeaf(9, "l3-interface")

    host_name = Enum.YLeaf(10, "host-name")


class Ipv4dhcpdGiaddrPolicy(Enum):
    """
    Ipv4dhcpdGiaddrPolicy (Enum Class)

    Ipv4dhcpd giaddr policy

    .. data:: giaddr_policy_keep = 0

    	Giaddr Policy Keep

    """

    giaddr_policy_keep = Enum.YLeaf(0, "giaddr-policy-keep")


class Ipv4dhcpdLayer(Enum):
    """
    Ipv4dhcpdLayer (Enum Class)

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
    Ipv4dhcpdMode (Enum Class)

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


class Ipv4dhcpdRelayGiaddrPolicy(Enum):
    """
    Ipv4dhcpdRelayGiaddrPolicy (Enum Class)

    Ipv4dhcpd relay giaddr policy

    .. data:: replace = 1

    	Replace

    .. data:: drop = 2

    	Drop

    """

    replace = Enum.YLeaf(1, "replace")

    drop = Enum.YLeaf(2, "drop")


class Ipv4dhcpdRelayInfoOptionAuthenticate(Enum):
    """
    Ipv4dhcpdRelayInfoOptionAuthenticate (Enum Class)

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
    Ipv4dhcpdRelayInfoOptionPolicy (Enum Class)

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
    Ipv4dhcpdRelayInfoOptionvpnMode (Enum Class)

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
    LeaseLimitValue (Enum Class)

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
    MacMismatchAction (Enum Class)

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
    Matchaction (Enum Class)

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
    Matchoption (Enum Class)

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
    Policy (Enum Class)

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
    ProxyAction (Enum Class)

    Proxy action

    .. data:: allow = 0

    	Allow vendor specific DHCP Discover

    .. data:: drop = 1

    	Drop vendor specific DHCP Discover

    .. data:: relay = 2

    	Relay vendor-id specific DHCP packets unaltered

    """

    allow = Enum.YLeaf(0, "allow")

    drop = Enum.YLeaf(1, "drop")

    relay = Enum.YLeaf(2, "relay")



class Ipv4Dhcpd(Entity):
    """
    DHCP IPV4 configuration
    
    .. attribute:: vrfs
    
    	VRF Table
    	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs>`
    
    .. attribute:: profiles
    
    	DHCP IPV4 Profile Table
    	**type**\:  :py:class:`Profiles <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles>`
    
    .. attribute:: database
    
    	Enable DHCP binding database storage to file system
    	**type**\:  :py:class:`Database <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Database>`
    
    .. attribute:: interfaces
    
    	DHCP IPV4 Interface Table
    	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces>`
    
    .. attribute:: duplicate_mac_allowed
    
    	Allow Duplicate MAC Address
    	**type**\:  :py:class:`DuplicateMacAllowed <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.DuplicateMacAllowed>`
    
    	**presence node**\: True
    
    .. attribute:: rate_limit
    
    	Rate limit ingress packets
    	**type**\:  :py:class:`RateLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.RateLimit>`
    
    .. attribute:: enable
    
    	DHCP IPV4 configuration
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    	**mandatory**\: True
    
    .. attribute:: outer_cos
    
    	Configure outer cos values for dhcp packets
    	**type**\: int
    
    	**range:** 0..7
    
    .. attribute:: allow_client_id_change
    
    	For BNG session, allow client id change for a client MAC
    	**type**\: :py:class:`Empty<ydk.types.Empty>`
    
    .. attribute:: inner_cos
    
    	Configure inner cos values for dhcp packets
    	**type**\: int
    
    	**range:** 0..7
    
    

    This class is a :ref:`presence class<presence-class>`

    """

    _prefix = 'ipv4-dhcpd-cfg'
    _revision = '2017-09-30'

    def __init__(self):
        super(Ipv4Dhcpd, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-dhcpd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-dhcpd-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("vrfs", ("vrfs", Ipv4Dhcpd.Vrfs)), ("profiles", ("profiles", Ipv4Dhcpd.Profiles)), ("database", ("database", Ipv4Dhcpd.Database)), ("interfaces", ("interfaces", Ipv4Dhcpd.Interfaces)), ("duplicate-mac-allowed", ("duplicate_mac_allowed", Ipv4Dhcpd.DuplicateMacAllowed)), ("rate-limit", ("rate_limit", Ipv4Dhcpd.RateLimit))])
        self.is_presence_container = True
        self._leafs = OrderedDict([
            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
            ('outer_cos', (YLeaf(YType.uint32, 'outer-cos'), ['int'])),
            ('allow_client_id_change', (YLeaf(YType.empty, 'allow-client-id-change'), ['Empty'])),
            ('inner_cos', (YLeaf(YType.uint32, 'inner-cos'), ['int'])),
        ])
        self.enable = None
        self.outer_cos = None
        self.allow_client_id_change = None
        self.inner_cos = None

        self.vrfs = Ipv4Dhcpd.Vrfs()
        self.vrfs.parent = self
        self._children_name_map["vrfs"] = "vrfs"

        self.profiles = Ipv4Dhcpd.Profiles()
        self.profiles.parent = self
        self._children_name_map["profiles"] = "profiles"

        self.database = Ipv4Dhcpd.Database()
        self.database.parent = self
        self._children_name_map["database"] = "database"

        self.interfaces = Ipv4Dhcpd.Interfaces()
        self.interfaces.parent = self
        self._children_name_map["interfaces"] = "interfaces"

        self.duplicate_mac_allowed = None
        self._children_name_map["duplicate_mac_allowed"] = "duplicate-mac-allowed"

        self.rate_limit = Ipv4Dhcpd.RateLimit()
        self.rate_limit.parent = self
        self._children_name_map["rate_limit"] = "rate-limit"
        self._segment_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(Ipv4Dhcpd, ['enable', 'outer_cos', 'allow_client_id_change', 'inner_cos'], name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table
        	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Vrfs.Vrf))])
            self._leafs = OrderedDict()

            self.vrf = YList(self)
            self._segment_path = lambda: "vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Vrfs, [], name, value)


        class Vrf(Entity):
            """
            VRF table
            
            .. attribute:: vrf_name  (key)
            
            	VRF Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf.Profile>`
            
            	**presence node**\: True
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Ipv4Dhcpd.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf_name']
                self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Vrfs.Vrf.Profile))])
                self._leafs = OrderedDict([
                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                ])
                self.vrf_name = None

                self.profile = None
                self._children_name_map["profile"] = "profile"
                self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/vrfs/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Vrfs.Vrf, ['vrf_name'], name, value)


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: vrf_profile_name
                
                	Profile name
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: mode
                
                	Dhcp mode
                	**type**\:  :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Vrfs.Vrf.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('vrf_profile_name', (YLeaf(YType.str, 'vrf-profile-name'), ['str'])),
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdMode', '')])),
                    ])
                    self.vrf_profile_name = None
                    self.mode = None
                    self._segment_path = lambda: "profile"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Vrfs.Vrf.Profile, ['vrf_profile_name', 'mode'], name, value)


    class Profiles(Entity):
        """
        DHCP IPV4 Profile Table
        
        .. attribute:: profile
        
        	DHCP IPV4 Profile
        	**type**\: list of  		 :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("profile", ("profile", Ipv4Dhcpd.Profiles.Profile))])
            self._leafs = OrderedDict()

            self.profile = YList(self)
            self._segment_path = lambda: "profiles"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Profiles, [], name, value)


        class Profile(Entity):
            """
            DHCP IPV4 Profile
            
            .. attribute:: profile_name  (key)
            
            	Profile Name
            	**type**\: str
            
            	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
            
            .. attribute:: modes
            
            	DHCP IPV4 Profile modes
            	**type**\:  :py:class:`Modes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Ipv4Dhcpd.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['profile_name']
                self._child_classes = OrderedDict([("modes", ("modes", Ipv4Dhcpd.Profiles.Profile.Modes))])
                self._leafs = OrderedDict([
                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                ])
                self.profile_name = None

                self.modes = Ipv4Dhcpd.Profiles.Profile.Modes()
                self.modes.parent = self
                self._children_name_map["modes"] = "modes"
                self._segment_path = lambda: "profile" + "[profile-name='" + str(self.profile_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/profiles/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile, ['profile_name'], name, value)


            class Modes(Entity):
                """
                DHCP IPV4 Profile modes
                
                .. attribute:: mode
                
                	DHCP IPV4 Profile mode
                	**type**\: list of  		 :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Profiles.Profile.Modes, self).__init__()

                    self.yang_name = "modes"
                    self.yang_parent_name = "profile"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("mode", ("mode", Ipv4Dhcpd.Profiles.Profile.Modes.Mode))])
                    self._leafs = OrderedDict()

                    self.mode = YList(self)
                    self._segment_path = lambda: "modes"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes, [], name, value)


                class Mode(Entity):
                    """
                    DHCP IPV4 Profile mode
                    
                    .. attribute:: mode  (key)
                    
                    	DHCP IPV4 Profile mode
                    	**type**\:  :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                    
                    .. attribute:: snoop
                    
                    	DHCP Snoop profile
                    	**type**\:  :py:class:`Snoop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop>`
                    
                    .. attribute:: base
                    
                    	DHCP Base Profile
                    	**type**\:  :py:class:`Base <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: server
                    
                    	DHCP Server profile
                    	**type**\:  :py:class:`Server <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: relay
                    
                    	DHCP Relay profile
                    	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay>`
                    
                    .. attribute:: proxy
                    
                    	DHCP proxy profile
                    	**type**\:  :py:class:`Proxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: enable
                    
                    	Enable the DHCP IPV4 Profile mode
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, self).__init__()

                        self.yang_name = "mode"
                        self.yang_parent_name = "modes"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['mode']
                        self._child_classes = OrderedDict([("snoop", ("snoop", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop)), ("base", ("base", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base)), ("server", ("server", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server)), ("relay", ("relay", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay)), ("proxy", ("proxy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy))])
                        self._leafs = OrderedDict([
                            ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdMode', '')])),
                            ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                        ])
                        self.mode = None
                        self.enable = None

                        self.snoop = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop()
                        self.snoop.parent = self
                        self._children_name_map["snoop"] = "snoop"

                        self.base = None
                        self._children_name_map["base"] = "base"

                        self.server = None
                        self._children_name_map["server"] = "server"

                        self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay()
                        self.relay.parent = self
                        self._children_name_map["relay"] = "relay"

                        self.proxy = None
                        self._children_name_map["proxy"] = "proxy"
                        self._segment_path = lambda: "mode" + "[mode='" + str(self.mode) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, ['mode', 'enable'], name, value)


                    class Snoop(Entity):
                        """
                        DHCP Snoop profile
                        
                        .. attribute:: relay_information_option
                        
                        	DHCP Snoop profile
                        	**type**\:  :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption>`
                        
                        .. attribute:: trusted
                        
                        	Trusted sources
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, self).__init__()

                            self.yang_name = "snoop"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("relay-information-option", ("relay_information_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption))])
                            self._leafs = OrderedDict([
                                ('trusted', (YLeaf(YType.empty, 'trusted'), ['Empty'])),
                            ])
                            self.trusted = None

                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self._children_name_map["relay_information_option"] = "relay-information-option"
                            self._segment_path = lambda: "snoop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, ['trusted'], name, value)


                        class RelayInformationOption(Entity):
                            """
                            DHCP Snoop profile
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:  :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId>`
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "snoop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("remote-id", ("remote_id", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId))])
                                self._leafs = OrderedDict([
                                    ('insert', (YLeaf(YType.empty, 'insert'), ['Empty'])),
                                    ('allow_untrusted', (YLeaf(YType.empty, 'allow-untrusted'), ['Empty'])),
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionPolicy', '')])),
                                ])
                                self.insert = None
                                self.allow_untrusted = None
                                self.policy = None

                                self.remote_id = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId()
                                self.remote_id.parent = self
                                self._children_name_map["remote_id"] = "remote-id"
                                self._segment_path = lambda: "relay-information-option"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, ['insert', 'allow_untrusted', 'policy'], name, value)


                            class RemoteId(Entity):
                                """
                                Enter remote\-id value
                                
                                .. attribute:: format_type
                                
                                	Format type, 1. Hex 2. ASCII
                                	**type**\: int
                                
                                	**range:** 1..2
                                
                                .. attribute:: remote_id_value
                                
                                	Enter remote\-id value
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, self).__init__()

                                    self.yang_name = "remote-id"
                                    self.yang_parent_name = "relay-information-option"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('format_type', (YLeaf(YType.uint32, 'format-type'), ['int'])),
                                        ('remote_id_value', (YLeaf(YType.str, 'remote-id-value'), ['str'])),
                                    ])
                                    self.format_type = None
                                    self.remote_id_value = None
                                    self._segment_path = lambda: "remote-id"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, ['format_type', 'remote_id_value'], name, value)


                    class Base(Entity):
                        """
                        DHCP Base Profile
                        
                        .. attribute:: default_profile
                        
                        	Enable the default profile
                        	**type**\:  :py:class:`DefaultProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match>`
                        
                        .. attribute:: base_relay_opt
                        
                        	Insert Relay Agent Information circuit ID and remote ID suboptions in client request
                        	**type**\:  :py:class:`BaseRelayOpt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt>`
                        
                        .. attribute:: base_match
                        
                        	Insert match keyword
                        	**type**\:  :py:class:`BaseMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch>`
                        
                        .. attribute:: enable
                        
                        	Enable the DHCP IPv4 Base Profile
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, self).__init__()

                            self.yang_name = "base"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("default-profile", ("default_profile", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile)), ("match", ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match)), ("base-relay-opt", ("base_relay_opt", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt)), ("base-match", ("base_match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.enable = None

                            self.default_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile()
                            self.default_profile.parent = self
                            self._children_name_map["default_profile"] = "default-profile"

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"

                            self.base_relay_opt = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt()
                            self.base_relay_opt.parent = self
                            self._children_name_map["base_relay_opt"] = "base-relay-opt"

                            self.base_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch()
                            self.base_match.parent = self
                            self._children_name_map["base_match"] = "base-match"
                            self._segment_path = lambda: "base"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, ['enable'], name, value)


                        class DefaultProfile(Entity):
                            """
                            Enable the default profile
                            
                            .. attribute:: profile_name
                            
                            	Profile name
                            	**type**\: str
                            
                            	**length:** 1..64
                            
                            .. attribute:: profile_mode
                            
                            	none
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, self).__init__()

                                self.yang_name = "default-profile"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                    ('profile_mode', (YLeaf(YType.uint32, 'profile-mode'), ['int'])),
                                ])
                                self.profile_name = None
                                self.profile_mode = None
                                self._segment_path = lambda: "default-profile"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, ['profile_name', 'profile_mode'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:  :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters>`
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:  :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("option-filters", ("option_filters", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters)), ("def-options", ("def_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions))])
                                self._leafs = OrderedDict()

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"
                                self._segment_path = lambda: "match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match, [], name, value)


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("option-filter", ("option_filter", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter))])
                                    self._leafs = OrderedDict()

                                    self.option_filter = YList(self)
                                    self._segment_path = lambda: "option-filters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, [], name, value)


                                class OptionFilter(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pattern  (key)
                                    
                                    	Enter hex pattern string
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  (key)
                                    
                                    	Set constant integer
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: option_action
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`BaseAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseAction>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['matchoption','pattern','format']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('matchoption', (YLeaf(YType.uint32, 'matchoption'), ['int'])),
                                            ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                                            ('format', (YLeaf(YType.uint32, 'format'), ['int'])),
                                            ('option_action', (YLeaf(YType.enumeration, 'option-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'BaseAction', '')])),
                                        ])
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.option_action = None
                                        self._segment_path = lambda: "option-filter" + "[matchoption='" + str(self.matchoption) + "']" + "[pattern='" + str(self.pattern) + "']" + "[format='" + str(self.format) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, ['matchoption', 'pattern', 'format', 'option_action'], name, value)


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("def-option", ("def_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption))])
                                    self._leafs = OrderedDict()

                                    self.def_option = YList(self)
                                    self._segment_path = lambda: "def-options"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, [], name, value)


                                class DefOption(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`BaseAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.BaseAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['def_matchoption']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('def_matchoption', (YLeaf(YType.uint32, 'def-matchoption'), ['int'])),
                                            ('def_matchaction', (YLeaf(YType.enumeration, 'def-matchaction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'BaseAction', '')])),
                                        ])
                                        self.def_matchoption = None
                                        self.def_matchaction = None
                                        self._segment_path = lambda: "def-option" + "[def-matchoption='" + str(self.def_matchoption) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, ['def_matchoption', 'def_matchaction'], name, value)


                        class BaseRelayOpt(Entity):
                            """
                            Insert Relay Agent Information circuit ID
                            and remote ID suboptions in client request
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\: str
                            
                            	**length:** 1..256
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, self).__init__()

                                self.yang_name = "base-relay-opt"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('authenticate', (YLeaf(YType.uint32, 'authenticate'), ['int'])),
                                ])
                                self.remote_id = None
                                self.authenticate = None
                                self._segment_path = lambda: "base-relay-opt"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, ['remote_id', 'authenticate'], name, value)


                        class BaseMatch(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: options
                            
                            	Specify match option
                            	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch, self).__init__()

                                self.yang_name = "base-match"
                                self.yang_parent_name = "base"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("options", ("options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options))])
                                self._leafs = OrderedDict()

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._segment_path = lambda: "base-match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch, [], name, value)


                            class Options(Entity):
                                """
                                Specify match option
                                
                                .. attribute:: option
                                
                                	none
                                	**type**\: list of  		 :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "base-match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("option", ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option))])
                                    self._leafs = OrderedDict()

                                    self.option = YList(self)
                                    self._segment_path = lambda: "options"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, [], name, value)


                                class Option(Entity):
                                    """
                                    none
                                    
                                    .. attribute:: opt60  (key)
                                    
                                    	none
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: opt60_hex_str  (key)
                                    
                                    	Enter hex pattern string
                                    	**type**\: str
                                    
                                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                    
                                    .. attribute:: format  (key)
                                    
                                    	Set constant integer
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: option_profile
                                    
                                    	Enter a profile
                                    	**type**\:  :py:class:`OptionProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['opt60','opt60_hex_str','format']
                                        self._child_classes = OrderedDict([("option-profile", ("option_profile", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile))])
                                        self._leafs = OrderedDict([
                                            ('opt60', (YLeaf(YType.uint32, 'opt60'), ['int'])),
                                            ('opt60_hex_str', (YLeaf(YType.str, 'opt60-hex-str'), ['str'])),
                                            ('format', (YLeaf(YType.uint32, 'format'), ['int'])),
                                        ])
                                        self.opt60 = None
                                        self.opt60_hex_str = None
                                        self.format = None

                                        self.option_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile()
                                        self.option_profile.parent = self
                                        self._children_name_map["option_profile"] = "option-profile"
                                        self._segment_path = lambda: "option" + "[opt60='" + str(self.opt60) + "']" + "[opt60-hex-str='" + str(self.opt60_hex_str) + "']" + "[format='" + str(self.format) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, ['opt60', 'opt60_hex_str', 'format'], name, value)


                                    class OptionProfile(Entity):
                                        """
                                        Enter a profile
                                        
                                        .. attribute:: profile_name
                                        
                                        	Profile name
                                        	**type**\: str
                                        
                                        	**length:** 1..64
                                        
                                        .. attribute:: profile_mode
                                        
                                        	none
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, self).__init__()

                                            self.yang_name = "option-profile"
                                            self.yang_parent_name = "option"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                                                ('profile_mode', (YLeaf(YType.uint32, 'profile-mode'), ['int'])),
                                            ])
                                            self.profile_name = None
                                            self.profile_mode = None
                                            self._segment_path = lambda: "option-profile"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, ['profile_name', 'profile_mode'], name, value)


                    class Server(Entity):
                        """
                        DHCP Server profile
                        
                        .. attribute:: server_id_check
                        
                        	Validate server ID check
                        	**type**\:  :py:class:`ServerIdCheck <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck>`
                        
                        .. attribute:: lease_limit
                        
                        	Specify limit lease
                        	**type**\:  :py:class:`LeaseLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit>`
                        
                        .. attribute:: requested_ip_address
                        
                        	Validate Requested IP Address
                        	**type**\:  :py:class:`RequestedIpAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress>`
                        
                        .. attribute:: aaa_server
                        
                        	Enable aaa dhcp option force\-insert
                        	**type**\:  :py:class:`AaaServer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer>`
                        
                        .. attribute:: default_routers
                        
                        	default routers
                        	**type**\:  :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters>`
                        
                        .. attribute:: net_bios_name_servers
                        
                        	NetBIOS name servers
                        	**type**\:  :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers>`
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match>`
                        
                        .. attribute:: broadcast_flag
                        
                        	None
                        	**type**\:  :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag>`
                        
                        .. attribute:: session
                        
                        	Change sessions configuration
                        	**type**\:  :py:class:`Session <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session>`
                        
                        .. attribute:: classes
                        
                        	Table of Class
                        	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes>`
                        
                        .. attribute:: relay
                        
                        	Specify Relay Agent Information Option configuration
                        	**type**\:  :py:class:`Relay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay>`
                        
                        .. attribute:: lease
                        
                        	lease
                        	**type**\:  :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease>`
                        
                        .. attribute:: netbios_node_type
                        
                        	NetBIOS node type
                        	**type**\:  :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType>`
                        
                        .. attribute:: dns_servers
                        
                        	DNS servers
                        	**type**\:  :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers>`
                        
                        .. attribute:: dhcp_to_aaa
                        
                        	Enable to provide the list of options need to send to aaa
                        	**type**\:  :py:class:`DhcpToAaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa>`
                        
                        .. attribute:: server_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: enable
                        
                        	DHCP IPV4 profile mode enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        .. attribute:: subnet_mask
                        
                        	Configure Subnet Mask
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: pool
                        
                        	Specify the Pool name
                        	**type**\: str
                        
                        	**length:** 1..64
                        
                        .. attribute:: domain_name
                        
                        	Domain name
                        	**type**\: str
                        
                        	**length:** 1..256
                        
                        .. attribute:: secure_arp
                        
                        	Enable Secure Arp
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: arp_instal_skip_stdalone
                        
                        	Skip ARP installation for standalone sessions
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: boot_filename
                        
                        	Boot Filename
                        	**type**\: str
                        
                        	**length:** 1..128
                        
                        .. attribute:: next_server
                        
                        	Configure the tftp\-server IP to be used by the client
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: option_codes
                        
                        	Table of OptionCode
                        	**type**\:  :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes>`
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("server-id-check", ("server_id_check", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck)), ("lease-limit", ("lease_limit", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit)), ("requested-ip-address", ("requested_ip_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress)), ("aaa-server", ("aaa_server", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer)), ("default-routers", ("default_routers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters)), ("net-bios-name-servers", ("net_bios_name_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers)), ("match", ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match)), ("broadcast-flag", ("broadcast_flag", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag)), ("session", ("session", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session)), ("classes", ("classes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes)), ("relay", ("relay", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay)), ("lease", ("lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease)), ("netbios-node-type", ("netbios_node_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType)), ("dns-servers", ("dns_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers)), ("dhcp-to-aaa", ("dhcp_to_aaa", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa)), ("option-codes", ("option_codes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('server_allow_move', (YLeaf(YType.empty, 'server-allow-move'), ['Empty'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                ('subnet_mask', (YLeaf(YType.str, 'subnet-mask'), ['str'])),
                                ('pool', (YLeaf(YType.str, 'pool'), ['str'])),
                                ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                ('secure_arp', (YLeaf(YType.empty, 'secure-arp'), ['Empty'])),
                                ('arp_instal_skip_stdalone', (YLeaf(YType.empty, 'arp-instal-skip-stdalone'), ['Empty'])),
                                ('boot_filename', (YLeaf(YType.str, 'boot-filename'), ['str'])),
                                ('next_server', (YLeaf(YType.str, 'next-server'), ['str'])),
                            ])
                            self.server_allow_move = None
                            self.enable = None
                            self.subnet_mask = None
                            self.pool = None
                            self.domain_name = None
                            self.secure_arp = None
                            self.arp_instal_skip_stdalone = None
                            self.boot_filename = None
                            self.next_server = None

                            self.server_id_check = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck()
                            self.server_id_check.parent = self
                            self._children_name_map["server_id_check"] = "server-id-check"

                            self.lease_limit = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit()
                            self.lease_limit.parent = self
                            self._children_name_map["lease_limit"] = "lease-limit"

                            self.requested_ip_address = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress()
                            self.requested_ip_address.parent = self
                            self._children_name_map["requested_ip_address"] = "requested-ip-address"

                            self.aaa_server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer()
                            self.aaa_server.parent = self
                            self._children_name_map["aaa_server"] = "aaa-server"

                            self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters()
                            self.default_routers.parent = self
                            self._children_name_map["default_routers"] = "default-routers"

                            self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers()
                            self.net_bios_name_servers.parent = self
                            self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"

                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self._children_name_map["broadcast_flag"] = "broadcast-flag"

                            self.session = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session()
                            self.session.parent = self
                            self._children_name_map["session"] = "session"

                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"

                            self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay()
                            self.relay.parent = self
                            self._children_name_map["relay"] = "relay"

                            self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease()
                            self.lease.parent = self
                            self._children_name_map["lease"] = "lease"

                            self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType()
                            self.netbios_node_type.parent = self
                            self._children_name_map["netbios_node_type"] = "netbios-node-type"

                            self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers()
                            self.dns_servers.parent = self
                            self._children_name_map["dns_servers"] = "dns-servers"

                            self.dhcp_to_aaa = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa()
                            self.dhcp_to_aaa.parent = self
                            self._children_name_map["dhcp_to_aaa"] = "dhcp-to-aaa"

                            self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes()
                            self.option_codes.parent = self
                            self._children_name_map["option_codes"] = "option-codes"
                            self._segment_path = lambda: "server"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, ['server_allow_move', 'enable', 'subnet_mask', 'pool', 'domain_name', 'secure_arp', 'arp_instal_skip_stdalone', 'boot_filename', 'next_server'], name, value)


                        class ServerIdCheck(Entity):
                            """
                            Validate server ID check
                            
                            .. attribute:: check
                            
                            	specify server\-id\-check disable
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, self).__init__()

                                self.yang_name = "server-id-check"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('check', (YLeaf(YType.empty, 'check'), ['Empty'])),
                                ])
                                self.check = None
                                self._segment_path = lambda: "server-id-check"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, ['check'], name, value)


                        class LeaseLimit(Entity):
                            """
                            Specify limit lease
                            
                            .. attribute:: lease_limit_value
                            
                            	Configure Lease limit value
                            	**type**\:  :py:class:`LeaseLimitValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.LeaseLimitValue>`
                            
                            .. attribute:: range
                            
                            	Value of limit lease count in Decimal
                            	**type**\: int
                            
                            	**range:** 1..240000
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, self).__init__()

                                self.yang_name = "lease-limit"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('lease_limit_value', (YLeaf(YType.enumeration, 'lease-limit-value'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'LeaseLimitValue', '')])),
                                    ('range', (YLeaf(YType.uint32, 'range'), ['int'])),
                                ])
                                self.lease_limit_value = None
                                self.range = None
                                self._segment_path = lambda: "lease-limit"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, ['lease_limit_value', 'range'], name, value)


                        class RequestedIpAddress(Entity):
                            """
                            Validate Requested IP Address
                            
                            .. attribute:: check
                            
                            	specify requested\-ip\-address\-check disable
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, self).__init__()

                                self.yang_name = "requested-ip-address"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('check', (YLeaf(YType.empty, 'check'), ['Empty'])),
                                ])
                                self.check = None
                                self._segment_path = lambda: "requested-ip-address"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, ['check'], name, value)


                        class AaaServer(Entity):
                            """
                            Enable aaa dhcp option force\-insert
                            
                            .. attribute:: dhcp_option
                            
                            	Enable aaa dhcp option force\-insert
                            	**type**\:  :py:class:`DhcpOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer, self).__init__()

                                self.yang_name = "aaa-server"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("dhcp-option", ("dhcp_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption))])
                                self._leafs = OrderedDict()

                                self.dhcp_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption()
                                self.dhcp_option.parent = self
                                self._children_name_map["dhcp_option"] = "dhcp-option"
                                self._segment_path = lambda: "aaa-server"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer, [], name, value)


                            class DhcpOption(Entity):
                                """
                                Enable aaa dhcp option force\-insert
                                
                                .. attribute:: force_insert
                                
                                	Enable aaa dhcp option force\-insert
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption, self).__init__()

                                    self.yang_name = "dhcp-option"
                                    self.yang_parent_name = "aaa-server"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('force_insert', (YLeaf(YType.empty, 'force-insert'), ['Empty'])),
                                    ])
                                    self.force_insert = None
                                    self._segment_path = lambda: "dhcp-option"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.AaaServer.DhcpOption, ['force_insert'], name, value)


                        class DefaultRouters(Entity):
                            """
                            default routers
                            
                            .. attribute:: default_router
                            
                            	Router's IP address
                            	**type**\: list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, self).__init__()

                                self.yang_name = "default-routers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('default_router', (YLeafList(YType.str, 'default-router'), ['str'])),
                                ])
                                self.default_router = []
                                self._segment_path = lambda: "default-routers"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, ['default_router'], name, value)


                        class NetBiosNameServers(Entity):
                            """
                            NetBIOS name servers
                            
                            .. attribute:: net_bios_name_server
                            
                            	NetBIOSNameServer's IP address
                            	**type**\: list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, self).__init__()

                                self.yang_name = "net-bios-name-servers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('net_bios_name_server', (YLeafList(YType.str, 'net-bios-name-server'), ['str'])),
                                ])
                                self.net_bios_name_server = []
                                self._segment_path = lambda: "net-bios-name-servers"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, ['net_bios_name_server'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: option_defaults
                            
                            	Table of OptionDefault
                            	**type**\:  :py:class:`OptionDefaults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults>`
                            
                            .. attribute:: options
                            
                            	Table of Option
                            	**type**\:  :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("option-defaults", ("option_defaults", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults)), ("options", ("options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options))])
                                self._leafs = OrderedDict()

                                self.option_defaults = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults()
                                self.option_defaults.parent = self
                                self._children_name_map["option_defaults"] = "option-defaults"

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._segment_path = lambda: "match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match, [], name, value)


                            class OptionDefaults(Entity):
                                """
                                Table of OptionDefault
                                
                                .. attribute:: option_default
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`OptionDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, self).__init__()

                                    self.yang_name = "option-defaults"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("option-default", ("option_default", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault))])
                                    self._leafs = OrderedDict()

                                    self.option_default = YList(self)
                                    self._segment_path = lambda: "option-defaults"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, [], name, value)


                                class OptionDefault(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\:  :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`Matchaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchaction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, self).__init__()

                                        self.yang_name = "option-default"
                                        self.yang_parent_name = "option-defaults"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['matchoption']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('matchoption', (YLeaf(YType.enumeration, 'matchoption'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Matchoption', '')])),
                                            ('matchaction', (YLeaf(YType.enumeration, 'matchaction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Matchaction', '')])),
                                        ])
                                        self.matchoption = None
                                        self.matchaction = None
                                        self._segment_path = lambda: "option-default" + "[matchoption='" + str(self.matchoption) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, ['matchoption', 'matchaction'], name, value)


                            class Options(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("option", ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option))])
                                    self._leafs = OrderedDict()

                                    self.option = YList(self)
                                    self._segment_path = lambda: "options"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, [], name, value)


                                class Option(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\:  :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                    
                                    .. attribute:: pattern  (key)
                                    
                                    	Enter hex pattern string
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  (key)
                                    
                                    	Set constant integer
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`Matchaction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchaction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['matchoption','pattern','format']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('matchoption', (YLeaf(YType.enumeration, 'matchoption'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Matchoption', '')])),
                                            ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                                            ('format', (YLeaf(YType.uint32, 'format'), ['int'])),
                                            ('matchaction', (YLeaf(YType.enumeration, 'matchaction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Matchaction', '')])),
                                        ])
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.matchaction = None
                                        self._segment_path = lambda: "option" + "[matchoption='" + str(self.matchoption) + "']" + "[pattern='" + str(self.pattern) + "']" + "[format='" + str(self.format) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, ['matchoption', 'pattern', 'format', 'matchaction'], name, value)


                        class BroadcastFlag(Entity):
                            """
                            None
                            
                            .. attribute:: policy
                            
                            	Specify broadcast flag policy
                            	**type**\:  :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Policy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Policy', '')])),
                                ])
                                self.policy = None
                                self._segment_path = lambda: "broadcast-flag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, ['policy'], name, value)


                        class Session(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:  :py:class:`ThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session, self).__init__()

                                self.yang_name = "session"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("throttle-type", ("throttle_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType))])
                                self._leafs = OrderedDict()

                                self.throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType()
                                self.throttle_type.parent = self
                                self._children_name_map["throttle_type"] = "throttle-type"
                                self._segment_path = lambda: "session"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session, [], name, value)


                            class ThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:  :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType, self).__init__()

                                    self.yang_name = "throttle-type"
                                    self.yang_parent_name = "session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("mac-throttle", ("mac_throttle", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle))])
                                    self._leafs = OrderedDict()

                                    self.mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle()
                                    self.mac_throttle.parent = self
                                    self._children_name_map["mac_throttle"] = "mac-throttle"
                                    self._segment_path = lambda: "throttle-type"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType, [], name, value)


                                class MacThrottle(Entity):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\: int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\: int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, self).__init__()

                                        self.yang_name = "mac-throttle"
                                        self.yang_parent_name = "throttle-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_discover', (YLeaf(YType.uint32, 'num-discover'), ['int'])),
                                            ('num_request', (YLeaf(YType.uint32, 'num-request'), ['int'])),
                                            ('num_block', (YLeaf(YType.uint32, 'num-block'), ['int'])),
                                        ])
                                        self.num_discover = None
                                        self.num_request = None
                                        self.num_block = None
                                        self._segment_path = lambda: "mac-throttle"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, ['num_discover', 'num_request', 'num_block'], name, value)


                        class Classes(Entity):
                            """
                            Table of Class
                            
                            .. attribute:: class_
                            
                            	Create or enter server profile class
                            	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("class", ("class_", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class))])
                                self._leafs = OrderedDict()

                                self.class_ = YList(self)
                                self._segment_path = lambda: "classes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, [], name, value)


                            class Class(Entity):
                                """
                                Create or enter server profile class
                                
                                .. attribute:: class_name  (key)
                                
                                	class name
                                	**type**\: str
                                
                                	**length:** 1..128
                                
                                .. attribute:: default_routers
                                
                                	default routers
                                	**type**\:  :py:class:`DefaultRouters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DefaultRouters>`
                                
                                .. attribute:: net_bios_name_servers
                                
                                	NetBIOS name servers
                                	**type**\:  :py:class:`NetBiosNameServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetBiosNameServers>`
                                
                                .. attribute:: class_match
                                
                                	Insert match keyword
                                	**type**\:  :py:class:`ClassMatch <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch>`
                                
                                .. attribute:: lease
                                
                                	lease
                                	**type**\:  :py:class:`Lease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.Lease>`
                                
                                .. attribute:: netbios_node_type
                                
                                	NetBIOS node type
                                	**type**\:  :py:class:`NetbiosNodeType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetbiosNodeType>`
                                
                                .. attribute:: dns_servers
                                
                                	DNS servers
                                	**type**\:  :py:class:`DnsServers <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DnsServers>`
                                
                                .. attribute:: subnet_mask
                                
                                	Configure Subnet Mask
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: pool
                                
                                	Specify the pool
                                	**type**\: str
                                
                                .. attribute:: enable
                                
                                	Enable Create or enter server profile class. Deletion of this object also causes deletion of all associated objects under Class
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                .. attribute:: domain_name
                                
                                	Domain name
                                	**type**\: str
                                
                                	**length:** 1..256
                                
                                .. attribute:: boot_filename
                                
                                	Boot Filename
                                	**type**\: str
                                
                                	**length:** 1..128
                                
                                .. attribute:: next_server
                                
                                	Configure the tftp\-server IP to be used by the client
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: option_codes
                                
                                	Table of OptionCode
                                	**type**\:  :py:class:`OptionCodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['class_name']
                                    self._child_classes = OrderedDict([("default-routers", ("default_routers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DefaultRouters)), ("net-bios-name-servers", ("net_bios_name_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetBiosNameServers)), ("class-match", ("class_match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch)), ("lease", ("lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.Lease)), ("netbios-node-type", ("netbios_node_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetbiosNodeType)), ("dns-servers", ("dns_servers", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DnsServers)), ("option-codes", ("option_codes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes))])
                                    self._leafs = OrderedDict([
                                        ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                        ('subnet_mask', (YLeaf(YType.str, 'subnet-mask'), ['str'])),
                                        ('pool', (YLeaf(YType.str, 'pool'), ['str'])),
                                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                        ('domain_name', (YLeaf(YType.str, 'domain-name'), ['str'])),
                                        ('boot_filename', (YLeaf(YType.str, 'boot-filename'), ['str'])),
                                        ('next_server', (YLeaf(YType.str, 'next-server'), ['str'])),
                                    ])
                                    self.class_name = None
                                    self.subnet_mask = None
                                    self.pool = None
                                    self.enable = None
                                    self.domain_name = None
                                    self.boot_filename = None
                                    self.next_server = None

                                    self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DefaultRouters()
                                    self.default_routers.parent = self
                                    self._children_name_map["default_routers"] = "default-routers"

                                    self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetBiosNameServers()
                                    self.net_bios_name_servers.parent = self
                                    self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"

                                    self.class_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch()
                                    self.class_match.parent = self
                                    self._children_name_map["class_match"] = "class-match"

                                    self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.Lease()
                                    self.lease.parent = self
                                    self._children_name_map["lease"] = "lease"

                                    self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetbiosNodeType()
                                    self.netbios_node_type.parent = self
                                    self._children_name_map["netbios_node_type"] = "netbios-node-type"

                                    self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DnsServers()
                                    self.dns_servers.parent = self
                                    self._children_name_map["dns_servers"] = "dns-servers"

                                    self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes()
                                    self.option_codes.parent = self
                                    self._children_name_map["option_codes"] = "option-codes"
                                    self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class, ['class_name', 'subnet_mask', 'pool', 'enable', 'domain_name', 'boot_filename', 'next_server'], name, value)


                                class DefaultRouters(Entity):
                                    """
                                    default routers
                                    
                                    .. attribute:: default_router
                                    
                                    	Router's IP address
                                    	**type**\: list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DefaultRouters, self).__init__()

                                        self.yang_name = "default-routers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('default_router', (YLeafList(YType.str, 'default-router'), ['str'])),
                                        ])
                                        self.default_router = []
                                        self._segment_path = lambda: "default-routers"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DefaultRouters, ['default_router'], name, value)


                                class NetBiosNameServers(Entity):
                                    """
                                    NetBIOS name servers
                                    
                                    .. attribute:: net_bios_name_server
                                    
                                    	NetBIOSNameServer's IP address
                                    	**type**\: list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetBiosNameServers, self).__init__()

                                        self.yang_name = "net-bios-name-servers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('net_bios_name_server', (YLeafList(YType.str, 'net-bios-name-server'), ['str'])),
                                        ])
                                        self.net_bios_name_server = []
                                        self._segment_path = lambda: "net-bios-name-servers"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetBiosNameServers, ['net_bios_name_server'], name, value)


                                class ClassMatch(Entity):
                                    """
                                    Insert match keyword
                                    
                                    .. attribute:: class_options
                                    
                                    	Table of Class\-Option
                                    	**type**\:  :py:class:`ClassOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions>`
                                    
                                    .. attribute:: l2_interface
                                    
                                    	Specify match l2\-interface
                                    	**type**\: str
                                    
                                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                                    
                                    .. attribute:: vrf
                                    
                                    	Specify match VRF
                                    	**type**\: str
                                    
                                    	**length:** 1..32
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch, self).__init__()

                                        self.yang_name = "class-match"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("class-options", ("class_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions))])
                                        self._leafs = OrderedDict([
                                            ('l2_interface', (YLeaf(YType.str, 'l2-interface'), ['str'])),
                                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                        ])
                                        self.l2_interface = None
                                        self.vrf = None

                                        self.class_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions()
                                        self.class_options.parent = self
                                        self._children_name_map["class_options"] = "class-options"
                                        self._segment_path = lambda: "class-match"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch, ['l2_interface', 'vrf'], name, value)


                                    class ClassOptions(Entity):
                                        """
                                        Table of Class\-Option
                                        
                                        .. attribute:: class_option
                                        
                                        	Specify match option
                                        	**type**\: list of  		 :py:class:`ClassOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions.ClassOption>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions, self).__init__()

                                            self.yang_name = "class-options"
                                            self.yang_parent_name = "class-match"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([("class-option", ("class_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions.ClassOption))])
                                            self._leafs = OrderedDict()

                                            self.class_option = YList(self)
                                            self._segment_path = lambda: "class-options"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions, [], name, value)


                                        class ClassOption(Entity):
                                            """
                                            Specify match option
                                            
                                            .. attribute:: matchoption  (key)
                                            
                                            	Match options
                                            	**type**\:  :py:class:`Matchoption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Matchoption>`
                                            
                                            .. attribute:: pattern
                                            
                                            	Enter hex pattern string
                                            	**type**\: str
                                            
                                            	**length:** 1..64
                                            
                                            .. attribute:: bit_mask
                                            
                                            	Enter bit mask pattern string
                                            	**type**\: str
                                            
                                            	**length:** 1..64
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2017-09-30'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions.ClassOption, self).__init__()

                                                self.yang_name = "class-option"
                                                self.yang_parent_name = "class-options"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['matchoption']
                                                self._child_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('matchoption', (YLeaf(YType.enumeration, 'matchoption'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Matchoption', '')])),
                                                    ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                                                    ('bit_mask', (YLeaf(YType.str, 'bit-mask'), ['str'])),
                                                ])
                                                self.matchoption = None
                                                self.pattern = None
                                                self.bit_mask = None
                                                self._segment_path = lambda: "class-option" + "[matchoption='" + str(self.matchoption) + "']"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.ClassMatch.ClassOptions.ClassOption, ['matchoption', 'pattern', 'bit_mask'], name, value)


                                class Lease(Entity):
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

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.Lease, self).__init__()

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
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.Lease, ['infinite', 'days', 'hours', 'minutes'], name, value)


                                class NetbiosNodeType(Entity):
                                    """
                                    NetBIOS node type
                                    
                                    .. attribute:: broadcast_node
                                    
                                    	Set string
                                    	**type**\: str
                                    
                                    .. attribute:: hybrid_node
                                    
                                    	Set string
                                    	**type**\: str
                                    
                                    .. attribute:: mixed_node
                                    
                                    	Set string
                                    	**type**\: str
                                    
                                    .. attribute:: peer_to_peer_node
                                    
                                    	Set string
                                    	**type**\: str
                                    
                                    .. attribute:: hexadecimal
                                    
                                    	Hexadecimal number
                                    	**type**\: str
                                    
                                    	**pattern:** [0\-9a\-fA\-F]{1,8}
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetbiosNodeType, self).__init__()

                                        self.yang_name = "netbios-node-type"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('broadcast_node', (YLeaf(YType.str, 'broadcast-node'), ['str'])),
                                            ('hybrid_node', (YLeaf(YType.str, 'hybrid-node'), ['str'])),
                                            ('mixed_node', (YLeaf(YType.str, 'mixed-node'), ['str'])),
                                            ('peer_to_peer_node', (YLeaf(YType.str, 'peer-to-peer-node'), ['str'])),
                                            ('hexadecimal', (YLeaf(YType.str, 'hexadecimal'), ['str'])),
                                        ])
                                        self.broadcast_node = None
                                        self.hybrid_node = None
                                        self.mixed_node = None
                                        self.peer_to_peer_node = None
                                        self.hexadecimal = None
                                        self._segment_path = lambda: "netbios-node-type"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.NetbiosNodeType, ['broadcast_node', 'hybrid_node', 'mixed_node', 'peer_to_peer_node', 'hexadecimal'], name, value)


                                class DnsServers(Entity):
                                    """
                                    DNS servers
                                    
                                    .. attribute:: dns_server
                                    
                                    	DNS Server's IP address
                                    	**type**\: list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DnsServers, self).__init__()

                                        self.yang_name = "dns-servers"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('dns_server', (YLeafList(YType.str, 'dns-server'), ['str'])),
                                        ])
                                        self.dns_server = []
                                        self._segment_path = lambda: "dns-servers"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.DnsServers, ['dns_server'], name, value)


                                class OptionCodes(Entity):
                                    """
                                    Table of OptionCode
                                    
                                    .. attribute:: option_code
                                    
                                    	DHCP option code
                                    	**type**\: list of  		 :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes.OptionCode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes, self).__init__()

                                        self.yang_name = "option-codes"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("option-code", ("option_code", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes.OptionCode))])
                                        self._leafs = OrderedDict()

                                        self.option_code = YList(self)
                                        self._segment_path = lambda: "option-codes"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes, [], name, value)


                                    class OptionCode(Entity):
                                        """
                                        DHCP option code
                                        
                                        .. attribute:: option_code  (key)
                                        
                                        	DHCP option code
                                        	**type**\: int
                                        
                                        	**range:** 0..255
                                        
                                        .. attribute:: ascii_string
                                        
                                        	ASCII string
                                        	**type**\: str
                                        
                                        .. attribute:: hex_string
                                        
                                        	Hexadecimal string
                                        	**type**\: str
                                        
                                        .. attribute:: force_insert
                                        
                                        	Set constant integer
                                        	**type**\: int
                                        
                                        	**range:** 0..4294967295
                                        
                                        .. attribute:: ip_address
                                        
                                        	Server's IP address
                                        	**type**\: list of str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes.OptionCode, self).__init__()

                                            self.yang_name = "option-code"
                                            self.yang_parent_name = "option-codes"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['option_code']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('option_code', (YLeaf(YType.uint32, 'option-code'), ['int'])),
                                                ('ascii_string', (YLeaf(YType.str, 'ascii-string'), ['str'])),
                                                ('hex_string', (YLeaf(YType.str, 'hex-string'), ['str'])),
                                                ('force_insert', (YLeaf(YType.uint32, 'force-insert'), ['int'])),
                                                ('ip_address', (YLeafList(YType.str, 'ip-address'), ['str'])),
                                            ])
                                            self.option_code = None
                                            self.ascii_string = None
                                            self.hex_string = None
                                            self.force_insert = None
                                            self.ip_address = []
                                            self._segment_path = lambda: "option-code" + "[option-code='" + str(self.option_code) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class.OptionCodes.OptionCode, ['option_code', 'ascii_string', 'hex_string', 'force_insert', 'ip_address'], name, value)


                        class Relay(Entity):
                            """
                            Specify Relay Agent Information Option
                            configuration
                            
                            .. attribute:: authenticate
                            
                            	Specify Relay Agent Information Option authenticate
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, self).__init__()

                                self.yang_name = "relay"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('authenticate', (YLeaf(YType.uint32, 'authenticate'), ['int'])),
                                ])
                                self.authenticate = None
                                self._segment_path = lambda: "relay"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, ['authenticate'], name, value)


                        class Lease(Entity):
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

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, self).__init__()

                                self.yang_name = "lease"
                                self.yang_parent_name = "server"
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
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, ['infinite', 'days', 'hours', 'minutes'], name, value)


                        class NetbiosNodeType(Entity):
                            """
                            NetBIOS node type
                            
                            .. attribute:: broadcast_node
                            
                            	Set string
                            	**type**\: str
                            
                            .. attribute:: hybrid_node
                            
                            	Set string
                            	**type**\: str
                            
                            .. attribute:: mixed_node
                            
                            	Set string
                            	**type**\: str
                            
                            .. attribute:: peer_to_peer_node
                            
                            	Set string
                            	**type**\: str
                            
                            .. attribute:: hexadecimal
                            
                            	Hexadecimal number
                            	**type**\: str
                            
                            	**pattern:** [0\-9a\-fA\-F]{1,8}
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, self).__init__()

                                self.yang_name = "netbios-node-type"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('broadcast_node', (YLeaf(YType.str, 'broadcast-node'), ['str'])),
                                    ('hybrid_node', (YLeaf(YType.str, 'hybrid-node'), ['str'])),
                                    ('mixed_node', (YLeaf(YType.str, 'mixed-node'), ['str'])),
                                    ('peer_to_peer_node', (YLeaf(YType.str, 'peer-to-peer-node'), ['str'])),
                                    ('hexadecimal', (YLeaf(YType.str, 'hexadecimal'), ['str'])),
                                ])
                                self.broadcast_node = None
                                self.hybrid_node = None
                                self.mixed_node = None
                                self.peer_to_peer_node = None
                                self.hexadecimal = None
                                self._segment_path = lambda: "netbios-node-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, ['broadcast_node', 'hybrid_node', 'mixed_node', 'peer_to_peer_node', 'hexadecimal'], name, value)


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	DNS Server's IP address
                            	**type**\: list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dns_server', (YLeafList(YType.str, 'dns-server'), ['str'])),
                                ])
                                self.dns_server = []
                                self._segment_path = lambda: "dns-servers"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, ['dns_server'], name, value)


                        class DhcpToAaa(Entity):
                            """
                            Enable to provide the list of options need
                            to send to aaa
                            
                            .. attribute:: option
                            
                            	option type
                            	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa, self).__init__()

                                self.yang_name = "dhcp-to-aaa"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("option", ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option))])
                                self._leafs = OrderedDict()

                                self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option()
                                self.option.parent = self
                                self._children_name_map["option"] = "option"
                                self._segment_path = lambda: "dhcp-to-aaa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa, [], name, value)


                            class Option(Entity):
                                """
                                option type
                                
                                .. attribute:: list
                                
                                	List of options
                                	**type**\:  :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option.List>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option, self).__init__()

                                    self.yang_name = "option"
                                    self.yang_parent_name = "dhcp-to-aaa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("list", ("list", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option.List))])
                                    self._leafs = OrderedDict()

                                    self.list = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option.List()
                                    self.list.parent = self
                                    self._children_name_map["list"] = "list"
                                    self._segment_path = lambda: "option"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option, [], name, value)


                                class List(Entity):
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

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option.List, self).__init__()

                                        self.yang_name = "list"
                                        self.yang_parent_name = "option"
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
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DhcpToAaa.Option.List, ['option_all', 'option_number'], name, value)


                        class OptionCodes(Entity):
                            """
                            Table of OptionCode
                            
                            .. attribute:: option_code
                            
                            	DHCP option code
                            	**type**\: list of  		 :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, self).__init__()

                                self.yang_name = "option-codes"
                                self.yang_parent_name = "server"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("option-code", ("option_code", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode))])
                                self._leafs = OrderedDict()

                                self.option_code = YList(self)
                                self._segment_path = lambda: "option-codes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, [], name, value)


                            class OptionCode(Entity):
                                """
                                DHCP option code
                                
                                .. attribute:: option_code  (key)
                                
                                	DHCP option code
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: ascii_string
                                
                                	ASCII string
                                	**type**\: str
                                
                                .. attribute:: hex_string
                                
                                	Hexadecimal string
                                	**type**\: str
                                
                                .. attribute:: force_insert
                                
                                	Set constant integer
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: ip_address
                                
                                	Server's IP address
                                	**type**\: list of str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, self).__init__()

                                    self.yang_name = "option-code"
                                    self.yang_parent_name = "option-codes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['option_code']
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('option_code', (YLeaf(YType.uint32, 'option-code'), ['int'])),
                                        ('ascii_string', (YLeaf(YType.str, 'ascii-string'), ['str'])),
                                        ('hex_string', (YLeaf(YType.str, 'hex-string'), ['str'])),
                                        ('force_insert', (YLeaf(YType.uint32, 'force-insert'), ['int'])),
                                        ('ip_address', (YLeafList(YType.str, 'ip-address'), ['str'])),
                                    ])
                                    self.option_code = None
                                    self.ascii_string = None
                                    self.hex_string = None
                                    self.force_insert = None
                                    self.ip_address = []
                                    self._segment_path = lambda: "option-code" + "[option-code='" + str(self.option_code) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, ['option_code', 'ascii_string', 'hex_string', 'force_insert', 'ip_address'], name, value)


                    class Relay(Entity):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:  :py:class:`GiAddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: vrfs
                        
                        	VRF Helper Addresses
                        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs>`
                        
                        .. attribute:: relay_information_option
                        
                        	Relay agent information option
                        	**type**\:  :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption>`
                        
                        .. attribute:: broadcast_policy
                        
                        	Broadcast Flag policy
                        	**type**\:  :py:class:`BroadcastPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: mac_mismatch_action
                        
                        	Action to take if L2 header source Mac and dhcp header mac address don't match
                        	**type**\:  :py:class:`MacMismatchAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.MacMismatchAction>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay, self).__init__()

                            self.yang_name = "relay"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("gi-addr-policy", ("gi_addr_policy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy)), ("vrfs", ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs)), ("relay-information-option", ("relay_information_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption)), ("broadcast-policy", ("broadcast_policy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy))])
                            self._leafs = OrderedDict([
                                ('mac_mismatch_action', (YLeaf(YType.enumeration, 'mac-mismatch-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'MacMismatchAction', '')])),
                            ])
                            self.mac_mismatch_action = None

                            self.gi_addr_policy = None
                            self._children_name_map["gi_addr_policy"] = "gi-addr-policy"

                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"

                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self._children_name_map["relay_information_option"] = "relay-information-option"

                            self.broadcast_policy = None
                            self._children_name_map["broadcast_policy"] = "broadcast-policy"
                            self._segment_path = lambda: "relay"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay, ['mac_mismatch_action'], name, value)


                        class GiAddrPolicy(Entity):
                            """
                            GIADDR policy
                            
                            .. attribute:: policy
                            
                            	GIADDR policy
                            	**type**\:  :py:class:`Ipv4dhcpdRelayGiaddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayGiaddrPolicy>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, self).__init__()

                                self.yang_name = "gi-addr-policy"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayGiaddrPolicy', '')])),
                                ])
                                self.policy = None
                                self._segment_path = lambda: "gi-addr-policy"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, ['policy'], name, value)


                        class Vrfs(Entity):
                            """
                            VRF Helper Addresses
                            
                            .. attribute:: vrf
                            
                            	VRF Name
                            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf))])
                                self._leafs = OrderedDict()

                                self.vrf = YList(self)
                                self._segment_path = lambda: "vrfs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, [], name, value)


                            class Vrf(Entity):
                                """
                                VRF Name
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF Name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper Addresses
                                	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name']
                                    self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses))])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.vrf_name = None

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, ['vrf_name'], name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper Addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper Address
                                    	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("helper-address", ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress))])
                                        self._leafs = OrderedDict()

                                        self.helper_address = YList(self)
                                        self._segment_path = lambda: "helper-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, [], name, value)


                                    class HelperAddress(Entity):
                                        """
                                        Helper Address
                                        
                                        .. attribute:: ip_address  (key)
                                        
                                        	IPV4 Address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: enable
                                        
                                        	Enable helper \- deprecated
                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                        
                                        .. attribute:: gateway_address
                                        
                                        	GatewayAddress
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['ip_address']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('ip_address', (YLeaf(YType.str, 'ip-address'), ['str'])),
                                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                                ('gateway_address', (YLeaf(YType.str, 'gateway-address'), ['str'])),
                                            ])
                                            self.ip_address = None
                                            self.enable = None
                                            self.gateway_address = None
                                            self._segment_path = lambda: "helper-address" + "[ip-address='" + str(self.ip_address) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, ['ip_address', 'enable', 'gateway_address'], name, value)


                        class RelayInformationOption(Entity):
                            """
                            Relay agent information option
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionvpnMode>`
                            
                            .. attribute:: subscriber_id
                            
                            	Subscriber ID
                            	**type**\: str
                            
                            .. attribute:: insert
                            
                            	Insert Relay Agent Information circuit ID and remote ID suboptions in client requests
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: check
                            
                            	Check Relay Agent Information Option in server reply
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('vpn_mode', (YLeaf(YType.enumeration, 'vpn-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionvpnMode', '')])),
                                    ('subscriber_id', (YLeaf(YType.str, 'subscriber-id'), ['str'])),
                                    ('insert', (YLeaf(YType.empty, 'insert'), ['Empty'])),
                                    ('check', (YLeaf(YType.empty, 'check'), ['Empty'])),
                                    ('vpn', (YLeaf(YType.empty, 'vpn'), ['Empty'])),
                                    ('allow_untrusted', (YLeaf(YType.empty, 'allow-untrusted'), ['Empty'])),
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionPolicy', '')])),
                                ])
                                self.vpn_mode = None
                                self.subscriber_id = None
                                self.insert = None
                                self.check = None
                                self.vpn = None
                                self.allow_untrusted = None
                                self.policy = None
                                self._segment_path = lambda: "relay-information-option"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, ['vpn_mode', 'subscriber_id', 'insert', 'check', 'vpn', 'allow_untrusted', 'policy'], name, value)


                        class BroadcastPolicy(Entity):
                            """
                            Broadcast Flag policy
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:  :py:class:`Ipv4dhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdBroadcastFlagPolicy>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, self).__init__()

                                self.yang_name = "broadcast-policy"
                                self.yang_parent_name = "relay"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdBroadcastFlagPolicy', '')])),
                                ])
                                self.policy = None
                                self._segment_path = lambda: "broadcast-policy"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, ['policy'], name, value)


                    class Proxy(Entity):
                        """
                        DHCP proxy profile
                        
                        .. attribute:: giaddr
                        
                        	Specify gateway address policy
                        	**type**\:  :py:class:`Giaddr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: classes
                        
                        	DHCP class table
                        	**type**\:  :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes>`
                        
                        .. attribute:: auth_username
                        
                        	Authentication Username formating
                        	**type**\:  :py:class:`AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: relay_information
                        
                        	Relay agent information option
                        	**type**\:  :py:class:`RelayInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation>`
                        
                        .. attribute:: dhcp_to_aaa
                        
                        	Enable to provide the list of options need to send to aaa
                        	**type**\:  :py:class:`DhcpToAaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa>`
                        
                        .. attribute:: vrfs
                        
                        	List of VRFs
                        	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs>`
                        
                        .. attribute:: sessions
                        
                        	Change sessions configuration
                        	**type**\:  :py:class:`Sessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions>`
                        
                        .. attribute:: limit_lease
                        
                        	Proxy limit lease
                        	**type**\:  :py:class:`LimitLease <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: lease_proxy
                        
                        	DHCPv4 lease proxy
                        	**type**\:  :py:class:`LeaseProxy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy>`
                        
                        .. attribute:: broadcast_flag
                        
                        	Specify broadcast flag
                        	**type**\:  :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: match
                        
                        	Insert match keyword
                        	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match>`
                        
                        .. attribute:: proxy_allow_move
                        
                        	Allow dhcp subscriber move
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: secure_arp
                        
                        	DHCP IPV4 profile proxy secure\-arp enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: delayed_authen_proxy
                        
                        	For BNG session, delay the authentication
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: enable
                        
                        	DHCP IPV4 profile mode enable
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, self).__init__()

                            self.yang_name = "proxy"
                            self.yang_parent_name = "mode"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("giaddr", ("giaddr", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr)), ("classes", ("classes", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes)), ("auth-username", ("auth_username", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername)), ("relay-information", ("relay_information", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation)), ("dhcp-to-aaa", ("dhcp_to_aaa", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa)), ("vrfs", ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs)), ("sessions", ("sessions", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions)), ("limit-lease", ("limit_lease", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease)), ("lease-proxy", ("lease_proxy", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy)), ("broadcast-flag", ("broadcast_flag", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag)), ("match", ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match))])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('proxy_allow_move', (YLeaf(YType.empty, 'proxy-allow-move'), ['Empty'])),
                                ('secure_arp', (YLeaf(YType.empty, 'secure-arp'), ['Empty'])),
                                ('delayed_authen_proxy', (YLeaf(YType.empty, 'delayed-authen-proxy'), ['Empty'])),
                                ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                            ])
                            self.proxy_allow_move = None
                            self.secure_arp = None
                            self.delayed_authen_proxy = None
                            self.enable = None

                            self.giaddr = None
                            self._children_name_map["giaddr"] = "giaddr"

                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"

                            self.auth_username = None
                            self._children_name_map["auth_username"] = "auth-username"

                            self.relay_information = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation()
                            self.relay_information.parent = self
                            self._children_name_map["relay_information"] = "relay-information"

                            self.dhcp_to_aaa = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa()
                            self.dhcp_to_aaa.parent = self
                            self._children_name_map["dhcp_to_aaa"] = "dhcp-to-aaa"

                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs()
                            self.vrfs.parent = self
                            self._children_name_map["vrfs"] = "vrfs"

                            self.sessions = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions()
                            self.sessions.parent = self
                            self._children_name_map["sessions"] = "sessions"

                            self.limit_lease = None
                            self._children_name_map["limit_lease"] = "limit-lease"

                            self.lease_proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy()
                            self.lease_proxy.parent = self
                            self._children_name_map["lease_proxy"] = "lease-proxy"

                            self.broadcast_flag = None
                            self._children_name_map["broadcast_flag"] = "broadcast-flag"

                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match()
                            self.match.parent = self
                            self._children_name_map["match"] = "match"
                            self._segment_path = lambda: "proxy"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, ['proxy_allow_move', 'secure_arp', 'delayed_authen_proxy', 'enable'], name, value)


                        class Giaddr(Entity):
                            """
                            Specify gateway address policy
                            
                            .. attribute:: policy
                            
                            	Gateway address policy
                            	**type**\:  :py:class:`Ipv4dhcpdGiaddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdGiaddrPolicy>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr, self).__init__()

                                self.yang_name = "giaddr"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdGiaddrPolicy', '')])),
                                ])
                                self.policy = None
                                self._segment_path = lambda: "giaddr"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Giaddr, ['policy'], name, value)


                        class Classes(Entity):
                            """
                            DHCP class table
                            
                            .. attribute:: class_
                            
                            	DHCP class
                            	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("class", ("class_", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class))])
                                self._leafs = OrderedDict()

                                self.class_ = YList(self)
                                self._segment_path = lambda: "classes"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, [], name, value)


                            class Class(Entity):
                                """
                                DHCP class
                                
                                .. attribute:: class_name  (key)
                                
                                	Class name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: match
                                
                                	Match option
                                	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match>`
                                
                                .. attribute:: vrfs
                                
                                	List of VRFs
                                	**type**\:  :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs>`
                                
                                .. attribute:: enable
                                
                                	Enable the DHCP IPV4 proxy class
                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['class_name']
                                    self._child_classes = OrderedDict([("match", ("match", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match)), ("vrfs", ("vrfs", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs))])
                                    self._leafs = OrderedDict([
                                        ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                                        ('enable', (YLeaf(YType.empty, 'enable'), ['Empty'])),
                                    ])
                                    self.class_name = None
                                    self.enable = None

                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"

                                    self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs()
                                    self.vrfs.parent = self
                                    self._children_name_map["vrfs"] = "vrfs"
                                    self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class, ['class_name', 'enable'], name, value)


                                class Match(Entity):
                                    """
                                    Match option
                                    
                                    .. attribute:: option
                                    
                                    	Match option
                                    	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match.Option>`
                                    
                                    .. attribute:: vrf
                                    
                                    	Match VRF name
                                    	**type**\: str
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match, self).__init__()

                                        self.yang_name = "match"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("option", ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match.Option))])
                                        self._leafs = OrderedDict([
                                            ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                        ])
                                        self.vrf = None

                                        self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match.Option()
                                        self.option.parent = self
                                        self._children_name_map["option"] = "option"
                                        self._segment_path = lambda: "match"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match, ['vrf'], name, value)


                                    class Option(Entity):
                                        """
                                        Match option
                                        
                                        .. attribute:: option_type
                                        
                                        	Match option
                                        	**type**\:  :py:class:`Dhcpv4MatchOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4MatchOption>`
                                        
                                        .. attribute:: pattern
                                        
                                        	Hex pattern string
                                        	**type**\: str
                                        
                                        .. attribute:: bit_mask
                                        
                                        	Bit mask pattern
                                        	**type**\: str
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match.Option, self).__init__()

                                            self.yang_name = "option"
                                            self.yang_parent_name = "match"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('option_type', (YLeaf(YType.enumeration, 'option-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4MatchOption', '')])),
                                                ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                                                ('bit_mask', (YLeaf(YType.str, 'bit-mask'), ['str'])),
                                            ])
                                            self.option_type = None
                                            self.pattern = None
                                            self.bit_mask = None
                                            self._segment_path = lambda: "option"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Match.Option, ['option_type', 'pattern', 'bit_mask'], name, value)


                                class Vrfs(Entity):
                                    """
                                    List of VRFs
                                    
                                    .. attribute:: vrf
                                    
                                    	VRF name
                                    	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs, self).__init__()

                                        self.yang_name = "vrfs"
                                        self.yang_parent_name = "class"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf))])
                                        self._leafs = OrderedDict()

                                        self.vrf = YList(self)
                                        self._segment_path = lambda: "vrfs"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs, [], name, value)


                                    class Vrf(Entity):
                                        """
                                        VRF name
                                        
                                        .. attribute:: vrf_name  (key)
                                        
                                        	VRF name
                                        	**type**\: str
                                        
                                        	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                        
                                        .. attribute:: helper_addresses
                                        
                                        	Helper addresses
                                        	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf, self).__init__()

                                            self.yang_name = "vrf"
                                            self.yang_parent_name = "vrfs"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['vrf_name']
                                            self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses))])
                                            self._leafs = OrderedDict([
                                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                            ])
                                            self.vrf_name = None

                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self
                                            self._children_name_map["helper_addresses"] = "helper-addresses"
                                            self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf, ['vrf_name'], name, value)


                                        class HelperAddresses(Entity):
                                            """
                                            Helper addresses
                                            
                                            .. attribute:: helper_address
                                            
                                            	Helper address
                                            	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2017-09-30'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses, self).__init__()

                                                self.yang_name = "helper-addresses"
                                                self.yang_parent_name = "vrf"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = []
                                                self._child_classes = OrderedDict([("helper-address", ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses.HelperAddress))])
                                                self._leafs = OrderedDict()

                                                self.helper_address = YList(self)
                                                self._segment_path = lambda: "helper-addresses"
                                                self._is_frozen = True

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses, [], name, value)


                                            class HelperAddress(Entity):
                                                """
                                                Helper address
                                                
                                                .. attribute:: server_address  (key)
                                                
                                                	IPv4 address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                .. attribute:: gateway_address
                                                
                                                	Gateway address
                                                	**type**\: str
                                                
                                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                                
                                                	**mandatory**\: True
                                                
                                                

                                                """

                                                _prefix = 'ipv4-dhcpd-cfg'
                                                _revision = '2017-09-30'

                                                def __init__(self):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                                    self.yang_name = "helper-address"
                                                    self.yang_parent_name = "helper-addresses"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = ['server_address']
                                                    self._child_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                                                        ('gateway_address', (YLeaf(YType.str, 'gateway-address'), ['str'])),
                                                    ])
                                                    self.server_address = None
                                                    self.gateway_address = None
                                                    self._segment_path = lambda: "helper-address" + "[server-address='" + str(self.server_address) + "']"
                                                    self._is_frozen = True

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class.Vrfs.Vrf.HelperAddresses.HelperAddress, ['server_address', 'gateway_address'], name, value)


                        class AuthUsername(Entity):
                            """
                            Authentication Username formating
                            
                            .. attribute:: arg1
                            
                            	Username Formatting first argument 
                            	**type**\:  :py:class:`Dhcpv4AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4AuthUsername>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: arg2
                            
                            	Username Formatting second argument 
                            	**type**\:  :py:class:`Dhcpv4AuthUsername <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4AuthUsername>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername, self).__init__()

                                self.yang_name = "auth-username"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('arg1', (YLeaf(YType.enumeration, 'arg1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4AuthUsername', '')])),
                                    ('arg2', (YLeaf(YType.enumeration, 'arg2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4AuthUsername', '')])),
                                ])
                                self.arg1 = None
                                self.arg2 = None
                                self._segment_path = lambda: "auth-username"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.AuthUsername, ['arg1', 'arg2'], name, value)


                        class RelayInformation(Entity):
                            """
                            Relay agent information option
                            
                            .. attribute:: option
                            
                            	Insert relay rgent information circuit ID and remote ID suboptions in client requests
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: circuit_id
                            
                            	Insert Circuit\-id sub\-option
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: policy
                            
                            	Relay information option policy
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionvpnMode>`
                            
                            .. attribute:: remote_id_xr
                            
                            	Insert Remote\-id sub\-option
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: remote_id_suppress
                            
                            	Suppress Remote ID
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: check
                            
                            	Check relay agent information option in server reply
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: remote_id
                            
                            	Remote ID
                            	**type**\: str
                            
                            .. attribute:: authenticate
                            
                            	Relay information option authenticate
                            	**type**\:  :py:class:`Ipv4dhcpdRelayInfoOptionAuthenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdRelayInfoOptionAuthenticate>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, self).__init__()

                                self.yang_name = "relay-information"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('option', (YLeaf(YType.empty, 'option'), ['Empty'])),
                                    ('vpn', (YLeaf(YType.empty, 'vpn'), ['Empty'])),
                                    ('allow_untrusted', (YLeaf(YType.empty, 'allow-untrusted'), ['Empty'])),
                                    ('circuit_id', (YLeaf(YType.empty, 'circuit-id'), ['Empty'])),
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionPolicy', '')])),
                                    ('vpn_mode', (YLeaf(YType.enumeration, 'vpn-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionvpnMode', '')])),
                                    ('remote_id_xr', (YLeaf(YType.empty, 'remote-id-xr'), ['Empty'])),
                                    ('remote_id_suppress', (YLeaf(YType.empty, 'remote-id-suppress'), ['Empty'])),
                                    ('check', (YLeaf(YType.empty, 'check'), ['Empty'])),
                                    ('remote_id', (YLeaf(YType.str, 'remote-id'), ['str'])),
                                    ('authenticate', (YLeaf(YType.enumeration, 'authenticate'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdRelayInfoOptionAuthenticate', '')])),
                                ])
                                self.option = None
                                self.vpn = None
                                self.allow_untrusted = None
                                self.circuit_id = None
                                self.policy = None
                                self.vpn_mode = None
                                self.remote_id_xr = None
                                self.remote_id_suppress = None
                                self.check = None
                                self.remote_id = None
                                self.authenticate = None
                                self._segment_path = lambda: "relay-information"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, ['option', 'vpn', 'allow_untrusted', 'circuit_id', 'policy', 'vpn_mode', 'remote_id_xr', 'remote_id_suppress', 'check', 'remote_id', 'authenticate'], name, value)


                        class DhcpToAaa(Entity):
                            """
                            Enable to provide the list of options need
                            to send to aaa
                            
                            .. attribute:: option
                            
                            	option type
                            	**type**\:  :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa, self).__init__()

                                self.yang_name = "dhcp-to-aaa"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("option", ("option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option))])
                                self._leafs = OrderedDict()

                                self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option()
                                self.option.parent = self
                                self._children_name_map["option"] = "option"
                                self._segment_path = lambda: "dhcp-to-aaa"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa, [], name, value)


                            class Option(Entity):
                                """
                                option type
                                
                                .. attribute:: list
                                
                                	List of options
                                	**type**\:  :py:class:`List <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option.List>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option, self).__init__()

                                    self.yang_name = "option"
                                    self.yang_parent_name = "dhcp-to-aaa"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("list", ("list", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option.List))])
                                    self._leafs = OrderedDict()

                                    self.list = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option.List()
                                    self.list.parent = self
                                    self._children_name_map["list"] = "list"
                                    self._segment_path = lambda: "option"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option, [], name, value)


                                class List(Entity):
                                    """
                                    List of options
                                    
                                    .. attribute:: option_all
                                    
                                    	option all
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: option
                                    
                                    	List of options
                                    	**type**\: list of int
                                    
                                    	**range:** 1..255
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option.List, self).__init__()

                                        self.yang_name = "list"
                                        self.yang_parent_name = "option"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('option_all', (YLeaf(YType.uint32, 'option-all'), ['int'])),
                                            ('option', (YLeafList(YType.uint32, 'option'), ['int'])),
                                        ])
                                        self.option_all = None
                                        self.option = []
                                        self._segment_path = lambda: "list"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.DhcpToAaa.Option.List, ['option_all', 'option'], name, value)


                        class Vrfs(Entity):
                            """
                            List of VRFs
                            
                            .. attribute:: vrf
                            
                            	VRF name
                            	**type**\: list of  		 :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("vrf", ("vrf", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf))])
                                self._leafs = OrderedDict()

                                self.vrf = YList(self)
                                self._segment_path = lambda: "vrfs"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, [], name, value)


                            class Vrf(Entity):
                                """
                                VRF name
                                
                                .. attribute:: vrf_name  (key)
                                
                                	VRF name
                                	**type**\: str
                                
                                	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                                
                                .. attribute:: helper_addresses
                                
                                	Helper addresses
                                	**type**\:  :py:class:`HelperAddresses <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['vrf_name']
                                    self._child_classes = OrderedDict([("helper-addresses", ("helper_addresses", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses))])
                                    self._leafs = OrderedDict([
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.vrf_name = None

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._segment_path = lambda: "vrf" + "[vrf-name='" + str(self.vrf_name) + "']"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, ['vrf_name'], name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper address
                                    	**type**\: list of  		 :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("helper-address", ("helper_address", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress))])
                                        self._leafs = OrderedDict()

                                        self.helper_address = YList(self)
                                        self._segment_path = lambda: "helper-addresses"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, [], name, value)


                                    class HelperAddress(Entity):
                                        """
                                        Helper address
                                        
                                        .. attribute:: server_address  (key)
                                        
                                        	IPv4 address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        .. attribute:: gateway_address
                                        
                                        	Gateway address
                                        	**type**\: str
                                        
                                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                        
                                        	**mandatory**\: True
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2017-09-30'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = ['server_address']
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('server_address', (YLeaf(YType.str, 'server-address'), ['str'])),
                                                ('gateway_address', (YLeaf(YType.str, 'gateway-address'), ['str'])),
                                            ])
                                            self.server_address = None
                                            self.gateway_address = None
                                            self._segment_path = lambda: "helper-address" + "[server-address='" + str(self.server_address) + "']"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, ['server_address', 'gateway_address'], name, value)


                        class Sessions(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: proxy_throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:  :py:class:`ProxyThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions, self).__init__()

                                self.yang_name = "sessions"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("proxy-throttle-type", ("proxy_throttle_type", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType))])
                                self._leafs = OrderedDict()

                                self.proxy_throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType()
                                self.proxy_throttle_type.parent = self
                                self._children_name_map["proxy_throttle_type"] = "proxy-throttle-type"
                                self._segment_path = lambda: "sessions"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions, [], name, value)


                            class ProxyThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: proxy_mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:  :py:class:`ProxyMacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType, self).__init__()

                                    self.yang_name = "proxy-throttle-type"
                                    self.yang_parent_name = "sessions"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("proxy-mac-throttle", ("proxy_mac_throttle", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle))])
                                    self._leafs = OrderedDict()

                                    self.proxy_mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle()
                                    self.proxy_mac_throttle.parent = self
                                    self._children_name_map["proxy_mac_throttle"] = "proxy-mac-throttle"
                                    self._segment_path = lambda: "proxy-throttle-type"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType, [], name, value)


                                class ProxyMacThrottle(Entity):
                                    """
                                    Throttle DHCP sessions from any one MAC
                                    address
                                    
                                    .. attribute:: num_discover
                                    
                                    	Number of discovers at which to throttle
                                    	**type**\: int
                                    
                                    	**range:** 1..65535
                                    
                                    .. attribute:: num_request
                                    
                                    	Throttle request period (in secs)
                                    	**type**\: int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    .. attribute:: num_block
                                    
                                    	Throttle blocking period (in secs)
                                    	**type**\: int
                                    
                                    	**range:** 1..100
                                    
                                    	**units**\: second
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, self).__init__()

                                        self.yang_name = "proxy-mac-throttle"
                                        self.yang_parent_name = "proxy-throttle-type"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('num_discover', (YLeaf(YType.uint32, 'num-discover'), ['int'])),
                                            ('num_request', (YLeaf(YType.uint32, 'num-request'), ['int'])),
                                            ('num_block', (YLeaf(YType.uint32, 'num-block'), ['int'])),
                                        ])
                                        self.num_discover = None
                                        self.num_request = None
                                        self.num_block = None
                                        self._segment_path = lambda: "proxy-mac-throttle"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, ['num_discover', 'num_request', 'num_block'], name, value)


                        class LimitLease(Entity):
                            """
                            Proxy limit lease
                            
                            .. attribute:: limit_type
                            
                            	Lease limit type
                            	**type**\:  :py:class:`Dhcpv4LimitLease1 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Dhcpv4LimitLease1>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: limit_lease_count
                            
                            	Limit lease count
                            	**type**\: int
                            
                            	**range:** 1..240000
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, self).__init__()

                                self.yang_name = "limit-lease"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('limit_type', (YLeaf(YType.enumeration, 'limit-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Dhcpv4LimitLease1', '')])),
                                    ('limit_lease_count', (YLeaf(YType.uint32, 'limit-lease-count'), ['int'])),
                                ])
                                self.limit_type = None
                                self.limit_lease_count = None
                                self._segment_path = lambda: "limit-lease"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, ['limit_type', 'limit_lease_count'], name, value)


                        class LeaseProxy(Entity):
                            """
                            DHCPv4 lease proxy
                            
                            .. attribute:: client_lease_time
                            
                            	Specify client lease proxy time
                            	**type**\: int
                            
                            	**range:** 300..4294967295
                            
                            .. attribute:: set_server_options
                            
                            	Set DHCP server sent options in lease proxy generating ACK
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, self).__init__()

                                self.yang_name = "lease-proxy"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('client_lease_time', (YLeaf(YType.uint32, 'client-lease-time'), ['int'])),
                                    ('set_server_options', (YLeaf(YType.empty, 'set-server-options'), ['Empty'])),
                                ])
                                self.client_lease_time = None
                                self.set_server_options = None
                                self._segment_path = lambda: "lease-proxy"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, ['client_lease_time', 'set_server_options'], name, value)


                        class BroadcastFlag(Entity):
                            """
                            Specify broadcast flag
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:  :py:class:`Ipv4dhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdBroadcastFlagPolicy>`
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('policy', (YLeaf(YType.enumeration, 'policy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdBroadcastFlagPolicy', '')])),
                                ])
                                self.policy = None
                                self._segment_path = lambda: "broadcast-flag"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, ['policy'], name, value)


                        class Match(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: def_options
                            
                            	Table of Option
                            	**type**\:  :py:class:`DefOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions>`
                            
                            .. attribute:: option_filters
                            
                            	Table of Option
                            	**type**\:  :py:class:`OptionFilters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2017-09-30'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "proxy"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("def-options", ("def_options", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions)), ("option-filters", ("option_filters", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters))])
                                self._leafs = OrderedDict()

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"
                                self._segment_path = lambda: "match"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match, [], name, value)


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("def-option", ("def_option", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption))])
                                    self._leafs = OrderedDict()

                                    self.def_option = YList(self)
                                    self._segment_path = lambda: "def-options"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, [], name, value)


                                class DefOption(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: def_matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: def_matchaction
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`ProxyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['def_matchoption']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('def_matchoption', (YLeaf(YType.uint32, 'def-matchoption'), ['int'])),
                                            ('def_matchaction', (YLeaf(YType.enumeration, 'def-matchaction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'ProxyAction', '')])),
                                        ])
                                        self.def_matchoption = None
                                        self.def_matchaction = None
                                        self._segment_path = lambda: "def-option" + "[def-matchoption='" + str(self.def_matchoption) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, ['def_matchoption', 'def_matchaction'], name, value)


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of  		 :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2017-09-30'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("option-filter", ("option_filter", Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter))])
                                    self._leafs = OrderedDict()

                                    self.option_filter = YList(self)
                                    self._segment_path = lambda: "option-filters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, [], name, value)


                                class OptionFilter(Entity):
                                    """
                                    Specify match option
                                    
                                    .. attribute:: matchoption  (key)
                                    
                                    	Match option 60
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: pattern  (key)
                                    
                                    	Enter hex pattern string
                                    	**type**\: str
                                    
                                    	**length:** 1..64
                                    
                                    .. attribute:: format  (key)
                                    
                                    	Set constant integer
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: matchaction
                                    
                                    	Vendor action
                                    	**type**\:  :py:class:`ProxyAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.ProxyAction>`
                                    
                                    	**mandatory**\: True
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2017-09-30'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['matchoption','pattern','format']
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('matchoption', (YLeaf(YType.uint32, 'matchoption'), ['int'])),
                                            ('pattern', (YLeaf(YType.str, 'pattern'), ['str'])),
                                            ('format', (YLeaf(YType.uint32, 'format'), ['int'])),
                                            ('matchaction', (YLeaf(YType.enumeration, 'matchaction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'ProxyAction', '')])),
                                        ])
                                        self.matchoption = None
                                        self.pattern = None
                                        self.format = None
                                        self.matchaction = None
                                        self._segment_path = lambda: "option-filter" + "[matchoption='" + str(self.matchoption) + "']" + "[pattern='" + str(self.pattern) + "']" + "[format='" + str(self.format) + "']"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, ['matchoption', 'pattern', 'format', 'matchaction'], name, value)


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
        
        .. attribute:: snoop
        
        	Enable DHCP snoop binding database storage to file system
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

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('proxy', (YLeaf(YType.empty, 'proxy'), ['Empty'])),
                ('server', (YLeaf(YType.empty, 'server'), ['Empty'])),
                ('snoop', (YLeaf(YType.empty, 'snoop'), ['Empty'])),
                ('full_write_interval', (YLeaf(YType.uint32, 'full-write-interval'), ['int'])),
                ('incremental_write_interval', (YLeaf(YType.uint32, 'incremental-write-interval'), ['int'])),
            ])
            self.proxy = None
            self.server = None
            self.snoop = None
            self.full_write_interval = None
            self.incremental_write_interval = None
            self._segment_path = lambda: "database"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Database, ['proxy', 'server', 'snoop', 'full_write_interval', 'incremental_write_interval'], name, value)


    class Interfaces(Entity):
        """
        DHCP IPV4 Interface Table
        
        .. attribute:: interface
        
        	DHCP IPV4 Interface
        	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("interface", ("interface", Ipv4Dhcpd.Interfaces.Interface))])
            self._leafs = OrderedDict()

            self.interface = YList(self)
            self._segment_path = lambda: "interfaces"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.Interfaces, [], name, value)


        class Interface(Entity):
            """
            DHCP IPV4 Interface
            
            .. attribute:: interface_name  (key)
            
            	Interface Name
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
            
            .. attribute:: proxy_interface
            
            	DHCP IPv4 proxy information
            	**type**\:  :py:class:`ProxyInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface>`
            
            .. attribute:: base_interface
            
            	DHCP IPv4 Base profile information
            	**type**\:  :py:class:`BaseInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface>`
            
            .. attribute:: relay_interface
            
            	DHCP IPv4 relay information
            	**type**\:  :py:class:`RelayInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface>`
            
            .. attribute:: static_mode
            
            	Static Table Entries containing MAC address to IP address bindings
            	**type**\:  :py:class:`StaticMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode>`
            
            .. attribute:: profile
            
            	Profile name and mode
            	**type**\:  :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.Profile>`
            
            	**presence node**\: True
            
            .. attribute:: server_interface
            
            	DHCP IPv4 Server information
            	**type**\:  :py:class:`ServerInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface>`
            
            .. attribute:: snoop_interface
            
            	DHCP IPv4 snoop information
            	**type**\:  :py:class:`SnoopInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface>`
            
            

            """

            _prefix = 'ipv4-dhcpd-cfg'
            _revision = '2017-09-30'

            def __init__(self):
                super(Ipv4Dhcpd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface_name']
                self._child_classes = OrderedDict([("proxy-interface", ("proxy_interface", Ipv4Dhcpd.Interfaces.Interface.ProxyInterface)), ("base-interface", ("base_interface", Ipv4Dhcpd.Interfaces.Interface.BaseInterface)), ("relay-interface", ("relay_interface", Ipv4Dhcpd.Interfaces.Interface.RelayInterface)), ("static-mode", ("static_mode", Ipv4Dhcpd.Interfaces.Interface.StaticMode)), ("profile", ("profile", Ipv4Dhcpd.Interfaces.Interface.Profile)), ("server-interface", ("server_interface", Ipv4Dhcpd.Interfaces.Interface.ServerInterface)), ("snoop-interface", ("snoop_interface", Ipv4Dhcpd.Interfaces.Interface.SnoopInterface))])
                self._leafs = OrderedDict([
                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                ])
                self.interface_name = None

                self.proxy_interface = Ipv4Dhcpd.Interfaces.Interface.ProxyInterface()
                self.proxy_interface.parent = self
                self._children_name_map["proxy_interface"] = "proxy-interface"

                self.base_interface = Ipv4Dhcpd.Interfaces.Interface.BaseInterface()
                self.base_interface.parent = self
                self._children_name_map["base_interface"] = "base-interface"

                self.relay_interface = Ipv4Dhcpd.Interfaces.Interface.RelayInterface()
                self.relay_interface.parent = self
                self._children_name_map["relay_interface"] = "relay-interface"

                self.static_mode = Ipv4Dhcpd.Interfaces.Interface.StaticMode()
                self.static_mode.parent = self
                self._children_name_map["static_mode"] = "static-mode"

                self.profile = None
                self._children_name_map["profile"] = "profile"

                self.server_interface = Ipv4Dhcpd.Interfaces.Interface.ServerInterface()
                self.server_interface.parent = self
                self._children_name_map["server_interface"] = "server-interface"

                self.snoop_interface = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface()
                self.snoop_interface.parent = self
                self._children_name_map["snoop_interface"] = "snoop-interface"
                self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/interfaces/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface, ['interface_name'], name, value)


            class ProxyInterface(Entity):
                """
                DHCP IPv4 proxy information
                
                .. attribute:: dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`DhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, self).__init__()

                    self.yang_name = "proxy-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("dhcp-circuit-id", ("dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId))])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None

                    self.dhcp_circuit_id = None
                    self._children_name_map["dhcp_circuit_id"] = "dhcp-circuit-id"
                    self._segment_path = lambda: "proxy-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, ['profile'], name, value)


                class DhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, self).__init__()

                        self.yang_name = "dhcp-circuit-id"
                        self.yang_parent_name = "proxy-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                            ('format', (YLeaf(YType.enumeration, 'format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmt', '')])),
                            ('argument1', (YLeaf(YType.enumeration, 'argument1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument2', (YLeaf(YType.enumeration, 'argument2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument3', (YLeaf(YType.enumeration, 'argument3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument4', (YLeaf(YType.enumeration, 'argument4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument5', (YLeaf(YType.enumeration, 'argument5'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument6', (YLeaf(YType.enumeration, 'argument6'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument7', (YLeaf(YType.enumeration, 'argument7'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument8', (YLeaf(YType.enumeration, 'argument8'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument9', (YLeaf(YType.enumeration, 'argument9'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument10', (YLeaf(YType.enumeration, 'argument10'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument11', (YLeaf(YType.enumeration, 'argument11'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument12', (YLeaf(YType.enumeration, 'argument12'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument13', (YLeaf(YType.enumeration, 'argument13'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument14', (YLeaf(YType.enumeration, 'argument14'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument15', (YLeaf(YType.enumeration, 'argument15'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument16', (YLeaf(YType.enumeration, 'argument16'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                        ])
                        self.circuit_id = None
                        self.format = None
                        self.argument1 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self._segment_path = lambda: "dhcp-circuit-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, ['circuit_id', 'format', 'argument1', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16'], name, value)


            class BaseInterface(Entity):
                """
                DHCP IPv4 Base profile information
                
                .. attribute:: base_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`BaseDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, self).__init__()

                    self.yang_name = "base-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("base-dhcp-circuit-id", ("base_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId))])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None

                    self.base_dhcp_circuit_id = None
                    self._children_name_map["base_dhcp_circuit_id"] = "base-dhcp-circuit-id"
                    self._segment_path = lambda: "base-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, ['profile'], name, value)


                class BaseDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, self).__init__()

                        self.yang_name = "base-dhcp-circuit-id"
                        self.yang_parent_name = "base-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                            ('format', (YLeaf(YType.enumeration, 'format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmt', '')])),
                            ('argument1', (YLeaf(YType.enumeration, 'argument1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument2', (YLeaf(YType.enumeration, 'argument2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument3', (YLeaf(YType.enumeration, 'argument3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument4', (YLeaf(YType.enumeration, 'argument4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument5', (YLeaf(YType.enumeration, 'argument5'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument6', (YLeaf(YType.enumeration, 'argument6'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument7', (YLeaf(YType.enumeration, 'argument7'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument8', (YLeaf(YType.enumeration, 'argument8'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument9', (YLeaf(YType.enumeration, 'argument9'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument10', (YLeaf(YType.enumeration, 'argument10'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument11', (YLeaf(YType.enumeration, 'argument11'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument12', (YLeaf(YType.enumeration, 'argument12'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument13', (YLeaf(YType.enumeration, 'argument13'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument14', (YLeaf(YType.enumeration, 'argument14'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument15', (YLeaf(YType.enumeration, 'argument15'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument16', (YLeaf(YType.enumeration, 'argument16'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                        ])
                        self.circuit_id = None
                        self.format = None
                        self.argument1 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self._segment_path = lambda: "base-dhcp-circuit-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, ['circuit_id', 'format', 'argument1', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16'], name, value)


            class RelayInterface(Entity):
                """
                DHCP IPv4 relay information
                
                .. attribute:: relay_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`RelayDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface, self).__init__()

                    self.yang_name = "relay-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("relay-dhcp-circuit-id", ("relay_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId))])
                    self._leafs = OrderedDict()

                    self.relay_dhcp_circuit_id = None
                    self._children_name_map["relay_dhcp_circuit_id"] = "relay-dhcp-circuit-id"
                    self._segment_path = lambda: "relay-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.RelayInterface, [], name, value)


                class RelayDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, self).__init__()

                        self.yang_name = "relay-dhcp-circuit-id"
                        self.yang_parent_name = "relay-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                            ('format', (YLeaf(YType.enumeration, 'format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmt', '')])),
                            ('argument1', (YLeaf(YType.enumeration, 'argument1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument2', (YLeaf(YType.enumeration, 'argument2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument3', (YLeaf(YType.enumeration, 'argument3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument4', (YLeaf(YType.enumeration, 'argument4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument5', (YLeaf(YType.enumeration, 'argument5'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument6', (YLeaf(YType.enumeration, 'argument6'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument7', (YLeaf(YType.enumeration, 'argument7'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument8', (YLeaf(YType.enumeration, 'argument8'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument9', (YLeaf(YType.enumeration, 'argument9'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument10', (YLeaf(YType.enumeration, 'argument10'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument11', (YLeaf(YType.enumeration, 'argument11'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument12', (YLeaf(YType.enumeration, 'argument12'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument13', (YLeaf(YType.enumeration, 'argument13'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument14', (YLeaf(YType.enumeration, 'argument14'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument15', (YLeaf(YType.enumeration, 'argument15'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument16', (YLeaf(YType.enumeration, 'argument16'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                        ])
                        self.circuit_id = None
                        self.format = None
                        self.argument1 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self._segment_path = lambda: "relay-dhcp-circuit-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, ['circuit_id', 'format', 'argument1', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16'], name, value)


            class StaticMode(Entity):
                """
                Static Table Entries containing MAC address to
                IP address bindings
                
                .. attribute:: statics
                
                	Static Table Entries containing MAC address to IP address bindings
                	**type**\:  :py:class:`Statics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.StaticMode, self).__init__()

                    self.yang_name = "static-mode"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("statics", ("statics", Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics))])
                    self._leafs = OrderedDict()

                    self.statics = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics()
                    self.statics.parent = self
                    self._children_name_map["statics"] = "statics"
                    self._segment_path = lambda: "static-mode"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.StaticMode, [], name, value)


                class Statics(Entity):
                    """
                    Static Table Entries containing MAC address
                    to IP address bindings
                    
                    .. attribute:: static
                    
                    	DHCP static binding of Mac address to IP address
                    	**type**\: list of  		 :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, self).__init__()

                        self.yang_name = "statics"
                        self.yang_parent_name = "static-mode"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("static", ("static", Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static))])
                        self._leafs = OrderedDict()

                        self.static = YList(self)
                        self._segment_path = lambda: "statics"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, [], name, value)


                    class Static(Entity):
                        """
                        DHCP static binding of Mac address to IP
                        address
                        
                        .. attribute:: mac_address  (key)
                        
                        	MACAddress
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: client_id  (key)
                        
                        	Client Id
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: layer  (key)
                        
                        	DHCP IPV4 Static layer
                        	**type**\:  :py:class:`Ipv4dhcpdLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdLayer>`
                        
                        .. attribute:: static_address
                        
                        	IP address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2017-09-30'

                        def __init__(self):
                            super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, self).__init__()

                            self.yang_name = "static"
                            self.yang_parent_name = "statics"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mac_address','client_id','layer']
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mac_address', (YLeaf(YType.str, 'mac-address'), ['str'])),
                                ('client_id', (YLeaf(YType.uint32, 'client-id'), ['int'])),
                                ('layer', (YLeaf(YType.enumeration, 'layer'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdLayer', '')])),
                                ('static_address', (YLeaf(YType.str, 'static-address'), ['str'])),
                            ])
                            self.mac_address = None
                            self.client_id = None
                            self.layer = None
                            self.static_address = None
                            self._segment_path = lambda: "static" + "[mac-address='" + str(self.mac_address) + "']" + "[client-id='" + str(self.client_id) + "']" + "[layer='" + str(self.layer) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, ['mac_address', 'client_id', 'layer', 'static_address'], name, value)


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: profile_name
                
                	Profile name
                	**type**\: str
                
                	**mandatory**\: True
                
                .. attribute:: mode
                
                	DHCP mode
                	**type**\:  :py:class:`Ipv4dhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdMode>`
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('profile_name', (YLeaf(YType.str, 'profile-name'), ['str'])),
                        ('mode', (YLeaf(YType.enumeration, 'mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdMode', '')])),
                    ])
                    self.profile_name = None
                    self.mode = None
                    self._segment_path = lambda: "profile"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.Profile, ['profile_name', 'mode'], name, value)


            class ServerInterface(Entity):
                """
                DHCP IPv4 Server information
                
                .. attribute:: server_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:  :py:class:`ServerDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId>`
                
                	**presence node**\: True
                
                .. attribute:: profile
                
                	Interface profile name
                	**type**\: str
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, self).__init__()

                    self.yang_name = "server-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("server-dhcp-circuit-id", ("server_dhcp_circuit_id", Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId))])
                    self._leafs = OrderedDict([
                        ('profile', (YLeaf(YType.str, 'profile'), ['str'])),
                    ])
                    self.profile = None

                    self.server_dhcp_circuit_id = None
                    self._children_name_map["server_dhcp_circuit_id"] = "server-dhcp-circuit-id"
                    self._segment_path = lambda: "server-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, ['profile'], name, value)


                class ServerDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\: str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:  :py:class:`Ipv4dhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:  :py:class:`Ipv4dhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4dhcpdFmtSpecifier>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, self).__init__()

                        self.yang_name = "server-dhcp-circuit-id"
                        self.yang_parent_name = "server-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('circuit_id', (YLeaf(YType.str, 'circuit-id'), ['str'])),
                            ('format', (YLeaf(YType.enumeration, 'format'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmt', '')])),
                            ('argument1', (YLeaf(YType.enumeration, 'argument1'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument2', (YLeaf(YType.enumeration, 'argument2'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument3', (YLeaf(YType.enumeration, 'argument3'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument4', (YLeaf(YType.enumeration, 'argument4'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument5', (YLeaf(YType.enumeration, 'argument5'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument6', (YLeaf(YType.enumeration, 'argument6'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument7', (YLeaf(YType.enumeration, 'argument7'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument8', (YLeaf(YType.enumeration, 'argument8'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument9', (YLeaf(YType.enumeration, 'argument9'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument10', (YLeaf(YType.enumeration, 'argument10'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument11', (YLeaf(YType.enumeration, 'argument11'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument12', (YLeaf(YType.enumeration, 'argument12'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument13', (YLeaf(YType.enumeration, 'argument13'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument14', (YLeaf(YType.enumeration, 'argument14'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument15', (YLeaf(YType.enumeration, 'argument15'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                            ('argument16', (YLeaf(YType.enumeration, 'argument16'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg', 'Ipv4dhcpdFmtSpecifier', '')])),
                        ])
                        self.circuit_id = None
                        self.format = None
                        self.argument1 = None
                        self.argument2 = None
                        self.argument3 = None
                        self.argument4 = None
                        self.argument5 = None
                        self.argument6 = None
                        self.argument7 = None
                        self.argument8 = None
                        self.argument9 = None
                        self.argument10 = None
                        self.argument11 = None
                        self.argument12 = None
                        self.argument13 = None
                        self.argument14 = None
                        self.argument15 = None
                        self.argument16 = None
                        self._segment_path = lambda: "server-dhcp-circuit-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, ['circuit_id', 'format', 'argument1', 'argument2', 'argument3', 'argument4', 'argument5', 'argument6', 'argument7', 'argument8', 'argument9', 'argument10', 'argument11', 'argument12', 'argument13', 'argument14', 'argument15', 'argument16'], name, value)


            class SnoopInterface(Entity):
                """
                DHCP IPv4 snoop information
                
                .. attribute:: snoop_circuit_id
                
                	Configure circuit ID for snoop 1. Hex 2. ASCII
                	**type**\:  :py:class:`SnoopCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2017-09-30'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface, self).__init__()

                    self.yang_name = "snoop-interface"
                    self.yang_parent_name = "interface"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("snoop-circuit-id", ("snoop_circuit_id", Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId))])
                    self._leafs = OrderedDict()

                    self.snoop_circuit_id = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId()
                    self.snoop_circuit_id.parent = self
                    self._children_name_map["snoop_circuit_id"] = "snoop-circuit-id"
                    self._segment_path = lambda: "snoop-interface"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface, [], name, value)


                class SnoopCircuitId(Entity):
                    """
                    Configure circuit ID for snoop 1. Hex 2.
                    ASCII
                    
                    .. attribute:: format_type
                    
                    	Format type, 1. Hex 2. ASCII
                    	**type**\: int
                    
                    	**range:** 1..2
                    
                    .. attribute:: circuit_id_value
                    
                    	Enter circuit\-id value
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2017-09-30'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, self).__init__()

                        self.yang_name = "snoop-circuit-id"
                        self.yang_parent_name = "snoop-interface"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('format_type', (YLeaf(YType.uint32, 'format-type'), ['int'])),
                            ('circuit_id_value', (YLeaf(YType.str, 'circuit-id-value'), ['str'])),
                        ])
                        self.format_type = None
                        self.circuit_id_value = None
                        self._segment_path = lambda: "snoop-circuit-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, ['format_type', 'circuit_id_value'], name, value)


    class DuplicateMacAllowed(Entity):
        """
        Allow Duplicate MAC Address
        
        .. attribute:: duplicate_mac
        
        	Duplicate mac is allowed
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        	**mandatory**\: True
        
        .. attribute:: exclude_vlan
        
        	Exclude vlan
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: include_giaddr
        
        	Include giaddr
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.DuplicateMacAllowed, self).__init__()

            self.yang_name = "duplicate-mac-allowed"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self.is_presence_container = True
            self._leafs = OrderedDict([
                ('duplicate_mac', (YLeaf(YType.empty, 'duplicate-mac'), ['Empty'])),
                ('exclude_vlan', (YLeaf(YType.empty, 'exclude-vlan'), ['Empty'])),
                ('include_giaddr', (YLeaf(YType.empty, 'include-giaddr'), ['Empty'])),
            ])
            self.duplicate_mac = None
            self.exclude_vlan = None
            self.include_giaddr = None
            self._segment_path = lambda: "duplicate-mac-allowed"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.DuplicateMacAllowed, ['duplicate_mac', 'exclude_vlan', 'include_giaddr'], name, value)


    class RateLimit(Entity):
        """
        Rate limit ingress packets
        
        .. attribute:: num_period
        
        	Rate limiter period in msec (default\: 200 msec)
        	**type**\: int
        
        	**range:** 1..1000
        
        	**default value**\: 200
        
        .. attribute:: num_discover
        
        	Max DISCOVER packets per rate\-limiter period (default 100)
        	**type**\: int
        
        	**range:** 0..1000
        
        	**default value**\: 100
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2017-09-30'

        def __init__(self):
            super(Ipv4Dhcpd.RateLimit, self).__init__()

            self.yang_name = "rate-limit"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('num_period', (YLeaf(YType.uint32, 'num-period'), ['int'])),
                ('num_discover', (YLeaf(YType.uint32, 'num-discover'), ['int'])),
            ])
            self.num_period = None
            self.num_discover = None
            self._segment_path = lambda: "rate-limit"
            self._absolute_path = lambda: "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(Ipv4Dhcpd.RateLimit, ['num_period', 'num_discover'], name, value)

    def clone_ptr(self):
        self._top_entity = Ipv4Dhcpd()
        return self._top_entity

