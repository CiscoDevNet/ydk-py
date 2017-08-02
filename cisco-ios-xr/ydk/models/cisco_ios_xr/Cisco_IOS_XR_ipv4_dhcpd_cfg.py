""" Cisco_IOS_XR_ipv4_dhcpd_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ipv4\-dhcpd package configuration.

This module contains definitions
for the following management objects\:
  ipv4\-dhcpd\: DHCP IPV4 configuration

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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


class Ipv4DhcpdBroadcastFlagPolicy(Enum):
    """
    Ipv4DhcpdBroadcastFlagPolicy

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


class Ipv4DhcpdFmt(Enum):
    """
    Ipv4DhcpdFmt

    Ipv4dhcpd fmt

    .. data:: no_format = 0

    	Not a Format String

    .. data:: format = 1

    	Format String

    """

    no_format = Enum.YLeaf(0, "no-format")

    format = Enum.YLeaf(1, "format")


class Ipv4DhcpdFmtSpecifier(Enum):
    """
    Ipv4DhcpdFmtSpecifier

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


class Ipv4DhcpdGiaddrPolicy(Enum):
    """
    Ipv4DhcpdGiaddrPolicy

    Ipv4dhcpd giaddr policy

    .. data:: keep = 0

    	Keep

    .. data:: replace = 1

    	Replace

    .. data:: drop = 2

    	Drop

    """

    keep = Enum.YLeaf(0, "keep")

    replace = Enum.YLeaf(1, "replace")

    drop = Enum.YLeaf(2, "drop")


class Ipv4DhcpdLayer(Enum):
    """
    Ipv4DhcpdLayer

    Ipv4dhcpd layer

    .. data:: layer2 = 2

    	Layer2

    .. data:: layer3 = 3

    	Layer3

    """

    layer2 = Enum.YLeaf(2, "layer2")

    layer3 = Enum.YLeaf(3, "layer3")


class Ipv4DhcpdMode(Enum):
    """
    Ipv4DhcpdMode

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


class Ipv4DhcpdRelayInfoOptionAuthenticate(Enum):
    """
    Ipv4DhcpdRelayInfoOptionAuthenticate

    Ipv4dhcpd relay info option authenticate

    .. data:: received = 0

    	Received

    .. data:: inserted = 1

    	Inserted

    """

    received = Enum.YLeaf(0, "received")

    inserted = Enum.YLeaf(1, "inserted")


class Ipv4DhcpdRelayInfoOptionPolicy(Enum):
    """
    Ipv4DhcpdRelayInfoOptionPolicy

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


class Ipv4DhcpdRelayInfoOptionvpnMode(Enum):
    """
    Ipv4DhcpdRelayInfoOptionvpnMode

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
    _revision = '2015-11-09'

    def __init__(self):
        super(Ipv4Dhcpd, self).__init__()
        self._top_entity = None

        self.yang_name = "ipv4-dhcpd"
        self.yang_parent_name = "Cisco-IOS-XR-ipv4-dhcpd-cfg"

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

    def __setattr__(self, name, value):
        self._check_monkey_patching_error(name, value)
        with _handle_type_error():
            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                    "Please use list append or extend method."
                                    .format(value))
            if isinstance(value, Enum.YLeaf):
                value = value.name
            if name in ("allow_client_id_change",
                        "enable",
                        "inner_cos",
                        "outer_cos") and name in self.__dict__:
                if isinstance(value, YLeaf):
                    self.__dict__[name].set(value.get())
                elif isinstance(value, YLeafList):
                    super(Ipv4Dhcpd, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(Ipv4Dhcpd, self).__setattr__(name, value)


    class Vrfs(Entity):
        """
        VRF Table
        
        .. attribute:: vrf
        
        	VRF table
        	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Vrfs.Vrf>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Vrfs, self).__init__()

            self.yang_name = "vrfs"
            self.yang_parent_name = "ipv4-dhcpd"

            self.vrf = YList(self)

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
                        super(Ipv4Dhcpd.Vrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.Vrfs, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Vrfs.Vrf, self).__init__()

                self.yang_name = "vrf"
                self.yang_parent_name = "vrfs"

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.profile = None
                self._children_name_map["profile"] = "profile"
                self._children_yang_names.add("profile")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Dhcpd.Vrfs.Vrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Dhcpd.Vrfs.Vrf, self).__setattr__(name, value)


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	Dhcp mode
                	**type**\:   :py:class:`Ipv4DhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdMode>`
                
                	**mandatory**\: True
                
                .. attribute:: vrf_profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Vrfs.Vrf.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "vrf"
                    self.is_presence_container = True

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.vrf_profile_name = YLeaf(YType.str, "vrf-profile-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mode",
                                    "vrf_profile_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Dhcpd.Vrfs.Vrf.Profile, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Vrfs.Vrf.Profile, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mode.is_set or
                        self.vrf_profile_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.vrf_profile_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "profile" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.vrf_profile_name.is_set or self.vrf_profile_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vrf_profile_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mode" or name == "vrf-profile-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "vrf-profile-name"):
                        self.vrf_profile_name = value
                        self.vrf_profile_name.value_namespace = name_space
                        self.vrf_profile_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.vrf_name.is_set or
                    (self.profile is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    (self.profile is not None and self.profile.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "profile"):
                    if (self.profile is None):
                        self.profile = Ipv4Dhcpd.Vrfs.Vrf.Profile()
                        self.profile.parent = self
                        self._children_name_map["profile"] = "profile"
                    return self.profile

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "profile" or name == "vrf-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "vrf"):
                for c in self.vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv4Dhcpd.Vrfs.Vrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Profiles(Entity):
        """
        DHCP IPV4 Profile Table
        
        .. attribute:: profile
        
        	DHCP IPV4 Profile
        	**type**\: list of    :py:class:`Profile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Profiles, self).__init__()

            self.yang_name = "profiles"
            self.yang_parent_name = "ipv4-dhcpd"

            self.profile = YList(self)

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
                        super(Ipv4Dhcpd.Profiles, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.Profiles, self).__setattr__(name, value)


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
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Profiles.Profile, self).__init__()

                self.yang_name = "profile"
                self.yang_parent_name = "profiles"

                self.profile_name = YLeaf(YType.str, "profile-name")

                self.modes = Ipv4Dhcpd.Profiles.Profile.Modes()
                self.modes.parent = self
                self._children_name_map["modes"] = "modes"
                self._children_yang_names.add("modes")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("profile_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Dhcpd.Profiles.Profile, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Dhcpd.Profiles.Profile, self).__setattr__(name, value)


            class Modes(Entity):
                """
                DHCP IPV4 Profile modes
                
                .. attribute:: mode
                
                	DHCP IPV4 Profile mode
                	**type**\: list of    :py:class:`Mode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Profiles.Profile.Modes, self).__init__()

                    self.yang_name = "modes"
                    self.yang_parent_name = "profile"

                    self.mode = YList(self)

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
                                super(Ipv4Dhcpd.Profiles.Profile.Modes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Profiles.Profile.Modes, self).__setattr__(name, value)


                class Mode(Entity):
                    """
                    DHCP IPV4 Profile mode
                    
                    .. attribute:: mode  <key>
                    
                    	DHCP IPV4 Profile mode
                    	**type**\:   :py:class:`Ipv4DhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdMode>`
                    
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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, self).__init__()

                        self.yang_name = "mode"
                        self.yang_parent_name = "modes"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("mode",
                                        "enable") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode, self).__setattr__(name, value)


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, self).__init__()

                            self.yang_name = "snoop"
                            self.yang_parent_name = "mode"

                            self.trusted = YLeaf(YType.empty, "trusted")

                            self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption()
                            self.relay_information_option.parent = self
                            self._children_name_map["relay_information_option"] = "relay-information-option"
                            self._children_yang_names.add("relay-information-option")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("trusted") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop, self).__setattr__(name, value)


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
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: remote_id
                            
                            	Enter remote\-id value
                            	**type**\:   :py:class:`RemoteId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "snoop"

                                self.allow_untrusted = YLeaf(YType.empty, "allow-untrusted")

                                self.insert = YLeaf(YType.empty, "insert")

                                self.policy = YLeaf(YType.enumeration, "policy")

                                self.remote_id = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId()
                                self.remote_id.parent = self
                                self._children_name_map["remote_id"] = "remote-id"
                                self._children_yang_names.add("remote-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("allow_untrusted",
                                                "insert",
                                                "policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, self).__init__()

                                    self.yang_name = "remote-id"
                                    self.yang_parent_name = "relay-information-option"

                                    self.format_type = YLeaf(YType.uint32, "format-type")

                                    self.remote_id_value = YLeaf(YType.str, "remote-id-value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("format_type",
                                                    "remote_id_value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.format_type.is_set or
                                        self.remote_id_value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.format_type.yfilter != YFilter.not_set or
                                        self.remote_id_value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "remote-id" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.format_type.is_set or self.format_type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.format_type.get_name_leafdata())
                                    if (self.remote_id_value.is_set or self.remote_id_value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.remote_id_value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "format-type" or name == "remote-id-value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "format-type"):
                                        self.format_type = value
                                        self.format_type.value_namespace = name_space
                                        self.format_type.value_namespace_prefix = name_space_prefix
                                    if(value_path == "remote-id-value"):
                                        self.remote_id_value = value
                                        self.remote_id_value.value_namespace = name_space
                                        self.remote_id_value.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.allow_untrusted.is_set or
                                    self.insert.is_set or
                                    self.policy.is_set or
                                    (self.remote_id is not None and self.remote_id.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.allow_untrusted.yfilter != YFilter.not_set or
                                    self.insert.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set or
                                    (self.remote_id is not None and self.remote_id.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "relay-information-option" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.allow_untrusted.is_set or self.allow_untrusted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allow_untrusted.get_name_leafdata())
                                if (self.insert.is_set or self.insert.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.insert.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "remote-id"):
                                    if (self.remote_id is None):
                                        self.remote_id = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption.RemoteId()
                                        self.remote_id.parent = self
                                        self._children_name_map["remote_id"] = "remote-id"
                                    return self.remote_id

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "remote-id" or name == "allow-untrusted" or name == "insert" or name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "allow-untrusted"):
                                    self.allow_untrusted = value
                                    self.allow_untrusted.value_namespace = name_space
                                    self.allow_untrusted.value_namespace_prefix = name_space_prefix
                                if(value_path == "insert"):
                                    self.insert = value
                                    self.insert.value_namespace = name_space
                                    self.insert.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.trusted.is_set or
                                (self.relay_information_option is not None and self.relay_information_option.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.trusted.yfilter != YFilter.not_set or
                                (self.relay_information_option is not None and self.relay_information_option.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "snoop" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.trusted.is_set or self.trusted.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.trusted.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "relay-information-option"):
                                if (self.relay_information_option is None):
                                    self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop.RelayInformationOption()
                                    self.relay_information_option.parent = self
                                    self._children_name_map["relay_information_option"] = "relay-information-option"
                                return self.relay_information_option

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "relay-information-option" or name == "trusted"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "trusted"):
                                self.trusted = value
                                self.trusted.value_namespace = name_space
                                self.trusted.value_namespace_prefix = name_space_prefix


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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, self).__init__()

                            self.yang_name = "base"
                            self.yang_parent_name = "mode"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("enable") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base, self).__setattr__(name, value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, self).__init__()

                                self.yang_name = "default-profile"
                                self.yang_parent_name = "base"

                                self.profile_mode = YLeaf(YType.int32, "profile-mode")

                                self.profile_name = YLeaf(YType.str, "profile-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("profile_mode",
                                                "profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.profile_mode.is_set or
                                    self.profile_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_mode.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "default-profile" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.profile_mode.is_set or self.profile_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_mode.get_name_leafdata())
                                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-mode" or name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-mode"):
                                    self.profile_mode = value
                                    self.profile_mode.value_namespace = name_space
                                    self.profile_mode.value_namespace_prefix = name_space_prefix
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "base"

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"
                                self._children_yang_names.add("def-options")

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"
                                self._children_yang_names.add("option-filters")


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"

                                    self.option_filter = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"

                                        self.matchoption = YLeaf(YType.int32, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.option_action = YLeaf(YType.enumeration, "option-action")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("matchoption",
                                                        "pattern",
                                                        "format",
                                                        "option_action") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.matchoption.is_set or
                                            self.pattern.is_set or
                                            self.format.is_set or
                                            self.option_action.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.matchoption.yfilter != YFilter.not_set or
                                            self.pattern.yfilter != YFilter.not_set or
                                            self.format.yfilter != YFilter.not_set or
                                            self.option_action.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option-filter" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.matchoption.is_set or self.matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchoption.get_name_leafdata())
                                        if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pattern.get_name_leafdata())
                                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.format.get_name_leafdata())
                                        if (self.option_action.is_set or self.option_action.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.option_action.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "matchoption" or name == "pattern" or name == "format" or name == "option-action"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "matchoption"):
                                            self.matchoption = value
                                            self.matchoption.value_namespace = name_space
                                            self.matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pattern"):
                                            self.pattern = value
                                            self.pattern.value_namespace = name_space
                                            self.pattern.value_namespace_prefix = name_space_prefix
                                        if(value_path == "format"):
                                            self.format = value
                                            self.format.value_namespace = name_space
                                            self.format.value_namespace_prefix = name_space_prefix
                                        if(value_path == "option-action"):
                                            self.option_action = value
                                            self.option_action.value_namespace = name_space
                                            self.option_action.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.option_filter:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.option_filter:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "option-filters" + path_buffer

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

                                    if (child_yang_name == "option-filter"):
                                        for c in self.option_filter:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters.OptionFilter()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.option_filter.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option-filter"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"

                                    self.def_option = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"

                                        self.def_matchoption = YLeaf(YType.int32, "def-matchoption")

                                        self.def_matchaction = YLeaf(YType.enumeration, "def-matchaction")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("def_matchoption",
                                                        "def_matchaction") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.def_matchoption.is_set or
                                            self.def_matchaction.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.def_matchoption.yfilter != YFilter.not_set or
                                            self.def_matchaction.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "def-option" + "[def-matchoption='" + self.def_matchoption.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.def_matchoption.is_set or self.def_matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.def_matchoption.get_name_leafdata())
                                        if (self.def_matchaction.is_set or self.def_matchaction.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.def_matchaction.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "def-matchoption" or name == "def-matchaction"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "def-matchoption"):
                                            self.def_matchoption = value
                                            self.def_matchoption.value_namespace = name_space
                                            self.def_matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "def-matchaction"):
                                            self.def_matchaction = value
                                            self.def_matchaction.value_namespace = name_space
                                            self.def_matchaction.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.def_option:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.def_option:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "def-options" + path_buffer

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

                                    if (child_yang_name == "def-option"):
                                        for c in self.def_option:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions.DefOption()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.def_option.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "def-option"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    (self.def_options is not None and self.def_options.has_data()) or
                                    (self.option_filters is not None and self.option_filters.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.def_options is not None and self.def_options.has_operation()) or
                                    (self.option_filters is not None and self.option_filters.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "match" + path_buffer

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

                                if (child_yang_name == "def-options"):
                                    if (self.def_options is None):
                                        self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.DefOptions()
                                        self.def_options.parent = self
                                        self._children_name_map["def_options"] = "def-options"
                                    return self.def_options

                                if (child_yang_name == "option-filters"):
                                    if (self.option_filters is None):
                                        self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match.OptionFilters()
                                        self.option_filters.parent = self
                                        self._children_name_map["option_filters"] = "option-filters"
                                    return self.option_filters

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "def-options" or name == "option-filters"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, self).__init__()

                                self.yang_name = "base-relay-opt"
                                self.yang_parent_name = "base"

                                self.authenticate = YLeaf(YType.int32, "authenticate")

                                self.remote_id = YLeaf(YType.str, "remote-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("authenticate",
                                                "remote_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.authenticate.is_set or
                                    self.remote_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.authenticate.yfilter != YFilter.not_set or
                                    self.remote_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "base-relay-opt" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.authenticate.is_set or self.authenticate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authenticate.get_name_leafdata())
                                if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "authenticate" or name == "remote-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "authenticate"):
                                    self.authenticate = value
                                    self.authenticate.value_namespace = name_space
                                    self.authenticate.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id"):
                                    self.remote_id = value
                                    self.remote_id.value_namespace = name_space
                                    self.remote_id.value_namespace_prefix = name_space_prefix


                        class BaseMatch(Entity):
                            """
                            Insert match keyword
                            
                            .. attribute:: options
                            
                            	Specify match option
                            	**type**\:   :py:class:`Options <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch, self).__init__()

                                self.yang_name = "base-match"
                                self.yang_parent_name = "base"

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._children_yang_names.add("options")


                            class Options(Entity):
                                """
                                Specify match option
                                
                                .. attribute:: option
                                
                                	none
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "base-match"

                                    self.option = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"

                                        self.opt60 = YLeaf(YType.int32, "opt60")

                                        self.opt60_hex_str = YLeaf(YType.str, "opt60-hex-str")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.option_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile()
                                        self.option_profile.parent = self
                                        self._children_name_map["option_profile"] = "option-profile"
                                        self._children_yang_names.add("option-profile")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("opt60",
                                                        "opt60_hex_str",
                                                        "format") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, self).__init__()

                                            self.yang_name = "option-profile"
                                            self.yang_parent_name = "option"

                                            self.profile_mode = YLeaf(YType.int32, "profile-mode")

                                            self.profile_name = YLeaf(YType.str, "profile-name")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("profile_mode",
                                                            "profile_name") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.profile_mode.is_set or
                                                self.profile_name.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.profile_mode.yfilter != YFilter.not_set or
                                                self.profile_name.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "option-profile" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.profile_mode.is_set or self.profile_mode.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.profile_mode.get_name_leafdata())
                                            if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.profile_name.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "profile-mode" or name == "profile-name"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "profile-mode"):
                                                self.profile_mode = value
                                                self.profile_mode.value_namespace = name_space
                                                self.profile_mode.value_namespace_prefix = name_space_prefix
                                            if(value_path == "profile-name"):
                                                self.profile_name = value
                                                self.profile_name.value_namespace = name_space
                                                self.profile_name.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.opt60.is_set or
                                            self.opt60_hex_str.is_set or
                                            self.format.is_set or
                                            (self.option_profile is not None and self.option_profile.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.opt60.yfilter != YFilter.not_set or
                                            self.opt60_hex_str.yfilter != YFilter.not_set or
                                            self.format.yfilter != YFilter.not_set or
                                            (self.option_profile is not None and self.option_profile.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option" + "[opt60='" + self.opt60.get() + "']" + "[opt60-hex-str='" + self.opt60_hex_str.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.opt60.is_set or self.opt60.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.opt60.get_name_leafdata())
                                        if (self.opt60_hex_str.is_set or self.opt60_hex_str.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.opt60_hex_str.get_name_leafdata())
                                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.format.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "option-profile"):
                                            if (self.option_profile is None):
                                                self.option_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option.OptionProfile()
                                                self.option_profile.parent = self
                                                self._children_name_map["option_profile"] = "option-profile"
                                            return self.option_profile

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "option-profile" or name == "opt60" or name == "opt60-hex-str" or name == "format"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "opt60"):
                                            self.opt60 = value
                                            self.opt60.value_namespace = name_space
                                            self.opt60.value_namespace_prefix = name_space_prefix
                                        if(value_path == "opt60-hex-str"):
                                            self.opt60_hex_str = value
                                            self.opt60_hex_str.value_namespace = name_space
                                            self.opt60_hex_str.value_namespace_prefix = name_space_prefix
                                        if(value_path == "format"):
                                            self.format = value
                                            self.format.value_namespace = name_space
                                            self.format.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.option:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.option:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "options" + path_buffer

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

                                    if (child_yang_name == "option"):
                                        for c in self.option:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options.Option()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.option.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.options is not None and self.options.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.options is not None and self.options.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "base-match" + path_buffer

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

                                if (child_yang_name == "options"):
                                    if (self.options is None):
                                        self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch.Options()
                                        self.options.parent = self
                                        self._children_name_map["options"] = "options"
                                    return self.options

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "options"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.enable.is_set or
                                (self.base_match is not None and self.base_match.has_data()) or
                                (self.base_relay_opt is not None and self.base_relay_opt.has_data()) or
                                (self.default_profile is not None and self.default_profile.has_data()) or
                                (self.match is not None and self.match.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                (self.base_match is not None and self.base_match.has_operation()) or
                                (self.base_relay_opt is not None and self.base_relay_opt.has_operation()) or
                                (self.default_profile is not None and self.default_profile.has_operation()) or
                                (self.match is not None and self.match.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "base" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "base-match"):
                                if (self.base_match is None):
                                    self.base_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseMatch()
                                    self.base_match.parent = self
                                    self._children_name_map["base_match"] = "base-match"
                                return self.base_match

                            if (child_yang_name == "base-relay-opt"):
                                if (self.base_relay_opt is None):
                                    self.base_relay_opt = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.BaseRelayOpt()
                                    self.base_relay_opt.parent = self
                                    self._children_name_map["base_relay_opt"] = "base-relay-opt"
                                return self.base_relay_opt

                            if (child_yang_name == "default-profile"):
                                if (self.default_profile is None):
                                    self.default_profile = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.DefaultProfile()
                                    self.default_profile.parent = self
                                    self._children_name_map["default_profile"] = "default-profile"
                                return self.default_profile

                            if (child_yang_name == "match"):
                                if (self.match is None):
                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                return self.match

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "base-match" or name == "base-relay-opt" or name == "default-profile" or name == "match" or name == "enable"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix


                    class Server(Entity):
                        """
                        DHCP Server profile
                        
                        .. attribute:: aaa
                        
                        	Enable aaa dhcp option force\-insert
                        	**type**\:   :py:class:`Aaa <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, self).__init__()

                            self.yang_name = "server"
                            self.yang_parent_name = "mode"

                            self.boot_filename = YLeaf(YType.str, "boot-filename")

                            self.domain_name = YLeaf(YType.str, "domain-name")

                            self.infinite_lease = YLeaf(YType.empty, "infinite-lease")

                            self.next_server = YLeaf(YType.str, "next-server")

                            self.pool = YLeaf(YType.str, "pool")

                            self.secure_arp = YLeaf(YType.empty, "secure-arp")

                            self.server_allow_move = YLeaf(YType.empty, "server-allow-move")

                            self.subnet_mask = YLeaf(YType.str, "subnet-mask")

                            self.aaa = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa()
                            self.aaa.parent = self
                            self._children_name_map["aaa"] = "aaa"
                            self._children_yang_names.add("aaa")

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("boot_filename",
                                            "domain_name",
                                            "infinite_lease",
                                            "next_server",
                                            "pool",
                                            "secure_arp",
                                            "server_allow_move",
                                            "subnet_mask") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server, self).__setattr__(name, value)


                        class ServerIdCheck(Entity):
                            """
                            Validate server ID check
                            
                            .. attribute:: check
                            
                            	specify server\-id\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, self).__init__()

                                self.yang_name = "server-id-check"
                                self.yang_parent_name = "server"

                                self.check = YLeaf(YType.empty, "check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck, self).__setattr__(name, value)

                            def has_data(self):
                                return self.check.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "server-id-check" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.check.is_set or self.check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "check"):
                                    self.check = value
                                    self.check.value_namespace = name_space
                                    self.check.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, self).__init__()

                                self.yang_name = "lease-limit"
                                self.yang_parent_name = "server"

                                self.lease_limit_value = YLeaf(YType.enumeration, "lease-limit-value")

                                self.range = YLeaf(YType.uint32, "range")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("lease_limit_value",
                                                "range") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.lease_limit_value.is_set or
                                    self.range.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.lease_limit_value.yfilter != YFilter.not_set or
                                    self.range.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lease-limit" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.lease_limit_value.is_set or self.lease_limit_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.lease_limit_value.get_name_leafdata())
                                if (self.range.is_set or self.range.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.range.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "lease-limit-value" or name == "range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "lease-limit-value"):
                                    self.lease_limit_value = value
                                    self.lease_limit_value.value_namespace = name_space
                                    self.lease_limit_value.value_namespace_prefix = name_space_prefix
                                if(value_path == "range"):
                                    self.range = value
                                    self.range.value_namespace = name_space
                                    self.range.value_namespace_prefix = name_space_prefix


                        class RequestedIpAddress(Entity):
                            """
                            Validate Requested IP Address
                            
                            .. attribute:: check
                            
                            	specify requested\-ip\-address\-check disable
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, self).__init__()

                                self.yang_name = "requested-ip-address"
                                self.yang_parent_name = "server"

                                self.check = YLeaf(YType.empty, "check")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("check") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress, self).__setattr__(name, value)

                            def has_data(self):
                                return self.check.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.check.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "requested-ip-address" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.check.is_set or self.check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.check.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "check"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "check"):
                                    self.check = value
                                    self.check.value_namespace = name_space
                                    self.check.value_namespace_prefix = name_space_prefix


                        class DefaultRouters(Entity):
                            """
                            default routers
                            
                            .. attribute:: default_router
                            
                            	Router's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, self).__init__()

                                self.yang_name = "default-routers"
                                self.yang_parent_name = "server"

                                self.default_router = YLeafList(YType.str, "default-router")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("default_router") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.default_router.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.default_router.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.default_router.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "default-routers" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.default_router.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "default-router"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "default-router"):
                                    self.default_router.append(value)


                        class NetBiosNameServers(Entity):
                            """
                            NetBIOS name servers
                            
                            .. attribute:: net_bios_name_server
                            
                            	NetBIOSNameServer's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, self).__init__()

                                self.yang_name = "net-bios-name-servers"
                                self.yang_parent_name = "server"

                                self.net_bios_name_server = YLeafList(YType.str, "net-bios-name-server")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("net_bios_name_server") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.net_bios_name_server.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.net_bios_name_server.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.net_bios_name_server.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "net-bios-name-servers" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.net_bios_name_server.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "net-bios-name-server"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "net-bios-name-server"):
                                    self.net_bios_name_server.append(value)


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "server"

                                self.option_defaults = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults()
                                self.option_defaults.parent = self
                                self._children_name_map["option_defaults"] = "option-defaults"
                                self._children_yang_names.add("option-defaults")

                                self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options()
                                self.options.parent = self
                                self._children_name_map["options"] = "options"
                                self._children_yang_names.add("options")


                            class OptionDefaults(Entity):
                                """
                                Table of OptionDefault
                                
                                .. attribute:: option_default
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionDefault <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, self).__init__()

                                    self.yang_name = "option-defaults"
                                    self.yang_parent_name = "match"

                                    self.option_default = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, self).__init__()

                                        self.yang_name = "option-default"
                                        self.yang_parent_name = "option-defaults"

                                        self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("matchoption",
                                                        "matchaction") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.matchoption.is_set or
                                            self.matchaction.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.matchoption.yfilter != YFilter.not_set or
                                            self.matchaction.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option-default" + "[matchoption='" + self.matchoption.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.matchoption.is_set or self.matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchoption.get_name_leafdata())
                                        if (self.matchaction.is_set or self.matchaction.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchaction.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "matchoption" or name == "matchaction"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "matchoption"):
                                            self.matchoption = value
                                            self.matchoption.value_namespace = name_space
                                            self.matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "matchaction"):
                                            self.matchaction = value
                                            self.matchaction.value_namespace = name_space
                                            self.matchaction.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.option_default:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.option_default:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "option-defaults" + path_buffer

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

                                    if (child_yang_name == "option-default"):
                                        for c in self.option_default:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults.OptionDefault()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.option_default.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option-default"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class Options(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`Option <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, self).__init__()

                                    self.yang_name = "options"
                                    self.yang_parent_name = "match"

                                    self.option = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, self).__init__()

                                        self.yang_name = "option"
                                        self.yang_parent_name = "options"

                                        self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("matchoption",
                                                        "pattern",
                                                        "format",
                                                        "matchaction") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.matchoption.is_set or
                                            self.pattern.is_set or
                                            self.format.is_set or
                                            self.matchaction.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.matchoption.yfilter != YFilter.not_set or
                                            self.pattern.yfilter != YFilter.not_set or
                                            self.format.yfilter != YFilter.not_set or
                                            self.matchaction.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.matchoption.is_set or self.matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchoption.get_name_leafdata())
                                        if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pattern.get_name_leafdata())
                                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.format.get_name_leafdata())
                                        if (self.matchaction.is_set or self.matchaction.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchaction.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "matchoption" or name == "pattern" or name == "format" or name == "matchaction"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "matchoption"):
                                            self.matchoption = value
                                            self.matchoption.value_namespace = name_space
                                            self.matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pattern"):
                                            self.pattern = value
                                            self.pattern.value_namespace = name_space
                                            self.pattern.value_namespace_prefix = name_space_prefix
                                        if(value_path == "format"):
                                            self.format = value
                                            self.format.value_namespace = name_space
                                            self.format.value_namespace_prefix = name_space_prefix
                                        if(value_path == "matchaction"):
                                            self.matchaction = value
                                            self.matchaction.value_namespace = name_space
                                            self.matchaction.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.option:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.option:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "options" + path_buffer

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

                                    if (child_yang_name == "option"):
                                        for c in self.option:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options.Option()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.option.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    (self.option_defaults is not None and self.option_defaults.has_data()) or
                                    (self.options is not None and self.options.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.option_defaults is not None and self.option_defaults.has_operation()) or
                                    (self.options is not None and self.options.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "match" + path_buffer

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

                                if (child_yang_name == "option-defaults"):
                                    if (self.option_defaults is None):
                                        self.option_defaults = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.OptionDefaults()
                                        self.option_defaults.parent = self
                                        self._children_name_map["option_defaults"] = "option-defaults"
                                    return self.option_defaults

                                if (child_yang_name == "options"):
                                    if (self.options is None):
                                        self.options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match.Options()
                                        self.options.parent = self
                                        self._children_name_map["options"] = "options"
                                    return self.options

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "option-defaults" or name == "options"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class BroadcastFlag(Entity):
                            """
                            None
                            
                            .. attribute:: policy
                            
                            	Specify broadcast flag policy
                            	**type**\:   :py:class:`Policy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Policy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "server"

                                self.policy = YLeaf(YType.enumeration, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag, self).__setattr__(name, value)

                            def has_data(self):
                                return self.policy.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "broadcast-flag" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


                        class Session(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session, self).__init__()

                                self.yang_name = "session"
                                self.yang_parent_name = "server"

                                self.throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType()
                                self.throttle_type.parent = self
                                self._children_name_map["throttle_type"] = "throttle-type"
                                self._children_yang_names.add("throttle-type")


                            class ThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`MacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType, self).__init__()

                                    self.yang_name = "throttle-type"
                                    self.yang_parent_name = "session"

                                    self.mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle()
                                    self.mac_throttle.parent = self
                                    self._children_name_map["mac_throttle"] = "mac-throttle"
                                    self._children_yang_names.add("mac-throttle")


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, self).__init__()

                                        self.yang_name = "mac-throttle"
                                        self.yang_parent_name = "throttle-type"

                                        self.num_block = YLeaf(YType.uint32, "num-block")

                                        self.num_discover = YLeaf(YType.uint32, "num-discover")

                                        self.num_request = YLeaf(YType.uint32, "num-request")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_block",
                                                        "num_discover",
                                                        "num_request") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_block.is_set or
                                            self.num_discover.is_set or
                                            self.num_request.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_block.yfilter != YFilter.not_set or
                                            self.num_discover.yfilter != YFilter.not_set or
                                            self.num_request.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "mac-throttle" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_block.is_set or self.num_block.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_block.get_name_leafdata())
                                        if (self.num_discover.is_set or self.num_discover.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_discover.get_name_leafdata())
                                        if (self.num_request.is_set or self.num_request.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_request.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-block" or name == "num-discover" or name == "num-request"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-block"):
                                            self.num_block = value
                                            self.num_block.value_namespace = name_space
                                            self.num_block.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-discover"):
                                            self.num_discover = value
                                            self.num_discover.value_namespace = name_space
                                            self.num_discover.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-request"):
                                            self.num_request = value
                                            self.num_request.value_namespace = name_space
                                            self.num_request.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.mac_throttle is not None and self.mac_throttle.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.mac_throttle is not None and self.mac_throttle.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "throttle-type" + path_buffer

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

                                    if (child_yang_name == "mac-throttle"):
                                        if (self.mac_throttle is None):
                                            self.mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType.MacThrottle()
                                            self.mac_throttle.parent = self
                                            self._children_name_map["mac_throttle"] = "mac-throttle"
                                        return self.mac_throttle

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "mac-throttle"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.throttle_type is not None and self.throttle_type.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.throttle_type is not None and self.throttle_type.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "session" + path_buffer

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

                                if (child_yang_name == "throttle-type"):
                                    if (self.throttle_type is None):
                                        self.throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session.ThrottleType()
                                        self.throttle_type.parent = self
                                        self._children_name_map["throttle_type"] = "throttle-type"
                                    return self.throttle_type

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "throttle-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Classes(Entity):
                            """
                            Table of Class
                            
                            .. attribute:: class_
                            
                            	Create or enter server profile class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "server"

                                self.class_ = YList(self)

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
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"

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

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("class_name",
                                                    "boot_filename",
                                                    "domain_name",
                                                    "enable",
                                                    "infinite_lease",
                                                    "next_server",
                                                    "pool",
                                                    "subnet_mask") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_, self).__setattr__(name, value)


                                class DefaultRouters(Entity):
                                    """
                                    default routers
                                    
                                    .. attribute:: default_router
                                    
                                    	Router's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters, self).__init__()

                                        self.yang_name = "default-routers"
                                        self.yang_parent_name = "class"

                                        self.default_router = YLeafList(YType.str, "default-router")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("default_router") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.default_router.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.default_router.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.default_router.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "default-routers" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.default_router.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "default-router"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "default-router"):
                                            self.default_router.append(value)


                                class NetBiosNameServers(Entity):
                                    """
                                    NetBIOS name servers
                                    
                                    .. attribute:: net_bios_name_server
                                    
                                    	NetBIOSNameServer's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers, self).__init__()

                                        self.yang_name = "net-bios-name-servers"
                                        self.yang_parent_name = "class"

                                        self.net_bios_name_server = YLeafList(YType.str, "net-bios-name-server")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("net_bios_name_server") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.net_bios_name_server.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.net_bios_name_server.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.net_bios_name_server.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "net-bios-name-servers" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.net_bios_name_server.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "net-bios-name-server"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "net-bios-name-server"):
                                            self.net_bios_name_server.append(value)


                                class ClassMatch(Entity):
                                    """
                                    Insert match keyword
                                    
                                    .. attribute:: class_options
                                    
                                    	Table of Class\-Option
                                    	**type**\:   :py:class:`ClassOptions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions>`
                                    
                                    .. attribute:: l2_interface
                                    
                                    	Specify match l2\-interface
                                    	**type**\:  str
                                    
                                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                                    
                                    .. attribute:: vrf
                                    
                                    	Specify match VRF
                                    	**type**\:  str
                                    
                                    	**length:** 1..32
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch, self).__init__()

                                        self.yang_name = "class-match"
                                        self.yang_parent_name = "class"

                                        self.l2_interface = YLeaf(YType.str, "l2-interface")

                                        self.vrf = YLeaf(YType.str, "vrf")

                                        self.class_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions()
                                        self.class_options.parent = self
                                        self._children_name_map["class_options"] = "class-options"
                                        self._children_yang_names.add("class-options")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("l2_interface",
                                                        "vrf") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch, self).__setattr__(name, value)


                                    class ClassOptions(Entity):
                                        """
                                        Table of Class\-Option
                                        
                                        .. attribute:: class_option
                                        
                                        	Specify match option
                                        	**type**\: list of    :py:class:`ClassOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption>`
                                        
                                        

                                        """

                                        _prefix = 'ipv4-dhcpd-cfg'
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions, self).__init__()

                                            self.yang_name = "class-options"
                                            self.yang_parent_name = "class-match"

                                            self.class_option = YList(self)

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
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions, self).__setattr__(name, value)


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
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption, self).__init__()

                                                self.yang_name = "class-option"
                                                self.yang_parent_name = "class-options"

                                                self.matchoption = YLeaf(YType.enumeration, "matchoption")

                                                self.bit_mask = YLeaf(YType.str, "bit-mask")

                                                self.pattern = YLeaf(YType.str, "pattern")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("matchoption",
                                                                "bit_mask",
                                                                "pattern") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption, self).__setattr__(name, value)

                                            def has_data(self):
                                                return (
                                                    self.matchoption.is_set or
                                                    self.bit_mask.is_set or
                                                    self.pattern.is_set)

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.matchoption.yfilter != YFilter.not_set or
                                                    self.bit_mask.yfilter != YFilter.not_set or
                                                    self.pattern.yfilter != YFilter.not_set)

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "class-option" + "[matchoption='" + self.matchoption.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.matchoption.is_set or self.matchoption.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.matchoption.get_name_leafdata())
                                                if (self.bit_mask.is_set or self.bit_mask.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.bit_mask.get_name_leafdata())
                                                if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.pattern.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "matchoption" or name == "bit-mask" or name == "pattern"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "matchoption"):
                                                    self.matchoption = value
                                                    self.matchoption.value_namespace = name_space
                                                    self.matchoption.value_namespace_prefix = name_space_prefix
                                                if(value_path == "bit-mask"):
                                                    self.bit_mask = value
                                                    self.bit_mask.value_namespace = name_space
                                                    self.bit_mask.value_namespace_prefix = name_space_prefix
                                                if(value_path == "pattern"):
                                                    self.pattern = value
                                                    self.pattern.value_namespace = name_space
                                                    self.pattern.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.class_option:
                                                if (c.has_data()):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for c in self.class_option:
                                                if (c.has_operation()):
                                                    return True
                                            return self.yfilter != YFilter.not_set

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "class-options" + path_buffer

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

                                            if (child_yang_name == "class-option"):
                                                for c in self.class_option:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions.ClassOption()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.class_option.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "class-option"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        return (
                                            self.l2_interface.is_set or
                                            self.vrf.is_set or
                                            (self.class_options is not None and self.class_options.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.l2_interface.yfilter != YFilter.not_set or
                                            self.vrf.yfilter != YFilter.not_set or
                                            (self.class_options is not None and self.class_options.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "class-match" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.l2_interface.is_set or self.l2_interface.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.l2_interface.get_name_leafdata())
                                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vrf.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "class-options"):
                                            if (self.class_options is None):
                                                self.class_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch.ClassOptions()
                                                self.class_options.parent = self
                                                self._children_name_map["class_options"] = "class-options"
                                            return self.class_options

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "class-options" or name == "l2-interface" or name == "vrf"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "l2-interface"):
                                            self.l2_interface = value
                                            self.l2_interface.value_namespace = name_space
                                            self.l2_interface.value_namespace_prefix = name_space_prefix
                                        if(value_path == "vrf"):
                                            self.vrf = value
                                            self.vrf.value_namespace = name_space
                                            self.vrf.value_namespace_prefix = name_space_prefix


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease, self).__init__()

                                        self.yang_name = "lease"
                                        self.yang_parent_name = "class"

                                        self.days = YLeaf(YType.uint32, "days")

                                        self.hours = YLeaf(YType.uint32, "hours")

                                        self.infinite = YLeaf(YType.str, "infinite")

                                        self.minutes = YLeaf(YType.uint32, "minutes")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("days",
                                                        "hours",
                                                        "infinite",
                                                        "minutes") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.days.is_set or
                                            self.hours.is_set or
                                            self.infinite.is_set or
                                            self.minutes.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.days.yfilter != YFilter.not_set or
                                            self.hours.yfilter != YFilter.not_set or
                                            self.infinite.yfilter != YFilter.not_set or
                                            self.minutes.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "lease" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.days.is_set or self.days.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.days.get_name_leafdata())
                                        if (self.hours.is_set or self.hours.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hours.get_name_leafdata())
                                        if (self.infinite.is_set or self.infinite.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.infinite.get_name_leafdata())
                                        if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.minutes.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "days" or name == "hours" or name == "infinite" or name == "minutes"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "days"):
                                            self.days = value
                                            self.days.value_namespace = name_space
                                            self.days.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hours"):
                                            self.hours = value
                                            self.hours.value_namespace = name_space
                                            self.hours.value_namespace_prefix = name_space_prefix
                                        if(value_path == "infinite"):
                                            self.infinite = value
                                            self.infinite.value_namespace = name_space
                                            self.infinite.value_namespace_prefix = name_space_prefix
                                        if(value_path == "minutes"):
                                            self.minutes = value
                                            self.minutes.value_namespace = name_space
                                            self.minutes.value_namespace_prefix = name_space_prefix


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType, self).__init__()

                                        self.yang_name = "netbios-node-type"
                                        self.yang_parent_name = "class"

                                        self.broadcast_node = YLeaf(YType.str, "broadcast-node")

                                        self.hexadecimal = YLeaf(YType.str, "hexadecimal")

                                        self.hybrid_node = YLeaf(YType.str, "hybrid-node")

                                        self.mixed_node = YLeaf(YType.str, "mixed-node")

                                        self.peer_to_peer_node = YLeaf(YType.str, "peer-to-peer-node")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("broadcast_node",
                                                        "hexadecimal",
                                                        "hybrid_node",
                                                        "mixed_node",
                                                        "peer_to_peer_node") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.broadcast_node.is_set or
                                            self.hexadecimal.is_set or
                                            self.hybrid_node.is_set or
                                            self.mixed_node.is_set or
                                            self.peer_to_peer_node.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.broadcast_node.yfilter != YFilter.not_set or
                                            self.hexadecimal.yfilter != YFilter.not_set or
                                            self.hybrid_node.yfilter != YFilter.not_set or
                                            self.mixed_node.yfilter != YFilter.not_set or
                                            self.peer_to_peer_node.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "netbios-node-type" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.broadcast_node.is_set or self.broadcast_node.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.broadcast_node.get_name_leafdata())
                                        if (self.hexadecimal.is_set or self.hexadecimal.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hexadecimal.get_name_leafdata())
                                        if (self.hybrid_node.is_set or self.hybrid_node.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.hybrid_node.get_name_leafdata())
                                        if (self.mixed_node.is_set or self.mixed_node.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.mixed_node.get_name_leafdata())
                                        if (self.peer_to_peer_node.is_set or self.peer_to_peer_node.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.peer_to_peer_node.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "broadcast-node" or name == "hexadecimal" or name == "hybrid-node" or name == "mixed-node" or name == "peer-to-peer-node"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "broadcast-node"):
                                            self.broadcast_node = value
                                            self.broadcast_node.value_namespace = name_space
                                            self.broadcast_node.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hexadecimal"):
                                            self.hexadecimal = value
                                            self.hexadecimal.value_namespace = name_space
                                            self.hexadecimal.value_namespace_prefix = name_space_prefix
                                        if(value_path == "hybrid-node"):
                                            self.hybrid_node = value
                                            self.hybrid_node.value_namespace = name_space
                                            self.hybrid_node.value_namespace_prefix = name_space_prefix
                                        if(value_path == "mixed-node"):
                                            self.mixed_node = value
                                            self.mixed_node.value_namespace = name_space
                                            self.mixed_node.value_namespace_prefix = name_space_prefix
                                        if(value_path == "peer-to-peer-node"):
                                            self.peer_to_peer_node = value
                                            self.peer_to_peer_node.value_namespace = name_space
                                            self.peer_to_peer_node.value_namespace_prefix = name_space_prefix


                                class DnsServers(Entity):
                                    """
                                    DNS servers
                                    
                                    .. attribute:: dns_server
                                    
                                    	DNS Server's IP address
                                    	**type**\:  list of str
                                    
                                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers, self).__init__()

                                        self.yang_name = "dns-servers"
                                        self.yang_parent_name = "class"

                                        self.dns_server = YLeafList(YType.str, "dns-server")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("dns_server") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers, self).__setattr__(name, value)

                                    def has_data(self):
                                        for leaf in self.dns_server.getYLeafs():
                                            if (leaf.yfilter != YFilter.not_set):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for leaf in self.dns_server.getYLeafs():
                                            if (leaf.is_set):
                                                return True
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.dns_server.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "dns-servers" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()

                                        leaf_name_data.extend(self.dns_server.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "dns-server"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "dns-server"):
                                            self.dns_server.append(value)


                                class OptionCodes(Entity):
                                    """
                                    Table of OptionCode
                                    
                                    .. attribute:: option_code
                                    
                                    	DHCP option code
                                    	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes, self).__init__()

                                        self.yang_name = "option-codes"
                                        self.yang_parent_name = "class"

                                        self.option_code = YList(self)

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
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode, self).__init__()

                                            self.yang_name = "option-code"
                                            self.yang_parent_name = "option-codes"

                                            self.option_code = YLeaf(YType.uint32, "option-code")

                                            self.ascii_string = YLeaf(YType.str, "ascii-string")

                                            self.force_insert = YLeaf(YType.int32, "force-insert")

                                            self.hex_string = YLeaf(YType.str, "hex-string")

                                            self.ip_address = YLeafList(YType.str, "ip-address")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("option_code",
                                                            "ascii_string",
                                                            "force_insert",
                                                            "hex_string",
                                                            "ip_address") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode, self).__setattr__(name, value)

                                        def has_data(self):
                                            for leaf in self.ip_address.getYLeafs():
                                                if (leaf.yfilter != YFilter.not_set):
                                                    return True
                                            return (
                                                self.option_code.is_set or
                                                self.ascii_string.is_set or
                                                self.force_insert.is_set or
                                                self.hex_string.is_set)

                                        def has_operation(self):
                                            for leaf in self.ip_address.getYLeafs():
                                                if (leaf.is_set):
                                                    return True
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.option_code.yfilter != YFilter.not_set or
                                                self.ascii_string.yfilter != YFilter.not_set or
                                                self.force_insert.yfilter != YFilter.not_set or
                                                self.hex_string.yfilter != YFilter.not_set or
                                                self.ip_address.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "option-code" + "[option-code='" + self.option_code.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.option_code.is_set or self.option_code.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.option_code.get_name_leafdata())
                                            if (self.ascii_string.is_set or self.ascii_string.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.ascii_string.get_name_leafdata())
                                            if (self.force_insert.is_set or self.force_insert.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.force_insert.get_name_leafdata())
                                            if (self.hex_string.is_set or self.hex_string.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.hex_string.get_name_leafdata())

                                            leaf_name_data.extend(self.ip_address.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "option-code" or name == "ascii-string" or name == "force-insert" or name == "hex-string" or name == "ip-address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "option-code"):
                                                self.option_code = value
                                                self.option_code.value_namespace = name_space
                                                self.option_code.value_namespace_prefix = name_space_prefix
                                            if(value_path == "ascii-string"):
                                                self.ascii_string = value
                                                self.ascii_string.value_namespace = name_space
                                                self.ascii_string.value_namespace_prefix = name_space_prefix
                                            if(value_path == "force-insert"):
                                                self.force_insert = value
                                                self.force_insert.value_namespace = name_space
                                                self.force_insert.value_namespace_prefix = name_space_prefix
                                            if(value_path == "hex-string"):
                                                self.hex_string = value
                                                self.hex_string.value_namespace = name_space
                                                self.hex_string.value_namespace_prefix = name_space_prefix
                                            if(value_path == "ip-address"):
                                                self.ip_address.append(value)

                                    def has_data(self):
                                        for c in self.option_code:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.option_code:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option-codes" + path_buffer

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

                                        if (child_yang_name == "option-code"):
                                            for c in self.option_code:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes.OptionCode()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.option_code.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "option-code"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.class_name.is_set or
                                        self.boot_filename.is_set or
                                        self.domain_name.is_set or
                                        self.enable.is_set or
                                        self.infinite_lease.is_set or
                                        self.next_server.is_set or
                                        self.pool.is_set or
                                        self.subnet_mask.is_set or
                                        (self.class_match is not None and self.class_match.has_data()) or
                                        (self.default_routers is not None and self.default_routers.has_data()) or
                                        (self.dns_servers is not None and self.dns_servers.has_data()) or
                                        (self.lease is not None and self.lease.has_data()) or
                                        (self.net_bios_name_servers is not None and self.net_bios_name_servers.has_data()) or
                                        (self.netbios_node_type is not None and self.netbios_node_type.has_data()) or
                                        (self.option_codes is not None and self.option_codes.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.class_name.yfilter != YFilter.not_set or
                                        self.boot_filename.yfilter != YFilter.not_set or
                                        self.domain_name.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        self.infinite_lease.yfilter != YFilter.not_set or
                                        self.next_server.yfilter != YFilter.not_set or
                                        self.pool.yfilter != YFilter.not_set or
                                        self.subnet_mask.yfilter != YFilter.not_set or
                                        (self.class_match is not None and self.class_match.has_operation()) or
                                        (self.default_routers is not None and self.default_routers.has_operation()) or
                                        (self.dns_servers is not None and self.dns_servers.has_operation()) or
                                        (self.lease is not None and self.lease.has_operation()) or
                                        (self.net_bios_name_servers is not None and self.net_bios_name_servers.has_operation()) or
                                        (self.netbios_node_type is not None and self.netbios_node_type.has_operation()) or
                                        (self.option_codes is not None and self.option_codes.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.class_name.get_name_leafdata())
                                    if (self.boot_filename.is_set or self.boot_filename.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.boot_filename.get_name_leafdata())
                                    if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.domain_name.get_name_leafdata())
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())
                                    if (self.infinite_lease.is_set or self.infinite_lease.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.infinite_lease.get_name_leafdata())
                                    if (self.next_server.is_set or self.next_server.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.next_server.get_name_leafdata())
                                    if (self.pool.is_set or self.pool.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.pool.get_name_leafdata())
                                    if (self.subnet_mask.is_set or self.subnet_mask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.subnet_mask.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "class-match"):
                                        if (self.class_match is None):
                                            self.class_match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.ClassMatch()
                                            self.class_match.parent = self
                                            self._children_name_map["class_match"] = "class-match"
                                        return self.class_match

                                    if (child_yang_name == "default-routers"):
                                        if (self.default_routers is None):
                                            self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DefaultRouters()
                                            self.default_routers.parent = self
                                            self._children_name_map["default_routers"] = "default-routers"
                                        return self.default_routers

                                    if (child_yang_name == "dns-servers"):
                                        if (self.dns_servers is None):
                                            self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.DnsServers()
                                            self.dns_servers.parent = self
                                            self._children_name_map["dns_servers"] = "dns-servers"
                                        return self.dns_servers

                                    if (child_yang_name == "lease"):
                                        if (self.lease is None):
                                            self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.Lease()
                                            self.lease.parent = self
                                            self._children_name_map["lease"] = "lease"
                                        return self.lease

                                    if (child_yang_name == "net-bios-name-servers"):
                                        if (self.net_bios_name_servers is None):
                                            self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetBiosNameServers()
                                            self.net_bios_name_servers.parent = self
                                            self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"
                                        return self.net_bios_name_servers

                                    if (child_yang_name == "netbios-node-type"):
                                        if (self.netbios_node_type is None):
                                            self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.NetbiosNodeType()
                                            self.netbios_node_type.parent = self
                                            self._children_name_map["netbios_node_type"] = "netbios-node-type"
                                        return self.netbios_node_type

                                    if (child_yang_name == "option-codes"):
                                        if (self.option_codes is None):
                                            self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_.OptionCodes()
                                            self.option_codes.parent = self
                                            self._children_name_map["option_codes"] = "option-codes"
                                        return self.option_codes

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "class-match" or name == "default-routers" or name == "dns-servers" or name == "lease" or name == "net-bios-name-servers" or name == "netbios-node-type" or name == "option-codes" or name == "class-name" or name == "boot-filename" or name == "domain-name" or name == "enable" or name == "infinite-lease" or name == "next-server" or name == "pool" or name == "subnet-mask"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "class-name"):
                                        self.class_name = value
                                        self.class_name.value_namespace = name_space
                                        self.class_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "boot-filename"):
                                        self.boot_filename = value
                                        self.boot_filename.value_namespace = name_space
                                        self.boot_filename.value_namespace_prefix = name_space_prefix
                                    if(value_path == "domain-name"):
                                        self.domain_name = value
                                        self.domain_name.value_namespace = name_space
                                        self.domain_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix
                                    if(value_path == "infinite-lease"):
                                        self.infinite_lease = value
                                        self.infinite_lease.value_namespace = name_space
                                        self.infinite_lease.value_namespace_prefix = name_space_prefix
                                    if(value_path == "next-server"):
                                        self.next_server = value
                                        self.next_server.value_namespace = name_space
                                        self.next_server.value_namespace_prefix = name_space_prefix
                                    if(value_path == "pool"):
                                        self.pool = value
                                        self.pool.value_namespace = name_space
                                        self.pool.value_namespace_prefix = name_space_prefix
                                    if(value_path == "subnet-mask"):
                                        self.subnet_mask = value
                                        self.subnet_mask.value_namespace = name_space
                                        self.subnet_mask.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.class_:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.class_:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "classes" + path_buffer

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

                                if (child_yang_name == "class"):
                                    for c in self.class_:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes.Class_()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.class_.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "class"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, self).__init__()

                                self.yang_name = "relay"
                                self.yang_parent_name = "server"

                                self.authenticate = YLeaf(YType.int32, "authenticate")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("authenticate") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay, self).__setattr__(name, value)

                            def has_data(self):
                                return self.authenticate.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.authenticate.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "relay" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.authenticate.is_set or self.authenticate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authenticate.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "authenticate"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "authenticate"):
                                    self.authenticate = value
                                    self.authenticate.value_namespace = name_space
                                    self.authenticate.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, self).__init__()

                                self.yang_name = "lease"
                                self.yang_parent_name = "server"

                                self.days = YLeaf(YType.uint32, "days")

                                self.hours = YLeaf(YType.uint32, "hours")

                                self.infinite = YLeaf(YType.str, "infinite")

                                self.minutes = YLeaf(YType.uint32, "minutes")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("days",
                                                "hours",
                                                "infinite",
                                                "minutes") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.days.is_set or
                                    self.hours.is_set or
                                    self.infinite.is_set or
                                    self.minutes.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.days.yfilter != YFilter.not_set or
                                    self.hours.yfilter != YFilter.not_set or
                                    self.infinite.yfilter != YFilter.not_set or
                                    self.minutes.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lease" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.days.is_set or self.days.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.days.get_name_leafdata())
                                if (self.hours.is_set or self.hours.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hours.get_name_leafdata())
                                if (self.infinite.is_set or self.infinite.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.infinite.get_name_leafdata())
                                if (self.minutes.is_set or self.minutes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.minutes.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "days" or name == "hours" or name == "infinite" or name == "minutes"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "days"):
                                    self.days = value
                                    self.days.value_namespace = name_space
                                    self.days.value_namespace_prefix = name_space_prefix
                                if(value_path == "hours"):
                                    self.hours = value
                                    self.hours.value_namespace = name_space
                                    self.hours.value_namespace_prefix = name_space_prefix
                                if(value_path == "infinite"):
                                    self.infinite = value
                                    self.infinite.value_namespace = name_space
                                    self.infinite.value_namespace_prefix = name_space_prefix
                                if(value_path == "minutes"):
                                    self.minutes = value
                                    self.minutes.value_namespace = name_space
                                    self.minutes.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, self).__init__()

                                self.yang_name = "netbios-node-type"
                                self.yang_parent_name = "server"

                                self.broadcast_node = YLeaf(YType.str, "broadcast-node")

                                self.hexadecimal = YLeaf(YType.str, "hexadecimal")

                                self.hybrid_node = YLeaf(YType.str, "hybrid-node")

                                self.mixed_node = YLeaf(YType.str, "mixed-node")

                                self.peer_to_peer_node = YLeaf(YType.str, "peer-to-peer-node")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("broadcast_node",
                                                "hexadecimal",
                                                "hybrid_node",
                                                "mixed_node",
                                                "peer_to_peer_node") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.broadcast_node.is_set or
                                    self.hexadecimal.is_set or
                                    self.hybrid_node.is_set or
                                    self.mixed_node.is_set or
                                    self.peer_to_peer_node.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.broadcast_node.yfilter != YFilter.not_set or
                                    self.hexadecimal.yfilter != YFilter.not_set or
                                    self.hybrid_node.yfilter != YFilter.not_set or
                                    self.mixed_node.yfilter != YFilter.not_set or
                                    self.peer_to_peer_node.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "netbios-node-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.broadcast_node.is_set or self.broadcast_node.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.broadcast_node.get_name_leafdata())
                                if (self.hexadecimal.is_set or self.hexadecimal.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hexadecimal.get_name_leafdata())
                                if (self.hybrid_node.is_set or self.hybrid_node.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.hybrid_node.get_name_leafdata())
                                if (self.mixed_node.is_set or self.mixed_node.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mixed_node.get_name_leafdata())
                                if (self.peer_to_peer_node.is_set or self.peer_to_peer_node.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.peer_to_peer_node.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "broadcast-node" or name == "hexadecimal" or name == "hybrid-node" or name == "mixed-node" or name == "peer-to-peer-node"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "broadcast-node"):
                                    self.broadcast_node = value
                                    self.broadcast_node.value_namespace = name_space
                                    self.broadcast_node.value_namespace_prefix = name_space_prefix
                                if(value_path == "hexadecimal"):
                                    self.hexadecimal = value
                                    self.hexadecimal.value_namespace = name_space
                                    self.hexadecimal.value_namespace_prefix = name_space_prefix
                                if(value_path == "hybrid-node"):
                                    self.hybrid_node = value
                                    self.hybrid_node.value_namespace = name_space
                                    self.hybrid_node.value_namespace_prefix = name_space_prefix
                                if(value_path == "mixed-node"):
                                    self.mixed_node = value
                                    self.mixed_node.value_namespace = name_space
                                    self.mixed_node.value_namespace_prefix = name_space_prefix
                                if(value_path == "peer-to-peer-node"):
                                    self.peer_to_peer_node = value
                                    self.peer_to_peer_node.value_namespace = name_space
                                    self.peer_to_peer_node.value_namespace_prefix = name_space_prefix


                        class Aaa(Entity):
                            """
                            Enable aaa dhcp option force\-insert
                            
                            .. attribute:: dhcp_option
                            
                            	Enable aaa dhcp option force\-insert
                            	**type**\:   :py:class:`DhcpOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa, self).__init__()

                                self.yang_name = "aaa"
                                self.yang_parent_name = "server"

                                self.dhcp_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption()
                                self.dhcp_option.parent = self
                                self._children_name_map["dhcp_option"] = "dhcp-option"
                                self._children_yang_names.add("dhcp-option")


                            class DhcpOption(Entity):
                                """
                                Enable aaa dhcp option force\-insert
                                
                                .. attribute:: force_insert
                                
                                	Enable aaa dhcp option force\-insert
                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption, self).__init__()

                                    self.yang_name = "dhcp-option"
                                    self.yang_parent_name = "aaa"

                                    self.force_insert = YLeaf(YType.empty, "force-insert")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("force_insert") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.force_insert.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.force_insert.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "dhcp-option" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.force_insert.is_set or self.force_insert.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.force_insert.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "force-insert"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "force-insert"):
                                        self.force_insert = value
                                        self.force_insert.value_namespace = name_space
                                        self.force_insert.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (self.dhcp_option is not None and self.dhcp_option.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.dhcp_option is not None and self.dhcp_option.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "aaa" + path_buffer

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

                                if (child_yang_name == "dhcp-option"):
                                    if (self.dhcp_option is None):
                                        self.dhcp_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa.DhcpOption()
                                        self.dhcp_option.parent = self
                                        self._children_name_map["dhcp_option"] = "dhcp-option"
                                    return self.dhcp_option

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dhcp-option"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class DnsServers(Entity):
                            """
                            DNS servers
                            
                            .. attribute:: dns_server
                            
                            	DNS Server's IP address
                            	**type**\:  list of str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, self).__init__()

                                self.yang_name = "dns-servers"
                                self.yang_parent_name = "server"

                                self.dns_server = YLeafList(YType.str, "dns-server")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dns_server") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers, self).__setattr__(name, value)

                            def has_data(self):
                                for leaf in self.dns_server.getYLeafs():
                                    if (leaf.yfilter != YFilter.not_set):
                                        return True
                                return False

                            def has_operation(self):
                                for leaf in self.dns_server.getYLeafs():
                                    if (leaf.is_set):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dns_server.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dns-servers" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()

                                leaf_name_data.extend(self.dns_server.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dns-server"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dns-server"):
                                    self.dns_server.append(value)


                        class OptionCodes(Entity):
                            """
                            Table of OptionCode
                            
                            .. attribute:: option_code
                            
                            	DHCP option code
                            	**type**\: list of    :py:class:`OptionCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, self).__init__()

                                self.yang_name = "option-codes"
                                self.yang_parent_name = "server"

                                self.option_code = YList(self)

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
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, self).__init__()

                                    self.yang_name = "option-code"
                                    self.yang_parent_name = "option-codes"

                                    self.option_code = YLeaf(YType.uint32, "option-code")

                                    self.ascii_string = YLeaf(YType.str, "ascii-string")

                                    self.force_insert = YLeaf(YType.int32, "force-insert")

                                    self.hex_string = YLeaf(YType.str, "hex-string")

                                    self.ip_address = YLeafList(YType.str, "ip-address")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("option_code",
                                                    "ascii_string",
                                                    "force_insert",
                                                    "hex_string",
                                                    "ip_address") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode, self).__setattr__(name, value)

                                def has_data(self):
                                    for leaf in self.ip_address.getYLeafs():
                                        if (leaf.yfilter != YFilter.not_set):
                                            return True
                                    return (
                                        self.option_code.is_set or
                                        self.ascii_string.is_set or
                                        self.force_insert.is_set or
                                        self.hex_string.is_set)

                                def has_operation(self):
                                    for leaf in self.ip_address.getYLeafs():
                                        if (leaf.is_set):
                                            return True
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.option_code.yfilter != YFilter.not_set or
                                        self.ascii_string.yfilter != YFilter.not_set or
                                        self.force_insert.yfilter != YFilter.not_set or
                                        self.hex_string.yfilter != YFilter.not_set or
                                        self.ip_address.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "option-code" + "[option-code='" + self.option_code.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.option_code.is_set or self.option_code.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.option_code.get_name_leafdata())
                                    if (self.ascii_string.is_set or self.ascii_string.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ascii_string.get_name_leafdata())
                                    if (self.force_insert.is_set or self.force_insert.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.force_insert.get_name_leafdata())
                                    if (self.hex_string.is_set or self.hex_string.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.hex_string.get_name_leafdata())

                                    leaf_name_data.extend(self.ip_address.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option-code" or name == "ascii-string" or name == "force-insert" or name == "hex-string" or name == "ip-address"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "option-code"):
                                        self.option_code = value
                                        self.option_code.value_namespace = name_space
                                        self.option_code.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ascii-string"):
                                        self.ascii_string = value
                                        self.ascii_string.value_namespace = name_space
                                        self.ascii_string.value_namespace_prefix = name_space_prefix
                                    if(value_path == "force-insert"):
                                        self.force_insert = value
                                        self.force_insert.value_namespace = name_space
                                        self.force_insert.value_namespace_prefix = name_space_prefix
                                    if(value_path == "hex-string"):
                                        self.hex_string = value
                                        self.hex_string.value_namespace = name_space
                                        self.hex_string.value_namespace_prefix = name_space_prefix
                                    if(value_path == "ip-address"):
                                        self.ip_address.append(value)

                            def has_data(self):
                                for c in self.option_code:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.option_code:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "option-codes" + path_buffer

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

                                if (child_yang_name == "option-code"):
                                    for c in self.option_code:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes.OptionCode()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.option_code.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "option-code"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.boot_filename.is_set or
                                self.domain_name.is_set or
                                self.infinite_lease.is_set or
                                self.next_server.is_set or
                                self.pool.is_set or
                                self.secure_arp.is_set or
                                self.server_allow_move.is_set or
                                self.subnet_mask.is_set or
                                (self.aaa is not None and self.aaa.has_data()) or
                                (self.broadcast_flag is not None and self.broadcast_flag.has_data()) or
                                (self.classes is not None and self.classes.has_data()) or
                                (self.default_routers is not None and self.default_routers.has_data()) or
                                (self.dns_servers is not None and self.dns_servers.has_data()) or
                                (self.lease is not None and self.lease.has_data()) or
                                (self.lease_limit is not None and self.lease_limit.has_data()) or
                                (self.match is not None and self.match.has_data()) or
                                (self.net_bios_name_servers is not None and self.net_bios_name_servers.has_data()) or
                                (self.netbios_node_type is not None and self.netbios_node_type.has_data()) or
                                (self.option_codes is not None and self.option_codes.has_data()) or
                                (self.relay is not None and self.relay.has_data()) or
                                (self.requested_ip_address is not None and self.requested_ip_address.has_data()) or
                                (self.server_id_check is not None and self.server_id_check.has_data()) or
                                (self.session is not None and self.session.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.boot_filename.yfilter != YFilter.not_set or
                                self.domain_name.yfilter != YFilter.not_set or
                                self.infinite_lease.yfilter != YFilter.not_set or
                                self.next_server.yfilter != YFilter.not_set or
                                self.pool.yfilter != YFilter.not_set or
                                self.secure_arp.yfilter != YFilter.not_set or
                                self.server_allow_move.yfilter != YFilter.not_set or
                                self.subnet_mask.yfilter != YFilter.not_set or
                                (self.aaa is not None and self.aaa.has_operation()) or
                                (self.broadcast_flag is not None and self.broadcast_flag.has_operation()) or
                                (self.classes is not None and self.classes.has_operation()) or
                                (self.default_routers is not None and self.default_routers.has_operation()) or
                                (self.dns_servers is not None and self.dns_servers.has_operation()) or
                                (self.lease is not None and self.lease.has_operation()) or
                                (self.lease_limit is not None and self.lease_limit.has_operation()) or
                                (self.match is not None and self.match.has_operation()) or
                                (self.net_bios_name_servers is not None and self.net_bios_name_servers.has_operation()) or
                                (self.netbios_node_type is not None and self.netbios_node_type.has_operation()) or
                                (self.option_codes is not None and self.option_codes.has_operation()) or
                                (self.relay is not None and self.relay.has_operation()) or
                                (self.requested_ip_address is not None and self.requested_ip_address.has_operation()) or
                                (self.server_id_check is not None and self.server_id_check.has_operation()) or
                                (self.session is not None and self.session.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "server" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.boot_filename.is_set or self.boot_filename.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.boot_filename.get_name_leafdata())
                            if (self.domain_name.is_set or self.domain_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.domain_name.get_name_leafdata())
                            if (self.infinite_lease.is_set or self.infinite_lease.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.infinite_lease.get_name_leafdata())
                            if (self.next_server.is_set or self.next_server.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.next_server.get_name_leafdata())
                            if (self.pool.is_set or self.pool.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pool.get_name_leafdata())
                            if (self.secure_arp.is_set or self.secure_arp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.secure_arp.get_name_leafdata())
                            if (self.server_allow_move.is_set or self.server_allow_move.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.server_allow_move.get_name_leafdata())
                            if (self.subnet_mask.is_set or self.subnet_mask.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.subnet_mask.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "aaa"):
                                if (self.aaa is None):
                                    self.aaa = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Aaa()
                                    self.aaa.parent = self
                                    self._children_name_map["aaa"] = "aaa"
                                return self.aaa

                            if (child_yang_name == "broadcast-flag"):
                                if (self.broadcast_flag is None):
                                    self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.BroadcastFlag()
                                    self.broadcast_flag.parent = self
                                    self._children_name_map["broadcast_flag"] = "broadcast-flag"
                                return self.broadcast_flag

                            if (child_yang_name == "classes"):
                                if (self.classes is None):
                                    self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Classes()
                                    self.classes.parent = self
                                    self._children_name_map["classes"] = "classes"
                                return self.classes

                            if (child_yang_name == "default-routers"):
                                if (self.default_routers is None):
                                    self.default_routers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DefaultRouters()
                                    self.default_routers.parent = self
                                    self._children_name_map["default_routers"] = "default-routers"
                                return self.default_routers

                            if (child_yang_name == "dns-servers"):
                                if (self.dns_servers is None):
                                    self.dns_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.DnsServers()
                                    self.dns_servers.parent = self
                                    self._children_name_map["dns_servers"] = "dns-servers"
                                return self.dns_servers

                            if (child_yang_name == "lease"):
                                if (self.lease is None):
                                    self.lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Lease()
                                    self.lease.parent = self
                                    self._children_name_map["lease"] = "lease"
                                return self.lease

                            if (child_yang_name == "lease-limit"):
                                if (self.lease_limit is None):
                                    self.lease_limit = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.LeaseLimit()
                                    self.lease_limit.parent = self
                                    self._children_name_map["lease_limit"] = "lease-limit"
                                return self.lease_limit

                            if (child_yang_name == "match"):
                                if (self.match is None):
                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                return self.match

                            if (child_yang_name == "net-bios-name-servers"):
                                if (self.net_bios_name_servers is None):
                                    self.net_bios_name_servers = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetBiosNameServers()
                                    self.net_bios_name_servers.parent = self
                                    self._children_name_map["net_bios_name_servers"] = "net-bios-name-servers"
                                return self.net_bios_name_servers

                            if (child_yang_name == "netbios-node-type"):
                                if (self.netbios_node_type is None):
                                    self.netbios_node_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.NetbiosNodeType()
                                    self.netbios_node_type.parent = self
                                    self._children_name_map["netbios_node_type"] = "netbios-node-type"
                                return self.netbios_node_type

                            if (child_yang_name == "option-codes"):
                                if (self.option_codes is None):
                                    self.option_codes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.OptionCodes()
                                    self.option_codes.parent = self
                                    self._children_name_map["option_codes"] = "option-codes"
                                return self.option_codes

                            if (child_yang_name == "relay"):
                                if (self.relay is None):
                                    self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Relay()
                                    self.relay.parent = self
                                    self._children_name_map["relay"] = "relay"
                                return self.relay

                            if (child_yang_name == "requested-ip-address"):
                                if (self.requested_ip_address is None):
                                    self.requested_ip_address = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.RequestedIpAddress()
                                    self.requested_ip_address.parent = self
                                    self._children_name_map["requested_ip_address"] = "requested-ip-address"
                                return self.requested_ip_address

                            if (child_yang_name == "server-id-check"):
                                if (self.server_id_check is None):
                                    self.server_id_check = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.ServerIdCheck()
                                    self.server_id_check.parent = self
                                    self._children_name_map["server_id_check"] = "server-id-check"
                                return self.server_id_check

                            if (child_yang_name == "session"):
                                if (self.session is None):
                                    self.session = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server.Session()
                                    self.session.parent = self
                                    self._children_name_map["session"] = "session"
                                return self.session

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "aaa" or name == "broadcast-flag" or name == "classes" or name == "default-routers" or name == "dns-servers" or name == "lease" or name == "lease-limit" or name == "match" or name == "net-bios-name-servers" or name == "netbios-node-type" or name == "option-codes" or name == "relay" or name == "requested-ip-address" or name == "server-id-check" or name == "session" or name == "boot-filename" or name == "domain-name" or name == "infinite-lease" or name == "next-server" or name == "pool" or name == "secure-arp" or name == "server-allow-move" or name == "subnet-mask"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "boot-filename"):
                                self.boot_filename = value
                                self.boot_filename.value_namespace = name_space
                                self.boot_filename.value_namespace_prefix = name_space_prefix
                            if(value_path == "domain-name"):
                                self.domain_name = value
                                self.domain_name.value_namespace = name_space
                                self.domain_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "infinite-lease"):
                                self.infinite_lease = value
                                self.infinite_lease.value_namespace = name_space
                                self.infinite_lease.value_namespace_prefix = name_space_prefix
                            if(value_path == "next-server"):
                                self.next_server = value
                                self.next_server.value_namespace = name_space
                                self.next_server.value_namespace_prefix = name_space_prefix
                            if(value_path == "pool"):
                                self.pool = value
                                self.pool.value_namespace = name_space
                                self.pool.value_namespace_prefix = name_space_prefix
                            if(value_path == "secure-arp"):
                                self.secure_arp = value
                                self.secure_arp.value_namespace = name_space
                                self.secure_arp.value_namespace_prefix = name_space_prefix
                            if(value_path == "server-allow-move"):
                                self.server_allow_move = value
                                self.server_allow_move.value_namespace = name_space
                                self.server_allow_move.value_namespace_prefix = name_space_prefix
                            if(value_path == "subnet-mask"):
                                self.subnet_mask = value
                                self.subnet_mask.value_namespace = name_space
                                self.subnet_mask.value_namespace_prefix = name_space_prefix


                    class Relay(Entity):
                        """
                        DHCP Relay profile
                        
                        .. attribute:: broadcast_policy
                        
                        	Broadcast Flag policy
                        	**type**\:   :py:class:`BroadcastPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy>`
                        
                        .. attribute:: gi_addr_policy
                        
                        	GIADDR policy
                        	**type**\:   :py:class:`GiAddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy>`
                        
                        .. attribute:: relay_information_option
                        
                        	Relay agent information option
                        	**type**\:   :py:class:`RelayInformationOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption>`
                        
                        .. attribute:: vrfs
                        
                        	VRF Helper Addresses
                        	**type**\:   :py:class:`Vrfs <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs>`
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay, self).__init__()

                            self.yang_name = "relay"
                            self.yang_parent_name = "mode"

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


                        class GiAddrPolicy(Entity):
                            """
                            GIADDR policy
                            
                            .. attribute:: policy
                            
                            	GIADDR policy
                            	**type**\:   :py:class:`Ipv4DhcpdGiaddrPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdGiaddrPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, self).__init__()

                                self.yang_name = "gi-addr-policy"
                                self.yang_parent_name = "relay"

                                self.policy = YLeaf(YType.enumeration, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy, self).__setattr__(name, value)

                            def has_data(self):
                                return self.policy.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "gi-addr-policy" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


                        class Vrfs(Entity):
                            """
                            VRF Helper Addresses
                            
                            .. attribute:: vrf
                            
                            	VRF Name
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "relay"

                                self.vrf = YList(self)

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
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._children_yang_names.add("helper-addresses")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf, self).__setattr__(name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper Addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper Address
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"

                                        self.helper_address = YList(self)

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
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"

                                            self.ip_address = YLeaf(YType.str, "ip-address")

                                            self.enable = YLeaf(YType.empty, "enable")

                                            self.gateway_address = YLeaf(YType.str, "gateway-address")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("ip_address",
                                                            "enable",
                                                            "gateway_address") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.ip_address.is_set or
                                                self.enable.is_set or
                                                self.gateway_address.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.ip_address.yfilter != YFilter.not_set or
                                                self.enable.yfilter != YFilter.not_set or
                                                self.gateway_address.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "helper-address" + "[ip-address='" + self.ip_address.get() + "']" + path_buffer

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
                                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.enable.get_name_leafdata())
                                            if (self.gateway_address.is_set or self.gateway_address.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.gateway_address.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "ip-address" or name == "enable" or name == "gateway-address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "ip-address"):
                                                self.ip_address = value
                                                self.ip_address.value_namespace = name_space
                                                self.ip_address.value_namespace_prefix = name_space_prefix
                                            if(value_path == "enable"):
                                                self.enable = value
                                                self.enable.value_namespace = name_space
                                                self.enable.value_namespace_prefix = name_space_prefix
                                            if(value_path == "gateway-address"):
                                                self.gateway_address = value
                                                self.gateway_address.value_namespace = name_space
                                                self.gateway_address.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.helper_address:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.helper_address:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "helper-addresses" + path_buffer

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

                                        if (child_yang_name == "helper-address"):
                                            for c in self.helper_address:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses.HelperAddress()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.helper_address.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "helper-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.vrf_name.is_set or
                                        (self.helper_addresses is not None and self.helper_addresses.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "helper-addresses"):
                                        if (self.helper_addresses is None):
                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self
                                            self._children_name_map["helper_addresses"] = "helper-addresses"
                                        return self.helper_addresses

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "helper-addresses" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.vrf:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.vrf:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "vrfs" + path_buffer

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

                                if (child_yang_name == "vrf"):
                                    for c in self.vrf:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs.Vrf()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.vrf.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "vrf"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicy>`
                            
                            .. attribute:: subscriber_id
                            
                            	Subscriber ID
                            	**type**\:  str
                            
                            .. attribute:: vpn
                            
                            	Insert VPN options
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: vpn_mode
                            
                            	VPN Mode
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionvpnMode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, self).__init__()

                                self.yang_name = "relay-information-option"
                                self.yang_parent_name = "relay"

                                self.allow_untrusted = YLeaf(YType.empty, "allow-untrusted")

                                self.check = YLeaf(YType.empty, "check")

                                self.insert = YLeaf(YType.empty, "insert")

                                self.policy = YLeaf(YType.enumeration, "policy")

                                self.subscriber_id = YLeaf(YType.str, "subscriber-id")

                                self.vpn = YLeaf(YType.empty, "vpn")

                                self.vpn_mode = YLeaf(YType.enumeration, "vpn-mode")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("allow_untrusted",
                                                "check",
                                                "insert",
                                                "policy",
                                                "subscriber_id",
                                                "vpn",
                                                "vpn_mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.allow_untrusted.is_set or
                                    self.check.is_set or
                                    self.insert.is_set or
                                    self.policy.is_set or
                                    self.subscriber_id.is_set or
                                    self.vpn.is_set or
                                    self.vpn_mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.allow_untrusted.yfilter != YFilter.not_set or
                                    self.check.yfilter != YFilter.not_set or
                                    self.insert.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set or
                                    self.subscriber_id.yfilter != YFilter.not_set or
                                    self.vpn.yfilter != YFilter.not_set or
                                    self.vpn_mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "relay-information-option" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.allow_untrusted.is_set or self.allow_untrusted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allow_untrusted.get_name_leafdata())
                                if (self.check.is_set or self.check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.check.get_name_leafdata())
                                if (self.insert.is_set or self.insert.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.insert.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())
                                if (self.subscriber_id.is_set or self.subscriber_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.subscriber_id.get_name_leafdata())
                                if (self.vpn.is_set or self.vpn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vpn.get_name_leafdata())
                                if (self.vpn_mode.is_set or self.vpn_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vpn_mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "allow-untrusted" or name == "check" or name == "insert" or name == "policy" or name == "subscriber-id" or name == "vpn" or name == "vpn-mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "allow-untrusted"):
                                    self.allow_untrusted = value
                                    self.allow_untrusted.value_namespace = name_space
                                    self.allow_untrusted.value_namespace_prefix = name_space_prefix
                                if(value_path == "check"):
                                    self.check = value
                                    self.check.value_namespace = name_space
                                    self.check.value_namespace_prefix = name_space_prefix
                                if(value_path == "insert"):
                                    self.insert = value
                                    self.insert.value_namespace = name_space
                                    self.insert.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix
                                if(value_path == "subscriber-id"):
                                    self.subscriber_id = value
                                    self.subscriber_id.value_namespace = name_space
                                    self.subscriber_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "vpn"):
                                    self.vpn = value
                                    self.vpn.value_namespace = name_space
                                    self.vpn.value_namespace_prefix = name_space_prefix
                                if(value_path == "vpn-mode"):
                                    self.vpn_mode = value
                                    self.vpn_mode.value_namespace = name_space
                                    self.vpn_mode.value_namespace_prefix = name_space_prefix


                        class BroadcastPolicy(Entity):
                            """
                            Broadcast Flag policy
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:   :py:class:`Ipv4DhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdBroadcastFlagPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, self).__init__()

                                self.yang_name = "broadcast-policy"
                                self.yang_parent_name = "relay"

                                self.policy = YLeaf(YType.enumeration, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy, self).__setattr__(name, value)

                            def has_data(self):
                                return self.policy.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "broadcast-policy" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.broadcast_policy is not None and self.broadcast_policy.has_data()) or
                                (self.gi_addr_policy is not None and self.gi_addr_policy.has_data()) or
                                (self.relay_information_option is not None and self.relay_information_option.has_data()) or
                                (self.vrfs is not None and self.vrfs.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.broadcast_policy is not None and self.broadcast_policy.has_operation()) or
                                (self.gi_addr_policy is not None and self.gi_addr_policy.has_operation()) or
                                (self.relay_information_option is not None and self.relay_information_option.has_operation()) or
                                (self.vrfs is not None and self.vrfs.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "relay" + path_buffer

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

                            if (child_yang_name == "broadcast-policy"):
                                if (self.broadcast_policy is None):
                                    self.broadcast_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.BroadcastPolicy()
                                    self.broadcast_policy.parent = self
                                    self._children_name_map["broadcast_policy"] = "broadcast-policy"
                                return self.broadcast_policy

                            if (child_yang_name == "gi-addr-policy"):
                                if (self.gi_addr_policy is None):
                                    self.gi_addr_policy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.GiAddrPolicy()
                                    self.gi_addr_policy.parent = self
                                    self._children_name_map["gi_addr_policy"] = "gi-addr-policy"
                                return self.gi_addr_policy

                            if (child_yang_name == "relay-information-option"):
                                if (self.relay_information_option is None):
                                    self.relay_information_option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.RelayInformationOption()
                                    self.relay_information_option.parent = self
                                    self._children_name_map["relay_information_option"] = "relay-information-option"
                                return self.relay_information_option

                            if (child_yang_name == "vrfs"):
                                if (self.vrfs is None):
                                    self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay.Vrfs()
                                    self.vrfs.parent = self
                                    self._children_name_map["vrfs"] = "vrfs"
                                return self.vrfs

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "broadcast-policy" or name == "gi-addr-policy" or name == "relay-information-option" or name == "vrfs"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass


                    class Proxy(Entity):
                        """
                        DHCP proxy profile
                        
                        .. attribute:: broadcast_flag
                        
                        	Specify broadcast flag
                        	**type**\:   :py:class:`BroadcastFlag <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag>`
                        
                        .. attribute:: classes
                        
                        	DHCP class table
                        	**type**\:   :py:class:`Classes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes>`
                        
                        .. attribute:: enable
                        
                        	DHCP IPV4 profile mode enable
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
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
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, self).__init__()

                            self.yang_name = "proxy"
                            self.yang_parent_name = "mode"

                            self.enable = YLeaf(YType.empty, "enable")

                            self.proxy_allow_move = YLeaf(YType.empty, "proxy-allow-move")

                            self.secure_arp = YLeaf(YType.empty, "secure-arp")

                            self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag()
                            self.broadcast_flag.parent = self
                            self._children_name_map["broadcast_flag"] = "broadcast-flag"
                            self._children_yang_names.add("broadcast-flag")

                            self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes()
                            self.classes.parent = self
                            self._children_name_map["classes"] = "classes"
                            self._children_yang_names.add("classes")

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("enable",
                                            "proxy_allow_move",
                                            "secure_arp") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy, self).__setattr__(name, value)


                        class Classes(Entity):
                            """
                            DHCP class table
                            
                            .. attribute:: class_
                            
                            	DHCP class
                            	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, self).__init__()

                                self.yang_name = "classes"
                                self.yang_parent_name = "proxy"

                                self.class_ = YList(self)

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
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_, self).__init__()

                                    self.yang_name = "class"
                                    self.yang_parent_name = "classes"

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

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("class_name",
                                                    "enable") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match, self).__init__()

                                        self.yang_name = "match"
                                        self.yang_parent_name = "class"

                                        self.vrf = YLeaf(YType.str, "vrf")

                                        self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option()
                                        self.option.parent = self
                                        self._children_name_map["option"] = "option"
                                        self._children_yang_names.add("option")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("vrf") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option, self).__init__()

                                            self.yang_name = "option"
                                            self.yang_parent_name = "match"

                                            self.bit_mask = YLeaf(YType.str, "bit-mask")

                                            self.option_type = YLeaf(YType.enumeration, "option-type")

                                            self.pattern = YLeaf(YType.str, "pattern")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("bit_mask",
                                                            "option_type",
                                                            "pattern") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.bit_mask.is_set or
                                                self.option_type.is_set or
                                                self.pattern.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.bit_mask.yfilter != YFilter.not_set or
                                                self.option_type.yfilter != YFilter.not_set or
                                                self.pattern.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "option" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.bit_mask.is_set or self.bit_mask.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.bit_mask.get_name_leafdata())
                                            if (self.option_type.is_set or self.option_type.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.option_type.get_name_leafdata())
                                            if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.pattern.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "bit-mask" or name == "option-type" or name == "pattern"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "bit-mask"):
                                                self.bit_mask = value
                                                self.bit_mask.value_namespace = name_space
                                                self.bit_mask.value_namespace_prefix = name_space_prefix
                                            if(value_path == "option-type"):
                                                self.option_type = value
                                                self.option_type.value_namespace = name_space
                                                self.option_type.value_namespace_prefix = name_space_prefix
                                            if(value_path == "pattern"):
                                                self.pattern = value
                                                self.pattern.value_namespace = name_space
                                                self.pattern.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        return (
                                            self.vrf.is_set or
                                            (self.option is not None and self.option.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.vrf.yfilter != YFilter.not_set or
                                            (self.option is not None and self.option.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "match" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.vrf.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "option"):
                                            if (self.option is None):
                                                self.option = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match.Option()
                                                self.option.parent = self
                                                self._children_name_map["option"] = "option"
                                            return self.option

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "option" or name == "vrf"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "vrf"):
                                            self.vrf = value
                                            self.vrf.value_namespace = name_space
                                            self.vrf.value_namespace_prefix = name_space_prefix


                                class Vrfs(Entity):
                                    """
                                    List of VRFs
                                    
                                    .. attribute:: vrf
                                    
                                    	VRF name
                                    	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs, self).__init__()

                                        self.yang_name = "vrfs"
                                        self.yang_parent_name = "class"

                                        self.vrf = YList(self)

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
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf, self).__init__()

                                            self.yang_name = "vrf"
                                            self.yang_parent_name = "vrfs"

                                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self
                                            self._children_name_map["helper_addresses"] = "helper-addresses"
                                            self._children_yang_names.add("helper-addresses")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("vrf_name") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf, self).__setattr__(name, value)


                                        class HelperAddresses(Entity):
                                            """
                                            Helper addresses
                                            
                                            .. attribute:: helper_address
                                            
                                            	Helper address
                                            	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                            
                                            

                                            """

                                            _prefix = 'ipv4-dhcpd-cfg'
                                            _revision = '2015-11-09'

                                            def __init__(self):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses, self).__init__()

                                                self.yang_name = "helper-addresses"
                                                self.yang_parent_name = "vrf"

                                                self.helper_address = YList(self)

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
                                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)


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
                                                _revision = '2015-11-09'

                                                def __init__(self):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                                    self.yang_name = "helper-address"
                                                    self.yang_parent_name = "helper-addresses"

                                                    self.server_address = YLeaf(YType.str, "server-address")

                                                    self.gateway_address = YLeaf(YType.str, "gateway-address")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("server_address",
                                                                    "gateway_address") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.server_address.is_set or
                                                        self.gateway_address.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.server_address.yfilter != YFilter.not_set or
                                                        self.gateway_address.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "helper-address" + "[server-address='" + self.server_address.get() + "']" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.server_address.get_name_leafdata())
                                                    if (self.gateway_address.is_set or self.gateway_address.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.gateway_address.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "server-address" or name == "gateway-address"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "server-address"):
                                                        self.server_address = value
                                                        self.server_address.value_namespace = name_space
                                                        self.server_address.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "gateway-address"):
                                                        self.gateway_address = value
                                                        self.gateway_address.value_namespace = name_space
                                                        self.gateway_address.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                for c in self.helper_address:
                                                    if (c.has_data()):
                                                        return True
                                                return False

                                            def has_operation(self):
                                                for c in self.helper_address:
                                                    if (c.has_operation()):
                                                        return True
                                                return self.yfilter != YFilter.not_set

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "helper-addresses" + path_buffer

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

                                                if (child_yang_name == "helper-address"):
                                                    for c in self.helper_address:
                                                        segment = c.get_segment_path()
                                                        if (segment_path == segment):
                                                            return c
                                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses.HelperAddress()
                                                    c.parent = self
                                                    local_reference_key = "ydk::seg::%s" % segment_path
                                                    self._local_refs[local_reference_key] = c
                                                    self.helper_address.append(c)
                                                    return c

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "helper-address"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                pass

                                        def has_data(self):
                                            return (
                                                self.vrf_name.is_set or
                                                (self.helper_addresses is not None and self.helper_addresses.has_data()))

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.vrf_name.yfilter != YFilter.not_set or
                                                (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            if (child_yang_name == "helper-addresses"):
                                                if (self.helper_addresses is None):
                                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf.HelperAddresses()
                                                    self.helper_addresses.parent = self
                                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                                return self.helper_addresses

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "helper-addresses" or name == "vrf-name"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "vrf-name"):
                                                self.vrf_name = value
                                                self.vrf_name.value_namespace = name_space
                                                self.vrf_name.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.vrf:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.vrf:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "vrfs" + path_buffer

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

                                        if (child_yang_name == "vrf"):
                                            for c in self.vrf:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs.Vrf()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.vrf.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "vrf"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.class_name.is_set or
                                        self.enable.is_set or
                                        (self.match is not None and self.match.has_data()) or
                                        (self.vrfs is not None and self.vrfs.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.class_name.yfilter != YFilter.not_set or
                                        self.enable.yfilter != YFilter.not_set or
                                        (self.match is not None and self.match.has_operation()) or
                                        (self.vrfs is not None and self.vrfs.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.class_name.is_set or self.class_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.class_name.get_name_leafdata())
                                    if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enable.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "match"):
                                        if (self.match is None):
                                            self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Match()
                                            self.match.parent = self
                                            self._children_name_map["match"] = "match"
                                        return self.match

                                    if (child_yang_name == "vrfs"):
                                        if (self.vrfs is None):
                                            self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_.Vrfs()
                                            self.vrfs.parent = self
                                            self._children_name_map["vrfs"] = "vrfs"
                                        return self.vrfs

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "match" or name == "vrfs" or name == "class-name" or name == "enable"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "class-name"):
                                        self.class_name = value
                                        self.class_name.value_namespace = name_space
                                        self.class_name.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enable"):
                                        self.enable = value
                                        self.enable.value_namespace = name_space
                                        self.enable.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.class_:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.class_:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "classes" + path_buffer

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

                                if (child_yang_name == "class"):
                                    for c in self.class_:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes.Class_()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.class_.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "class"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class RelayInformation(Entity):
                            """
                            Relay agent information option
                            
                            .. attribute:: allow_untrusted
                            
                            	Forward untrusted packets
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: authenticate
                            
                            	Relay information option authenticate
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionAuthenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionAuthenticate>`
                            
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
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionPolicy>`
                            
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
                            	**type**\:   :py:class:`Ipv4DhcpdRelayInfoOptionvpnMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdRelayInfoOptionvpnMode>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, self).__init__()

                                self.yang_name = "relay-information"
                                self.yang_parent_name = "proxy"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("allow_untrusted",
                                                "authenticate",
                                                "check",
                                                "circuit_id",
                                                "option",
                                                "policy",
                                                "remote_id",
                                                "remote_id_suppress",
                                                "remote_id_xr",
                                                "vpn",
                                                "vpn_mode") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.allow_untrusted.is_set or
                                    self.authenticate.is_set or
                                    self.check.is_set or
                                    self.circuit_id.is_set or
                                    self.option.is_set or
                                    self.policy.is_set or
                                    self.remote_id.is_set or
                                    self.remote_id_suppress.is_set or
                                    self.remote_id_xr.is_set or
                                    self.vpn.is_set or
                                    self.vpn_mode.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.allow_untrusted.yfilter != YFilter.not_set or
                                    self.authenticate.yfilter != YFilter.not_set or
                                    self.check.yfilter != YFilter.not_set or
                                    self.circuit_id.yfilter != YFilter.not_set or
                                    self.option.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set or
                                    self.remote_id.yfilter != YFilter.not_set or
                                    self.remote_id_suppress.yfilter != YFilter.not_set or
                                    self.remote_id_xr.yfilter != YFilter.not_set or
                                    self.vpn.yfilter != YFilter.not_set or
                                    self.vpn_mode.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "relay-information" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.allow_untrusted.is_set or self.allow_untrusted.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.allow_untrusted.get_name_leafdata())
                                if (self.authenticate.is_set or self.authenticate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.authenticate.get_name_leafdata())
                                if (self.check.is_set or self.check.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.check.get_name_leafdata())
                                if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.circuit_id.get_name_leafdata())
                                if (self.option.is_set or self.option.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.option.get_name_leafdata())
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())
                                if (self.remote_id.is_set or self.remote_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id.get_name_leafdata())
                                if (self.remote_id_suppress.is_set or self.remote_id_suppress.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id_suppress.get_name_leafdata())
                                if (self.remote_id_xr.is_set or self.remote_id_xr.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_id_xr.get_name_leafdata())
                                if (self.vpn.is_set or self.vpn.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vpn.get_name_leafdata())
                                if (self.vpn_mode.is_set or self.vpn_mode.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vpn_mode.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "allow-untrusted" or name == "authenticate" or name == "check" or name == "circuit-id" or name == "option" or name == "policy" or name == "remote-id" or name == "remote-id-suppress" or name == "remote-id-xr" or name == "vpn" or name == "vpn-mode"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "allow-untrusted"):
                                    self.allow_untrusted = value
                                    self.allow_untrusted.value_namespace = name_space
                                    self.allow_untrusted.value_namespace_prefix = name_space_prefix
                                if(value_path == "authenticate"):
                                    self.authenticate = value
                                    self.authenticate.value_namespace = name_space
                                    self.authenticate.value_namespace_prefix = name_space_prefix
                                if(value_path == "check"):
                                    self.check = value
                                    self.check.value_namespace = name_space
                                    self.check.value_namespace_prefix = name_space_prefix
                                if(value_path == "circuit-id"):
                                    self.circuit_id = value
                                    self.circuit_id.value_namespace = name_space
                                    self.circuit_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "option"):
                                    self.option = value
                                    self.option.value_namespace = name_space
                                    self.option.value_namespace_prefix = name_space_prefix
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id"):
                                    self.remote_id = value
                                    self.remote_id.value_namespace = name_space
                                    self.remote_id.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id-suppress"):
                                    self.remote_id_suppress = value
                                    self.remote_id_suppress.value_namespace = name_space
                                    self.remote_id_suppress.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-id-xr"):
                                    self.remote_id_xr = value
                                    self.remote_id_xr.value_namespace = name_space
                                    self.remote_id_xr.value_namespace_prefix = name_space_prefix
                                if(value_path == "vpn"):
                                    self.vpn = value
                                    self.vpn.value_namespace = name_space
                                    self.vpn.value_namespace_prefix = name_space_prefix
                                if(value_path == "vpn-mode"):
                                    self.vpn_mode = value
                                    self.vpn_mode.value_namespace = name_space
                                    self.vpn_mode.value_namespace_prefix = name_space_prefix


                        class Vrfs(Entity):
                            """
                            List of VRFs
                            
                            .. attribute:: vrf
                            
                            	VRF name
                            	**type**\: list of    :py:class:`Vrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, self).__init__()

                                self.yang_name = "vrfs"
                                self.yang_parent_name = "proxy"

                                self.vrf = YList(self)

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
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs, self).__setattr__(name, value)


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
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, self).__init__()

                                    self.yang_name = "vrf"
                                    self.yang_parent_name = "vrfs"

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                    self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses()
                                    self.helper_addresses.parent = self
                                    self._children_name_map["helper_addresses"] = "helper-addresses"
                                    self._children_yang_names.add("helper-addresses")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf, self).__setattr__(name, value)


                                class HelperAddresses(Entity):
                                    """
                                    Helper addresses
                                    
                                    .. attribute:: helper_address
                                    
                                    	Helper address
                                    	**type**\: list of    :py:class:`HelperAddress <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress>`
                                    
                                    

                                    """

                                    _prefix = 'ipv4-dhcpd-cfg'
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, self).__init__()

                                        self.yang_name = "helper-addresses"
                                        self.yang_parent_name = "vrf"

                                        self.helper_address = YList(self)

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
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses, self).__setattr__(name, value)


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
                                        _revision = '2015-11-09'

                                        def __init__(self):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__init__()

                                            self.yang_name = "helper-address"
                                            self.yang_parent_name = "helper-addresses"

                                            self.server_address = YLeaf(YType.str, "server-address")

                                            self.gateway_address = YLeaf(YType.str, "gateway-address")

                                        def __setattr__(self, name, value):
                                            self._check_monkey_patching_error(name, value)
                                            with _handle_type_error():
                                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                        "Please use list append or extend method."
                                                                        .format(value))
                                                if isinstance(value, Enum.YLeaf):
                                                    value = value.name
                                                if name in ("server_address",
                                                            "gateway_address") and name in self.__dict__:
                                                    if isinstance(value, YLeaf):
                                                        self.__dict__[name].set(value.get())
                                                    elif isinstance(value, YLeafList):
                                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress, self).__setattr__(name, value)

                                        def has_data(self):
                                            return (
                                                self.server_address.is_set or
                                                self.gateway_address.is_set)

                                        def has_operation(self):
                                            return (
                                                self.yfilter != YFilter.not_set or
                                                self.server_address.yfilter != YFilter.not_set or
                                                self.gateway_address.yfilter != YFilter.not_set)

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "helper-address" + "[server-address='" + self.server_address.get() + "']" + path_buffer

                                            return path_buffer

                                        def get_entity_path(self, ancestor):
                                            path_buffer = ""
                                            if (ancestor is None):
                                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                            else:
                                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                            leaf_name_data = LeafDataList()
                                            if (self.server_address.is_set or self.server_address.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.server_address.get_name_leafdata())
                                            if (self.gateway_address.is_set or self.gateway_address.yfilter != YFilter.not_set):
                                                leaf_name_data.append(self.gateway_address.get_name_leafdata())

                                            entity_path = EntityPath(path_buffer, leaf_name_data)
                                            return entity_path

                                        def get_child_by_name(self, child_yang_name, segment_path):
                                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                            if child is not None:
                                                return child

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "server-address" or name == "gateway-address"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            if(value_path == "server-address"):
                                                self.server_address = value
                                                self.server_address.value_namespace = name_space
                                                self.server_address.value_namespace_prefix = name_space_prefix
                                            if(value_path == "gateway-address"):
                                                self.gateway_address = value
                                                self.gateway_address.value_namespace = name_space
                                                self.gateway_address.value_namespace_prefix = name_space_prefix

                                    def has_data(self):
                                        for c in self.helper_address:
                                            if (c.has_data()):
                                                return True
                                        return False

                                    def has_operation(self):
                                        for c in self.helper_address:
                                            if (c.has_operation()):
                                                return True
                                        return self.yfilter != YFilter.not_set

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "helper-addresses" + path_buffer

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

                                        if (child_yang_name == "helper-address"):
                                            for c in self.helper_address:
                                                segment = c.get_segment_path()
                                                if (segment_path == segment):
                                                    return c
                                            c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses.HelperAddress()
                                            c.parent = self
                                            local_reference_key = "ydk::seg::%s" % segment_path
                                            self._local_refs[local_reference_key] = c
                                            self.helper_address.append(c)
                                            return c

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "helper-address"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        pass

                                def has_data(self):
                                    return (
                                        self.vrf_name.is_set or
                                        (self.helper_addresses is not None and self.helper_addresses.has_data()))

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set or
                                        (self.helper_addresses is not None and self.helper_addresses.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "vrf" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    if (child_yang_name == "helper-addresses"):
                                        if (self.helper_addresses is None):
                                            self.helper_addresses = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf.HelperAddresses()
                                            self.helper_addresses.parent = self
                                            self._children_name_map["helper_addresses"] = "helper-addresses"
                                        return self.helper_addresses

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "helper-addresses" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.vrf:
                                    if (c.has_data()):
                                        return True
                                return False

                            def has_operation(self):
                                for c in self.vrf:
                                    if (c.has_operation()):
                                        return True
                                return self.yfilter != YFilter.not_set

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "vrfs" + path_buffer

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

                                if (child_yang_name == "vrf"):
                                    for c in self.vrf:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs.Vrf()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.vrf.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "vrf"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


                        class Sessions(Entity):
                            """
                            Change sessions configuration
                            
                            .. attribute:: proxy_throttle_type
                            
                            	Throttle DHCP sessions based on MAC address
                            	**type**\:   :py:class:`ProxyThrottleType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions, self).__init__()

                                self.yang_name = "sessions"
                                self.yang_parent_name = "proxy"

                                self.proxy_throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType()
                                self.proxy_throttle_type.parent = self
                                self._children_name_map["proxy_throttle_type"] = "proxy-throttle-type"
                                self._children_yang_names.add("proxy-throttle-type")


                            class ProxyThrottleType(Entity):
                                """
                                Throttle DHCP sessions based on MAC
                                address
                                
                                .. attribute:: proxy_mac_throttle
                                
                                	Throttle DHCP sessions from any one MAC address
                                	**type**\:   :py:class:`ProxyMacThrottle <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType, self).__init__()

                                    self.yang_name = "proxy-throttle-type"
                                    self.yang_parent_name = "sessions"

                                    self.proxy_mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle()
                                    self.proxy_mac_throttle.parent = self
                                    self._children_name_map["proxy_mac_throttle"] = "proxy-mac-throttle"
                                    self._children_yang_names.add("proxy-mac-throttle")


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, self).__init__()

                                        self.yang_name = "proxy-mac-throttle"
                                        self.yang_parent_name = "proxy-throttle-type"

                                        self.num_block = YLeaf(YType.uint32, "num-block")

                                        self.num_discover = YLeaf(YType.uint32, "num-discover")

                                        self.num_request = YLeaf(YType.uint32, "num-request")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("num_block",
                                                        "num_discover",
                                                        "num_request") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.num_block.is_set or
                                            self.num_discover.is_set or
                                            self.num_request.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.num_block.yfilter != YFilter.not_set or
                                            self.num_discover.yfilter != YFilter.not_set or
                                            self.num_request.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "proxy-mac-throttle" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.num_block.is_set or self.num_block.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_block.get_name_leafdata())
                                        if (self.num_discover.is_set or self.num_discover.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_discover.get_name_leafdata())
                                        if (self.num_request.is_set or self.num_request.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.num_request.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "num-block" or name == "num-discover" or name == "num-request"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "num-block"):
                                            self.num_block = value
                                            self.num_block.value_namespace = name_space
                                            self.num_block.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-discover"):
                                            self.num_discover = value
                                            self.num_discover.value_namespace = name_space
                                            self.num_discover.value_namespace_prefix = name_space_prefix
                                        if(value_path == "num-request"):
                                            self.num_request = value
                                            self.num_request.value_namespace = name_space
                                            self.num_request.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    return (self.proxy_mac_throttle is not None and self.proxy_mac_throttle.has_data())

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        (self.proxy_mac_throttle is not None and self.proxy_mac_throttle.has_operation()))

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "proxy-throttle-type" + path_buffer

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

                                    if (child_yang_name == "proxy-mac-throttle"):
                                        if (self.proxy_mac_throttle is None):
                                            self.proxy_mac_throttle = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType.ProxyMacThrottle()
                                            self.proxy_mac_throttle.parent = self
                                            self._children_name_map["proxy_mac_throttle"] = "proxy-mac-throttle"
                                        return self.proxy_mac_throttle

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "proxy-mac-throttle"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (self.proxy_throttle_type is not None and self.proxy_throttle_type.has_data())

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.proxy_throttle_type is not None and self.proxy_throttle_type.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "sessions" + path_buffer

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

                                if (child_yang_name == "proxy-throttle-type"):
                                    if (self.proxy_throttle_type is None):
                                        self.proxy_throttle_type = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions.ProxyThrottleType()
                                        self.proxy_throttle_type.parent = self
                                        self._children_name_map["proxy_throttle_type"] = "proxy-throttle-type"
                                    return self.proxy_throttle_type

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "proxy-throttle-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, self).__init__()

                                self.yang_name = "limit-lease"
                                self.yang_parent_name = "proxy"
                                self.is_presence_container = True

                                self.limit_lease_count = YLeaf(YType.uint32, "limit-lease-count")

                                self.limit_type = YLeaf(YType.enumeration, "limit-type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("limit_lease_count",
                                                "limit_type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.limit_lease_count.is_set or
                                    self.limit_type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.limit_lease_count.yfilter != YFilter.not_set or
                                    self.limit_type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "limit-lease" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.limit_lease_count.is_set or self.limit_lease_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit_lease_count.get_name_leafdata())
                                if (self.limit_type.is_set or self.limit_type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.limit_type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "limit-lease-count" or name == "limit-type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "limit-lease-count"):
                                    self.limit_lease_count = value
                                    self.limit_lease_count.value_namespace = name_space
                                    self.limit_lease_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "limit-type"):
                                    self.limit_type = value
                                    self.limit_type.value_namespace = name_space
                                    self.limit_type.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, self).__init__()

                                self.yang_name = "lease-proxy"
                                self.yang_parent_name = "proxy"

                                self.client_lease_time = YLeaf(YType.uint32, "client-lease-time")

                                self.set_server_options = YLeaf(YType.empty, "set-server-options")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("client_lease_time",
                                                "set_server_options") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.client_lease_time.is_set or
                                    self.set_server_options.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.client_lease_time.yfilter != YFilter.not_set or
                                    self.set_server_options.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "lease-proxy" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.client_lease_time.is_set or self.client_lease_time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.client_lease_time.get_name_leafdata())
                                if (self.set_server_options.is_set or self.set_server_options.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.set_server_options.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "client-lease-time" or name == "set-server-options"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "client-lease-time"):
                                    self.client_lease_time = value
                                    self.client_lease_time.value_namespace = name_space
                                    self.client_lease_time.value_namespace_prefix = name_space_prefix
                                if(value_path == "set-server-options"):
                                    self.set_server_options = value
                                    self.set_server_options.value_namespace = name_space
                                    self.set_server_options.value_namespace_prefix = name_space_prefix


                        class BroadcastFlag(Entity):
                            """
                            Specify broadcast flag
                            
                            .. attribute:: policy
                            
                            	Broadcast flag policy
                            	**type**\:   :py:class:`Ipv4DhcpdBroadcastFlagPolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdBroadcastFlagPolicy>`
                            
                            

                            """

                            _prefix = 'ipv4-dhcpd-cfg'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, self).__init__()

                                self.yang_name = "broadcast-flag"
                                self.yang_parent_name = "proxy"

                                self.policy = YLeaf(YType.enumeration, "policy")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("policy") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag, self).__setattr__(name, value)

                            def has_data(self):
                                return self.policy.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.policy.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "broadcast-flag" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.policy.is_set or self.policy.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.policy.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "policy"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "policy"):
                                    self.policy = value
                                    self.policy.value_namespace = name_space
                                    self.policy.value_namespace_prefix = name_space_prefix


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
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match, self).__init__()

                                self.yang_name = "match"
                                self.yang_parent_name = "proxy"

                                self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions()
                                self.def_options.parent = self
                                self._children_name_map["def_options"] = "def-options"
                                self._children_yang_names.add("def-options")

                                self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters()
                                self.option_filters.parent = self
                                self._children_name_map["option_filters"] = "option-filters"
                                self._children_yang_names.add("option-filters")


                            class DefOptions(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: def_option
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`DefOption <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, self).__init__()

                                    self.yang_name = "def-options"
                                    self.yang_parent_name = "match"

                                    self.def_option = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, self).__init__()

                                        self.yang_name = "def-option"
                                        self.yang_parent_name = "def-options"

                                        self.def_matchoption = YLeaf(YType.int32, "def-matchoption")

                                        self.def_matchaction = YLeaf(YType.enumeration, "def-matchaction")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("def_matchoption",
                                                        "def_matchaction") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.def_matchoption.is_set or
                                            self.def_matchaction.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.def_matchoption.yfilter != YFilter.not_set or
                                            self.def_matchaction.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "def-option" + "[def-matchoption='" + self.def_matchoption.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.def_matchoption.is_set or self.def_matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.def_matchoption.get_name_leafdata())
                                        if (self.def_matchaction.is_set or self.def_matchaction.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.def_matchaction.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "def-matchoption" or name == "def-matchaction"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "def-matchoption"):
                                            self.def_matchoption = value
                                            self.def_matchoption.value_namespace = name_space
                                            self.def_matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "def-matchaction"):
                                            self.def_matchaction = value
                                            self.def_matchaction.value_namespace = name_space
                                            self.def_matchaction.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.def_option:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.def_option:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "def-options" + path_buffer

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

                                    if (child_yang_name == "def-option"):
                                        for c in self.def_option:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions.DefOption()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.def_option.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "def-option"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass


                            class OptionFilters(Entity):
                                """
                                Table of Option
                                
                                .. attribute:: option_filter
                                
                                	Specify match option
                                	**type**\: list of    :py:class:`OptionFilter <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter>`
                                
                                

                                """

                                _prefix = 'ipv4-dhcpd-cfg'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, self).__init__()

                                    self.yang_name = "option-filters"
                                    self.yang_parent_name = "match"

                                    self.option_filter = YList(self)

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
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters, self).__setattr__(name, value)


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
                                    _revision = '2015-11-09'

                                    def __init__(self):
                                        super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, self).__init__()

                                        self.yang_name = "option-filter"
                                        self.yang_parent_name = "option-filters"

                                        self.matchoption = YLeaf(YType.int32, "matchoption")

                                        self.pattern = YLeaf(YType.str, "pattern")

                                        self.format = YLeaf(YType.int32, "format")

                                        self.matchaction = YLeaf(YType.enumeration, "matchaction")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("matchoption",
                                                        "pattern",
                                                        "format",
                                                        "matchaction") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter, self).__setattr__(name, value)

                                    def has_data(self):
                                        return (
                                            self.matchoption.is_set or
                                            self.pattern.is_set or
                                            self.format.is_set or
                                            self.matchaction.is_set)

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.matchoption.yfilter != YFilter.not_set or
                                            self.pattern.yfilter != YFilter.not_set or
                                            self.format.yfilter != YFilter.not_set or
                                            self.matchaction.yfilter != YFilter.not_set)

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "option-filter" + "[matchoption='" + self.matchoption.get() + "']" + "[pattern='" + self.pattern.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.matchoption.is_set or self.matchoption.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchoption.get_name_leafdata())
                                        if (self.pattern.is_set or self.pattern.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.pattern.get_name_leafdata())
                                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.format.get_name_leafdata())
                                        if (self.matchaction.is_set or self.matchaction.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.matchaction.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "matchoption" or name == "pattern" or name == "format" or name == "matchaction"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "matchoption"):
                                            self.matchoption = value
                                            self.matchoption.value_namespace = name_space
                                            self.matchoption.value_namespace_prefix = name_space_prefix
                                        if(value_path == "pattern"):
                                            self.pattern = value
                                            self.pattern.value_namespace = name_space
                                            self.pattern.value_namespace_prefix = name_space_prefix
                                        if(value_path == "format"):
                                            self.format = value
                                            self.format.value_namespace = name_space
                                            self.format.value_namespace_prefix = name_space_prefix
                                        if(value_path == "matchaction"):
                                            self.matchaction = value
                                            self.matchaction.value_namespace = name_space
                                            self.matchaction.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.option_filter:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.option_filter:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "option-filters" + path_buffer

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

                                    if (child_yang_name == "option-filter"):
                                        for c in self.option_filter:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters.OptionFilter()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.option_filter.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "option-filter"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    (self.def_options is not None and self.def_options.has_data()) or
                                    (self.option_filters is not None and self.option_filters.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    (self.def_options is not None and self.def_options.has_operation()) or
                                    (self.option_filters is not None and self.option_filters.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "match" + path_buffer

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

                                if (child_yang_name == "def-options"):
                                    if (self.def_options is None):
                                        self.def_options = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.DefOptions()
                                        self.def_options.parent = self
                                        self._children_name_map["def_options"] = "def-options"
                                    return self.def_options

                                if (child_yang_name == "option-filters"):
                                    if (self.option_filters is None):
                                        self.option_filters = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match.OptionFilters()
                                        self.option_filters.parent = self
                                        self._children_name_map["option_filters"] = "option-filters"
                                    return self.option_filters

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "def-options" or name == "option-filters"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                pass

                        def has_data(self):
                            return (
                                self.enable.is_set or
                                self.proxy_allow_move.is_set or
                                self.secure_arp.is_set or
                                (self.broadcast_flag is not None and self.broadcast_flag.has_data()) or
                                (self.classes is not None and self.classes.has_data()) or
                                (self.lease_proxy is not None and self.lease_proxy.has_data()) or
                                (self.match is not None and self.match.has_data()) or
                                (self.relay_information is not None and self.relay_information.has_data()) or
                                (self.sessions is not None and self.sessions.has_data()) or
                                (self.vrfs is not None and self.vrfs.has_data()) or
                                (self.limit_lease is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                self.proxy_allow_move.yfilter != YFilter.not_set or
                                self.secure_arp.yfilter != YFilter.not_set or
                                (self.broadcast_flag is not None and self.broadcast_flag.has_operation()) or
                                (self.classes is not None and self.classes.has_operation()) or
                                (self.lease_proxy is not None and self.lease_proxy.has_operation()) or
                                (self.limit_lease is not None and self.limit_lease.has_operation()) or
                                (self.match is not None and self.match.has_operation()) or
                                (self.relay_information is not None and self.relay_information.has_operation()) or
                                (self.sessions is not None and self.sessions.has_operation()) or
                                (self.vrfs is not None and self.vrfs.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "proxy" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.enable.get_name_leafdata())
                            if (self.proxy_allow_move.is_set or self.proxy_allow_move.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.proxy_allow_move.get_name_leafdata())
                            if (self.secure_arp.is_set or self.secure_arp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.secure_arp.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "broadcast-flag"):
                                if (self.broadcast_flag is None):
                                    self.broadcast_flag = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.BroadcastFlag()
                                    self.broadcast_flag.parent = self
                                    self._children_name_map["broadcast_flag"] = "broadcast-flag"
                                return self.broadcast_flag

                            if (child_yang_name == "classes"):
                                if (self.classes is None):
                                    self.classes = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Classes()
                                    self.classes.parent = self
                                    self._children_name_map["classes"] = "classes"
                                return self.classes

                            if (child_yang_name == "lease-proxy"):
                                if (self.lease_proxy is None):
                                    self.lease_proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LeaseProxy()
                                    self.lease_proxy.parent = self
                                    self._children_name_map["lease_proxy"] = "lease-proxy"
                                return self.lease_proxy

                            if (child_yang_name == "limit-lease"):
                                if (self.limit_lease is None):
                                    self.limit_lease = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.LimitLease()
                                    self.limit_lease.parent = self
                                    self._children_name_map["limit_lease"] = "limit-lease"
                                return self.limit_lease

                            if (child_yang_name == "match"):
                                if (self.match is None):
                                    self.match = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Match()
                                    self.match.parent = self
                                    self._children_name_map["match"] = "match"
                                return self.match

                            if (child_yang_name == "relay-information"):
                                if (self.relay_information is None):
                                    self.relay_information = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.RelayInformation()
                                    self.relay_information.parent = self
                                    self._children_name_map["relay_information"] = "relay-information"
                                return self.relay_information

                            if (child_yang_name == "sessions"):
                                if (self.sessions is None):
                                    self.sessions = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Sessions()
                                    self.sessions.parent = self
                                    self._children_name_map["sessions"] = "sessions"
                                return self.sessions

                            if (child_yang_name == "vrfs"):
                                if (self.vrfs is None):
                                    self.vrfs = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy.Vrfs()
                                    self.vrfs.parent = self
                                    self._children_name_map["vrfs"] = "vrfs"
                                return self.vrfs

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "broadcast-flag" or name == "classes" or name == "lease-proxy" or name == "limit-lease" or name == "match" or name == "relay-information" or name == "sessions" or name == "vrfs" or name == "enable" or name == "proxy-allow-move" or name == "secure-arp"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "proxy-allow-move"):
                                self.proxy_allow_move = value
                                self.proxy_allow_move.value_namespace = name_space
                                self.proxy_allow_move.value_namespace_prefix = name_space_prefix
                            if(value_path == "secure-arp"):
                                self.secure_arp = value
                                self.secure_arp.value_namespace = name_space
                                self.secure_arp.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.mode.is_set or
                            self.enable.is_set or
                            (self.base is not None and self.base.has_data()) or
                            (self.proxy is not None and self.proxy.has_data()) or
                            (self.relay is not None and self.relay.has_data()) or
                            (self.server is not None and self.server.has_data()) or
                            (self.snoop is not None and self.snoop.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.mode.yfilter != YFilter.not_set or
                            self.enable.yfilter != YFilter.not_set or
                            (self.base is not None and self.base.has_operation()) or
                            (self.proxy is not None and self.proxy.has_operation()) or
                            (self.relay is not None and self.relay.has_operation()) or
                            (self.server is not None and self.server.has_operation()) or
                            (self.snoop is not None and self.snoop.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "mode" + "[mode='" + self.mode.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mode.get_name_leafdata())
                        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.enable.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "base"):
                            if (self.base is None):
                                self.base = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Base()
                                self.base.parent = self
                                self._children_name_map["base"] = "base"
                            return self.base

                        if (child_yang_name == "proxy"):
                            if (self.proxy is None):
                                self.proxy = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Proxy()
                                self.proxy.parent = self
                                self._children_name_map["proxy"] = "proxy"
                            return self.proxy

                        if (child_yang_name == "relay"):
                            if (self.relay is None):
                                self.relay = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Relay()
                                self.relay.parent = self
                                self._children_name_map["relay"] = "relay"
                            return self.relay

                        if (child_yang_name == "server"):
                            if (self.server is None):
                                self.server = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Server()
                                self.server.parent = self
                                self._children_name_map["server"] = "server"
                            return self.server

                        if (child_yang_name == "snoop"):
                            if (self.snoop is None):
                                self.snoop = Ipv4Dhcpd.Profiles.Profile.Modes.Mode.Snoop()
                                self.snoop.parent = self
                                self._children_name_map["snoop"] = "snoop"
                            return self.snoop

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "base" or name == "proxy" or name == "relay" or name == "server" or name == "snoop" or name == "mode" or name == "enable"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "mode"):
                            self.mode = value
                            self.mode.value_namespace = name_space
                            self.mode.value_namespace_prefix = name_space_prefix
                        if(value_path == "enable"):
                            self.enable = value
                            self.enable.value_namespace = name_space
                            self.enable.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.mode:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.mode:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "modes" + path_buffer

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

                    if (child_yang_name == "mode"):
                        for c in self.mode:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = Ipv4Dhcpd.Profiles.Profile.Modes.Mode()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.mode.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mode"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.profile_name.is_set or
                    (self.modes is not None and self.modes.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.profile_name.yfilter != YFilter.not_set or
                    (self.modes is not None and self.modes.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "profile" + "[profile-name='" + self.profile_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/profiles/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.profile_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "modes"):
                    if (self.modes is None):
                        self.modes = Ipv4Dhcpd.Profiles.Profile.Modes()
                        self.modes.parent = self
                        self._children_name_map["modes"] = "modes"
                    return self.modes

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "modes" or name == "profile-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "profile-name"):
                    self.profile_name = value
                    self.profile_name.value_namespace = name_space
                    self.profile_name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.profile:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.profile:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "profiles" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "profile"):
                for c in self.profile:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = Ipv4Dhcpd.Profiles.Profile()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.profile.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "profile"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Database, self).__init__()

            self.yang_name = "database"
            self.yang_parent_name = "ipv4-dhcpd"

            self.full_write_interval = YLeaf(YType.uint32, "full-write-interval")

            self.incremental_write_interval = YLeaf(YType.uint32, "incremental-write-interval")

            self.proxy = YLeaf(YType.empty, "proxy")

            self.server = YLeaf(YType.empty, "server")

            self.snoop = YLeaf(YType.empty, "snoop")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("full_write_interval",
                            "incremental_write_interval",
                            "proxy",
                            "server",
                            "snoop") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Dhcpd.Database, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.Database, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.full_write_interval.is_set or
                self.incremental_write_interval.is_set or
                self.proxy.is_set or
                self.server.is_set or
                self.snoop.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.full_write_interval.yfilter != YFilter.not_set or
                self.incremental_write_interval.yfilter != YFilter.not_set or
                self.proxy.yfilter != YFilter.not_set or
                self.server.yfilter != YFilter.not_set or
                self.snoop.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "database" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.full_write_interval.is_set or self.full_write_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.full_write_interval.get_name_leafdata())
            if (self.incremental_write_interval.is_set or self.incremental_write_interval.yfilter != YFilter.not_set):
                leaf_name_data.append(self.incremental_write_interval.get_name_leafdata())
            if (self.proxy.is_set or self.proxy.yfilter != YFilter.not_set):
                leaf_name_data.append(self.proxy.get_name_leafdata())
            if (self.server.is_set or self.server.yfilter != YFilter.not_set):
                leaf_name_data.append(self.server.get_name_leafdata())
            if (self.snoop.is_set or self.snoop.yfilter != YFilter.not_set):
                leaf_name_data.append(self.snoop.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "full-write-interval" or name == "incremental-write-interval" or name == "proxy" or name == "server" or name == "snoop"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "full-write-interval"):
                self.full_write_interval = value
                self.full_write_interval.value_namespace = name_space
                self.full_write_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "incremental-write-interval"):
                self.incremental_write_interval = value
                self.incremental_write_interval.value_namespace = name_space
                self.incremental_write_interval.value_namespace_prefix = name_space_prefix
            if(value_path == "proxy"):
                self.proxy = value
                self.proxy.value_namespace = name_space
                self.proxy.value_namespace_prefix = name_space_prefix
            if(value_path == "server"):
                self.server = value
                self.server.value_namespace = name_space
                self.server.value_namespace_prefix = name_space_prefix
            if(value_path == "snoop"):
                self.snoop = value
                self.snoop.value_namespace = name_space
                self.snoop.value_namespace_prefix = name_space_prefix


    class Interfaces(Entity):
        """
        DHCP IPV4 Interface Table
        
        .. attribute:: interface
        
        	DHCP IPV4 Interface
        	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface>`
        
        

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.Interfaces, self).__init__()

            self.yang_name = "interfaces"
            self.yang_parent_name = "ipv4-dhcpd"

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
                        super(Ipv4Dhcpd.Interfaces, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.Interfaces, self).__setattr__(name, value)


        class Interface(Entity):
            """
            DHCP IPV4 Interface
            
            .. attribute:: interface_name  <key>
            
            	Interface Name
            	**type**\:  str
            
            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
            
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
            _revision = '2015-11-09'

            def __init__(self):
                super(Ipv4Dhcpd.Interfaces.Interface, self).__init__()

                self.yang_name = "interface"
                self.yang_parent_name = "interfaces"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface_name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(Ipv4Dhcpd.Interfaces.Interface, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(Ipv4Dhcpd.Interfaces.Interface, self).__setattr__(name, value)


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, self).__init__()

                    self.yang_name = "proxy-interface"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                    self.dhcp_circuit_id = None
                    self._children_name_map["dhcp_circuit_id"] = "dhcp-circuit-id"
                    self._children_yang_names.add("dhcp-circuit-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface, self).__setattr__(name, value)


                class DhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, self).__init__()

                        self.yang_name = "dhcp-circuit-id"
                        self.yang_parent_name = "proxy-interface"
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("argument1",
                                        "argument10",
                                        "argument11",
                                        "argument12",
                                        "argument13",
                                        "argument14",
                                        "argument15",
                                        "argument16",
                                        "argument2",
                                        "argument3",
                                        "argument4",
                                        "argument5",
                                        "argument6",
                                        "argument7",
                                        "argument8",
                                        "argument9",
                                        "circuit_id",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.argument1.is_set or
                            self.argument10.is_set or
                            self.argument11.is_set or
                            self.argument12.is_set or
                            self.argument13.is_set or
                            self.argument14.is_set or
                            self.argument15.is_set or
                            self.argument16.is_set or
                            self.argument2.is_set or
                            self.argument3.is_set or
                            self.argument4.is_set or
                            self.argument5.is_set or
                            self.argument6.is_set or
                            self.argument7.is_set or
                            self.argument8.is_set or
                            self.argument9.is_set or
                            self.circuit_id.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.argument1.yfilter != YFilter.not_set or
                            self.argument10.yfilter != YFilter.not_set or
                            self.argument11.yfilter != YFilter.not_set or
                            self.argument12.yfilter != YFilter.not_set or
                            self.argument13.yfilter != YFilter.not_set or
                            self.argument14.yfilter != YFilter.not_set or
                            self.argument15.yfilter != YFilter.not_set or
                            self.argument16.yfilter != YFilter.not_set or
                            self.argument2.yfilter != YFilter.not_set or
                            self.argument3.yfilter != YFilter.not_set or
                            self.argument4.yfilter != YFilter.not_set or
                            self.argument5.yfilter != YFilter.not_set or
                            self.argument6.yfilter != YFilter.not_set or
                            self.argument7.yfilter != YFilter.not_set or
                            self.argument8.yfilter != YFilter.not_set or
                            self.argument9.yfilter != YFilter.not_set or
                            self.circuit_id.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "dhcp-circuit-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.argument1.is_set or self.argument1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument1.get_name_leafdata())
                        if (self.argument10.is_set or self.argument10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument10.get_name_leafdata())
                        if (self.argument11.is_set or self.argument11.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument11.get_name_leafdata())
                        if (self.argument12.is_set or self.argument12.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument12.get_name_leafdata())
                        if (self.argument13.is_set or self.argument13.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument13.get_name_leafdata())
                        if (self.argument14.is_set or self.argument14.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument14.get_name_leafdata())
                        if (self.argument15.is_set or self.argument15.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument15.get_name_leafdata())
                        if (self.argument16.is_set or self.argument16.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument16.get_name_leafdata())
                        if (self.argument2.is_set or self.argument2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument2.get_name_leafdata())
                        if (self.argument3.is_set or self.argument3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument3.get_name_leafdata())
                        if (self.argument4.is_set or self.argument4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument4.get_name_leafdata())
                        if (self.argument5.is_set or self.argument5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument5.get_name_leafdata())
                        if (self.argument6.is_set or self.argument6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument6.get_name_leafdata())
                        if (self.argument7.is_set or self.argument7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument7.get_name_leafdata())
                        if (self.argument8.is_set or self.argument8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument8.get_name_leafdata())
                        if (self.argument9.is_set or self.argument9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument9.get_name_leafdata())
                        if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.circuit_id.get_name_leafdata())
                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "argument1" or name == "argument10" or name == "argument11" or name == "argument12" or name == "argument13" or name == "argument14" or name == "argument15" or name == "argument16" or name == "argument2" or name == "argument3" or name == "argument4" or name == "argument5" or name == "argument6" or name == "argument7" or name == "argument8" or name == "argument9" or name == "circuit-id" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "argument1"):
                            self.argument1 = value
                            self.argument1.value_namespace = name_space
                            self.argument1.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument10"):
                            self.argument10 = value
                            self.argument10.value_namespace = name_space
                            self.argument10.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument11"):
                            self.argument11 = value
                            self.argument11.value_namespace = name_space
                            self.argument11.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument12"):
                            self.argument12 = value
                            self.argument12.value_namespace = name_space
                            self.argument12.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument13"):
                            self.argument13 = value
                            self.argument13.value_namespace = name_space
                            self.argument13.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument14"):
                            self.argument14 = value
                            self.argument14.value_namespace = name_space
                            self.argument14.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument15"):
                            self.argument15 = value
                            self.argument15.value_namespace = name_space
                            self.argument15.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument16"):
                            self.argument16 = value
                            self.argument16.value_namespace = name_space
                            self.argument16.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument2"):
                            self.argument2 = value
                            self.argument2.value_namespace = name_space
                            self.argument2.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument3"):
                            self.argument3 = value
                            self.argument3.value_namespace = name_space
                            self.argument3.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument4"):
                            self.argument4 = value
                            self.argument4.value_namespace = name_space
                            self.argument4.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument5"):
                            self.argument5 = value
                            self.argument5.value_namespace = name_space
                            self.argument5.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument6"):
                            self.argument6 = value
                            self.argument6.value_namespace = name_space
                            self.argument6.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument7"):
                            self.argument7 = value
                            self.argument7.value_namespace = name_space
                            self.argument7.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument8"):
                            self.argument8 = value
                            self.argument8.value_namespace = name_space
                            self.argument8.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument9"):
                            self.argument9 = value
                            self.argument9.value_namespace = name_space
                            self.argument9.value_namespace_prefix = name_space_prefix
                        if(value_path == "circuit-id"):
                            self.circuit_id = value
                            self.circuit_id.value_namespace = name_space
                            self.circuit_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.profile.is_set or
                        (self.dhcp_circuit_id is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set or
                        (self.dhcp_circuit_id is not None and self.dhcp_circuit_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "proxy-interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "dhcp-circuit-id"):
                        if (self.dhcp_circuit_id is None):
                            self.dhcp_circuit_id = Ipv4Dhcpd.Interfaces.Interface.ProxyInterface.DhcpCircuitId()
                            self.dhcp_circuit_id.parent = self
                            self._children_name_map["dhcp_circuit_id"] = "dhcp-circuit-id"
                        return self.dhcp_circuit_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "dhcp-circuit-id" or name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, self).__init__()

                    self.yang_name = "base-interface"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                    self.base_dhcp_circuit_id = None
                    self._children_name_map["base_dhcp_circuit_id"] = "base-dhcp-circuit-id"
                    self._children_yang_names.add("base-dhcp-circuit-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface, self).__setattr__(name, value)


                class BaseDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, self).__init__()

                        self.yang_name = "base-dhcp-circuit-id"
                        self.yang_parent_name = "base-interface"
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("argument1",
                                        "argument10",
                                        "argument11",
                                        "argument12",
                                        "argument13",
                                        "argument14",
                                        "argument15",
                                        "argument16",
                                        "argument2",
                                        "argument3",
                                        "argument4",
                                        "argument5",
                                        "argument6",
                                        "argument7",
                                        "argument8",
                                        "argument9",
                                        "circuit_id",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.argument1.is_set or
                            self.argument10.is_set or
                            self.argument11.is_set or
                            self.argument12.is_set or
                            self.argument13.is_set or
                            self.argument14.is_set or
                            self.argument15.is_set or
                            self.argument16.is_set or
                            self.argument2.is_set or
                            self.argument3.is_set or
                            self.argument4.is_set or
                            self.argument5.is_set or
                            self.argument6.is_set or
                            self.argument7.is_set or
                            self.argument8.is_set or
                            self.argument9.is_set or
                            self.circuit_id.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.argument1.yfilter != YFilter.not_set or
                            self.argument10.yfilter != YFilter.not_set or
                            self.argument11.yfilter != YFilter.not_set or
                            self.argument12.yfilter != YFilter.not_set or
                            self.argument13.yfilter != YFilter.not_set or
                            self.argument14.yfilter != YFilter.not_set or
                            self.argument15.yfilter != YFilter.not_set or
                            self.argument16.yfilter != YFilter.not_set or
                            self.argument2.yfilter != YFilter.not_set or
                            self.argument3.yfilter != YFilter.not_set or
                            self.argument4.yfilter != YFilter.not_set or
                            self.argument5.yfilter != YFilter.not_set or
                            self.argument6.yfilter != YFilter.not_set or
                            self.argument7.yfilter != YFilter.not_set or
                            self.argument8.yfilter != YFilter.not_set or
                            self.argument9.yfilter != YFilter.not_set or
                            self.circuit_id.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "base-dhcp-circuit-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.argument1.is_set or self.argument1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument1.get_name_leafdata())
                        if (self.argument10.is_set or self.argument10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument10.get_name_leafdata())
                        if (self.argument11.is_set or self.argument11.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument11.get_name_leafdata())
                        if (self.argument12.is_set or self.argument12.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument12.get_name_leafdata())
                        if (self.argument13.is_set or self.argument13.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument13.get_name_leafdata())
                        if (self.argument14.is_set or self.argument14.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument14.get_name_leafdata())
                        if (self.argument15.is_set or self.argument15.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument15.get_name_leafdata())
                        if (self.argument16.is_set or self.argument16.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument16.get_name_leafdata())
                        if (self.argument2.is_set or self.argument2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument2.get_name_leafdata())
                        if (self.argument3.is_set or self.argument3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument3.get_name_leafdata())
                        if (self.argument4.is_set or self.argument4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument4.get_name_leafdata())
                        if (self.argument5.is_set or self.argument5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument5.get_name_leafdata())
                        if (self.argument6.is_set or self.argument6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument6.get_name_leafdata())
                        if (self.argument7.is_set or self.argument7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument7.get_name_leafdata())
                        if (self.argument8.is_set or self.argument8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument8.get_name_leafdata())
                        if (self.argument9.is_set or self.argument9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument9.get_name_leafdata())
                        if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.circuit_id.get_name_leafdata())
                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "argument1" or name == "argument10" or name == "argument11" or name == "argument12" or name == "argument13" or name == "argument14" or name == "argument15" or name == "argument16" or name == "argument2" or name == "argument3" or name == "argument4" or name == "argument5" or name == "argument6" or name == "argument7" or name == "argument8" or name == "argument9" or name == "circuit-id" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "argument1"):
                            self.argument1 = value
                            self.argument1.value_namespace = name_space
                            self.argument1.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument10"):
                            self.argument10 = value
                            self.argument10.value_namespace = name_space
                            self.argument10.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument11"):
                            self.argument11 = value
                            self.argument11.value_namespace = name_space
                            self.argument11.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument12"):
                            self.argument12 = value
                            self.argument12.value_namespace = name_space
                            self.argument12.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument13"):
                            self.argument13 = value
                            self.argument13.value_namespace = name_space
                            self.argument13.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument14"):
                            self.argument14 = value
                            self.argument14.value_namespace = name_space
                            self.argument14.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument15"):
                            self.argument15 = value
                            self.argument15.value_namespace = name_space
                            self.argument15.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument16"):
                            self.argument16 = value
                            self.argument16.value_namespace = name_space
                            self.argument16.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument2"):
                            self.argument2 = value
                            self.argument2.value_namespace = name_space
                            self.argument2.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument3"):
                            self.argument3 = value
                            self.argument3.value_namespace = name_space
                            self.argument3.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument4"):
                            self.argument4 = value
                            self.argument4.value_namespace = name_space
                            self.argument4.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument5"):
                            self.argument5 = value
                            self.argument5.value_namespace = name_space
                            self.argument5.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument6"):
                            self.argument6 = value
                            self.argument6.value_namespace = name_space
                            self.argument6.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument7"):
                            self.argument7 = value
                            self.argument7.value_namespace = name_space
                            self.argument7.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument8"):
                            self.argument8 = value
                            self.argument8.value_namespace = name_space
                            self.argument8.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument9"):
                            self.argument9 = value
                            self.argument9.value_namespace = name_space
                            self.argument9.value_namespace_prefix = name_space_prefix
                        if(value_path == "circuit-id"):
                            self.circuit_id = value
                            self.circuit_id.value_namespace = name_space
                            self.circuit_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.profile.is_set or
                        (self.base_dhcp_circuit_id is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set or
                        (self.base_dhcp_circuit_id is not None and self.base_dhcp_circuit_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "base-interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "base-dhcp-circuit-id"):
                        if (self.base_dhcp_circuit_id is None):
                            self.base_dhcp_circuit_id = Ipv4Dhcpd.Interfaces.Interface.BaseInterface.BaseDhcpCircuitId()
                            self.base_dhcp_circuit_id.parent = self
                            self._children_name_map["base_dhcp_circuit_id"] = "base-dhcp-circuit-id"
                        return self.base_dhcp_circuit_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "base-dhcp-circuit-id" or name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class RelayInterface(Entity):
                """
                DHCP IPv4 relay information
                
                .. attribute:: relay_dhcp_circuit_id
                
                	Circuit ID value
                	**type**\:   :py:class:`RelayDhcpCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId>`
                
                	**presence node**\: True
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface, self).__init__()

                    self.yang_name = "relay-interface"
                    self.yang_parent_name = "interface"

                    self.relay_dhcp_circuit_id = None
                    self._children_name_map["relay_dhcp_circuit_id"] = "relay-dhcp-circuit-id"
                    self._children_yang_names.add("relay-dhcp-circuit-id")


                class RelayDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, self).__init__()

                        self.yang_name = "relay-dhcp-circuit-id"
                        self.yang_parent_name = "relay-interface"
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("argument1",
                                        "argument10",
                                        "argument11",
                                        "argument12",
                                        "argument13",
                                        "argument14",
                                        "argument15",
                                        "argument16",
                                        "argument2",
                                        "argument3",
                                        "argument4",
                                        "argument5",
                                        "argument6",
                                        "argument7",
                                        "argument8",
                                        "argument9",
                                        "circuit_id",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.argument1.is_set or
                            self.argument10.is_set or
                            self.argument11.is_set or
                            self.argument12.is_set or
                            self.argument13.is_set or
                            self.argument14.is_set or
                            self.argument15.is_set or
                            self.argument16.is_set or
                            self.argument2.is_set or
                            self.argument3.is_set or
                            self.argument4.is_set or
                            self.argument5.is_set or
                            self.argument6.is_set or
                            self.argument7.is_set or
                            self.argument8.is_set or
                            self.argument9.is_set or
                            self.circuit_id.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.argument1.yfilter != YFilter.not_set or
                            self.argument10.yfilter != YFilter.not_set or
                            self.argument11.yfilter != YFilter.not_set or
                            self.argument12.yfilter != YFilter.not_set or
                            self.argument13.yfilter != YFilter.not_set or
                            self.argument14.yfilter != YFilter.not_set or
                            self.argument15.yfilter != YFilter.not_set or
                            self.argument16.yfilter != YFilter.not_set or
                            self.argument2.yfilter != YFilter.not_set or
                            self.argument3.yfilter != YFilter.not_set or
                            self.argument4.yfilter != YFilter.not_set or
                            self.argument5.yfilter != YFilter.not_set or
                            self.argument6.yfilter != YFilter.not_set or
                            self.argument7.yfilter != YFilter.not_set or
                            self.argument8.yfilter != YFilter.not_set or
                            self.argument9.yfilter != YFilter.not_set or
                            self.circuit_id.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "relay-dhcp-circuit-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.argument1.is_set or self.argument1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument1.get_name_leafdata())
                        if (self.argument10.is_set or self.argument10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument10.get_name_leafdata())
                        if (self.argument11.is_set or self.argument11.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument11.get_name_leafdata())
                        if (self.argument12.is_set or self.argument12.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument12.get_name_leafdata())
                        if (self.argument13.is_set or self.argument13.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument13.get_name_leafdata())
                        if (self.argument14.is_set or self.argument14.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument14.get_name_leafdata())
                        if (self.argument15.is_set or self.argument15.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument15.get_name_leafdata())
                        if (self.argument16.is_set or self.argument16.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument16.get_name_leafdata())
                        if (self.argument2.is_set or self.argument2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument2.get_name_leafdata())
                        if (self.argument3.is_set or self.argument3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument3.get_name_leafdata())
                        if (self.argument4.is_set or self.argument4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument4.get_name_leafdata())
                        if (self.argument5.is_set or self.argument5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument5.get_name_leafdata())
                        if (self.argument6.is_set or self.argument6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument6.get_name_leafdata())
                        if (self.argument7.is_set or self.argument7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument7.get_name_leafdata())
                        if (self.argument8.is_set or self.argument8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument8.get_name_leafdata())
                        if (self.argument9.is_set or self.argument9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument9.get_name_leafdata())
                        if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.circuit_id.get_name_leafdata())
                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "argument1" or name == "argument10" or name == "argument11" or name == "argument12" or name == "argument13" or name == "argument14" or name == "argument15" or name == "argument16" or name == "argument2" or name == "argument3" or name == "argument4" or name == "argument5" or name == "argument6" or name == "argument7" or name == "argument8" or name == "argument9" or name == "circuit-id" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "argument1"):
                            self.argument1 = value
                            self.argument1.value_namespace = name_space
                            self.argument1.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument10"):
                            self.argument10 = value
                            self.argument10.value_namespace = name_space
                            self.argument10.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument11"):
                            self.argument11 = value
                            self.argument11.value_namespace = name_space
                            self.argument11.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument12"):
                            self.argument12 = value
                            self.argument12.value_namespace = name_space
                            self.argument12.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument13"):
                            self.argument13 = value
                            self.argument13.value_namespace = name_space
                            self.argument13.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument14"):
                            self.argument14 = value
                            self.argument14.value_namespace = name_space
                            self.argument14.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument15"):
                            self.argument15 = value
                            self.argument15.value_namespace = name_space
                            self.argument15.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument16"):
                            self.argument16 = value
                            self.argument16.value_namespace = name_space
                            self.argument16.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument2"):
                            self.argument2 = value
                            self.argument2.value_namespace = name_space
                            self.argument2.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument3"):
                            self.argument3 = value
                            self.argument3.value_namespace = name_space
                            self.argument3.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument4"):
                            self.argument4 = value
                            self.argument4.value_namespace = name_space
                            self.argument4.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument5"):
                            self.argument5 = value
                            self.argument5.value_namespace = name_space
                            self.argument5.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument6"):
                            self.argument6 = value
                            self.argument6.value_namespace = name_space
                            self.argument6.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument7"):
                            self.argument7 = value
                            self.argument7.value_namespace = name_space
                            self.argument7.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument8"):
                            self.argument8 = value
                            self.argument8.value_namespace = name_space
                            self.argument8.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument9"):
                            self.argument9 = value
                            self.argument9.value_namespace = name_space
                            self.argument9.value_namespace_prefix = name_space_prefix
                        if(value_path == "circuit-id"):
                            self.circuit_id = value
                            self.circuit_id.value_namespace = name_space
                            self.circuit_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.relay_dhcp_circuit_id is not None)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.relay_dhcp_circuit_id is not None and self.relay_dhcp_circuit_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "relay-interface" + path_buffer

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

                    if (child_yang_name == "relay-dhcp-circuit-id"):
                        if (self.relay_dhcp_circuit_id is None):
                            self.relay_dhcp_circuit_id = Ipv4Dhcpd.Interfaces.Interface.RelayInterface.RelayDhcpCircuitId()
                            self.relay_dhcp_circuit_id.parent = self
                            self._children_name_map["relay_dhcp_circuit_id"] = "relay-dhcp-circuit-id"
                        return self.relay_dhcp_circuit_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "relay-dhcp-circuit-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class StaticMode(Entity):
                """
                Static Table Entries containing MAC address to
                IP address bindings
                
                .. attribute:: statics
                
                	Static Table Entries containing MAC address to IP address bindings
                	**type**\:   :py:class:`Statics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.StaticMode, self).__init__()

                    self.yang_name = "static-mode"
                    self.yang_parent_name = "interface"

                    self.statics = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics()
                    self.statics.parent = self
                    self._children_name_map["statics"] = "statics"
                    self._children_yang_names.add("statics")


                class Statics(Entity):
                    """
                    Static Table Entries containing MAC address
                    to IP address bindings
                    
                    .. attribute:: static
                    
                    	DHCP static binding of Mac address to IP address
                    	**type**\: list of    :py:class:`Static <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static>`
                    
                    

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, self).__init__()

                        self.yang_name = "statics"
                        self.yang_parent_name = "static-mode"

                        self.static = YList(self)

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
                                    super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics, self).__setattr__(name, value)


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
                        	**type**\:   :py:class:`Ipv4DhcpdLayer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdLayer>`
                        
                        .. attribute:: static_address
                        
                        	IP address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'ipv4-dhcpd-cfg'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, self).__init__()

                            self.yang_name = "static"
                            self.yang_parent_name = "statics"

                            self.mac_address = YLeaf(YType.str, "mac-address")

                            self.client_id = YLeaf(YType.uint32, "client-id")

                            self.layer = YLeaf(YType.enumeration, "layer")

                            self.static_address = YLeaf(YType.str, "static-address")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("mac_address",
                                            "client_id",
                                            "layer",
                                            "static_address") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.mac_address.is_set or
                                self.client_id.is_set or
                                self.layer.is_set or
                                self.static_address.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.mac_address.yfilter != YFilter.not_set or
                                self.client_id.yfilter != YFilter.not_set or
                                self.layer.yfilter != YFilter.not_set or
                                self.static_address.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "static" + "[mac-address='" + self.mac_address.get() + "']" + "[client-id='" + self.client_id.get() + "']" + "[layer='" + self.layer.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_address.get_name_leafdata())
                            if (self.client_id.is_set or self.client_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.client_id.get_name_leafdata())
                            if (self.layer.is_set or self.layer.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.layer.get_name_leafdata())
                            if (self.static_address.is_set or self.static_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.static_address.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mac-address" or name == "client-id" or name == "layer" or name == "static-address"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "mac-address"):
                                self.mac_address = value
                                self.mac_address.value_namespace = name_space
                                self.mac_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "client-id"):
                                self.client_id = value
                                self.client_id.value_namespace = name_space
                                self.client_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "layer"):
                                self.layer = value
                                self.layer.value_namespace = name_space
                                self.layer.value_namespace_prefix = name_space_prefix
                            if(value_path == "static-address"):
                                self.static_address = value
                                self.static_address.value_namespace = name_space
                                self.static_address.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.static:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.static:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "statics" + path_buffer

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

                        if (child_yang_name == "static"):
                            for c in self.static:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics.Static()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.static.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "static"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (self.statics is not None and self.statics.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.statics is not None and self.statics.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "static-mode" + path_buffer

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

                    if (child_yang_name == "statics"):
                        if (self.statics is None):
                            self.statics = Ipv4Dhcpd.Interfaces.Interface.StaticMode.Statics()
                            self.statics.parent = self
                            self._children_name_map["statics"] = "statics"
                        return self.statics

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "statics"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Profile(Entity):
                """
                Profile name and mode
                
                .. attribute:: mode
                
                	DHCP mode
                	**type**\:   :py:class:`Ipv4DhcpdMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdMode>`
                
                	**mandatory**\: True
                
                .. attribute:: profile_name
                
                	Profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.Profile, self).__init__()

                    self.yang_name = "profile"
                    self.yang_parent_name = "interface"
                    self.is_presence_container = True

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.profile_name = YLeaf(YType.str, "profile-name")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("mode",
                                    "profile_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Dhcpd.Interfaces.Interface.Profile, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Interfaces.Interface.Profile, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.mode.is_set or
                        self.profile_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.profile_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "profile" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.profile_name.is_set or self.profile_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile_name.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "mode" or name == "profile-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "profile-name"):
                        self.profile_name = value
                        self.profile_name.value_namespace = name_space
                        self.profile_name.value_namespace_prefix = name_space_prefix


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
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, self).__init__()

                    self.yang_name = "server-interface"
                    self.yang_parent_name = "interface"

                    self.profile = YLeaf(YType.str, "profile")

                    self.server_dhcp_circuit_id = None
                    self._children_name_map["server_dhcp_circuit_id"] = "server-dhcp-circuit-id"
                    self._children_yang_names.add("server-dhcp-circuit-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("profile") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface, self).__setattr__(name, value)


                class ServerDhcpCircuitId(Entity):
                    """
                    Circuit ID value
                    
                    .. attribute:: argument1
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument10
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument11
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument12
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument13
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument14
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument15
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument16
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument2
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument3
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument4
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument5
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument6
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument7
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument8
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: argument9
                    
                    	Argument
                    	**type**\:   :py:class:`Ipv4DhcpdFmtSpecifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmtSpecifier>`
                    
                    .. attribute:: circuit_id
                    
                    	DHCP IPv4 circuit ID value
                    	**type**\:  str
                    
                    	**mandatory**\: True
                    
                    .. attribute:: format
                    
                    	Format String
                    	**type**\:   :py:class:`Ipv4DhcpdFmt <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4DhcpdFmt>`
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'ipv4-dhcpd-cfg'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, self).__init__()

                        self.yang_name = "server-dhcp-circuit-id"
                        self.yang_parent_name = "server-interface"
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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("argument1",
                                        "argument10",
                                        "argument11",
                                        "argument12",
                                        "argument13",
                                        "argument14",
                                        "argument15",
                                        "argument16",
                                        "argument2",
                                        "argument3",
                                        "argument4",
                                        "argument5",
                                        "argument6",
                                        "argument7",
                                        "argument8",
                                        "argument9",
                                        "circuit_id",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.argument1.is_set or
                            self.argument10.is_set or
                            self.argument11.is_set or
                            self.argument12.is_set or
                            self.argument13.is_set or
                            self.argument14.is_set or
                            self.argument15.is_set or
                            self.argument16.is_set or
                            self.argument2.is_set or
                            self.argument3.is_set or
                            self.argument4.is_set or
                            self.argument5.is_set or
                            self.argument6.is_set or
                            self.argument7.is_set or
                            self.argument8.is_set or
                            self.argument9.is_set or
                            self.circuit_id.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.argument1.yfilter != YFilter.not_set or
                            self.argument10.yfilter != YFilter.not_set or
                            self.argument11.yfilter != YFilter.not_set or
                            self.argument12.yfilter != YFilter.not_set or
                            self.argument13.yfilter != YFilter.not_set or
                            self.argument14.yfilter != YFilter.not_set or
                            self.argument15.yfilter != YFilter.not_set or
                            self.argument16.yfilter != YFilter.not_set or
                            self.argument2.yfilter != YFilter.not_set or
                            self.argument3.yfilter != YFilter.not_set or
                            self.argument4.yfilter != YFilter.not_set or
                            self.argument5.yfilter != YFilter.not_set or
                            self.argument6.yfilter != YFilter.not_set or
                            self.argument7.yfilter != YFilter.not_set or
                            self.argument8.yfilter != YFilter.not_set or
                            self.argument9.yfilter != YFilter.not_set or
                            self.circuit_id.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "server-dhcp-circuit-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.argument1.is_set or self.argument1.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument1.get_name_leafdata())
                        if (self.argument10.is_set or self.argument10.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument10.get_name_leafdata())
                        if (self.argument11.is_set or self.argument11.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument11.get_name_leafdata())
                        if (self.argument12.is_set or self.argument12.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument12.get_name_leafdata())
                        if (self.argument13.is_set or self.argument13.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument13.get_name_leafdata())
                        if (self.argument14.is_set or self.argument14.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument14.get_name_leafdata())
                        if (self.argument15.is_set or self.argument15.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument15.get_name_leafdata())
                        if (self.argument16.is_set or self.argument16.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument16.get_name_leafdata())
                        if (self.argument2.is_set or self.argument2.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument2.get_name_leafdata())
                        if (self.argument3.is_set or self.argument3.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument3.get_name_leafdata())
                        if (self.argument4.is_set or self.argument4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument4.get_name_leafdata())
                        if (self.argument5.is_set or self.argument5.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument5.get_name_leafdata())
                        if (self.argument6.is_set or self.argument6.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument6.get_name_leafdata())
                        if (self.argument7.is_set or self.argument7.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument7.get_name_leafdata())
                        if (self.argument8.is_set or self.argument8.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument8.get_name_leafdata())
                        if (self.argument9.is_set or self.argument9.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.argument9.get_name_leafdata())
                        if (self.circuit_id.is_set or self.circuit_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.circuit_id.get_name_leafdata())
                        if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "argument1" or name == "argument10" or name == "argument11" or name == "argument12" or name == "argument13" or name == "argument14" or name == "argument15" or name == "argument16" or name == "argument2" or name == "argument3" or name == "argument4" or name == "argument5" or name == "argument6" or name == "argument7" or name == "argument8" or name == "argument9" or name == "circuit-id" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "argument1"):
                            self.argument1 = value
                            self.argument1.value_namespace = name_space
                            self.argument1.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument10"):
                            self.argument10 = value
                            self.argument10.value_namespace = name_space
                            self.argument10.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument11"):
                            self.argument11 = value
                            self.argument11.value_namespace = name_space
                            self.argument11.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument12"):
                            self.argument12 = value
                            self.argument12.value_namespace = name_space
                            self.argument12.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument13"):
                            self.argument13 = value
                            self.argument13.value_namespace = name_space
                            self.argument13.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument14"):
                            self.argument14 = value
                            self.argument14.value_namespace = name_space
                            self.argument14.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument15"):
                            self.argument15 = value
                            self.argument15.value_namespace = name_space
                            self.argument15.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument16"):
                            self.argument16 = value
                            self.argument16.value_namespace = name_space
                            self.argument16.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument2"):
                            self.argument2 = value
                            self.argument2.value_namespace = name_space
                            self.argument2.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument3"):
                            self.argument3 = value
                            self.argument3.value_namespace = name_space
                            self.argument3.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument4"):
                            self.argument4 = value
                            self.argument4.value_namespace = name_space
                            self.argument4.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument5"):
                            self.argument5 = value
                            self.argument5.value_namespace = name_space
                            self.argument5.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument6"):
                            self.argument6 = value
                            self.argument6.value_namespace = name_space
                            self.argument6.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument7"):
                            self.argument7 = value
                            self.argument7.value_namespace = name_space
                            self.argument7.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument8"):
                            self.argument8 = value
                            self.argument8.value_namespace = name_space
                            self.argument8.value_namespace_prefix = name_space_prefix
                        if(value_path == "argument9"):
                            self.argument9 = value
                            self.argument9.value_namespace = name_space
                            self.argument9.value_namespace_prefix = name_space_prefix
                        if(value_path == "circuit-id"):
                            self.circuit_id = value
                            self.circuit_id.value_namespace = name_space
                            self.circuit_id.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.profile.is_set or
                        (self.server_dhcp_circuit_id is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile.yfilter != YFilter.not_set or
                        (self.server_dhcp_circuit_id is not None and self.server_dhcp_circuit_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "server-interface" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.profile.is_set or self.profile.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.profile.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "server-dhcp-circuit-id"):
                        if (self.server_dhcp_circuit_id is None):
                            self.server_dhcp_circuit_id = Ipv4Dhcpd.Interfaces.Interface.ServerInterface.ServerDhcpCircuitId()
                            self.server_dhcp_circuit_id.parent = self
                            self._children_name_map["server_dhcp_circuit_id"] = "server-dhcp-circuit-id"
                        return self.server_dhcp_circuit_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "server-dhcp-circuit-id" or name == "profile"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile"):
                        self.profile = value
                        self.profile.value_namespace = name_space
                        self.profile.value_namespace_prefix = name_space_prefix


            class SnoopInterface(Entity):
                """
                DHCP IPv4 snoop information
                
                .. attribute:: snoop_circuit_id
                
                	Configure circuit ID for snoop 1. Hex 2. ASCII
                	**type**\:   :py:class:`SnoopCircuitId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_dhcpd_cfg.Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId>`
                
                

                """

                _prefix = 'ipv4-dhcpd-cfg'
                _revision = '2015-11-09'

                def __init__(self):
                    super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface, self).__init__()

                    self.yang_name = "snoop-interface"
                    self.yang_parent_name = "interface"

                    self.snoop_circuit_id = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId()
                    self.snoop_circuit_id.parent = self
                    self._children_name_map["snoop_circuit_id"] = "snoop-circuit-id"
                    self._children_yang_names.add("snoop-circuit-id")


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
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, self).__init__()

                        self.yang_name = "snoop-circuit-id"
                        self.yang_parent_name = "snoop-interface"

                        self.circuit_id_value = YLeaf(YType.str, "circuit-id-value")

                        self.format_type = YLeaf(YType.uint32, "format-type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("circuit_id_value",
                                        "format_type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.circuit_id_value.is_set or
                            self.format_type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.circuit_id_value.yfilter != YFilter.not_set or
                            self.format_type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "snoop-circuit-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.circuit_id_value.is_set or self.circuit_id_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.circuit_id_value.get_name_leafdata())
                        if (self.format_type.is_set or self.format_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.format_type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "circuit-id-value" or name == "format-type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "circuit-id-value"):
                            self.circuit_id_value = value
                            self.circuit_id_value.value_namespace = name_space
                            self.circuit_id_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "format-type"):
                            self.format_type = value
                            self.format_type.value_namespace = name_space
                            self.format_type.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (self.snoop_circuit_id is not None and self.snoop_circuit_id.has_data())

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.snoop_circuit_id is not None and self.snoop_circuit_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "snoop-interface" + path_buffer

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

                    if (child_yang_name == "snoop-circuit-id"):
                        if (self.snoop_circuit_id is None):
                            self.snoop_circuit_id = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface.SnoopCircuitId()
                            self.snoop_circuit_id.parent = self
                            self._children_name_map["snoop_circuit_id"] = "snoop-circuit-id"
                        return self.snoop_circuit_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "snoop-circuit-id"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.interface_name.is_set or
                    (self.base_interface is not None and self.base_interface.has_data()) or
                    (self.proxy_interface is not None and self.proxy_interface.has_data()) or
                    (self.relay_interface is not None and self.relay_interface.has_data()) or
                    (self.server_interface is not None and self.server_interface.has_data()) or
                    (self.snoop_interface is not None and self.snoop_interface.has_data()) or
                    (self.static_mode is not None and self.static_mode.has_data()) or
                    (self.profile is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface_name.yfilter != YFilter.not_set or
                    (self.base_interface is not None and self.base_interface.has_operation()) or
                    (self.profile is not None and self.profile.has_operation()) or
                    (self.proxy_interface is not None and self.proxy_interface.has_operation()) or
                    (self.relay_interface is not None and self.relay_interface.has_operation()) or
                    (self.server_interface is not None and self.server_interface.has_operation()) or
                    (self.snoop_interface is not None and self.snoop_interface.has_operation()) or
                    (self.static_mode is not None and self.static_mode.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "interface" + "[interface-name='" + self.interface_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/interfaces/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface_name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "base-interface"):
                    if (self.base_interface is None):
                        self.base_interface = Ipv4Dhcpd.Interfaces.Interface.BaseInterface()
                        self.base_interface.parent = self
                        self._children_name_map["base_interface"] = "base-interface"
                    return self.base_interface

                if (child_yang_name == "profile"):
                    if (self.profile is None):
                        self.profile = Ipv4Dhcpd.Interfaces.Interface.Profile()
                        self.profile.parent = self
                        self._children_name_map["profile"] = "profile"
                    return self.profile

                if (child_yang_name == "proxy-interface"):
                    if (self.proxy_interface is None):
                        self.proxy_interface = Ipv4Dhcpd.Interfaces.Interface.ProxyInterface()
                        self.proxy_interface.parent = self
                        self._children_name_map["proxy_interface"] = "proxy-interface"
                    return self.proxy_interface

                if (child_yang_name == "relay-interface"):
                    if (self.relay_interface is None):
                        self.relay_interface = Ipv4Dhcpd.Interfaces.Interface.RelayInterface()
                        self.relay_interface.parent = self
                        self._children_name_map["relay_interface"] = "relay-interface"
                    return self.relay_interface

                if (child_yang_name == "server-interface"):
                    if (self.server_interface is None):
                        self.server_interface = Ipv4Dhcpd.Interfaces.Interface.ServerInterface()
                        self.server_interface.parent = self
                        self._children_name_map["server_interface"] = "server-interface"
                    return self.server_interface

                if (child_yang_name == "snoop-interface"):
                    if (self.snoop_interface is None):
                        self.snoop_interface = Ipv4Dhcpd.Interfaces.Interface.SnoopInterface()
                        self.snoop_interface.parent = self
                        self._children_name_map["snoop_interface"] = "snoop-interface"
                    return self.snoop_interface

                if (child_yang_name == "static-mode"):
                    if (self.static_mode is None):
                        self.static_mode = Ipv4Dhcpd.Interfaces.Interface.StaticMode()
                        self.static_mode.parent = self
                        self._children_name_map["static_mode"] = "static-mode"
                    return self.static_mode

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "base-interface" or name == "profile" or name == "proxy-interface" or name == "relay-interface" or name == "server-interface" or name == "snoop-interface" or name == "static-mode" or name == "interface-name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface-name"):
                    self.interface_name = value
                    self.interface_name.value_namespace = name_space
                    self.interface_name.value_namespace_prefix = name_space_prefix

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
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
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
                c = Ipv4Dhcpd.Interfaces.Interface()
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
        
        

        This class is a :ref:`presence class<presence-class>`

        """

        _prefix = 'ipv4-dhcpd-cfg'
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.DuplicateMacAllowed, self).__init__()

            self.yang_name = "duplicate-mac-allowed"
            self.yang_parent_name = "ipv4-dhcpd"
            self.is_presence_container = True

            self.duplicate_mac = YLeaf(YType.empty, "duplicate-mac")

            self.exclude_vlan = YLeaf(YType.empty, "exclude-vlan")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("duplicate_mac",
                            "exclude_vlan") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Dhcpd.DuplicateMacAllowed, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.DuplicateMacAllowed, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.duplicate_mac.is_set or
                self.exclude_vlan.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.duplicate_mac.yfilter != YFilter.not_set or
                self.exclude_vlan.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "duplicate-mac-allowed" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.duplicate_mac.is_set or self.duplicate_mac.yfilter != YFilter.not_set):
                leaf_name_data.append(self.duplicate_mac.get_name_leafdata())
            if (self.exclude_vlan.is_set or self.exclude_vlan.yfilter != YFilter.not_set):
                leaf_name_data.append(self.exclude_vlan.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "duplicate-mac" or name == "exclude-vlan"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "duplicate-mac"):
                self.duplicate_mac = value
                self.duplicate_mac.value_namespace = name_space
                self.duplicate_mac.value_namespace_prefix = name_space_prefix
            if(value_path == "exclude-vlan"):
                self.exclude_vlan = value
                self.exclude_vlan.value_namespace = name_space
                self.exclude_vlan.value_namespace_prefix = name_space_prefix


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
        _revision = '2015-11-09'

        def __init__(self):
            super(Ipv4Dhcpd.RateLimit, self).__init__()

            self.yang_name = "rate-limit"
            self.yang_parent_name = "ipv4-dhcpd"

            self.num_discover = YLeaf(YType.uint32, "num-discover")

            self.num_period = YLeaf(YType.uint32, "num-period")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("num_discover",
                            "num_period") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(Ipv4Dhcpd.RateLimit, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(Ipv4Dhcpd.RateLimit, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.num_discover.is_set or
                self.num_period.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.num_discover.yfilter != YFilter.not_set or
                self.num_period.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "rate-limit" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.num_discover.is_set or self.num_discover.yfilter != YFilter.not_set):
                leaf_name_data.append(self.num_discover.get_name_leafdata())
            if (self.num_period.is_set or self.num_period.yfilter != YFilter.not_set):
                leaf_name_data.append(self.num_period.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "num-discover" or name == "num-period"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "num-discover"):
                self.num_discover = value
                self.num_discover.value_namespace = name_space
                self.num_discover.value_namespace_prefix = name_space_prefix
            if(value_path == "num-period"):
                self.num_period = value
                self.num_period.value_namespace = name_space
                self.num_period.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            self.allow_client_id_change.is_set or
            self.enable.is_set or
            self.inner_cos.is_set or
            self.outer_cos.is_set or
            (self.database is not None and self.database.has_data()) or
            (self.interfaces is not None and self.interfaces.has_data()) or
            (self.profiles is not None and self.profiles.has_data()) or
            (self.rate_limit is not None and self.rate_limit.has_data()) or
            (self.vrfs is not None and self.vrfs.has_data()) or
            (self.duplicate_mac_allowed is not None))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            self.allow_client_id_change.yfilter != YFilter.not_set or
            self.enable.yfilter != YFilter.not_set or
            self.inner_cos.yfilter != YFilter.not_set or
            self.outer_cos.yfilter != YFilter.not_set or
            (self.database is not None and self.database.has_operation()) or
            (self.duplicate_mac_allowed is not None and self.duplicate_mac_allowed.has_operation()) or
            (self.interfaces is not None and self.interfaces.has_operation()) or
            (self.profiles is not None and self.profiles.has_operation()) or
            (self.rate_limit is not None and self.rate_limit.has_operation()) or
            (self.vrfs is not None and self.vrfs.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-ipv4-dhcpd-cfg:ipv4-dhcpd" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()
        if (self.allow_client_id_change.is_set or self.allow_client_id_change.yfilter != YFilter.not_set):
            leaf_name_data.append(self.allow_client_id_change.get_name_leafdata())
        if (self.enable.is_set or self.enable.yfilter != YFilter.not_set):
            leaf_name_data.append(self.enable.get_name_leafdata())
        if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
            leaf_name_data.append(self.inner_cos.get_name_leafdata())
        if (self.outer_cos.is_set or self.outer_cos.yfilter != YFilter.not_set):
            leaf_name_data.append(self.outer_cos.get_name_leafdata())

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "database"):
            if (self.database is None):
                self.database = Ipv4Dhcpd.Database()
                self.database.parent = self
                self._children_name_map["database"] = "database"
            return self.database

        if (child_yang_name == "duplicate-mac-allowed"):
            if (self.duplicate_mac_allowed is None):
                self.duplicate_mac_allowed = Ipv4Dhcpd.DuplicateMacAllowed()
                self.duplicate_mac_allowed.parent = self
                self._children_name_map["duplicate_mac_allowed"] = "duplicate-mac-allowed"
            return self.duplicate_mac_allowed

        if (child_yang_name == "interfaces"):
            if (self.interfaces is None):
                self.interfaces = Ipv4Dhcpd.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
            return self.interfaces

        if (child_yang_name == "profiles"):
            if (self.profiles is None):
                self.profiles = Ipv4Dhcpd.Profiles()
                self.profiles.parent = self
                self._children_name_map["profiles"] = "profiles"
            return self.profiles

        if (child_yang_name == "rate-limit"):
            if (self.rate_limit is None):
                self.rate_limit = Ipv4Dhcpd.RateLimit()
                self.rate_limit.parent = self
                self._children_name_map["rate_limit"] = "rate-limit"
            return self.rate_limit

        if (child_yang_name == "vrfs"):
            if (self.vrfs is None):
                self.vrfs = Ipv4Dhcpd.Vrfs()
                self.vrfs.parent = self
                self._children_name_map["vrfs"] = "vrfs"
            return self.vrfs

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "database" or name == "duplicate-mac-allowed" or name == "interfaces" or name == "profiles" or name == "rate-limit" or name == "vrfs" or name == "allow-client-id-change" or name == "enable" or name == "inner-cos" or name == "outer-cos"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        if(value_path == "allow-client-id-change"):
            self.allow_client_id_change = value
            self.allow_client_id_change.value_namespace = name_space
            self.allow_client_id_change.value_namespace_prefix = name_space_prefix
        if(value_path == "enable"):
            self.enable = value
            self.enable.value_namespace = name_space
            self.enable.value_namespace_prefix = name_space_prefix
        if(value_path == "inner-cos"):
            self.inner_cos = value
            self.inner_cos.value_namespace = name_space
            self.inner_cos.value_namespace_prefix = name_space_prefix
        if(value_path == "outer-cos"):
            self.outer_cos = value
            self.outer_cos.value_namespace = name_space
            self.outer_cos.value_namespace_prefix = name_space_prefix

    def clone_ptr(self):
        self._top_entity = Ipv4Dhcpd()
        return self._top_entity

