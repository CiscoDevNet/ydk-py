""" cisco_bridge_domain 

This YANG module describes the configuration and operational
model for bridge domain.

Terms and Acronyms
  AC \: Attachment Circuits

  BD \: Bridge Domain

  BCB \: Backbone Core Bridge

  BEB \: Backbone Edge Bridge

  B\-MAC \: Backbone MAC Address

  CE \: Customer Edge

  C\-MAC \: Customer/Client MAC Address

  DHCP \: Dynamic Host Configuration Protocol

  DAI \: Dynamic ARP Inspection

  EVC \: Ethernet Virtual Circuit

  IGMP \: Internet Group Management Protocol

  IPSG \: IP Source Guard

  L2VPN \: Layer 2 Virtual Private Network

  MLD \: Multicast Listener Discovery

  PBB \: Provider Backbone Bridge

  VLAN \: Virtual Local Area Network


"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BridgeDomainStateType(Enum):
    """
    BridgeDomainStateType

    Bridge domain states.

    .. data:: up = 0

    	Bridge domain is operationally Up.

    .. data:: down = 1

    	Bridge domain is operationally Down.

    .. data:: admin_down = 2

    	Bridge domain is shutdown by administrator.

    """

    up = Enum.YLeaf(0, "up")

    down = Enum.YLeaf(1, "down")

    admin_down = Enum.YLeaf(2, "admin-down")



class BridgeDomainConfig(Entity):
    """
    This container defines overall configuration data for bridge
    \-domains on a network device.
    
    .. attribute:: bridge_domains
    
    	Collection of bridge domains
    	**type**\:   :py:class:`BridgeDomains <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains>`
    
    .. attribute:: bridge_groups
    
    	Collection of bridge\-groups.  A Bridge\-group is logical grouping construct for bridge domains. It defines grouping of bridge\-domains under a named bridge\-group. For example all bridge\-domains belonging to a single customer can be grouped under a bridge \-group
    	**type**\:   :py:class:`BridgeGroups <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups>`
    
    .. attribute:: global_
    
    	Global configurations for bridge\-domains
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.Global_>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(BridgeDomainConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "bridge-domain-config"
        self.yang_parent_name = "cisco-bridge-domain"

        self.bridge_domains = BridgeDomainConfig.BridgeDomains()
        self.bridge_domains.parent = self
        self._children_name_map["bridge_domains"] = "bridge-domains"
        self._children_yang_names.add("bridge-domains")

        self.bridge_groups = BridgeDomainConfig.BridgeGroups()
        self.bridge_groups.parent = self
        self._children_name_map["bridge_groups"] = "bridge-groups"
        self._children_yang_names.add("bridge-groups")

        self.global_ = BridgeDomainConfig.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")


    class Global_(Entity):
        """
        Global configurations for bridge\-domains.
        
        .. attribute:: bd_state_notification_enabled
        
        	If this leaf is set to true, then it enables the emission of 'bd\-state\-notification'; otherwise these notifications are not emitted
        	**type**\:  bool
        
        .. attribute:: bd_state_notification_rate
        
        	This leaf defines the maximum number of 'bd\-state\- notification' that can be emitted from the device per second
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: pbb
        
        	Provider Backbone Bridging (PBB) related global configurations
        	**type**\:   :py:class:`Pbb <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.Global_.Pbb>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "bridge-domain-config"

            self.bd_state_notification_enabled = YLeaf(YType.boolean, "bd-state-notification-enabled")

            self.bd_state_notification_rate = YLeaf(YType.uint32, "bd-state-notification-rate")

            self.pbb = BridgeDomainConfig.Global_.Pbb()
            self.pbb.parent = self
            self._children_name_map["pbb"] = "pbb"
            self._children_yang_names.add("pbb")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bd_state_notification_enabled",
                            "bd_state_notification_rate") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeDomainConfig.Global_, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainConfig.Global_, self).__setattr__(name, value)


        class Pbb(Entity):
            """
            Provider Backbone Bridging (PBB) related global
            configurations.
            
            .. attribute:: backbone_src_mac
            
            	Backbone source mac address configuration for Provider Backbone Bridging (PBB)
            	**type**\:  str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.Global_.Pbb, self).__init__()

                self.yang_name = "pbb"
                self.yang_parent_name = "global"

                self.backbone_src_mac = YLeaf(YType.str, "backbone-src-mac")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("backbone_src_mac") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeDomainConfig.Global_.Pbb, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeDomainConfig.Global_.Pbb, self).__setattr__(name, value)

            def has_data(self):
                return self.backbone_src_mac.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.backbone_src_mac.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "pbb" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:bridge-domain-config/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.backbone_src_mac.is_set or self.backbone_src_mac.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.backbone_src_mac.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "backbone-src-mac"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "backbone-src-mac"):
                    self.backbone_src_mac = value
                    self.backbone_src_mac.value_namespace = name_space
                    self.backbone_src_mac.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.bd_state_notification_enabled.is_set or
                self.bd_state_notification_rate.is_set or
                (self.pbb is not None and self.pbb.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bd_state_notification_enabled.yfilter != YFilter.not_set or
                self.bd_state_notification_rate.yfilter != YFilter.not_set or
                (self.pbb is not None and self.pbb.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bd_state_notification_enabled.is_set or self.bd_state_notification_enabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bd_state_notification_enabled.get_name_leafdata())
            if (self.bd_state_notification_rate.is_set or self.bd_state_notification_rate.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bd_state_notification_rate.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "pbb"):
                if (self.pbb is None):
                    self.pbb = BridgeDomainConfig.Global_.Pbb()
                    self.pbb.parent = self
                    self._children_name_map["pbb"] = "pbb"
                return self.pbb

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "pbb" or name == "bd-state-notification-enabled" or name == "bd-state-notification-rate"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bd-state-notification-enabled"):
                self.bd_state_notification_enabled = value
                self.bd_state_notification_enabled.value_namespace = name_space
                self.bd_state_notification_enabled.value_namespace_prefix = name_space_prefix
            if(value_path == "bd-state-notification-rate"):
                self.bd_state_notification_rate = value
                self.bd_state_notification_rate.value_namespace = name_space
                self.bd_state_notification_rate.value_namespace_prefix = name_space_prefix


    class BridgeGroups(Entity):
        """
        Collection of bridge\-groups.
        
        A Bridge\-group is logical grouping construct for bridge
        domains. It defines grouping of bridge\-domains under a
        named bridge\-group. For example all bridge\-domains
        belonging to a single customer can be grouped under a bridge
        \-group
        
        .. attribute:: bridge_group
        
        	Bridge\-group configuration
        	**type**\: list of    :py:class:`BridgeGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups.BridgeGroup>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.BridgeGroups, self).__init__()

            self.yang_name = "bridge-groups"
            self.yang_parent_name = "bridge-domain-config"

            self.bridge_group = YList(self)

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
                        super(BridgeDomainConfig.BridgeGroups, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainConfig.BridgeGroups, self).__setattr__(name, value)


        class BridgeGroup(Entity):
            """
            Bridge\-group configuration.
            
            .. attribute:: name  <key>
            
            	Bridge\-group name
            	**type**\:  str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.BridgeGroups.BridgeGroup, self).__init__()

                self.yang_name = "bridge-group"
                self.yang_parent_name = "bridge-groups"

                self.name = YLeaf(YType.str, "name")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeDomainConfig.BridgeGroups.BridgeGroup, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeDomainConfig.BridgeGroups.BridgeGroup, self).__setattr__(name, value)

            def has_data(self):
                return self.name.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bridge-group" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:bridge-domain-config/bridge-groups/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bridge_group:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bridge_group:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bridge-groups" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bridge-group"):
                for c in self.bridge_group:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeDomainConfig.BridgeGroups.BridgeGroup()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bridge_group.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bridge-group"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class BridgeDomains(Entity):
        """
        Collection of bridge domains.
        
        .. attribute:: bridge_domain
        
        	Definition of a bridge\-domain
        	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.BridgeDomains, self).__init__()

            self.yang_name = "bridge-domains"
            self.yang_parent_name = "bridge-domain-config"

            self.bridge_domain = YList(self)

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
                        super(BridgeDomainConfig.BridgeDomains, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainConfig.BridgeDomains, self).__setattr__(name, value)


        class BridgeDomain(Entity):
            """
            Definition of a bridge\-domain.
            
            .. attribute:: id  <key>
            
            	Bridge domain name or number
            	**type**\:  str
            
            .. attribute:: bd_status_change_notification
            
            	Enable/disable bridge\-domain status change notification.  If true, any change in bridge\-domain operational status will be notified to client via 'bd\-status\-change' notification
            	**type**\:  bool
            
            .. attribute:: bridge_group
            
            	Reference to bridge\-group name. If bridge\-groups are supported, referred bridge\-group MUST be created first
            	**type**\:  str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups.BridgeGroup>`
            
            	**mandatory**\: True
            
            .. attribute:: dhcp_ipv4_snooping
            
            	Enable DHCP IPv4 snooping
            	**type**\:   :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping>`
            
            .. attribute:: dynamic_arp_inspection
            
            	Dynamic ARP Inspection (DAI) configurations
            	**type**\:   :py:class:`DynamicArpInspection <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection>`
            
            	**presence node**\: True
            
            .. attribute:: enabled
            
            	This leaf represents configured admin status of the bridge domain
            	**type**\:  bool
            
            	**default value**\: true
            
            .. attribute:: flooding_mode
            
            	Flood modes for optimization
            	**type**\:   :py:class:`FloodingMode <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingMode>`
            
            .. attribute:: igmp_snooping
            
            	Enable IGMP snooping
            	**type**\:   :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping>`
            
            .. attribute:: ip_source_guard
            
            	IP source guard (IPSG) configurations
            	**type**\:   :py:class:`IpSourceGuard <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard>`
            
            	**presence node**\: True
            
            .. attribute:: mac
            
            	MAC features for bridge domain
            	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac>`
            
            .. attribute:: members
            
            	Collection of bridge\-domain members
            	**type**\:   :py:class:`Members <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members>`
            
            .. attribute:: mld_snooping
            
            	Enable MLD snooping
            	**type**\:   :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping>`
            
            .. attribute:: mtu
            
            	The MTU size for bridge domain. All bridge domain members must have same MTU size to be operational in the domain
            	**type**\:  int
            
            	**range:** 46..65535
            
            .. attribute:: storm_control
            
            	A collection of storm control threshold and action configurations
            	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl>`
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.BridgeDomains.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "bridge-domains"

                self.id = YLeaf(YType.str, "id")

                self.bd_status_change_notification = YLeaf(YType.boolean, "bd-status-change-notification")

                self.bridge_group = YLeaf(YType.str, "bridge-group")

                self.enabled = YLeaf(YType.boolean, "enabled")

                self.flooding_mode = YLeaf(YType.enumeration, "flooding-mode")

                self.mtu = YLeaf(YType.uint16, "mtu")

                self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping()
                self.dhcp_ipv4_snooping.parent = self
                self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                self._children_yang_names.add("dhcp-ipv4-snooping")

                self.dynamic_arp_inspection = None
                self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                self._children_yang_names.add("dynamic-arp-inspection")

                self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping()
                self.igmp_snooping.parent = self
                self._children_name_map["igmp_snooping"] = "igmp-snooping"
                self._children_yang_names.add("igmp-snooping")

                self.ip_source_guard = None
                self._children_name_map["ip_source_guard"] = "ip-source-guard"
                self._children_yang_names.add("ip-source-guard")

                self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac()
                self.mac.parent = self
                self._children_name_map["mac"] = "mac"
                self._children_yang_names.add("mac")

                self.members = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")

                self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping()
                self.mld_snooping.parent = self
                self._children_name_map["mld_snooping"] = "mld-snooping"
                self._children_yang_names.add("mld-snooping")

                self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl()
                self.storm_control.parent = self
                self._children_name_map["storm_control"] = "storm-control"
                self._children_yang_names.add("storm-control")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id",
                                "bd_status_change_notification",
                                "bridge_group",
                                "enabled",
                                "flooding_mode",
                                "mtu") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain, self).__setattr__(name, value)

            class FloodingMode(Enum):
                """
                FloodingMode

                Flood modes for optimization.

                .. data:: convergence_optimized = 0

                	Flood mode optimized for convergence.

                .. data:: resilience_optimized = 1

                	Flood mode optimized for resiliency

                """

                convergence_optimized = Enum.YLeaf(0, "convergence-optimized")

                resilience_optimized = Enum.YLeaf(1, "resilience-optimized")



            class Members(Entity):
                """
                Collection of bridge\-domain members.
                
                .. attribute:: ac_member
                
                	List of Attachment circuits for current bridge\-domain
                	**type**\: list of    :py:class:`AcMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember>`
                
                .. attribute:: access_pw_member
                
                	Collection of access pseudowire members.  A Pseudowires can be a regular interface with ifType 'ifPwType' or it can represented as a non\-interface context. This container provides model definition for both types of the pseudowires
                	**type**\:   :py:class:`AccessPwMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember>`
                
                .. attribute:: vfi_member
                
                	List of Virtual Forrwarding Interfaces for current bridge\-domain
                	**type**\: list of    :py:class:`VfiMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "bridge-domain"

                    self.access_pw_member = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember()
                    self.access_pw_member.parent = self
                    self._children_name_map["access_pw_member"] = "access-pw-member"
                    self._children_yang_names.add("access-pw-member")

                    self.ac_member = YList(self)
                    self.vfi_member = YList(self)

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
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members, self).__setattr__(name, value)


                class AcMember(Entity):
                    """
                    List of Attachment circuits for current
                    bridge\-domain.
                    
                    .. attribute:: interface  <key>
                    
                    	Reference to an attchment circuit interface instance which is configured to be part of this bridge\-domain
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: dhcp_ipv4_snooping
                    
                    	Enable DHCP IPv4 snooping
                    	**type**\:   :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping>`
                    
                    .. attribute:: dynamic_arp_inspection
                    
                    	Dynamic ARP Inspection (DAI) configurations
                    	**type**\:   :py:class:`DynamicArpInspection <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection>`
                    
                    .. attribute:: flooding
                    
                    	Flooding configurations
                    	**type**\:   :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding>`
                    
                    .. attribute:: igmp_snooping
                    
                    	Enable IGMP snooping
                    	**type**\:   :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping>`
                    
                    .. attribute:: ip_source_guard
                    
                    	IP source guard (IPSG) configurations
                    	**type**\:   :py:class:`IpSourceGuard <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard>`
                    
                    .. attribute:: mac
                    
                    	MAC features for bridge domain
                    	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac>`
                    
                    .. attribute:: mld_snooping
                    
                    	Enable MLD snooping
                    	**type**\:   :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping>`
                    
                    .. attribute:: split_horizon_group
                    
                    	Bridge domain aggregates attachment circuits (ACs) and pseudowires (PWs) in one or more groups called Split Horizon Groups. When applied to bridge domains, Split Horizon refers to the flooding and forwarding behavior between members of a Split Horizon group. In general, frames received on one member of a split horizon group are not flooded out to the other members
                    	**type**\:   :py:class:`SplitHorizonGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: storm_control
                    
                    	A collection of storm control threshold and action configurations
                    	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember, self).__init__()

                        self.yang_name = "ac-member"
                        self.yang_parent_name = "members"

                        self.interface = YLeaf(YType.str, "interface")

                        self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping()
                        self.dhcp_ipv4_snooping.parent = self
                        self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                        self._children_yang_names.add("dhcp-ipv4-snooping")

                        self.dynamic_arp_inspection = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection()
                        self.dynamic_arp_inspection.parent = self
                        self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                        self._children_yang_names.add("dynamic-arp-inspection")

                        self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")

                        self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping()
                        self.igmp_snooping.parent = self
                        self._children_name_map["igmp_snooping"] = "igmp-snooping"
                        self._children_yang_names.add("igmp-snooping")

                        self.ip_source_guard = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard()
                        self.ip_source_guard.parent = self
                        self._children_name_map["ip_source_guard"] = "ip-source-guard"
                        self._children_yang_names.add("ip-source-guard")

                        self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")

                        self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping()
                        self.mld_snooping.parent = self
                        self._children_name_map["mld_snooping"] = "mld-snooping"
                        self._children_yang_names.add("mld-snooping")

                        self.split_horizon_group = None
                        self._children_name_map["split_horizon_group"] = "split-horizon-group"
                        self._children_yang_names.add("split-horizon-group")

                        self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                        self.storm_control.parent = self
                        self._children_name_map["storm_control"] = "storm-control"
                        self._children_yang_names.add("storm-control")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember, self).__setattr__(name, value)


                    class SplitHorizonGroup(Entity):
                        """
                        Bridge domain aggregates attachment circuits (ACs) and
                        pseudowires (PWs) in one or more groups called Split Horizon
                        Groups. When applied to bridge domains, Split Horizon refers
                        to the flooding and forwarding behavior between members of a
                        Split Horizon group. In general, frames received on one
                        member of a split horizon group are not flooded out to the
                        other members.
                        
                        .. attribute:: id
                        
                        	Split Horizon group number for bridge domain member
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**mandatory**\: True
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup, self).__init__()

                            self.yang_name = "split-horizon-group"
                            self.yang_parent_name = "ac-member"
                            self.is_presence_container = True

                            self.id = YLeaf(YType.uint16, "id")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup, self).__setattr__(name, value)

                        def has_data(self):
                            return self.id.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.id.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "split-horizon-group" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "id"):
                                self.id = value
                                self.id.value_namespace = name_space
                                self.id.value_namespace_prefix = name_space_prefix


                    class Mac(Entity):
                        """
                        MAC features for bridge domain.
                        
                        .. attribute:: aging
                        
                        	MAC aging configurations
                        	**type**\:   :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging>`
                        
                        .. attribute:: learning_enabled
                        
                        	Enable disable mac learning
                        	**type**\:  bool
                        
                        	**default value**\: true
                        
                        .. attribute:: limit
                        
                        	MAC table learning limit
                        	**type**\:   :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit>`
                        
                        .. attribute:: port_down
                        
                        	Port down event
                        	**type**\:   :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown>`
                        
                        .. attribute:: secure
                        
                        	MAC secure parameters
                        	**type**\:   :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "ac-member"

                            self.learning_enabled = YLeaf(YType.boolean, "learning-enabled")

                            self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging()
                            self.aging.parent = self
                            self._children_name_map["aging"] = "aging"
                            self._children_yang_names.add("aging")

                            self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit()
                            self.limit.parent = self
                            self._children_name_map["limit"] = "limit"
                            self._children_yang_names.add("limit")

                            self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown()
                            self.port_down.parent = self
                            self._children_name_map["port_down"] = "port-down"
                            self._children_yang_names.add("port-down")

                            self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure()
                            self.secure.parent = self
                            self._children_name_map["secure"] = "secure"
                            self._children_yang_names.add("secure")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("learning_enabled") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac, self).__setattr__(name, value)


                        class Limit(Entity):
                            """
                            MAC table learning limit.
                            
                            .. attribute:: action
                            
                            	MAC limit violation actions
                            	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                            
                            .. attribute:: maximum
                            
                            	Maximum number of mac addresses that can be learnt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: notification
                            
                            	MAC limit violation notifications
                            	**type**\:   :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit, self).__init__()

                                self.yang_name = "limit"
                                self.yang_parent_name = "mac"

                                self.action = YLeaf(YType.enumeration, "action")

                                self.maximum = YLeaf(YType.uint32, "maximum")

                                self.notification = YLeaf(YType.identityref, "notification")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("action",
                                                "maximum",
                                                "notification") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.action.is_set or
                                    self.maximum.is_set or
                                    self.notification.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.action.yfilter != YFilter.not_set or
                                    self.maximum.yfilter != YFilter.not_set or
                                    self.notification.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "limit" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.action.get_name_leafdata())
                                if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.maximum.get_name_leafdata())
                                if (self.notification.is_set or self.notification.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.notification.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "action" or name == "maximum" or name == "notification"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "action"):
                                    self.action = value
                                    self.action.value_namespace = name_space
                                    self.action.value_namespace_prefix = name_space_prefix
                                if(value_path == "maximum"):
                                    self.maximum = value
                                    self.maximum.value_namespace = name_space
                                    self.maximum.value_namespace_prefix = name_space_prefix
                                if(value_path == "notification"):
                                    self.notification = value
                                    self.notification.value_namespace = name_space
                                    self.notification.value_namespace_prefix = name_space_prefix


                        class Aging(Entity):
                            """
                            MAC aging configurations.
                            
                            .. attribute:: time
                            
                            	The timeout period in seconds for aging out dynamically learned forwarding information
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 300
                            
                            .. attribute:: type
                            
                            	MAC aging type
                            	**type**\:   :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging, self).__init__()

                                self.yang_name = "aging"
                                self.yang_parent_name = "mac"

                                self.time = YLeaf(YType.uint32, "time")

                                self.type = YLeaf(YType.enumeration, "type")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("time",
                                                "type") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.time.is_set or
                                    self.type.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.time.yfilter != YFilter.not_set or
                                    self.type.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "aging" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.time.get_name_leafdata())
                                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.type.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "time" or name == "type"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "time"):
                                    self.time = value
                                    self.time.value_namespace = name_space
                                    self.time.value_namespace_prefix = name_space_prefix
                                if(value_path == "type"):
                                    self.type = value
                                    self.type.value_namespace = name_space
                                    self.type.value_namespace_prefix = name_space_prefix


                        class PortDown(Entity):
                            """
                            Port down event
                            
                            .. attribute:: flush
                            
                            	Enable/Disable mac table flush when port moves to down state
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown, self).__init__()

                                self.yang_name = "port-down"
                                self.yang_parent_name = "mac"

                                self.flush = YLeaf(YType.boolean, "flush")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("flush") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown, self).__setattr__(name, value)

                            def has_data(self):
                                return self.flush.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.flush.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "port-down" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.flush.is_set or self.flush.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.flush.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "flush"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "flush"):
                                    self.flush = value
                                    self.flush.value_namespace = name_space
                                    self.flush.value_namespace_prefix = name_space_prefix


                        class Secure(Entity):
                            """
                            MAC secure parameters.
                            
                            .. attribute:: action
                            
                            	MAC secure action for violating packets
                            	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                            
                            	**default value**\: restrict
                            
                            .. attribute:: enabled
                            
                            	Enable or disable mac secure feature
                            	**type**\:  bool
                            
                            .. attribute:: logging
                            
                            	Enable/Disable logging
                            	**type**\:  bool
                            
                            	**default value**\: false
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure, self).__init__()

                                self.yang_name = "secure"
                                self.yang_parent_name = "mac"

                                self.action = YLeaf(YType.enumeration, "action")

                                self.enabled = YLeaf(YType.boolean, "enabled")

                                self.logging = YLeaf(YType.boolean, "logging")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("action",
                                                "enabled",
                                                "logging") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.action.is_set or
                                    self.enabled.is_set or
                                    self.logging.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.action.yfilter != YFilter.not_set or
                                    self.enabled.yfilter != YFilter.not_set or
                                    self.logging.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "secure" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.action.get_name_leafdata())
                                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled.get_name_leafdata())
                                if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.logging.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "action" or name == "enabled" or name == "logging"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "action"):
                                    self.action = value
                                    self.action.value_namespace = name_space
                                    self.action.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled"):
                                    self.enabled = value
                                    self.enabled.value_namespace = name_space
                                    self.enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "logging"):
                                    self.logging = value
                                    self.logging.value_namespace = name_space
                                    self.logging.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.learning_enabled.is_set or
                                (self.aging is not None and self.aging.has_data()) or
                                (self.limit is not None and self.limit.has_data()) or
                                (self.port_down is not None and self.port_down.has_data()) or
                                (self.secure is not None and self.secure.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.learning_enabled.yfilter != YFilter.not_set or
                                (self.aging is not None and self.aging.has_operation()) or
                                (self.limit is not None and self.limit.has_operation()) or
                                (self.port_down is not None and self.port_down.has_operation()) or
                                (self.secure is not None and self.secure.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mac" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.learning_enabled.is_set or self.learning_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.learning_enabled.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "aging"):
                                if (self.aging is None):
                                    self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging()
                                    self.aging.parent = self
                                    self._children_name_map["aging"] = "aging"
                                return self.aging

                            if (child_yang_name == "limit"):
                                if (self.limit is None):
                                    self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit()
                                    self.limit.parent = self
                                    self._children_name_map["limit"] = "limit"
                                return self.limit

                            if (child_yang_name == "port-down"):
                                if (self.port_down is None):
                                    self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown()
                                    self.port_down.parent = self
                                    self._children_name_map["port_down"] = "port-down"
                                return self.port_down

                            if (child_yang_name == "secure"):
                                if (self.secure is None):
                                    self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure()
                                    self.secure.parent = self
                                    self._children_name_map["secure"] = "secure"
                                return self.secure

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "aging" or name == "limit" or name == "port-down" or name == "secure" or name == "learning-enabled"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "learning-enabled"):
                                self.learning_enabled = value
                                self.learning_enabled.value_namespace = name_space
                                self.learning_enabled.value_namespace_prefix = name_space_prefix


                    class IgmpSnooping(Entity):
                        """
                        Enable IGMP snooping.
                        
                        .. attribute:: profile_name
                        
                        	IGMP snooping profile name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping, self).__init__()

                            self.yang_name = "igmp-snooping"
                            self.yang_parent_name = "ac-member"

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
                                if name in ("profile_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping, self).__setattr__(name, value)

                        def has_data(self):
                            return self.profile_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.profile_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "igmp-snooping" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "profile-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "profile-name"):
                                self.profile_name = value
                                self.profile_name.value_namespace = name_space
                                self.profile_name.value_namespace_prefix = name_space_prefix


                    class MldSnooping(Entity):
                        """
                        Enable MLD snooping
                        
                        .. attribute:: profile_name
                        
                        	MLD snooping profile name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping, self).__init__()

                            self.yang_name = "mld-snooping"
                            self.yang_parent_name = "ac-member"

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
                                if name in ("profile_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping, self).__setattr__(name, value)

                        def has_data(self):
                            return self.profile_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.profile_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mld-snooping" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "profile-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "profile-name"):
                                self.profile_name = value
                                self.profile_name.value_namespace = name_space
                                self.profile_name.value_namespace_prefix = name_space_prefix


                    class DhcpIpv4Snooping(Entity):
                        """
                        Enable DHCP IPv4 snooping.
                        
                        .. attribute:: profile_name
                        
                        	DHCPv4 snooping profile name
                        	**type**\:  str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping, self).__init__()

                            self.yang_name = "dhcp-ipv4-snooping"
                            self.yang_parent_name = "ac-member"

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
                                if name in ("profile_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping, self).__setattr__(name, value)

                        def has_data(self):
                            return self.profile_name.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.profile_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dhcp-ipv4-snooping" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "profile-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "profile-name"):
                                self.profile_name = value
                                self.profile_name.value_namespace = name_space
                                self.profile_name.value_namespace_prefix = name_space_prefix


                    class Flooding(Entity):
                        """
                        Flooding configurations.
                        
                        .. attribute:: disabled
                        
                        	Disable flooding
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: disabled_unknown_unicast
                        
                        	Disable unknown unicast flooding
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "ac-member"

                            self.disabled = YLeaf(YType.empty, "disabled")

                            self.disabled_unknown_unicast = YLeaf(YType.empty, "disabled-unknown-unicast")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("disabled",
                                            "disabled_unknown_unicast") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.disabled.is_set or
                                self.disabled_unknown_unicast.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.disabled.yfilter != YFilter.not_set or
                                self.disabled_unknown_unicast.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flooding" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disabled.get_name_leafdata())
                            if (self.disabled_unknown_unicast.is_set or self.disabled_unknown_unicast.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disabled_unknown_unicast.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "disabled" or name == "disabled-unknown-unicast"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "disabled"):
                                self.disabled = value
                                self.disabled.value_namespace = name_space
                                self.disabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "disabled-unknown-unicast"):
                                self.disabled_unknown_unicast = value
                                self.disabled_unknown_unicast.value_namespace = name_space
                                self.disabled_unknown_unicast.value_namespace_prefix = name_space_prefix


                    class StormControl(Entity):
                        """
                        A collection of storm control threshold and action
                        configurations.
                        
                        .. attribute:: action
                        
                        	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                        	**type**\:   :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                        
                        .. attribute:: thresholds
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__init__()

                            self.yang_name = "storm-control"
                            self.yang_parent_name = "ac-member"

                            self.action = YLeaf(YType.identityref, "action")

                            self.thresholds = YList(self)

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__setattr__(name, value)


                        class Thresholds(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                            	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: unit
                            
                            	This enumeration define unit of the traffic threshold value
                            	**type**\:   :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.Unit>`
                            
                            	**mandatory**\: True
                            
                            .. attribute:: value
                            
                            	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds, self).__init__()

                                self.yang_name = "thresholds"
                                self.yang_parent_name = "storm-control"

                                self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                                self.unit = YLeaf(YType.enumeration, "unit")

                                self.value = YLeaf(YType.uint32, "value")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("traffic_class",
                                                "unit",
                                                "value") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds, self).__setattr__(name, value)

                            class Unit(Enum):
                                """
                                Unit

                                This enumeration define unit of the traffic threshold

                                value.

                                .. data:: bps = 0

                                	Bits per second.

                                .. data:: kbps = 1

                                	Kilobits per second.

                                .. data:: pps = 2

                                	Packets per seconds.

                                """

                                bps = Enum.YLeaf(0, "bps")

                                kbps = Enum.YLeaf(1, "kbps")

                                pps = Enum.YLeaf(2, "pps")


                            def has_data(self):
                                return (
                                    self.traffic_class.is_set or
                                    self.unit.is_set or
                                    self.value.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set or
                                    self.unit.yfilter != YFilter.not_set or
                                    self.value.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "thresholds" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())
                                if (self.unit.is_set or self.unit.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.unit.get_name_leafdata())
                                if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.value.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "traffic-class" or name == "unit" or name == "value"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "unit"):
                                    self.unit = value
                                    self.unit.value_namespace = name_space
                                    self.unit.value_namespace_prefix = name_space_prefix
                                if(value_path == "value"):
                                    self.value = value
                                    self.value.value_namespace = name_space
                                    self.value.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.thresholds:
                                if (c.has_data()):
                                    return True
                            return self.action.is_set

                        def has_operation(self):
                            for c in self.thresholds:
                                if (c.has_operation()):
                                    return True
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "storm-control" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "thresholds"):
                                for c in self.thresholds:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.thresholds.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "thresholds" or name == "action"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action"):
                                self.action = value
                                self.action.value_namespace = name_space
                                self.action.value_namespace_prefix = name_space_prefix


                    class DynamicArpInspection(Entity):
                        """
                        Dynamic ARP Inspection (DAI) configurations.
                        
                        .. attribute:: address_validation
                        
                        	Enable address validation
                        	**type**\:   :py:class:`AddressValidation <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: enable
                        
                        	Enable or disable Dynamic ARP Inspection
                        	**type**\:  bool
                        
                        .. attribute:: logging
                        
                        	Enable DAI logging
                        	**type**\:  bool
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection, self).__init__()

                            self.yang_name = "dynamic-arp-inspection"
                            self.yang_parent_name = "ac-member"

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.logging = YLeaf(YType.boolean, "logging")

                            self.address_validation = None
                            self._children_name_map["address_validation"] = "address-validation"
                            self._children_yang_names.add("address-validation")

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
                                            "logging") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection, self).__setattr__(name, value)


                        class AddressValidation(Entity):
                            """
                            Enable address validation.
                            
                            .. attribute:: dst_mac
                            
                            	Match Destination MAC Address
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: ipv4
                            
                            	Match IPv4 Address
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: src_mac
                            
                            	Match Source MAC Address
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation, self).__init__()

                                self.yang_name = "address-validation"
                                self.yang_parent_name = "dynamic-arp-inspection"
                                self.is_presence_container = True

                                self.dst_mac = YLeaf(YType.empty, "dst-mac")

                                self.ipv4 = YLeaf(YType.empty, "ipv4")

                                self.src_mac = YLeaf(YType.empty, "src-mac")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("dst_mac",
                                                "ipv4",
                                                "src_mac") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.dst_mac.is_set or
                                    self.ipv4.is_set or
                                    self.src_mac.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.dst_mac.yfilter != YFilter.not_set or
                                    self.ipv4.yfilter != YFilter.not_set or
                                    self.src_mac.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "address-validation" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.dst_mac.is_set or self.dst_mac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dst_mac.get_name_leafdata())
                                if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv4.get_name_leafdata())
                                if (self.src_mac.is_set or self.src_mac.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.src_mac.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "dst-mac" or name == "ipv4" or name == "src-mac"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "dst-mac"):
                                    self.dst_mac = value
                                    self.dst_mac.value_namespace = name_space
                                    self.dst_mac.value_namespace_prefix = name_space_prefix
                                if(value_path == "ipv4"):
                                    self.ipv4 = value
                                    self.ipv4.value_namespace = name_space
                                    self.ipv4.value_namespace_prefix = name_space_prefix
                                if(value_path == "src-mac"):
                                    self.src_mac = value
                                    self.src_mac.value_namespace = name_space
                                    self.src_mac.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.enable.is_set or
                                self.logging.is_set or
                                (self.address_validation is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                self.logging.yfilter != YFilter.not_set or
                                (self.address_validation is not None and self.address_validation.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dynamic-arp-inspection" + path_buffer

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
                            if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.logging.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "address-validation"):
                                if (self.address_validation is None):
                                    self.address_validation = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation()
                                    self.address_validation.parent = self
                                    self._children_name_map["address_validation"] = "address-validation"
                                return self.address_validation

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-validation" or name == "enable" or name == "logging"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "logging"):
                                self.logging = value
                                self.logging.value_namespace = name_space
                                self.logging.value_namespace_prefix = name_space_prefix


                    class IpSourceGuard(Entity):
                        """
                        IP source guard (IPSG) configurations.
                        
                        .. attribute:: enable
                        
                        	Enable or disable IP source guard feature
                        	**type**\:  bool
                        
                        .. attribute:: logging
                        
                        	Enable IPSG logging
                        	**type**\:  bool
                        
                        	**default value**\: false
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard, self).__init__()

                            self.yang_name = "ip-source-guard"
                            self.yang_parent_name = "ac-member"

                            self.enable = YLeaf(YType.boolean, "enable")

                            self.logging = YLeaf(YType.boolean, "logging")

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
                                            "logging") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.enable.is_set or
                                self.logging.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.enable.yfilter != YFilter.not_set or
                                self.logging.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ip-source-guard" + path_buffer

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
                            if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.logging.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "enable" or name == "logging"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "enable"):
                                self.enable = value
                                self.enable.value_namespace = name_space
                                self.enable.value_namespace_prefix = name_space_prefix
                            if(value_path == "logging"):
                                self.logging = value
                                self.logging.value_namespace = name_space
                                self.logging.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_data()) or
                            (self.dynamic_arp_inspection is not None and self.dynamic_arp_inspection.has_data()) or
                            (self.flooding is not None and self.flooding.has_data()) or
                            (self.igmp_snooping is not None and self.igmp_snooping.has_data()) or
                            (self.ip_source_guard is not None and self.ip_source_guard.has_data()) or
                            (self.mac is not None and self.mac.has_data()) or
                            (self.mld_snooping is not None and self.mld_snooping.has_data()) or
                            (self.storm_control is not None and self.storm_control.has_data()) or
                            (self.split_horizon_group is not None))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_operation()) or
                            (self.dynamic_arp_inspection is not None and self.dynamic_arp_inspection.has_operation()) or
                            (self.flooding is not None and self.flooding.has_operation()) or
                            (self.igmp_snooping is not None and self.igmp_snooping.has_operation()) or
                            (self.ip_source_guard is not None and self.ip_source_guard.has_operation()) or
                            (self.mac is not None and self.mac.has_operation()) or
                            (self.mld_snooping is not None and self.mld_snooping.has_operation()) or
                            (self.split_horizon_group is not None and self.split_horizon_group.has_operation()) or
                            (self.storm_control is not None and self.storm_control.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ac-member" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dhcp-ipv4-snooping"):
                            if (self.dhcp_ipv4_snooping is None):
                                self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping()
                                self.dhcp_ipv4_snooping.parent = self
                                self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                            return self.dhcp_ipv4_snooping

                        if (child_yang_name == "dynamic-arp-inspection"):
                            if (self.dynamic_arp_inspection is None):
                                self.dynamic_arp_inspection = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection()
                                self.dynamic_arp_inspection.parent = self
                                self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                            return self.dynamic_arp_inspection

                        if (child_yang_name == "flooding"):
                            if (self.flooding is None):
                                self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding()
                                self.flooding.parent = self
                                self._children_name_map["flooding"] = "flooding"
                            return self.flooding

                        if (child_yang_name == "igmp-snooping"):
                            if (self.igmp_snooping is None):
                                self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping()
                                self.igmp_snooping.parent = self
                                self._children_name_map["igmp_snooping"] = "igmp-snooping"
                            return self.igmp_snooping

                        if (child_yang_name == "ip-source-guard"):
                            if (self.ip_source_guard is None):
                                self.ip_source_guard = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard()
                                self.ip_source_guard.parent = self
                                self._children_name_map["ip_source_guard"] = "ip-source-guard"
                            return self.ip_source_guard

                        if (child_yang_name == "mac"):
                            if (self.mac is None):
                                self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac()
                                self.mac.parent = self
                                self._children_name_map["mac"] = "mac"
                            return self.mac

                        if (child_yang_name == "mld-snooping"):
                            if (self.mld_snooping is None):
                                self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping()
                                self.mld_snooping.parent = self
                                self._children_name_map["mld_snooping"] = "mld-snooping"
                            return self.mld_snooping

                        if (child_yang_name == "split-horizon-group"):
                            if (self.split_horizon_group is None):
                                self.split_horizon_group = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup()
                                self.split_horizon_group.parent = self
                                self._children_name_map["split_horizon_group"] = "split-horizon-group"
                            return self.split_horizon_group

                        if (child_yang_name == "storm-control"):
                            if (self.storm_control is None):
                                self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                                self.storm_control.parent = self
                                self._children_name_map["storm_control"] = "storm-control"
                            return self.storm_control

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dhcp-ipv4-snooping" or name == "dynamic-arp-inspection" or name == "flooding" or name == "igmp-snooping" or name == "ip-source-guard" or name == "mac" or name == "mld-snooping" or name == "split-horizon-group" or name == "storm-control" or name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix


                class VfiMember(Entity):
                    """
                    List of Virtual Forrwarding Interfaces for current
                    bridge\-domain.
                    
                    .. attribute:: interface  <key>
                    
                    	Reference to an Virtual Forwarding Interface instance which is configured to be part of this bridge\-domain
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember, self).__init__()

                        self.yang_name = "vfi-member"
                        self.yang_parent_name = "members"

                        self.interface = YLeaf(YType.str, "interface")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember, self).__setattr__(name, value)

                    def has_data(self):
                        return self.interface.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vfi-member" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix


                class AccessPwMember(Entity):
                    """
                    Collection of access pseudowire members.
                    
                    A Pseudowires can be a regular interface with ifType
                    'ifPwType' or it can represented as a non\-interface
                    context. This container provides model definition for
                    both types of the pseudowires.
                    
                    .. attribute:: access_pw_if_member
                    
                    	List of interface based access pseudowires for current bridge\-domain
                    	**type**\: list of    :py:class:`AccessPwIfMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember>`
                    
                    .. attribute:: pw_neighbor_spec
                    
                    	Collection of neighbor specification based pseudo\-wires
                    	**type**\: list of    :py:class:`PwNeighborSpec <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__init__()

                        self.yang_name = "access-pw-member"
                        self.yang_parent_name = "members"

                        self.access_pw_if_member = YList(self)
                        self.pw_neighbor_spec = YList(self)

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
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__setattr__(name, value)


                    class AccessPwIfMember(Entity):
                        """
                        List of interface based access pseudowires for
                        current bridge\-domain.
                        
                        .. attribute:: interface  <key>
                        
                        	Reference to an access pseudo\-wire interface instance which is configured to be part of this bridge domain
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember, self).__init__()

                            self.yang_name = "access-pw-if-member"
                            self.yang_parent_name = "access-pw-member"

                            self.interface = YLeaf(YType.str, "interface")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember, self).__setattr__(name, value)

                        def has_data(self):
                            return self.interface.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "access-pw-if-member" + "[interface='" + self.interface.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix


                    class PwNeighborSpec(Entity):
                        """
                        Collection of neighbor specification based
                        pseudo\-wires.
                        
                        .. attribute:: neighbor_ip_address  <key>
                        
                        	IPv4 or IPv6 address of the neighbor
                        	**type**\: one of the below types:
                        
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        
                        ----
                        .. attribute:: vc_id  <key>
                        
                        	Pseudowire VC ID
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: backup
                        
                        	Backup pseudo\-wire
                        	**type**\:   :py:class:`Backup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup>`
                        
                        .. attribute:: dhcp_ipv4_snooping
                        
                        	Enable DHCP IPv4 snooping
                        	**type**\:   :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping>`
                        
                        .. attribute:: encap_type
                        
                        	Encapsulation configuration for this neighbor
                        	**type**\:   :py:class:`PwEncapsulationType <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationType>`
                        
                        .. attribute:: flooding
                        
                        	Flooding configurations
                        	**type**\:   :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding>`
                        
                        .. attribute:: igmp_snooping
                        
                        	Enable IGMP snooping
                        	**type**\:   :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping>`
                        
                        .. attribute:: mac
                        
                        	MAC features for bridge domain
                        	**type**\:   :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac>`
                        
                        .. attribute:: mld_snooping
                        
                        	Enable MLD snooping
                        	**type**\:   :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping>`
                        
                        .. attribute:: pw_class_template
                        
                        	Reference to a pseudowire template
                        	**type**\:  str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
                        
                        .. attribute:: source_ipv6
                        
                        	The local source IPv6 address. Note this should only be configured when neighbor address is IPv6 type
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: split_horizon_group
                        
                        	Bridge domain aggregates attachment circuits (ACs) and pseudowires (PWs) in one or more groups called Split Horizon Groups. When applied to bridge domains, Split Horizon refers to the flooding and forwarding behavior between members of a Split Horizon group. In general, frames received on one member of a split horizon group are not flooded out to the other members
                        	**type**\:   :py:class:`SplitHorizonGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: static_label
                        
                        	Statically configured labels, signalling should be none
                        	**type**\:   :py:class:`StaticLabel <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel>`
                        
                        .. attribute:: storm_control
                        
                        	A collection of storm control threshold and action configurations
                        	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl>`
                        
                        .. attribute:: tag_impose_vlan
                        
                        	Specify a tag for a VLAN ID for the pseudowire
                        	**type**\:  int
                        
                        	**range:** 1..4094
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec, self).__init__()

                            self.yang_name = "pw-neighbor-spec"
                            self.yang_parent_name = "access-pw-member"

                            self.neighbor_ip_address = YLeaf(YType.str, "neighbor-ip-address")

                            self.vc_id = YLeaf(YType.uint32, "vc-id")

                            self.encap_type = YLeaf(YType.identityref, "encap-type")

                            self.pw_class_template = YLeaf(YType.str, "pw-class-template")

                            self.source_ipv6 = YLeaf(YType.str, "source-ipv6")

                            self.tag_impose_vlan = YLeaf(YType.uint16, "tag-impose-vlan")

                            self.backup = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup()
                            self.backup.parent = self
                            self._children_name_map["backup"] = "backup"
                            self._children_yang_names.add("backup")

                            self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping()
                            self.dhcp_ipv4_snooping.parent = self
                            self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                            self._children_yang_names.add("dhcp-ipv4-snooping")

                            self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding()
                            self.flooding.parent = self
                            self._children_name_map["flooding"] = "flooding"
                            self._children_yang_names.add("flooding")

                            self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping()
                            self.igmp_snooping.parent = self
                            self._children_name_map["igmp_snooping"] = "igmp-snooping"
                            self._children_yang_names.add("igmp-snooping")

                            self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping()
                            self.mld_snooping.parent = self
                            self._children_name_map["mld_snooping"] = "mld-snooping"
                            self._children_yang_names.add("mld-snooping")

                            self.split_horizon_group = None
                            self._children_name_map["split_horizon_group"] = "split-horizon-group"
                            self._children_yang_names.add("split-horizon-group")

                            self.static_label = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel()
                            self.static_label.parent = self
                            self._children_name_map["static_label"] = "static-label"
                            self._children_yang_names.add("static-label")

                            self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl()
                            self.storm_control.parent = self
                            self._children_name_map["storm_control"] = "storm-control"
                            self._children_yang_names.add("storm-control")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("neighbor_ip_address",
                                            "vc_id",
                                            "encap_type",
                                            "pw_class_template",
                                            "source_ipv6",
                                            "tag_impose_vlan") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec, self).__setattr__(name, value)


                        class StaticLabel(Entity):
                            """
                            Statically configured labels, signalling should be none
                            
                            .. attribute:: local_label
                            
                            	Local MPLS label ID
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: remote_label
                            
                            	Remote MPLS label ID
                            	**type**\:  int
                            
                            	**range:** 16..1048575
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel, self).__init__()

                                self.yang_name = "static-label"
                                self.yang_parent_name = "pw-neighbor-spec"

                                self.local_label = YLeaf(YType.uint32, "local-label")

                                self.remote_label = YLeaf(YType.uint32, "remote-label")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("local_label",
                                                "remote_label") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.local_label.is_set or
                                    self.remote_label.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.local_label.yfilter != YFilter.not_set or
                                    self.remote_label.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "static-label" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.local_label.is_set or self.local_label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.local_label.get_name_leafdata())
                                if (self.remote_label.is_set or self.remote_label.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.remote_label.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "local-label" or name == "remote-label"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "local-label"):
                                    self.local_label = value
                                    self.local_label.value_namespace = name_space
                                    self.local_label.value_namespace_prefix = name_space_prefix
                                if(value_path == "remote-label"):
                                    self.remote_label = value
                                    self.remote_label.value_namespace = name_space
                                    self.remote_label.value_namespace_prefix = name_space_prefix


                        class SplitHorizonGroup(Entity):
                            """
                            Bridge domain aggregates attachment circuits (ACs) and
                            pseudowires (PWs) in one or more groups called Split Horizon
                            Groups. When applied to bridge domains, Split Horizon refers
                            to the flooding and forwarding behavior between members of a
                            Split Horizon group. In general, frames received on one
                            member of a split horizon group are not flooded out to the
                            other members.
                            
                            .. attribute:: id
                            
                            	Split Horizon group number for bridge domain member
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup, self).__init__()

                                self.yang_name = "split-horizon-group"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_presence_container = True

                                self.id = YLeaf(YType.uint16, "id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup, self).__setattr__(name, value)

                            def has_data(self):
                                return self.id.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "split-horizon-group" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "id"):
                                    self.id = value
                                    self.id.value_namespace = name_space
                                    self.id.value_namespace_prefix = name_space_prefix


                        class Mac(Entity):
                            """
                            MAC features for bridge domain.
                            
                            .. attribute:: aging
                            
                            	MAC aging configurations
                            	**type**\:   :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging>`
                            
                            .. attribute:: learning_enabled
                            
                            	Enable disable mac learning
                            	**type**\:  bool
                            
                            	**default value**\: true
                            
                            .. attribute:: limit
                            
                            	MAC table learning limit
                            	**type**\:   :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit>`
                            
                            .. attribute:: port_down
                            
                            	Port down event
                            	**type**\:   :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown>`
                            
                            .. attribute:: secure
                            
                            	MAC secure parameters
                            	**type**\:   :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "pw-neighbor-spec"

                                self.learning_enabled = YLeaf(YType.boolean, "learning-enabled")

                                self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging()
                                self.aging.parent = self
                                self._children_name_map["aging"] = "aging"
                                self._children_yang_names.add("aging")

                                self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit()
                                self.limit.parent = self
                                self._children_name_map["limit"] = "limit"
                                self._children_yang_names.add("limit")

                                self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown()
                                self.port_down.parent = self
                                self._children_name_map["port_down"] = "port-down"
                                self._children_yang_names.add("port-down")

                                self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure()
                                self.secure.parent = self
                                self._children_name_map["secure"] = "secure"
                                self._children_yang_names.add("secure")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("learning_enabled") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac, self).__setattr__(name, value)


                            class Limit(Entity):
                                """
                                MAC table learning limit.
                                
                                .. attribute:: action
                                
                                	MAC limit violation actions
                                	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                                
                                .. attribute:: maximum
                                
                                	Maximum number of mac addresses that can be learnt
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: notification
                                
                                	MAC limit violation notifications
                                	**type**\:   :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit, self).__init__()

                                    self.yang_name = "limit"
                                    self.yang_parent_name = "mac"

                                    self.action = YLeaf(YType.enumeration, "action")

                                    self.maximum = YLeaf(YType.uint32, "maximum")

                                    self.notification = YLeaf(YType.identityref, "notification")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("action",
                                                    "maximum",
                                                    "notification") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.action.is_set or
                                        self.maximum.is_set or
                                        self.notification.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action.yfilter != YFilter.not_set or
                                        self.maximum.yfilter != YFilter.not_set or
                                        self.notification.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "limit" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.action.get_name_leafdata())
                                    if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.maximum.get_name_leafdata())
                                    if (self.notification.is_set or self.notification.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.notification.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "action" or name == "maximum" or name == "notification"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action"):
                                        self.action = value
                                        self.action.value_namespace = name_space
                                        self.action.value_namespace_prefix = name_space_prefix
                                    if(value_path == "maximum"):
                                        self.maximum = value
                                        self.maximum.value_namespace = name_space
                                        self.maximum.value_namespace_prefix = name_space_prefix
                                    if(value_path == "notification"):
                                        self.notification = value
                                        self.notification.value_namespace = name_space
                                        self.notification.value_namespace_prefix = name_space_prefix


                            class Aging(Entity):
                                """
                                MAC aging configurations.
                                
                                .. attribute:: time
                                
                                	The timeout period in seconds for aging out dynamically learned forwarding information
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: seconds
                                
                                	**default value**\: 300
                                
                                .. attribute:: type
                                
                                	MAC aging type
                                	**type**\:   :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging, self).__init__()

                                    self.yang_name = "aging"
                                    self.yang_parent_name = "mac"

                                    self.time = YLeaf(YType.uint32, "time")

                                    self.type = YLeaf(YType.enumeration, "type")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("time",
                                                    "type") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.time.is_set or
                                        self.type.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.time.yfilter != YFilter.not_set or
                                        self.type.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "aging" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.time.get_name_leafdata())
                                    if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.type.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "time" or name == "type"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "time"):
                                        self.time = value
                                        self.time.value_namespace = name_space
                                        self.time.value_namespace_prefix = name_space_prefix
                                    if(value_path == "type"):
                                        self.type = value
                                        self.type.value_namespace = name_space
                                        self.type.value_namespace_prefix = name_space_prefix


                            class PortDown(Entity):
                                """
                                Port down event
                                
                                .. attribute:: flush
                                
                                	Enable/Disable mac table flush when port moves to down state
                                	**type**\:  bool
                                
                                	**default value**\: true
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown, self).__init__()

                                    self.yang_name = "port-down"
                                    self.yang_parent_name = "mac"

                                    self.flush = YLeaf(YType.boolean, "flush")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("flush") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown, self).__setattr__(name, value)

                                def has_data(self):
                                    return self.flush.is_set

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.flush.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "port-down" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.flush.is_set or self.flush.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.flush.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "flush"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "flush"):
                                        self.flush = value
                                        self.flush.value_namespace = name_space
                                        self.flush.value_namespace_prefix = name_space_prefix


                            class Secure(Entity):
                                """
                                MAC secure parameters.
                                
                                .. attribute:: action
                                
                                	MAC secure action for violating packets
                                	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                                
                                	**default value**\: restrict
                                
                                .. attribute:: enabled
                                
                                	Enable or disable mac secure feature
                                	**type**\:  bool
                                
                                .. attribute:: logging
                                
                                	Enable/Disable logging
                                	**type**\:  bool
                                
                                	**default value**\: false
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure, self).__init__()

                                    self.yang_name = "secure"
                                    self.yang_parent_name = "mac"

                                    self.action = YLeaf(YType.enumeration, "action")

                                    self.enabled = YLeaf(YType.boolean, "enabled")

                                    self.logging = YLeaf(YType.boolean, "logging")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("action",
                                                    "enabled",
                                                    "logging") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.action.is_set or
                                        self.enabled.is_set or
                                        self.logging.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.action.yfilter != YFilter.not_set or
                                        self.enabled.yfilter != YFilter.not_set or
                                        self.logging.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "secure" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.action.get_name_leafdata())
                                    if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.enabled.get_name_leafdata())
                                    if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.logging.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "action" or name == "enabled" or name == "logging"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "action"):
                                        self.action = value
                                        self.action.value_namespace = name_space
                                        self.action.value_namespace_prefix = name_space_prefix
                                    if(value_path == "enabled"):
                                        self.enabled = value
                                        self.enabled.value_namespace = name_space
                                        self.enabled.value_namespace_prefix = name_space_prefix
                                    if(value_path == "logging"):
                                        self.logging = value
                                        self.logging.value_namespace = name_space
                                        self.logging.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.learning_enabled.is_set or
                                    (self.aging is not None and self.aging.has_data()) or
                                    (self.limit is not None and self.limit.has_data()) or
                                    (self.port_down is not None and self.port_down.has_data()) or
                                    (self.secure is not None and self.secure.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.learning_enabled.yfilter != YFilter.not_set or
                                    (self.aging is not None and self.aging.has_operation()) or
                                    (self.limit is not None and self.limit.has_operation()) or
                                    (self.port_down is not None and self.port_down.has_operation()) or
                                    (self.secure is not None and self.secure.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mac" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.learning_enabled.is_set or self.learning_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.learning_enabled.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "aging"):
                                    if (self.aging is None):
                                        self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging()
                                        self.aging.parent = self
                                        self._children_name_map["aging"] = "aging"
                                    return self.aging

                                if (child_yang_name == "limit"):
                                    if (self.limit is None):
                                        self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit()
                                        self.limit.parent = self
                                        self._children_name_map["limit"] = "limit"
                                    return self.limit

                                if (child_yang_name == "port-down"):
                                    if (self.port_down is None):
                                        self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown()
                                        self.port_down.parent = self
                                        self._children_name_map["port_down"] = "port-down"
                                    return self.port_down

                                if (child_yang_name == "secure"):
                                    if (self.secure is None):
                                        self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure()
                                        self.secure.parent = self
                                        self._children_name_map["secure"] = "secure"
                                    return self.secure

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "aging" or name == "limit" or name == "port-down" or name == "secure" or name == "learning-enabled"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "learning-enabled"):
                                    self.learning_enabled = value
                                    self.learning_enabled.value_namespace = name_space
                                    self.learning_enabled.value_namespace_prefix = name_space_prefix


                        class IgmpSnooping(Entity):
                            """
                            Enable IGMP snooping.
                            
                            .. attribute:: profile_name
                            
                            	IGMP snooping profile name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping, self).__init__()

                                self.yang_name = "igmp-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"

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
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "igmp-snooping" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class MldSnooping(Entity):
                            """
                            Enable MLD snooping
                            
                            .. attribute:: profile_name
                            
                            	MLD snooping profile name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping, self).__init__()

                                self.yang_name = "mld-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"

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
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "mld-snooping" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class DhcpIpv4Snooping(Entity):
                            """
                            Enable DHCP IPv4 snooping.
                            
                            .. attribute:: profile_name
                            
                            	DHCPv4 snooping profile name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping, self).__init__()

                                self.yang_name = "dhcp-ipv4-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"

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
                                    if name in ("profile_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping, self).__setattr__(name, value)

                            def has_data(self):
                                return self.profile_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.profile_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "dhcp-ipv4-snooping" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "profile-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "profile-name"):
                                    self.profile_name = value
                                    self.profile_name.value_namespace = name_space
                                    self.profile_name.value_namespace_prefix = name_space_prefix


                        class Flooding(Entity):
                            """
                            Flooding configurations.
                            
                            .. attribute:: disabled
                            
                            	Disable flooding
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: disabled_unknown_unicast
                            
                            	Disable unknown unicast flooding
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding, self).__init__()

                                self.yang_name = "flooding"
                                self.yang_parent_name = "pw-neighbor-spec"

                                self.disabled = YLeaf(YType.empty, "disabled")

                                self.disabled_unknown_unicast = YLeaf(YType.empty, "disabled-unknown-unicast")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("disabled",
                                                "disabled_unknown_unicast") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.disabled.is_set or
                                    self.disabled_unknown_unicast.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.disabled.yfilter != YFilter.not_set or
                                    self.disabled_unknown_unicast.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "flooding" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disabled.get_name_leafdata())
                                if (self.disabled_unknown_unicast.is_set or self.disabled_unknown_unicast.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.disabled_unknown_unicast.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "disabled" or name == "disabled-unknown-unicast"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "disabled"):
                                    self.disabled = value
                                    self.disabled.value_namespace = name_space
                                    self.disabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "disabled-unknown-unicast"):
                                    self.disabled_unknown_unicast = value
                                    self.disabled_unknown_unicast.value_namespace = name_space
                                    self.disabled_unknown_unicast.value_namespace_prefix = name_space_prefix


                        class StormControl(Entity):
                            """
                            A collection of storm control threshold and action
                            configurations.
                            
                            .. attribute:: action
                            
                            	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                            	**type**\:   :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                            
                            .. attribute:: thresholds
                            
                            	A collection of storm control threshold configuration entries
                            	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl, self).__init__()

                                self.yang_name = "storm-control"
                                self.yang_parent_name = "pw-neighbor-spec"

                                self.action = YLeaf(YType.identityref, "action")

                                self.thresholds = YList(self)

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("action") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl, self).__setattr__(name, value)


                            class Thresholds(Entity):
                                """
                                A collection of storm control threshold configuration
                                entries.
                                
                                .. attribute:: traffic_class  <key>
                                
                                	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                                	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                                
                                .. attribute:: unit
                                
                                	This enumeration define unit of the traffic threshold value
                                	**type**\:   :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.Unit>`
                                
                                	**mandatory**\: True
                                
                                .. attribute:: value
                                
                                	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds, self).__init__()

                                    self.yang_name = "thresholds"
                                    self.yang_parent_name = "storm-control"

                                    self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                                    self.unit = YLeaf(YType.enumeration, "unit")

                                    self.value = YLeaf(YType.uint32, "value")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("traffic_class",
                                                    "unit",
                                                    "value") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds, self).__setattr__(name, value)

                                class Unit(Enum):
                                    """
                                    Unit

                                    This enumeration define unit of the traffic threshold

                                    value.

                                    .. data:: bps = 0

                                    	Bits per second.

                                    .. data:: kbps = 1

                                    	Kilobits per second.

                                    .. data:: pps = 2

                                    	Packets per seconds.

                                    """

                                    bps = Enum.YLeaf(0, "bps")

                                    kbps = Enum.YLeaf(1, "kbps")

                                    pps = Enum.YLeaf(2, "pps")


                                def has_data(self):
                                    return (
                                        self.traffic_class.is_set or
                                        self.unit.is_set or
                                        self.value.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.traffic_class.yfilter != YFilter.not_set or
                                        self.unit.yfilter != YFilter.not_set or
                                        self.value.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "thresholds" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.traffic_class.get_name_leafdata())
                                    if (self.unit.is_set or self.unit.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.unit.get_name_leafdata())
                                    if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.value.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "traffic-class" or name == "unit" or name == "value"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "traffic-class"):
                                        self.traffic_class = value
                                        self.traffic_class.value_namespace = name_space
                                        self.traffic_class.value_namespace_prefix = name_space_prefix
                                    if(value_path == "unit"):
                                        self.unit = value
                                        self.unit.value_namespace = name_space
                                        self.unit.value_namespace_prefix = name_space_prefix
                                    if(value_path == "value"):
                                        self.value = value
                                        self.value.value_namespace = name_space
                                        self.value.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                for c in self.thresholds:
                                    if (c.has_data()):
                                        return True
                                return self.action.is_set

                            def has_operation(self):
                                for c in self.thresholds:
                                    if (c.has_operation()):
                                        return True
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.action.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "storm-control" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.action.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "thresholds"):
                                    for c in self.thresholds:
                                        segment = c.get_segment_path()
                                        if (segment_path == segment):
                                            return c
                                    c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds()
                                    c.parent = self
                                    local_reference_key = "ydk::seg::%s" % segment_path
                                    self._local_refs[local_reference_key] = c
                                    self.thresholds.append(c)
                                    return c

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "thresholds" or name == "action"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "action"):
                                    self.action = value
                                    self.action.value_namespace = name_space
                                    self.action.value_namespace_prefix = name_space_prefix


                        class Backup(Entity):
                            """
                            Backup pseudo\-wire.
                            
                            .. attribute:: neighbor_ip_address
                            
                            	IPv4 or IPv6 address of the neighbor
                            	**type**\: one of the below types:
                            
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            
                            ----
                            .. attribute:: pw_class_template
                            
                            	Reference to a pseudowire template
                            	**type**\:  str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
                            
                            .. attribute:: vc_id
                            
                            	Pseudowire VC ID
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup, self).__init__()

                                self.yang_name = "backup"
                                self.yang_parent_name = "pw-neighbor-spec"

                                self.neighbor_ip_address = YLeaf(YType.str, "neighbor-ip-address")

                                self.pw_class_template = YLeaf(YType.str, "pw-class-template")

                                self.vc_id = YLeaf(YType.uint32, "vc-id")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("neighbor_ip_address",
                                                "pw_class_template",
                                                "vc_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.neighbor_ip_address.is_set or
                                    self.pw_class_template.is_set or
                                    self.vc_id.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.neighbor_ip_address.yfilter != YFilter.not_set or
                                    self.pw_class_template.yfilter != YFilter.not_set or
                                    self.vc_id.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "backup" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.neighbor_ip_address.is_set or self.neighbor_ip_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.neighbor_ip_address.get_name_leafdata())
                                if (self.pw_class_template.is_set or self.pw_class_template.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pw_class_template.get_name_leafdata())
                                if (self.vc_id.is_set or self.vc_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vc_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "neighbor-ip-address" or name == "pw-class-template" or name == "vc-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "neighbor-ip-address"):
                                    self.neighbor_ip_address = value
                                    self.neighbor_ip_address.value_namespace = name_space
                                    self.neighbor_ip_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "pw-class-template"):
                                    self.pw_class_template = value
                                    self.pw_class_template.value_namespace = name_space
                                    self.pw_class_template.value_namespace_prefix = name_space_prefix
                                if(value_path == "vc-id"):
                                    self.vc_id = value
                                    self.vc_id.value_namespace = name_space
                                    self.vc_id.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.neighbor_ip_address.is_set or
                                self.vc_id.is_set or
                                self.encap_type.is_set or
                                self.pw_class_template.is_set or
                                self.source_ipv6.is_set or
                                self.tag_impose_vlan.is_set or
                                (self.backup is not None and self.backup.has_data()) or
                                (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_data()) or
                                (self.flooding is not None and self.flooding.has_data()) or
                                (self.igmp_snooping is not None and self.igmp_snooping.has_data()) or
                                (self.mac is not None and self.mac.has_data()) or
                                (self.mld_snooping is not None and self.mld_snooping.has_data()) or
                                (self.static_label is not None and self.static_label.has_data()) or
                                (self.storm_control is not None and self.storm_control.has_data()) or
                                (self.split_horizon_group is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.neighbor_ip_address.yfilter != YFilter.not_set or
                                self.vc_id.yfilter != YFilter.not_set or
                                self.encap_type.yfilter != YFilter.not_set or
                                self.pw_class_template.yfilter != YFilter.not_set or
                                self.source_ipv6.yfilter != YFilter.not_set or
                                self.tag_impose_vlan.yfilter != YFilter.not_set or
                                (self.backup is not None and self.backup.has_operation()) or
                                (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_operation()) or
                                (self.flooding is not None and self.flooding.has_operation()) or
                                (self.igmp_snooping is not None and self.igmp_snooping.has_operation()) or
                                (self.mac is not None and self.mac.has_operation()) or
                                (self.mld_snooping is not None and self.mld_snooping.has_operation()) or
                                (self.split_horizon_group is not None and self.split_horizon_group.has_operation()) or
                                (self.static_label is not None and self.static_label.has_operation()) or
                                (self.storm_control is not None and self.storm_control.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pw-neighbor-spec" + "[neighbor-ip-address='" + self.neighbor_ip_address.get() + "']" + "[vc-id='" + self.vc_id.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.neighbor_ip_address.is_set or self.neighbor_ip_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.neighbor_ip_address.get_name_leafdata())
                            if (self.vc_id.is_set or self.vc_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vc_id.get_name_leafdata())
                            if (self.encap_type.is_set or self.encap_type.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.encap_type.get_name_leafdata())
                            if (self.pw_class_template.is_set or self.pw_class_template.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pw_class_template.get_name_leafdata())
                            if (self.source_ipv6.is_set or self.source_ipv6.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.source_ipv6.get_name_leafdata())
                            if (self.tag_impose_vlan.is_set or self.tag_impose_vlan.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.tag_impose_vlan.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "backup"):
                                if (self.backup is None):
                                    self.backup = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup()
                                    self.backup.parent = self
                                    self._children_name_map["backup"] = "backup"
                                return self.backup

                            if (child_yang_name == "dhcp-ipv4-snooping"):
                                if (self.dhcp_ipv4_snooping is None):
                                    self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping()
                                    self.dhcp_ipv4_snooping.parent = self
                                    self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                                return self.dhcp_ipv4_snooping

                            if (child_yang_name == "flooding"):
                                if (self.flooding is None):
                                    self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding()
                                    self.flooding.parent = self
                                    self._children_name_map["flooding"] = "flooding"
                                return self.flooding

                            if (child_yang_name == "igmp-snooping"):
                                if (self.igmp_snooping is None):
                                    self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping()
                                    self.igmp_snooping.parent = self
                                    self._children_name_map["igmp_snooping"] = "igmp-snooping"
                                return self.igmp_snooping

                            if (child_yang_name == "mac"):
                                if (self.mac is None):
                                    self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac()
                                    self.mac.parent = self
                                    self._children_name_map["mac"] = "mac"
                                return self.mac

                            if (child_yang_name == "mld-snooping"):
                                if (self.mld_snooping is None):
                                    self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping()
                                    self.mld_snooping.parent = self
                                    self._children_name_map["mld_snooping"] = "mld-snooping"
                                return self.mld_snooping

                            if (child_yang_name == "split-horizon-group"):
                                if (self.split_horizon_group is None):
                                    self.split_horizon_group = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup()
                                    self.split_horizon_group.parent = self
                                    self._children_name_map["split_horizon_group"] = "split-horizon-group"
                                return self.split_horizon_group

                            if (child_yang_name == "static-label"):
                                if (self.static_label is None):
                                    self.static_label = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel()
                                    self.static_label.parent = self
                                    self._children_name_map["static_label"] = "static-label"
                                return self.static_label

                            if (child_yang_name == "storm-control"):
                                if (self.storm_control is None):
                                    self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl()
                                    self.storm_control.parent = self
                                    self._children_name_map["storm_control"] = "storm-control"
                                return self.storm_control

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "backup" or name == "dhcp-ipv4-snooping" or name == "flooding" or name == "igmp-snooping" or name == "mac" or name == "mld-snooping" or name == "split-horizon-group" or name == "static-label" or name == "storm-control" or name == "neighbor-ip-address" or name == "vc-id" or name == "encap-type" or name == "pw-class-template" or name == "source-ipv6" or name == "tag-impose-vlan"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "neighbor-ip-address"):
                                self.neighbor_ip_address = value
                                self.neighbor_ip_address.value_namespace = name_space
                                self.neighbor_ip_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vc-id"):
                                self.vc_id = value
                                self.vc_id.value_namespace = name_space
                                self.vc_id.value_namespace_prefix = name_space_prefix
                            if(value_path == "encap-type"):
                                self.encap_type = value
                                self.encap_type.value_namespace = name_space
                                self.encap_type.value_namespace_prefix = name_space_prefix
                            if(value_path == "pw-class-template"):
                                self.pw_class_template = value
                                self.pw_class_template.value_namespace = name_space
                                self.pw_class_template.value_namespace_prefix = name_space_prefix
                            if(value_path == "source-ipv6"):
                                self.source_ipv6 = value
                                self.source_ipv6.value_namespace = name_space
                                self.source_ipv6.value_namespace_prefix = name_space_prefix
                            if(value_path == "tag-impose-vlan"):
                                self.tag_impose_vlan = value
                                self.tag_impose_vlan.value_namespace = name_space
                                self.tag_impose_vlan.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.access_pw_if_member:
                            if (c.has_data()):
                                return True
                        for c in self.pw_neighbor_spec:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.access_pw_if_member:
                            if (c.has_operation()):
                                return True
                        for c in self.pw_neighbor_spec:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-pw-member" + path_buffer

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

                        if (child_yang_name == "access-pw-if-member"):
                            for c in self.access_pw_if_member:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.access_pw_if_member.append(c)
                            return c

                        if (child_yang_name == "pw-neighbor-spec"):
                            for c in self.pw_neighbor_spec:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.pw_neighbor_spec.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "access-pw-if-member" or name == "pw-neighbor-spec"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    for c in self.ac_member:
                        if (c.has_data()):
                            return True
                    for c in self.vfi_member:
                        if (c.has_data()):
                            return True
                    return (self.access_pw_member is not None and self.access_pw_member.has_data())

                def has_operation(self):
                    for c in self.ac_member:
                        if (c.has_operation()):
                            return True
                    for c in self.vfi_member:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.access_pw_member is not None and self.access_pw_member.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "members" + path_buffer

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

                    if (child_yang_name == "ac-member"):
                        for c in self.ac_member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ac_member.append(c)
                        return c

                    if (child_yang_name == "access-pw-member"):
                        if (self.access_pw_member is None):
                            self.access_pw_member = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember()
                            self.access_pw_member.parent = self
                            self._children_name_map["access_pw_member"] = "access-pw-member"
                        return self.access_pw_member

                    if (child_yang_name == "vfi-member"):
                        for c in self.vfi_member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vfi_member.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ac-member" or name == "access-pw-member" or name == "vfi-member"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Mac(Entity):
                """
                MAC features for bridge domain.
                
                .. attribute:: aging
                
                	MAC aging configurations
                	**type**\:   :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging>`
                
                .. attribute:: flooding
                
                	Flooding configurations
                	**type**\:   :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding>`
                
                .. attribute:: learning_enabled
                
                	Enable disable mac learning
                	**type**\:  bool
                
                	**default value**\: true
                
                .. attribute:: limit
                
                	MAC table learning limit
                	**type**\:   :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit>`
                
                .. attribute:: port_down
                
                	Port down event
                	**type**\:   :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown>`
                
                .. attribute:: secure
                
                	MAC secure parameters
                	**type**\:   :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure>`
                
                	**presence node**\: True
                
                .. attribute:: static
                
                	Static mac address list parameters
                	**type**\:   :py:class:`Static <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac, self).__init__()

                    self.yang_name = "mac"
                    self.yang_parent_name = "bridge-domain"

                    self.learning_enabled = YLeaf(YType.boolean, "learning-enabled")

                    self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging()
                    self.aging.parent = self
                    self._children_name_map["aging"] = "aging"
                    self._children_yang_names.add("aging")

                    self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding()
                    self.flooding.parent = self
                    self._children_name_map["flooding"] = "flooding"
                    self._children_yang_names.add("flooding")

                    self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit()
                    self.limit.parent = self
                    self._children_name_map["limit"] = "limit"
                    self._children_yang_names.add("limit")

                    self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown()
                    self.port_down.parent = self
                    self._children_name_map["port_down"] = "port-down"
                    self._children_yang_names.add("port-down")

                    self.secure = None
                    self._children_name_map["secure"] = "secure"
                    self._children_yang_names.add("secure")

                    self.static = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static()
                    self.static.parent = self
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("learning_enabled") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac, self).__setattr__(name, value)


                class Limit(Entity):
                    """
                    MAC table learning limit.
                    
                    .. attribute:: action
                    
                    	MAC limit violation actions
                    	**type**\:   :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                    
                    .. attribute:: maximum
                    
                    	Maximum number of mac addresses that can be learnt
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification
                    
                    	MAC limit violation notifications
                    	**type**\:   :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit, self).__init__()

                        self.yang_name = "limit"
                        self.yang_parent_name = "mac"

                        self.action = YLeaf(YType.enumeration, "action")

                        self.maximum = YLeaf(YType.uint32, "maximum")

                        self.notification = YLeaf(YType.identityref, "notification")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("action",
                                        "maximum",
                                        "notification") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.action.is_set or
                            self.maximum.is_set or
                            self.notification.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.action.yfilter != YFilter.not_set or
                            self.maximum.yfilter != YFilter.not_set or
                            self.notification.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.action.get_name_leafdata())
                        if (self.maximum.is_set or self.maximum.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.maximum.get_name_leafdata())
                        if (self.notification.is_set or self.notification.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.notification.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "action" or name == "maximum" or name == "notification"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "action"):
                            self.action = value
                            self.action.value_namespace = name_space
                            self.action.value_namespace_prefix = name_space_prefix
                        if(value_path == "maximum"):
                            self.maximum = value
                            self.maximum.value_namespace = name_space
                            self.maximum.value_namespace_prefix = name_space_prefix
                        if(value_path == "notification"):
                            self.notification = value
                            self.notification.value_namespace = name_space
                            self.notification.value_namespace_prefix = name_space_prefix


                class Aging(Entity):
                    """
                    MAC aging configurations.
                    
                    .. attribute:: time
                    
                    	The timeout period in seconds for aging out dynamically learned forwarding information
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    	**default value**\: 300
                    
                    .. attribute:: type
                    
                    	MAC aging type
                    	**type**\:   :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging, self).__init__()

                        self.yang_name = "aging"
                        self.yang_parent_name = "mac"

                        self.time = YLeaf(YType.uint32, "time")

                        self.type = YLeaf(YType.enumeration, "type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("time",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.time.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.time.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "aging" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.time.is_set or self.time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.time.get_name_leafdata())
                        if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.type.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "time" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "time"):
                            self.time = value
                            self.time.value_namespace = name_space
                            self.time.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix


                class PortDown(Entity):
                    """
                    Port down event
                    
                    .. attribute:: flush
                    
                    	Enable/Disable mac table flush when port moves to down state
                    	**type**\:  bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown, self).__init__()

                        self.yang_name = "port-down"
                        self.yang_parent_name = "mac"

                        self.flush = YLeaf(YType.boolean, "flush")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("flush") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown, self).__setattr__(name, value)

                    def has_data(self):
                        return self.flush.is_set

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.flush.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "port-down" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.flush.is_set or self.flush.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flush.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flush"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "flush"):
                            self.flush = value
                            self.flush.value_namespace = name_space
                            self.flush.value_namespace_prefix = name_space_prefix


                class Flooding(Entity):
                    """
                    Flooding configurations.
                    
                    .. attribute:: disabled
                    
                    	Disable flooding
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disabled_unknown_unicast
                    
                    	Disable unknown unicast flooding
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding, self).__init__()

                        self.yang_name = "flooding"
                        self.yang_parent_name = "mac"

                        self.disabled = YLeaf(YType.empty, "disabled")

                        self.disabled_unknown_unicast = YLeaf(YType.empty, "disabled-unknown-unicast")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("disabled",
                                        "disabled_unknown_unicast") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.disabled.is_set or
                            self.disabled_unknown_unicast.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.disabled.yfilter != YFilter.not_set or
                            self.disabled_unknown_unicast.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flooding" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disabled.get_name_leafdata())
                        if (self.disabled_unknown_unicast.is_set or self.disabled_unknown_unicast.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.disabled_unknown_unicast.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "disabled" or name == "disabled-unknown-unicast"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "disabled"):
                            self.disabled = value
                            self.disabled.value_namespace = name_space
                            self.disabled.value_namespace_prefix = name_space_prefix
                        if(value_path == "disabled-unknown-unicast"):
                            self.disabled_unknown_unicast = value
                            self.disabled_unknown_unicast.value_namespace = name_space
                            self.disabled_unknown_unicast.value_namespace_prefix = name_space_prefix


                class Secure(Entity):
                    """
                    MAC secure parameters.
                    
                    .. attribute:: action
                    
                    	MAC secure action for violating packets
                    	**type**\:   :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                    
                    	**default value**\: restrict
                    
                    .. attribute:: logging
                    
                    	Enable/Disable logging
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure, self).__init__()

                        self.yang_name = "secure"
                        self.yang_parent_name = "mac"
                        self.is_presence_container = True

                        self.action = YLeaf(YType.enumeration, "action")

                        self.logging = YLeaf(YType.boolean, "logging")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("action",
                                        "logging") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.action.is_set or
                            self.logging.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.action.yfilter != YFilter.not_set or
                            self.logging.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "secure" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.action.get_name_leafdata())
                        if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.logging.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "action" or name == "logging"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "action"):
                            self.action = value
                            self.action.value_namespace = name_space
                            self.action.value_namespace_prefix = name_space_prefix
                        if(value_path == "logging"):
                            self.logging = value
                            self.logging.value_namespace = name_space
                            self.logging.value_namespace_prefix = name_space_prefix


                class Static(Entity):
                    """
                    Static mac address list parameters.
                    
                    .. attribute:: mac_addresses
                    
                    	MAC address entry
                    	**type**\: list of    :py:class:`MacAddresses <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "mac"

                        self.mac_addresses = YList(self)

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
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static, self).__setattr__(name, value)


                    class MacAddresses(Entity):
                        """
                        MAC address entry.
                        
                        .. attribute:: mac_addr  <key>
                        
                        	Static MAC address
                        	**type**\:  str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: drop
                        
                        	Drop packet
                        	**type**\:  bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses, self).__init__()

                            self.yang_name = "mac-addresses"
                            self.yang_parent_name = "static"

                            self.mac_addr = YLeaf(YType.str, "mac-addr")

                            self.drop = YLeaf(YType.boolean, "drop")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("mac_addr",
                                            "drop") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.mac_addr.is_set or
                                self.drop.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.mac_addr.yfilter != YFilter.not_set or
                                self.drop.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "mac-addresses" + "[mac-addr='" + self.mac_addr.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.mac_addr.is_set or self.mac_addr.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mac_addr.get_name_leafdata())
                            if (self.drop.is_set or self.drop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drop.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "mac-addr" or name == "drop"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "mac-addr"):
                                self.mac_addr = value
                                self.mac_addr.value_namespace = name_space
                                self.mac_addr.value_namespace_prefix = name_space_prefix
                            if(value_path == "drop"):
                                self.drop = value
                                self.drop.value_namespace = name_space
                                self.drop.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.mac_addresses:
                            if (c.has_data()):
                                return True
                        return False

                    def has_operation(self):
                        for c in self.mac_addresses:
                            if (c.has_operation()):
                                return True
                        return self.yfilter != YFilter.not_set

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "static" + path_buffer

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

                        if (child_yang_name == "mac-addresses"):
                            for c in self.mac_addresses:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.mac_addresses.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "mac-addresses"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass

                def has_data(self):
                    return (
                        self.learning_enabled.is_set or
                        (self.aging is not None and self.aging.has_data()) or
                        (self.flooding is not None and self.flooding.has_data()) or
                        (self.limit is not None and self.limit.has_data()) or
                        (self.port_down is not None and self.port_down.has_data()) or
                        (self.static is not None and self.static.has_data()) or
                        (self.secure is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.learning_enabled.yfilter != YFilter.not_set or
                        (self.aging is not None and self.aging.has_operation()) or
                        (self.flooding is not None and self.flooding.has_operation()) or
                        (self.limit is not None and self.limit.has_operation()) or
                        (self.port_down is not None and self.port_down.has_operation()) or
                        (self.secure is not None and self.secure.has_operation()) or
                        (self.static is not None and self.static.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mac" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.learning_enabled.is_set or self.learning_enabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.learning_enabled.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "aging"):
                        if (self.aging is None):
                            self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging()
                            self.aging.parent = self
                            self._children_name_map["aging"] = "aging"
                        return self.aging

                    if (child_yang_name == "flooding"):
                        if (self.flooding is None):
                            self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding()
                            self.flooding.parent = self
                            self._children_name_map["flooding"] = "flooding"
                        return self.flooding

                    if (child_yang_name == "limit"):
                        if (self.limit is None):
                            self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit()
                            self.limit.parent = self
                            self._children_name_map["limit"] = "limit"
                        return self.limit

                    if (child_yang_name == "port-down"):
                        if (self.port_down is None):
                            self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown()
                            self.port_down.parent = self
                            self._children_name_map["port_down"] = "port-down"
                        return self.port_down

                    if (child_yang_name == "secure"):
                        if (self.secure is None):
                            self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure()
                            self.secure.parent = self
                            self._children_name_map["secure"] = "secure"
                        return self.secure

                    if (child_yang_name == "static"):
                        if (self.static is None):
                            self.static = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static()
                            self.static.parent = self
                            self._children_name_map["static"] = "static"
                        return self.static

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "aging" or name == "flooding" or name == "limit" or name == "port-down" or name == "secure" or name == "static" or name == "learning-enabled"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "learning-enabled"):
                        self.learning_enabled = value
                        self.learning_enabled.value_namespace = name_space
                        self.learning_enabled.value_namespace_prefix = name_space_prefix


            class DynamicArpInspection(Entity):
                """
                Dynamic ARP Inspection (DAI) configurations.
                
                .. attribute:: address_validation
                
                	Enable address validation
                	**type**\:   :py:class:`AddressValidation <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation>`
                
                	**presence node**\: True
                
                .. attribute:: logging
                
                	Enable DAI logging
                	**type**\:  bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection, self).__init__()

                    self.yang_name = "dynamic-arp-inspection"
                    self.yang_parent_name = "bridge-domain"
                    self.is_presence_container = True

                    self.logging = YLeaf(YType.boolean, "logging")

                    self.address_validation = None
                    self._children_name_map["address_validation"] = "address-validation"
                    self._children_yang_names.add("address-validation")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("logging") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection, self).__setattr__(name, value)


                class AddressValidation(Entity):
                    """
                    Enable address validation.
                    
                    .. attribute:: dst_mac
                    
                    	Match Destination MAC Address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: ipv4
                    
                    	Match IPv4 Address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: src_mac
                    
                    	Match Source MAC Address
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation, self).__init__()

                        self.yang_name = "address-validation"
                        self.yang_parent_name = "dynamic-arp-inspection"
                        self.is_presence_container = True

                        self.dst_mac = YLeaf(YType.empty, "dst-mac")

                        self.ipv4 = YLeaf(YType.empty, "ipv4")

                        self.src_mac = YLeaf(YType.empty, "src-mac")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("dst_mac",
                                        "ipv4",
                                        "src_mac") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.dst_mac.is_set or
                            self.ipv4.is_set or
                            self.src_mac.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.dst_mac.yfilter != YFilter.not_set or
                            self.ipv4.yfilter != YFilter.not_set or
                            self.src_mac.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "address-validation" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.dst_mac.is_set or self.dst_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dst_mac.get_name_leafdata())
                        if (self.ipv4.is_set or self.ipv4.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ipv4.get_name_leafdata())
                        if (self.src_mac.is_set or self.src_mac.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.src_mac.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dst-mac" or name == "ipv4" or name == "src-mac"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "dst-mac"):
                            self.dst_mac = value
                            self.dst_mac.value_namespace = name_space
                            self.dst_mac.value_namespace_prefix = name_space_prefix
                        if(value_path == "ipv4"):
                            self.ipv4 = value
                            self.ipv4.value_namespace = name_space
                            self.ipv4.value_namespace_prefix = name_space_prefix
                        if(value_path == "src-mac"):
                            self.src_mac = value
                            self.src_mac.value_namespace = name_space
                            self.src_mac.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.logging.is_set or
                        (self.address_validation is not None))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.logging.yfilter != YFilter.not_set or
                        (self.address_validation is not None and self.address_validation.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dynamic-arp-inspection" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logging.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "address-validation"):
                        if (self.address_validation is None):
                            self.address_validation = BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation()
                            self.address_validation.parent = self
                            self._children_name_map["address_validation"] = "address-validation"
                        return self.address_validation

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "address-validation" or name == "logging"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "logging"):
                        self.logging = value
                        self.logging.value_namespace = name_space
                        self.logging.value_namespace_prefix = name_space_prefix


            class IpSourceGuard(Entity):
                """
                IP source guard (IPSG) configurations.
                
                .. attribute:: logging
                
                	Enable IPSG logging
                	**type**\:  bool
                
                	**default value**\: false
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard, self).__init__()

                    self.yang_name = "ip-source-guard"
                    self.yang_parent_name = "bridge-domain"
                    self.is_presence_container = True

                    self.logging = YLeaf(YType.boolean, "logging")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("logging") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard, self).__setattr__(name, value)

                def has_data(self):
                    return self.logging.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.logging.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "ip-source-guard" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.logging.is_set or self.logging.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.logging.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "logging"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "logging"):
                        self.logging = value
                        self.logging.value_namespace = name_space
                        self.logging.value_namespace_prefix = name_space_prefix


            class StormControl(Entity):
                """
                A collection of storm control threshold and action
                configurations.
                
                .. attribute:: action
                
                	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                	**type**\:   :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                
                .. attribute:: thresholds
                
                	A collection of storm control threshold configuration entries
                	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl, self).__init__()

                    self.yang_name = "storm-control"
                    self.yang_parent_name = "bridge-domain"

                    self.action = YLeaf(YType.identityref, "action")

                    self.thresholds = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("action") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl, self).__setattr__(name, value)


                class Thresholds(Entity):
                    """
                    A collection of storm control threshold configuration
                    entries.
                    
                    .. attribute:: traffic_class  <key>
                    
                    	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                    	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                    
                    .. attribute:: unit
                    
                    	This enumeration define unit of the traffic threshold value
                    	**type**\:   :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.Unit>`
                    
                    	**mandatory**\: True
                    
                    .. attribute:: value
                    
                    	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds, self).__init__()

                        self.yang_name = "thresholds"
                        self.yang_parent_name = "storm-control"

                        self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                        self.unit = YLeaf(YType.enumeration, "unit")

                        self.value = YLeaf(YType.uint32, "value")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("traffic_class",
                                        "unit",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds, self).__setattr__(name, value)

                    class Unit(Enum):
                        """
                        Unit

                        This enumeration define unit of the traffic threshold

                        value.

                        .. data:: bps = 0

                        	Bits per second.

                        .. data:: kbps = 1

                        	Kilobits per second.

                        .. data:: pps = 2

                        	Packets per seconds.

                        """

                        bps = Enum.YLeaf(0, "bps")

                        kbps = Enum.YLeaf(1, "kbps")

                        pps = Enum.YLeaf(2, "pps")


                    def has_data(self):
                        return (
                            self.traffic_class.is_set or
                            self.unit.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.traffic_class.yfilter != YFilter.not_set or
                            self.unit.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "thresholds" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_class.get_name_leafdata())
                        if (self.unit.is_set or self.unit.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.unit.get_name_leafdata())
                        if (self.value.is_set or self.value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "traffic-class" or name == "unit" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "traffic-class"):
                            self.traffic_class = value
                            self.traffic_class.value_namespace = name_space
                            self.traffic_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "unit"):
                            self.unit = value
                            self.unit.value_namespace = name_space
                            self.unit.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.thresholds:
                        if (c.has_data()):
                            return True
                    return self.action.is_set

                def has_operation(self):
                    for c in self.thresholds:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.action.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "storm-control" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.action.is_set or self.action.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.action.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "thresholds"):
                        for c in self.thresholds:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.thresholds.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "thresholds" or name == "action"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "action"):
                        self.action = value
                        self.action.value_namespace = name_space
                        self.action.value_namespace_prefix = name_space_prefix


            class IgmpSnooping(Entity):
                """
                Enable IGMP snooping.
                
                .. attribute:: disabled
                
                	Disable IGMP snooping
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: profile_name
                
                	IGMP snooping profile name
                	**type**\:  str
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping, self).__init__()

                    self.yang_name = "igmp-snooping"
                    self.yang_parent_name = "bridge-domain"

                    self.disabled = YLeaf(YType.empty, "disabled")

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
                        if name in ("disabled",
                                    "profile_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.disabled.is_set or
                        self.profile_name.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.disabled.yfilter != YFilter.not_set or
                        self.profile_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "igmp-snooping" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.disabled.is_set or self.disabled.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.disabled.get_name_leafdata())
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
                    if(name == "disabled" or name == "profile-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "disabled"):
                        self.disabled = value
                        self.disabled.value_namespace = name_space
                        self.disabled.value_namespace_prefix = name_space_prefix
                    if(value_path == "profile-name"):
                        self.profile_name = value
                        self.profile_name.value_namespace = name_space
                        self.profile_name.value_namespace_prefix = name_space_prefix


            class MldSnooping(Entity):
                """
                Enable MLD snooping
                
                .. attribute:: profile_name
                
                	MLD snooping profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping, self).__init__()

                    self.yang_name = "mld-snooping"
                    self.yang_parent_name = "bridge-domain"

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
                        if name in ("profile_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "mld-snooping" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile-name"):
                        self.profile_name = value
                        self.profile_name.value_namespace = name_space
                        self.profile_name.value_namespace_prefix = name_space_prefix


            class DhcpIpv4Snooping(Entity):
                """
                Enable DHCP IPv4 snooping.
                
                .. attribute:: profile_name
                
                	DHCPv4 snooping profile name
                	**type**\:  str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping, self).__init__()

                    self.yang_name = "dhcp-ipv4-snooping"
                    self.yang_parent_name = "bridge-domain"

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
                        if name in ("profile_name") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping, self).__setattr__(name, value)

                def has_data(self):
                    return self.profile_name.is_set

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.profile_name.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "dhcp-ipv4-snooping" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
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

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "profile-name"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "profile-name"):
                        self.profile_name = value
                        self.profile_name.value_namespace = name_space
                        self.profile_name.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.id.is_set or
                    self.bd_status_change_notification.is_set or
                    self.bridge_group.is_set or
                    self.enabled.is_set or
                    self.flooding_mode.is_set or
                    self.mtu.is_set or
                    (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_data()) or
                    (self.igmp_snooping is not None and self.igmp_snooping.has_data()) or
                    (self.mac is not None and self.mac.has_data()) or
                    (self.members is not None and self.members.has_data()) or
                    (self.mld_snooping is not None and self.mld_snooping.has_data()) or
                    (self.storm_control is not None and self.storm_control.has_data()) or
                    (self.dynamic_arp_inspection is not None) or
                    (self.ip_source_guard is not None))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    self.bd_status_change_notification.yfilter != YFilter.not_set or
                    self.bridge_group.yfilter != YFilter.not_set or
                    self.enabled.yfilter != YFilter.not_set or
                    self.flooding_mode.yfilter != YFilter.not_set or
                    self.mtu.yfilter != YFilter.not_set or
                    (self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping.has_operation()) or
                    (self.dynamic_arp_inspection is not None and self.dynamic_arp_inspection.has_operation()) or
                    (self.igmp_snooping is not None and self.igmp_snooping.has_operation()) or
                    (self.ip_source_guard is not None and self.ip_source_guard.has_operation()) or
                    (self.mac is not None and self.mac.has_operation()) or
                    (self.members is not None and self.members.has_operation()) or
                    (self.mld_snooping is not None and self.mld_snooping.has_operation()) or
                    (self.storm_control is not None and self.storm_control.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bridge-domain" + "[id='" + self.id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:bridge-domain-config/bridge-domains/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())
                if (self.bd_status_change_notification.is_set or self.bd_status_change_notification.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bd_status_change_notification.get_name_leafdata())
                if (self.bridge_group.is_set or self.bridge_group.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bridge_group.get_name_leafdata())
                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.enabled.get_name_leafdata())
                if (self.flooding_mode.is_set or self.flooding_mode.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.flooding_mode.get_name_leafdata())
                if (self.mtu.is_set or self.mtu.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mtu.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "dhcp-ipv4-snooping"):
                    if (self.dhcp_ipv4_snooping is None):
                        self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping()
                        self.dhcp_ipv4_snooping.parent = self
                        self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                    return self.dhcp_ipv4_snooping

                if (child_yang_name == "dynamic-arp-inspection"):
                    if (self.dynamic_arp_inspection is None):
                        self.dynamic_arp_inspection = BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection()
                        self.dynamic_arp_inspection.parent = self
                        self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                    return self.dynamic_arp_inspection

                if (child_yang_name == "igmp-snooping"):
                    if (self.igmp_snooping is None):
                        self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping()
                        self.igmp_snooping.parent = self
                        self._children_name_map["igmp_snooping"] = "igmp-snooping"
                    return self.igmp_snooping

                if (child_yang_name == "ip-source-guard"):
                    if (self.ip_source_guard is None):
                        self.ip_source_guard = BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard()
                        self.ip_source_guard.parent = self
                        self._children_name_map["ip_source_guard"] = "ip-source-guard"
                    return self.ip_source_guard

                if (child_yang_name == "mac"):
                    if (self.mac is None):
                        self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                    return self.mac

                if (child_yang_name == "members"):
                    if (self.members is None):
                        self.members = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members()
                        self.members.parent = self
                        self._children_name_map["members"] = "members"
                    return self.members

                if (child_yang_name == "mld-snooping"):
                    if (self.mld_snooping is None):
                        self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping()
                        self.mld_snooping.parent = self
                        self._children_name_map["mld_snooping"] = "mld-snooping"
                    return self.mld_snooping

                if (child_yang_name == "storm-control"):
                    if (self.storm_control is None):
                        self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl()
                        self.storm_control.parent = self
                        self._children_name_map["storm_control"] = "storm-control"
                    return self.storm_control

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "dhcp-ipv4-snooping" or name == "dynamic-arp-inspection" or name == "igmp-snooping" or name == "ip-source-guard" or name == "mac" or name == "members" or name == "mld-snooping" or name == "storm-control" or name == "id" or name == "bd-status-change-notification" or name == "bridge-group" or name == "enabled" or name == "flooding-mode" or name == "mtu"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix
                if(value_path == "bd-status-change-notification"):
                    self.bd_status_change_notification = value
                    self.bd_status_change_notification.value_namespace = name_space
                    self.bd_status_change_notification.value_namespace_prefix = name_space_prefix
                if(value_path == "bridge-group"):
                    self.bridge_group = value
                    self.bridge_group.value_namespace = name_space
                    self.bridge_group.value_namespace_prefix = name_space_prefix
                if(value_path == "enabled"):
                    self.enabled = value
                    self.enabled.value_namespace = name_space
                    self.enabled.value_namespace_prefix = name_space_prefix
                if(value_path == "flooding-mode"):
                    self.flooding_mode = value
                    self.flooding_mode.value_namespace = name_space
                    self.flooding_mode.value_namespace_prefix = name_space_prefix
                if(value_path == "mtu"):
                    self.mtu = value
                    self.mtu.value_namespace = name_space
                    self.mtu.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bridge_domain:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bridge_domain:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bridge-domains" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-config/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bridge-domain"):
                for c in self.bridge_domain:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeDomainConfig.BridgeDomains.BridgeDomain()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bridge_domain.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bridge-domain"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.bridge_domains is not None and self.bridge_domains.has_data()) or
            (self.bridge_groups is not None and self.bridge_groups.has_data()) or
            (self.global_ is not None and self.global_.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.bridge_domains is not None and self.bridge_domains.has_operation()) or
            (self.bridge_groups is not None and self.bridge_groups.has_operation()) or
            (self.global_ is not None and self.global_.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-bridge-domain:bridge-domain-config" + path_buffer

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

        if (child_yang_name == "bridge-domains"):
            if (self.bridge_domains is None):
                self.bridge_domains = BridgeDomainConfig.BridgeDomains()
                self.bridge_domains.parent = self
                self._children_name_map["bridge_domains"] = "bridge-domains"
            return self.bridge_domains

        if (child_yang_name == "bridge-groups"):
            if (self.bridge_groups is None):
                self.bridge_groups = BridgeDomainConfig.BridgeGroups()
                self.bridge_groups.parent = self
                self._children_name_map["bridge_groups"] = "bridge-groups"
            return self.bridge_groups

        if (child_yang_name == "global"):
            if (self.global_ is None):
                self.global_ = BridgeDomainConfig.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
            return self.global_

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bridge-domains" or name == "bridge-groups" or name == "global"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BridgeDomainConfig()
        return self._top_entity

class BridgeDomainState(Entity):
    """
    This container defines bridge\-domain operational data.
    
    .. attribute:: bridge_domains
    
    	Bridge domain state data
    	**type**\:   :py:class:`BridgeDomains <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains>`
    
    .. attribute:: mac_table
    
    	This list contains mac\-address entries for bridge domains
    	**type**\: list of    :py:class:`MacTable <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.MacTable>`
    
    .. attribute:: module_capabilities
    
    	This container defines module capabilities for bridge domain
    	**type**\:   :py:class:`ModuleCapabilities <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.ModuleCapabilities>`
    
    .. attribute:: system_capabilities
    
    	This container defines system capabilities for bridge domain
    	**type**\:   :py:class:`SystemCapabilities <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.SystemCapabilities>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(BridgeDomainState, self).__init__()
        self._top_entity = None

        self.yang_name = "bridge-domain-state"
        self.yang_parent_name = "cisco-bridge-domain"

        self.bridge_domains = BridgeDomainState.BridgeDomains()
        self.bridge_domains.parent = self
        self._children_name_map["bridge_domains"] = "bridge-domains"
        self._children_yang_names.add("bridge-domains")

        self.module_capabilities = BridgeDomainState.ModuleCapabilities()
        self.module_capabilities.parent = self
        self._children_name_map["module_capabilities"] = "module-capabilities"
        self._children_yang_names.add("module-capabilities")

        self.system_capabilities = BridgeDomainState.SystemCapabilities()
        self.system_capabilities.parent = self
        self._children_name_map["system_capabilities"] = "system-capabilities"
        self._children_yang_names.add("system-capabilities")

        self.mac_table = YList(self)

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
                    super(BridgeDomainState, self).__setattr__(name, value)
                else:
                    self.__dict__[name].set(value)
            else:
                if hasattr(value, "parent") and name != "parent":
                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                        value.parent = self
                    elif value.parent is None and value.yang_name in self._children_yang_names:
                        value.parent = self
                super(BridgeDomainState, self).__setattr__(name, value)


    class SystemCapabilities(Entity):
        """
        This container defines system capabilities for bridge
        domain.
        
        .. attribute:: max_ac_per_bd
        
        	Maximum number of attachment circuits per bridge\-domains
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_bd
        
        	Maximum number of bridge\-domains suported
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_interflex_if_per_bd
        
        	Maximum number of Interflex interfaces per bridge\-domains
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_pw_per_bd
        
        	Maximum number of access pseudowires per bridge\-domains
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_sh_group_per_bd
        
        	Maximum number of Split Horizon groups per bridge\-domains
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_vfi_per_bd
        
        	Maximum number of virtual forwarding instances per bridge\-domains
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.SystemCapabilities, self).__init__()

            self.yang_name = "system-capabilities"
            self.yang_parent_name = "bridge-domain-state"

            self.max_ac_per_bd = YLeaf(YType.uint32, "max-ac-per-bd")

            self.max_bd = YLeaf(YType.uint32, "max-bd")

            self.max_interflex_if_per_bd = YLeaf(YType.uint32, "max-interflex-if-per-bd")

            self.max_pw_per_bd = YLeaf(YType.uint32, "max-pw-per-bd")

            self.max_sh_group_per_bd = YLeaf(YType.uint32, "max-sh-group-per-bd")

            self.max_vfi_per_bd = YLeaf(YType.uint32, "max-vfi-per-bd")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("max_ac_per_bd",
                            "max_bd",
                            "max_interflex_if_per_bd",
                            "max_pw_per_bd",
                            "max_sh_group_per_bd",
                            "max_vfi_per_bd") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeDomainState.SystemCapabilities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainState.SystemCapabilities, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.max_ac_per_bd.is_set or
                self.max_bd.is_set or
                self.max_interflex_if_per_bd.is_set or
                self.max_pw_per_bd.is_set or
                self.max_sh_group_per_bd.is_set or
                self.max_vfi_per_bd.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.max_ac_per_bd.yfilter != YFilter.not_set or
                self.max_bd.yfilter != YFilter.not_set or
                self.max_interflex_if_per_bd.yfilter != YFilter.not_set or
                self.max_pw_per_bd.yfilter != YFilter.not_set or
                self.max_sh_group_per_bd.yfilter != YFilter.not_set or
                self.max_vfi_per_bd.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "system-capabilities" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.max_ac_per_bd.is_set or self.max_ac_per_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_ac_per_bd.get_name_leafdata())
            if (self.max_bd.is_set or self.max_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_bd.get_name_leafdata())
            if (self.max_interflex_if_per_bd.is_set or self.max_interflex_if_per_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_interflex_if_per_bd.get_name_leafdata())
            if (self.max_pw_per_bd.is_set or self.max_pw_per_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_pw_per_bd.get_name_leafdata())
            if (self.max_sh_group_per_bd.is_set or self.max_sh_group_per_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_sh_group_per_bd.get_name_leafdata())
            if (self.max_vfi_per_bd.is_set or self.max_vfi_per_bd.yfilter != YFilter.not_set):
                leaf_name_data.append(self.max_vfi_per_bd.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "max-ac-per-bd" or name == "max-bd" or name == "max-interflex-if-per-bd" or name == "max-pw-per-bd" or name == "max-sh-group-per-bd" or name == "max-vfi-per-bd"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "max-ac-per-bd"):
                self.max_ac_per_bd = value
                self.max_ac_per_bd.value_namespace = name_space
                self.max_ac_per_bd.value_namespace_prefix = name_space_prefix
            if(value_path == "max-bd"):
                self.max_bd = value
                self.max_bd.value_namespace = name_space
                self.max_bd.value_namespace_prefix = name_space_prefix
            if(value_path == "max-interflex-if-per-bd"):
                self.max_interflex_if_per_bd = value
                self.max_interflex_if_per_bd.value_namespace = name_space
                self.max_interflex_if_per_bd.value_namespace_prefix = name_space_prefix
            if(value_path == "max-pw-per-bd"):
                self.max_pw_per_bd = value
                self.max_pw_per_bd.value_namespace = name_space
                self.max_pw_per_bd.value_namespace_prefix = name_space_prefix
            if(value_path == "max-sh-group-per-bd"):
                self.max_sh_group_per_bd = value
                self.max_sh_group_per_bd.value_namespace = name_space
                self.max_sh_group_per_bd.value_namespace_prefix = name_space_prefix
            if(value_path == "max-vfi-per-bd"):
                self.max_vfi_per_bd = value
                self.max_vfi_per_bd.value_namespace = name_space
                self.max_vfi_per_bd.value_namespace_prefix = name_space_prefix


    class ModuleCapabilities(Entity):
        """
        This container defines module capabilities for bridge
        domain.
        
        .. attribute:: modules
        
        	Collection of capabillity statements for hardware module in the system
        	**type**\: list of    :py:class:`Modules <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.ModuleCapabilities.Modules>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.ModuleCapabilities, self).__init__()

            self.yang_name = "module-capabilities"
            self.yang_parent_name = "bridge-domain-state"

            self.modules = YList(self)

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
                        super(BridgeDomainState.ModuleCapabilities, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainState.ModuleCapabilities, self).__setattr__(name, value)


        class Modules(Entity):
            """
            Collection of capabillity statements for hardware
            module in the system.
            
            .. attribute:: name  <key>
            
            	Name of the hardware module such as linecards, for which capability is described
            	**type**\:  str
            
            .. attribute:: max_ac_per_bd
            
            	Maximum number of attachment circuits per bridge\-domains
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_bd
            
            	Maximum number of bridge\-domains suported
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_mac_per_bd
            
            	Maximum number of MAC addresses per bridge\-domains supported by this module
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_pdd_edge_bd
            
            	Maximum number of PBB Edge type bridge\-domains supported by this module
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_pw_per_bd
            
            	Maximum number of access pseudowires per bridge\-domains
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_sh_group_per_bd
            
            	Maximum number of Split Horizon groups per bridge\-domains
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_vfi_per_bd
            
            	Maximum number of virtual forwarding instances per bridge\-domains
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainState.ModuleCapabilities.Modules, self).__init__()

                self.yang_name = "modules"
                self.yang_parent_name = "module-capabilities"

                self.name = YLeaf(YType.str, "name")

                self.max_ac_per_bd = YLeaf(YType.uint32, "max-ac-per-bd")

                self.max_bd = YLeaf(YType.uint32, "max-bd")

                self.max_mac_per_bd = YLeaf(YType.uint32, "max-mac-per-bd")

                self.max_pdd_edge_bd = YLeaf(YType.uint32, "max-pdd-edge-bd")

                self.max_pw_per_bd = YLeaf(YType.uint32, "max-pw-per-bd")

                self.max_sh_group_per_bd = YLeaf(YType.uint32, "max-sh-group-per-bd")

                self.max_vfi_per_bd = YLeaf(YType.uint32, "max-vfi-per-bd")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("name",
                                "max_ac_per_bd",
                                "max_bd",
                                "max_mac_per_bd",
                                "max_pdd_edge_bd",
                                "max_pw_per_bd",
                                "max_sh_group_per_bd",
                                "max_vfi_per_bd") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeDomainState.ModuleCapabilities.Modules, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeDomainState.ModuleCapabilities.Modules, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.name.is_set or
                    self.max_ac_per_bd.is_set or
                    self.max_bd.is_set or
                    self.max_mac_per_bd.is_set or
                    self.max_pdd_edge_bd.is_set or
                    self.max_pw_per_bd.is_set or
                    self.max_sh_group_per_bd.is_set or
                    self.max_vfi_per_bd.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.max_ac_per_bd.yfilter != YFilter.not_set or
                    self.max_bd.yfilter != YFilter.not_set or
                    self.max_mac_per_bd.yfilter != YFilter.not_set or
                    self.max_pdd_edge_bd.yfilter != YFilter.not_set or
                    self.max_pw_per_bd.yfilter != YFilter.not_set or
                    self.max_sh_group_per_bd.yfilter != YFilter.not_set or
                    self.max_vfi_per_bd.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "modules" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:bridge-domain-state/module-capabilities/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.max_ac_per_bd.is_set or self.max_ac_per_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_ac_per_bd.get_name_leafdata())
                if (self.max_bd.is_set or self.max_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_bd.get_name_leafdata())
                if (self.max_mac_per_bd.is_set or self.max_mac_per_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_mac_per_bd.get_name_leafdata())
                if (self.max_pdd_edge_bd.is_set or self.max_pdd_edge_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_pdd_edge_bd.get_name_leafdata())
                if (self.max_pw_per_bd.is_set or self.max_pw_per_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_pw_per_bd.get_name_leafdata())
                if (self.max_sh_group_per_bd.is_set or self.max_sh_group_per_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_sh_group_per_bd.get_name_leafdata())
                if (self.max_vfi_per_bd.is_set or self.max_vfi_per_bd.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.max_vfi_per_bd.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "name" or name == "max-ac-per-bd" or name == "max-bd" or name == "max-mac-per-bd" or name == "max-pdd-edge-bd" or name == "max-pw-per-bd" or name == "max-sh-group-per-bd" or name == "max-vfi-per-bd"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "max-ac-per-bd"):
                    self.max_ac_per_bd = value
                    self.max_ac_per_bd.value_namespace = name_space
                    self.max_ac_per_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-bd"):
                    self.max_bd = value
                    self.max_bd.value_namespace = name_space
                    self.max_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-mac-per-bd"):
                    self.max_mac_per_bd = value
                    self.max_mac_per_bd.value_namespace = name_space
                    self.max_mac_per_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-pdd-edge-bd"):
                    self.max_pdd_edge_bd = value
                    self.max_pdd_edge_bd.value_namespace = name_space
                    self.max_pdd_edge_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-pw-per-bd"):
                    self.max_pw_per_bd = value
                    self.max_pw_per_bd.value_namespace = name_space
                    self.max_pw_per_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-sh-group-per-bd"):
                    self.max_sh_group_per_bd = value
                    self.max_sh_group_per_bd.value_namespace = name_space
                    self.max_sh_group_per_bd.value_namespace_prefix = name_space_prefix
                if(value_path == "max-vfi-per-bd"):
                    self.max_vfi_per_bd = value
                    self.max_vfi_per_bd.value_namespace = name_space
                    self.max_vfi_per_bd.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.modules:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.modules:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "module-capabilities" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "modules"):
                for c in self.modules:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeDomainState.ModuleCapabilities.Modules()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.modules.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "modules"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class BridgeDomains(Entity):
        """
        Bridge domain state data.
        
        .. attribute:: bridge_domain
        
        	Collection of bridge\-domain state data
        	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.BridgeDomains, self).__init__()

            self.yang_name = "bridge-domains"
            self.yang_parent_name = "bridge-domain-state"

            self.bridge_domain = YList(self)

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
                        super(BridgeDomainState.BridgeDomains, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainState.BridgeDomains, self).__setattr__(name, value)


        class BridgeDomain(Entity):
            """
            Collection of bridge\-domain state data.
            
            .. attribute:: id  <key>
            
            	Bridge domain name or number
            	**type**\:  str
            
            .. attribute:: bd_state
            
            	Bridge domain operational/admin status
            	**type**\:   :py:class:`BridgeDomainStateType <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainStateType>`
            
            	**mandatory**\: True
            
            .. attribute:: create_time
            
            	System time when this bridge\-domain was created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_status_change
            
            	Number of consecutive ticks since bridge\-domain status was changed last time
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_limit_reached
            
            	This leaf indicates if MAC address limit has been reached
            	**type**\:  bool
            
            .. attribute:: members
            
            	Collection of bridge\-domain members
            	**type**\:   :py:class:`Members <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members>`
            
            .. attribute:: p2mp_pw_disabled
            
            	Point to Mutipoint pseudowire state
            	**type**\:  bool
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainState.BridgeDomains.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "bridge-domains"

                self.id = YLeaf(YType.str, "id")

                self.bd_state = YLeaf(YType.enumeration, "bd-state")

                self.create_time = YLeaf(YType.uint32, "create-time")

                self.last_status_change = YLeaf(YType.uint32, "last-status-change")

                self.mac_limit_reached = YLeaf(YType.boolean, "mac-limit-reached")

                self.p2mp_pw_disabled = YLeaf(YType.boolean, "p2mp-pw-disabled")

                self.members = BridgeDomainState.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("id",
                                "bd_state",
                                "create_time",
                                "last_status_change",
                                "mac_limit_reached",
                                "p2mp_pw_disabled") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BridgeDomainState.BridgeDomains.BridgeDomain, self).__setattr__(name, value)


            class Members(Entity):
                """
                Collection of bridge\-domain members.
                
                .. attribute:: ac_member
                
                	List of attachment circuits for this bridge domains
                	**type**\: list of    :py:class:`AcMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember>`
                
                .. attribute:: access_pw_member
                
                	Collection of access pseudowire members of the bridge domain
                	**type**\: list of    :py:class:`AccessPwMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember>`
                
                .. attribute:: vfi_member
                
                	Reference to an instance of Bridge domain Virtual Forwarding Instance (VFI) name
                	**type**\: list of    :py:class:`VfiMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "bridge-domain"

                    self.ac_member = YList(self)
                    self.access_pw_member = YList(self)
                    self.vfi_member = YList(self)

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
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members, self).__setattr__(name, value)


                class AcMember(Entity):
                    """
                    List of attachment circuits for this bridge domains
                    
                    .. attribute:: interface  <key>
                    
                    	Reference to an instance of Bridge domain attachment circuit (AC) interface name
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
                    
                    .. attribute:: dai_stats
                    
                    	Dynamic ARP Inspection (DAI) statistics
                    	**type**\:   :py:class:`DaiStats <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats>`
                    
                    .. attribute:: ipsg_stats
                    
                    	IPSG stats
                    	**type**\:   :py:class:`IpsgStats <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats>`
                    
                    .. attribute:: static_mac_count
                    
                    	Number of static MAC address configured on this bridge\-domain member interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: storm_control
                    
                    	Storm control statistics
                    	**type**\:   :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember, self).__init__()

                        self.yang_name = "ac-member"
                        self.yang_parent_name = "members"

                        self.interface = YLeaf(YType.str, "interface")

                        self.static_mac_count = YLeaf(YType.uint32, "static-mac-count")

                        self.dai_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats()
                        self.dai_stats.parent = self
                        self._children_name_map["dai_stats"] = "dai-stats"
                        self._children_yang_names.add("dai-stats")

                        self.ipsg_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats()
                        self.ipsg_stats.parent = self
                        self._children_name_map["ipsg_stats"] = "ipsg-stats"
                        self._children_yang_names.add("ipsg-stats")

                        self.storm_control = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                        self.storm_control.parent = self
                        self._children_name_map["storm_control"] = "storm-control"
                        self._children_yang_names.add("storm-control")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "static_mac_count") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember, self).__setattr__(name, value)


                    class DaiStats(Entity):
                        """
                        Dynamic ARP Inspection (DAI) statistics.
                        
                        .. attribute:: byte_drops
                        
                        	Number of bytes dropped by interface due to DAI actions
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_drops
                        
                        	Number of packets dropped by interface due to DAI actions
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats, self).__init__()

                            self.yang_name = "dai-stats"
                            self.yang_parent_name = "ac-member"

                            self.byte_drops = YLeaf(YType.uint64, "byte-drops")

                            self.packet_drops = YLeaf(YType.uint64, "packet-drops")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("byte_drops",
                                            "packet_drops") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.byte_drops.is_set or
                                self.packet_drops.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.byte_drops.yfilter != YFilter.not_set or
                                self.packet_drops.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "dai-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.byte_drops.is_set or self.byte_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.byte_drops.get_name_leafdata())
                            if (self.packet_drops.is_set or self.packet_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_drops.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "byte-drops" or name == "packet-drops"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "byte-drops"):
                                self.byte_drops = value
                                self.byte_drops.value_namespace = name_space
                                self.byte_drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-drops"):
                                self.packet_drops = value
                                self.packet_drops.value_namespace = name_space
                                self.packet_drops.value_namespace_prefix = name_space_prefix


                    class IpsgStats(Entity):
                        """
                        IPSG stats.
                        
                        .. attribute:: byte_drops
                        
                        	Number of bytes dropped by interface due to IPSG actions
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: packet_drops
                        
                        	Number of packets dropped by interface due to IPSG actions
                        	**type**\:  int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats, self).__init__()

                            self.yang_name = "ipsg-stats"
                            self.yang_parent_name = "ac-member"

                            self.byte_drops = YLeaf(YType.uint64, "byte-drops")

                            self.packet_drops = YLeaf(YType.uint64, "packet-drops")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("byte_drops",
                                            "packet_drops") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.byte_drops.is_set or
                                self.packet_drops.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.byte_drops.yfilter != YFilter.not_set or
                                self.packet_drops.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipsg-stats" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.byte_drops.is_set or self.byte_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.byte_drops.get_name_leafdata())
                            if (self.packet_drops.is_set or self.packet_drops.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet_drops.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "byte-drops" or name == "packet-drops"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "byte-drops"):
                                self.byte_drops = value
                                self.byte_drops.value_namespace = name_space
                                self.byte_drops.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet-drops"):
                                self.packet_drops = value
                                self.packet_drops.value_namespace = name_space
                                self.packet_drops.value_namespace_prefix = name_space_prefix


                    class StormControl(Entity):
                        """
                        Storm control statistics.
                        
                        .. attribute:: drop_counter
                        
                        	Collection of packet drop statistics for ethernet traffic clasess
                        	**type**\: list of    :py:class:`DropCounter <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__init__()

                            self.yang_name = "storm-control"
                            self.yang_parent_name = "ac-member"

                            self.drop_counter = YList(self)

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
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__setattr__(name, value)


                        class DropCounter(Entity):
                            """
                            Collection of packet drop statistics for ethernet traffic
                            clasess.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	Ethernet traffic class i.e. broadcast, multicast or unknown unicast
                            	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: octate_drops
                            
                            	The total number of bytes of traffic dropped due to storm control violations
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: packet_drops
                            
                            	The total number of dropped packets due to storm control violations
                            	**type**\:  int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter, self).__init__()

                                self.yang_name = "drop-counter"
                                self.yang_parent_name = "storm-control"

                                self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                                self.octate_drops = YLeaf(YType.uint64, "octate-drops")

                                self.packet_drops = YLeaf(YType.uint64, "packet-drops")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("traffic_class",
                                                "octate_drops",
                                                "packet_drops") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.traffic_class.is_set or
                                    self.octate_drops.is_set or
                                    self.packet_drops.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set or
                                    self.octate_drops.yfilter != YFilter.not_set or
                                    self.packet_drops.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "drop-counter" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())
                                if (self.octate_drops.is_set or self.octate_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.octate_drops.get_name_leafdata())
                                if (self.packet_drops.is_set or self.packet_drops.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.packet_drops.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "traffic-class" or name == "octate-drops" or name == "packet-drops"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "octate-drops"):
                                    self.octate_drops = value
                                    self.octate_drops.value_namespace = name_space
                                    self.octate_drops.value_namespace_prefix = name_space_prefix
                                if(value_path == "packet-drops"):
                                    self.packet_drops = value
                                    self.packet_drops.value_namespace = name_space
                                    self.packet_drops.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.drop_counter:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.drop_counter:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "storm-control" + path_buffer

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

                            if (child_yang_name == "drop-counter"):
                                for c in self.drop_counter:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.drop_counter.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "drop-counter"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            self.static_mac_count.is_set or
                            (self.dai_stats is not None and self.dai_stats.has_data()) or
                            (self.ipsg_stats is not None and self.ipsg_stats.has_data()) or
                            (self.storm_control is not None and self.storm_control.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.static_mac_count.yfilter != YFilter.not_set or
                            (self.dai_stats is not None and self.dai_stats.has_operation()) or
                            (self.ipsg_stats is not None and self.ipsg_stats.has_operation()) or
                            (self.storm_control is not None and self.storm_control.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "ac-member" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.static_mac_count.is_set or self.static_mac_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.static_mac_count.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "dai-stats"):
                            if (self.dai_stats is None):
                                self.dai_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats()
                                self.dai_stats.parent = self
                                self._children_name_map["dai_stats"] = "dai-stats"
                            return self.dai_stats

                        if (child_yang_name == "ipsg-stats"):
                            if (self.ipsg_stats is None):
                                self.ipsg_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats()
                                self.ipsg_stats.parent = self
                                self._children_name_map["ipsg_stats"] = "ipsg-stats"
                            return self.ipsg_stats

                        if (child_yang_name == "storm-control"):
                            if (self.storm_control is None):
                                self.storm_control = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                                self.storm_control.parent = self
                                self._children_name_map["storm_control"] = "storm-control"
                            return self.storm_control

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "dai-stats" or name == "ipsg-stats" or name == "storm-control" or name == "interface" or name == "static-mac-count"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "static-mac-count"):
                            self.static_mac_count = value
                            self.static_mac_count.value_namespace = name_space
                            self.static_mac_count.value_namespace_prefix = name_space_prefix


                class VfiMember(Entity):
                    """
                    Reference to an instance of Bridge domain Virtual
                    Forwarding Instance (VFI) name.
                    
                    .. attribute:: interface  <key>
                    
                    	Bridge domain memeber interface name
                    	**type**\:  str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
                    
                    .. attribute:: flooding
                    
                    	Flooding operational status
                    	**type**\:   :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember, self).__init__()

                        self.yang_name = "vfi-member"
                        self.yang_parent_name = "members"

                        self.interface = YLeaf(YType.str, "interface")

                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember, self).__setattr__(name, value)


                    class Flooding(Entity):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "vfi-member"

                            self.status = YList(self)

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
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding, self).__setattr__(name, value)


                        class Status(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status, self).__init__()

                                self.yang_name = "status"
                                self.yang_parent_name = "flooding"

                                self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                                self.enabled = YLeaf(YType.boolean, "enabled")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("traffic_class",
                                                "enabled") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.traffic_class.is_set or
                                    self.enabled.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set or
                                    self.enabled.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "status" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())
                                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "traffic-class" or name == "enabled"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled"):
                                    self.enabled = value
                                    self.enabled.value_namespace = name_space
                                    self.enabled.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.status:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.status:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flooding" + path_buffer

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

                            if (child_yang_name == "status"):
                                for c in self.status:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.status.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "status"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.interface.is_set or
                            (self.flooding is not None and self.flooding.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            (self.flooding is not None and self.flooding.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "vfi-member" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "flooding"):
                            if (self.flooding is None):
                                self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding()
                                self.flooding.parent = self
                                self._children_name_map["flooding"] = "flooding"
                            return self.flooding

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flooding" or name == "interface"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix


                class AccessPwMember(Entity):
                    """
                    Collection of access pseudowire members of the bridge
                    domain.
                    
                    .. attribute:: vc_peer_address  <key>
                    
                    	Reference to peer ip address of a pseudowire instance
                    	**type**\: one of the below types:
                    
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    
                    ----
                    .. attribute:: vc_id  <key>
                    
                    	Reference to vc\-id of a pseudowire instance
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`vc_id <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
                    
                    .. attribute:: flooding
                    
                    	Flooding operational status
                    	**type**\:   :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__init__()

                        self.yang_name = "access-pw-member"
                        self.yang_parent_name = "members"

                        self.vc_peer_address = YLeaf(YType.str, "vc-peer-address")

                        self.vc_id = YLeaf(YType.str, "vc-id")

                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("vc_peer_address",
                                        "vc_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__setattr__(name, value)


                    class Flooding(Entity):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "access-pw-member"

                            self.status = YList(self)

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
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding, self).__setattr__(name, value)


                        class Status(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:   :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status, self).__init__()

                                self.yang_name = "status"
                                self.yang_parent_name = "flooding"

                                self.traffic_class = YLeaf(YType.enumeration, "traffic-class")

                                self.enabled = YLeaf(YType.boolean, "enabled")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("traffic_class",
                                                "enabled") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.traffic_class.is_set or
                                    self.enabled.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set or
                                    self.enabled.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "status" + "[traffic-class='" + self.traffic_class.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())
                                if (self.enabled.is_set or self.enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.enabled.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "traffic-class" or name == "enabled"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "enabled"):
                                    self.enabled = value
                                    self.enabled.value_namespace = name_space
                                    self.enabled.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.status:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.status:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flooding" + path_buffer

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

                            if (child_yang_name == "status"):
                                for c in self.status:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.status.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "status"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.vc_peer_address.is_set or
                            self.vc_id.is_set or
                            (self.flooding is not None and self.flooding.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.vc_peer_address.yfilter != YFilter.not_set or
                            self.vc_id.yfilter != YFilter.not_set or
                            (self.flooding is not None and self.flooding.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "access-pw-member" + "[vc-peer-address='" + self.vc_peer_address.get() + "']" + "[vc-id='" + self.vc_id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.vc_peer_address.is_set or self.vc_peer_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_peer_address.get_name_leafdata())
                        if (self.vc_id.is_set or self.vc_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.vc_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "flooding"):
                            if (self.flooding is None):
                                self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding()
                                self.flooding.parent = self
                                self._children_name_map["flooding"] = "flooding"
                            return self.flooding

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flooding" or name == "vc-peer-address" or name == "vc-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "vc-peer-address"):
                            self.vc_peer_address = value
                            self.vc_peer_address.value_namespace = name_space
                            self.vc_peer_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "vc-id"):
                            self.vc_id = value
                            self.vc_id.value_namespace = name_space
                            self.vc_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.ac_member:
                        if (c.has_data()):
                            return True
                    for c in self.access_pw_member:
                        if (c.has_data()):
                            return True
                    for c in self.vfi_member:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.ac_member:
                        if (c.has_operation()):
                            return True
                    for c in self.access_pw_member:
                        if (c.has_operation()):
                            return True
                    for c in self.vfi_member:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "members" + path_buffer

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

                    if (child_yang_name == "ac-member"):
                        for c in self.ac_member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.ac_member.append(c)
                        return c

                    if (child_yang_name == "access-pw-member"):
                        for c in self.access_pw_member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.access_pw_member.append(c)
                        return c

                    if (child_yang_name == "vfi-member"):
                        for c in self.vfi_member:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.vfi_member.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "ac-member" or name == "access-pw-member" or name == "vfi-member"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.id.is_set or
                    self.bd_state.is_set or
                    self.create_time.is_set or
                    self.last_status_change.is_set or
                    self.mac_limit_reached.is_set or
                    self.p2mp_pw_disabled.is_set or
                    (self.members is not None and self.members.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.id.yfilter != YFilter.not_set or
                    self.bd_state.yfilter != YFilter.not_set or
                    self.create_time.yfilter != YFilter.not_set or
                    self.last_status_change.yfilter != YFilter.not_set or
                    self.mac_limit_reached.yfilter != YFilter.not_set or
                    self.p2mp_pw_disabled.yfilter != YFilter.not_set or
                    (self.members is not None and self.members.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bridge-domain" + "[id='" + self.id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:bridge-domain-state/bridge-domains/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.id.get_name_leafdata())
                if (self.bd_state.is_set or self.bd_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bd_state.get_name_leafdata())
                if (self.create_time.is_set or self.create_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.create_time.get_name_leafdata())
                if (self.last_status_change.is_set or self.last_status_change.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_status_change.get_name_leafdata())
                if (self.mac_limit_reached.is_set or self.mac_limit_reached.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.mac_limit_reached.get_name_leafdata())
                if (self.p2mp_pw_disabled.is_set or self.p2mp_pw_disabled.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.p2mp_pw_disabled.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "members"):
                    if (self.members is None):
                        self.members = BridgeDomainState.BridgeDomains.BridgeDomain.Members()
                        self.members.parent = self
                        self._children_name_map["members"] = "members"
                    return self.members

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "members" or name == "id" or name == "bd-state" or name == "create-time" or name == "last-status-change" or name == "mac-limit-reached" or name == "p2mp-pw-disabled"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "id"):
                    self.id = value
                    self.id.value_namespace = name_space
                    self.id.value_namespace_prefix = name_space_prefix
                if(value_path == "bd-state"):
                    self.bd_state = value
                    self.bd_state.value_namespace = name_space
                    self.bd_state.value_namespace_prefix = name_space_prefix
                if(value_path == "create-time"):
                    self.create_time = value
                    self.create_time.value_namespace = name_space
                    self.create_time.value_namespace_prefix = name_space_prefix
                if(value_path == "last-status-change"):
                    self.last_status_change = value
                    self.last_status_change.value_namespace = name_space
                    self.last_status_change.value_namespace_prefix = name_space_prefix
                if(value_path == "mac-limit-reached"):
                    self.mac_limit_reached = value
                    self.mac_limit_reached.value_namespace = name_space
                    self.mac_limit_reached.value_namespace_prefix = name_space_prefix
                if(value_path == "p2mp-pw-disabled"):
                    self.p2mp_pw_disabled = value
                    self.p2mp_pw_disabled.value_namespace = name_space
                    self.p2mp_pw_disabled.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bridge_domain:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bridge_domain:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bridge-domains" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bridge-domain"):
                for c in self.bridge_domain:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BridgeDomainState.BridgeDomains.BridgeDomain()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bridge_domain.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bridge-domain"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class MacTable(Entity):
        """
        This list contains mac\-address entries for bridge
        domains.
        
        .. attribute:: bd_id  <key>
        
        	Bridge\-domain name where MAC entry is learnt
        	**type**\:  str
        
        .. attribute:: mac_address  <key>
        
        	MAC address
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: age
        
        	Time since mac address was learnt on the interface
        	**type**\:  int
        
        	**range:** 0..4294967295
        
        .. attribute:: interface
        
        	Reference to an interface instance where MAC  address is learnt
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        	**mandatory**\: True
        
        .. attribute:: location
        
        	Linecard / Module where mac address was learnt
        	**type**\:  str
        
        .. attribute:: mac_type
        
        	MAC address type
        	**type**\:   :py:class:`MacType <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.MacTable.MacType>`
        
        .. attribute:: ntfy_mac
        
        	TBD ?NTFY?
        	**type**\:  bool
        
        .. attribute:: secure_mac
        
        	Secure MAC address
        	**type**\:  bool
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.MacTable, self).__init__()

            self.yang_name = "mac-table"
            self.yang_parent_name = "bridge-domain-state"

            self.bd_id = YLeaf(YType.str, "bd-id")

            self.mac_address = YLeaf(YType.str, "mac-address")

            self.age = YLeaf(YType.uint32, "age")

            self.interface = YLeaf(YType.str, "interface")

            self.location = YLeaf(YType.str, "location")

            self.mac_type = YLeaf(YType.enumeration, "mac-type")

            self.ntfy_mac = YLeaf(YType.boolean, "ntfy-mac")

            self.secure_mac = YLeaf(YType.boolean, "secure-mac")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("bd_id",
                            "mac_address",
                            "age",
                            "interface",
                            "location",
                            "mac_type",
                            "ntfy_mac",
                            "secure_mac") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(BridgeDomainState.MacTable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BridgeDomainState.MacTable, self).__setattr__(name, value)

        class MacType(Enum):
            """
            MacType

            MAC address type.

            .. data:: static = 0

            	MAC address is configured statically.

            .. data:: dynamic = 1

            	MAC address is learnt dynamicaly.

            """

            static = Enum.YLeaf(0, "static")

            dynamic = Enum.YLeaf(1, "dynamic")


        def has_data(self):
            return (
                self.bd_id.is_set or
                self.mac_address.is_set or
                self.age.is_set or
                self.interface.is_set or
                self.location.is_set or
                self.mac_type.is_set or
                self.ntfy_mac.is_set or
                self.secure_mac.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.bd_id.yfilter != YFilter.not_set or
                self.mac_address.yfilter != YFilter.not_set or
                self.age.yfilter != YFilter.not_set or
                self.interface.yfilter != YFilter.not_set or
                self.location.yfilter != YFilter.not_set or
                self.mac_type.yfilter != YFilter.not_set or
                self.ntfy_mac.yfilter != YFilter.not_set or
                self.secure_mac.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "mac-table" + "[bd-id='" + self.bd_id.get() + "']" + "[mac-address='" + self.mac_address.get() + "']" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:bridge-domain-state/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.bd_id.is_set or self.bd_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bd_id.get_name_leafdata())
            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac_address.get_name_leafdata())
            if (self.age.is_set or self.age.yfilter != YFilter.not_set):
                leaf_name_data.append(self.age.get_name_leafdata())
            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface.get_name_leafdata())
            if (self.location.is_set or self.location.yfilter != YFilter.not_set):
                leaf_name_data.append(self.location.get_name_leafdata())
            if (self.mac_type.is_set or self.mac_type.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac_type.get_name_leafdata())
            if (self.ntfy_mac.is_set or self.ntfy_mac.yfilter != YFilter.not_set):
                leaf_name_data.append(self.ntfy_mac.get_name_leafdata())
            if (self.secure_mac.is_set or self.secure_mac.yfilter != YFilter.not_set):
                leaf_name_data.append(self.secure_mac.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bd-id" or name == "mac-address" or name == "age" or name == "interface" or name == "location" or name == "mac-type" or name == "ntfy-mac" or name == "secure-mac"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "bd-id"):
                self.bd_id = value
                self.bd_id.value_namespace = name_space
                self.bd_id.value_namespace_prefix = name_space_prefix
            if(value_path == "mac-address"):
                self.mac_address = value
                self.mac_address.value_namespace = name_space
                self.mac_address.value_namespace_prefix = name_space_prefix
            if(value_path == "age"):
                self.age = value
                self.age.value_namespace = name_space
                self.age.value_namespace_prefix = name_space_prefix
            if(value_path == "interface"):
                self.interface = value
                self.interface.value_namespace = name_space
                self.interface.value_namespace_prefix = name_space_prefix
            if(value_path == "location"):
                self.location = value
                self.location.value_namespace = name_space
                self.location.value_namespace_prefix = name_space_prefix
            if(value_path == "mac-type"):
                self.mac_type = value
                self.mac_type.value_namespace = name_space
                self.mac_type.value_namespace_prefix = name_space_prefix
            if(value_path == "ntfy-mac"):
                self.ntfy_mac = value
                self.ntfy_mac.value_namespace = name_space
                self.ntfy_mac.value_namespace_prefix = name_space_prefix
            if(value_path == "secure-mac"):
                self.secure_mac = value
                self.secure_mac.value_namespace = name_space
                self.secure_mac.value_namespace_prefix = name_space_prefix

    def has_data(self):
        for c in self.mac_table:
            if (c.has_data()):
                return True
        return (
            (self.bridge_domains is not None and self.bridge_domains.has_data()) or
            (self.module_capabilities is not None and self.module_capabilities.has_data()) or
            (self.system_capabilities is not None and self.system_capabilities.has_data()))

    def has_operation(self):
        for c in self.mac_table:
            if (c.has_operation()):
                return True
        return (
            self.yfilter != YFilter.not_set or
            (self.bridge_domains is not None and self.bridge_domains.has_operation()) or
            (self.module_capabilities is not None and self.module_capabilities.has_operation()) or
            (self.system_capabilities is not None and self.system_capabilities.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-bridge-domain:bridge-domain-state" + path_buffer

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

        if (child_yang_name == "bridge-domains"):
            if (self.bridge_domains is None):
                self.bridge_domains = BridgeDomainState.BridgeDomains()
                self.bridge_domains.parent = self
                self._children_name_map["bridge_domains"] = "bridge-domains"
            return self.bridge_domains

        if (child_yang_name == "mac-table"):
            for c in self.mac_table:
                segment = c.get_segment_path()
                if (segment_path == segment):
                    return c
            c = BridgeDomainState.MacTable()
            c.parent = self
            local_reference_key = "ydk::seg::%s" % segment_path
            self._local_refs[local_reference_key] = c
            self.mac_table.append(c)
            return c

        if (child_yang_name == "module-capabilities"):
            if (self.module_capabilities is None):
                self.module_capabilities = BridgeDomainState.ModuleCapabilities()
                self.module_capabilities.parent = self
                self._children_name_map["module_capabilities"] = "module-capabilities"
            return self.module_capabilities

        if (child_yang_name == "system-capabilities"):
            if (self.system_capabilities is None):
                self.system_capabilities = BridgeDomainState.SystemCapabilities()
                self.system_capabilities.parent = self
                self._children_name_map["system_capabilities"] = "system-capabilities"
            return self.system_capabilities

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "bridge-domains" or name == "mac-table" or name == "module-capabilities" or name == "system-capabilities"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BridgeDomainState()
        return self._top_entity

class ClearBridgeDomain(Entity):
    """
    Clear mac\-address table for bridge\-domain and allows a bridge
    to forward again after it was put in shutdown state as a
    result of exceeding the configured MAC limit.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomain.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomain.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(ClearBridgeDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-bridge-domain"
        self.yang_parent_name = "cisco-bridge-domain"

        self.input = ClearBridgeDomain.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearBridgeDomain.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: all
        
        	Clear all bridge\-domains configured on the device
        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: bd_id
        
        	Clear a single bridge\-domain
        	**type**\:  str
        
        .. attribute:: bg_id
        
        	Clears all bridge\-domains under this bridge\-group
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearBridgeDomain.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-bridge-domain"

            self.all = YLeaf(YType.empty, "all")

            self.bd_id = YLeaf(YType.str, "bd-id")

            self.bg_id = YLeaf(YType.str, "bg-id")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("all",
                            "bd_id",
                            "bg_id") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearBridgeDomain.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearBridgeDomain.Input, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.all.is_set or
                self.bd_id.is_set or
                self.bg_id.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.all.yfilter != YFilter.not_set or
                self.bd_id.yfilter != YFilter.not_set or
                self.bg_id.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:clear-bridge-domain/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.all.is_set or self.all.yfilter != YFilter.not_set):
                leaf_name_data.append(self.all.get_name_leafdata())
            if (self.bd_id.is_set or self.bd_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bd_id.get_name_leafdata())
            if (self.bg_id.is_set or self.bg_id.yfilter != YFilter.not_set):
                leaf_name_data.append(self.bg_id.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "all" or name == "bd-id" or name == "bg-id"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "all"):
                self.all = value
                self.all.value_namespace = name_space
                self.all.value_namespace_prefix = name_space_prefix
            if(value_path == "bd-id"):
                self.bd_id = value
                self.bd_id.value_namespace = name_space
                self.bd_id.value_namespace_prefix = name_space_prefix
            if(value_path == "bg-id"):
                self.bg_id = value
                self.bg_id.value_namespace = name_space
                self.bg_id.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearBridgeDomain.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-bridge-domain"

            self.errstr = YLeaf(YType.str, "errstr")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("errstr") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearBridgeDomain.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearBridgeDomain.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.errstr.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.errstr.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:clear-bridge-domain/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.errstr.is_set or self.errstr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.errstr.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "errstr"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "errstr"):
                self.errstr = value
                self.errstr.value_namespace = name_space
                self.errstr.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-bridge-domain:clear-bridge-domain" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ClearBridgeDomain.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = ClearBridgeDomain.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ClearBridgeDomain()
        return self._top_entity

class ClearMacAddress(Entity):
    """
    This RPC allows to clear dynamically learnt mac\-address
    entries from the mac\-address table.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(ClearMacAddress, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-mac-address"
        self.yang_parent_name = "cisco-bridge-domain"

        self.input = ClearMacAddress.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearMacAddress.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: bridge_domain
        
        	Clear mac\-address entries for given bridge\-domain(s)
        	**type**\:   :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Input.BridgeDomain>`
        
        .. attribute:: interface
        
        	Reference to an interface. Clear mac\-addesses learnt by by this interface
        	**type**\:  str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: mac_address
        
        	Clear a specific mac\-address entry from the mac\-table
        	**type**\:  str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearMacAddress.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-mac-address"

            self.interface = YLeaf(YType.str, "interface")

            self.mac_address = YLeaf(YType.str, "mac-address")

            self.bridge_domain = ClearMacAddress.Input.BridgeDomain()
            self.bridge_domain.parent = self
            self._children_name_map["bridge_domain"] = "bridge-domain"
            self._children_yang_names.add("bridge-domain")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("interface",
                            "mac_address") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearMacAddress.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearMacAddress.Input, self).__setattr__(name, value)


        class BridgeDomain(Entity):
            """
            Clear mac\-address entries for given bridge\-domain(s).
            
            .. attribute:: bd_id
            
            	Bridge\-domain identifier, clear all mac\-address entries dynamically learnt on this bridge\-domain
            	**type**\:  str
            
            	**mandatory**\: True
            
            .. attribute:: bg_id
            
            	Bridge\-group identifier, clear all mac\-address entries from all bridge\-domains under this bridge\-group
            	**type**\:  str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(ClearMacAddress.Input.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "input"

                self.bd_id = YLeaf(YType.str, "bd-id")

                self.bg_id = YLeaf(YType.str, "bg-id")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("bd_id",
                                "bg_id") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(ClearMacAddress.Input.BridgeDomain, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(ClearMacAddress.Input.BridgeDomain, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.bd_id.is_set or
                    self.bg_id.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.bd_id.yfilter != YFilter.not_set or
                    self.bg_id.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bridge-domain" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:clear-mac-address/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.bd_id.is_set or self.bd_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bd_id.get_name_leafdata())
                if (self.bg_id.is_set or self.bg_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bg_id.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bd-id" or name == "bg-id"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "bd-id"):
                    self.bd_id = value
                    self.bd_id.value_namespace = name_space
                    self.bd_id.value_namespace_prefix = name_space_prefix
                if(value_path == "bg-id"):
                    self.bg_id = value
                    self.bg_id.value_namespace = name_space
                    self.bg_id.value_namespace_prefix = name_space_prefix

        def has_data(self):
            return (
                self.interface.is_set or
                self.mac_address.is_set or
                (self.bridge_domain is not None and self.bridge_domain.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.interface.yfilter != YFilter.not_set or
                self.mac_address.yfilter != YFilter.not_set or
                (self.bridge_domain is not None and self.bridge_domain.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:clear-mac-address/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                leaf_name_data.append(self.interface.get_name_leafdata())
            if (self.mac_address.is_set or self.mac_address.yfilter != YFilter.not_set):
                leaf_name_data.append(self.mac_address.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bridge-domain"):
                if (self.bridge_domain is None):
                    self.bridge_domain = ClearMacAddress.Input.BridgeDomain()
                    self.bridge_domain.parent = self
                    self._children_name_map["bridge_domain"] = "bridge-domain"
                return self.bridge_domain

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bridge-domain" or name == "interface" or name == "mac-address"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "interface"):
                self.interface = value
                self.interface.value_namespace = name_space
                self.interface.value_namespace_prefix = name_space_prefix
            if(value_path == "mac-address"):
                self.mac_address = value
                self.mac_address.value_namespace = name_space
                self.mac_address.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearMacAddress.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-mac-address"

            self.errstr = YLeaf(YType.str, "errstr")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("errstr") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(ClearMacAddress.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(ClearMacAddress.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.errstr.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.errstr.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:clear-mac-address/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.errstr.is_set or self.errstr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.errstr.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "errstr"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "errstr"):
                self.errstr = value
                self.errstr.value_namespace = name_space
                self.errstr.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-bridge-domain:clear-mac-address" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = ClearMacAddress.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = ClearMacAddress.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = ClearMacAddress()
        return self._top_entity

class CreateParameterizedBridgeDomains(Entity):
    """
    Create bridge domains automatically from user defined
    parameters.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(CreateParameterizedBridgeDomains, self).__init__()
        self._top_entity = None

        self.yang_name = "create-parameterized-bridge-domains"
        self.yang_parent_name = "cisco-bridge-domain"

        self.input = CreateParameterizedBridgeDomains.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = CreateParameterizedBridgeDomains.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")


    class Input(Entity):
        """
        
        
        .. attribute:: member
        
        	Bridge\-domain member interface
        	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input.Member>`
        
        .. attribute:: parameter
        
        	Parameter for automatic bridge domain creation
        	**type**\:   :py:class:`Parameter <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input.Parameter>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(CreateParameterizedBridgeDomains.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "create-parameterized-bridge-domains"

            self.parameter = YLeaf(YType.enumeration, "parameter")

            self.member = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("parameter") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CreateParameterizedBridgeDomains.Input, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CreateParameterizedBridgeDomains.Input, self).__setattr__(name, value)

        class Parameter(Enum):
            """
            Parameter

            Parameter for automatic bridge domain creation.

            .. data:: vlan = 0

            	Create bridge-domains from vlan encapsulations of the

            	member interfaces.

            """

            vlan = Enum.YLeaf(0, "vlan")



        class Member(Entity):
            """
            Bridge\-domain member interface.
            
            .. attribute:: interface  <key>
            
            	Reference to an interface instance which is configured to be part of this bridge domain
            	**type**\:  str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(CreateParameterizedBridgeDomains.Input.Member, self).__init__()

                self.yang_name = "member"
                self.yang_parent_name = "input"

                self.interface = YLeaf(YType.str, "interface")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("interface") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CreateParameterizedBridgeDomains.Input.Member, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CreateParameterizedBridgeDomains.Input.Member, self).__setattr__(name, value)

            def has_data(self):
                return self.interface.is_set

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.interface.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "member" + "[interface='" + self.interface.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "cisco-bridge-domain:create-parameterized-bridge-domains/input/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.interface.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "interface"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "interface"):
                    self.interface = value
                    self.interface.value_namespace = name_space
                    self.interface.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.member:
                if (c.has_data()):
                    return True
            return self.parameter.is_set

        def has_operation(self):
            for c in self.member:
                if (c.has_operation()):
                    return True
            return (
                self.yfilter != YFilter.not_set or
                self.parameter.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "input" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:create-parameterized-bridge-domains/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.parameter.is_set or self.parameter.yfilter != YFilter.not_set):
                leaf_name_data.append(self.parameter.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "member"):
                for c in self.member:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CreateParameterizedBridgeDomains.Input.Member()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.member.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "member" or name == "parameter"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "parameter"):
                self.parameter = value
                self.parameter.value_namespace = name_space
                self.parameter.value_namespace_prefix = name_space_prefix


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(CreateParameterizedBridgeDomains.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "create-parameterized-bridge-domains"

            self.errstr = YLeaf(YType.str, "errstr")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("errstr") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CreateParameterizedBridgeDomains.Output, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CreateParameterizedBridgeDomains.Output, self).__setattr__(name, value)

        def has_data(self):
            return self.errstr.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.errstr.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "output" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "cisco-bridge-domain:create-parameterized-bridge-domains/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.errstr.is_set or self.errstr.yfilter != YFilter.not_set):
                leaf_name_data.append(self.errstr.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "errstr"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "errstr"):
                self.errstr = value
                self.errstr.value_namespace = name_space
                self.errstr.value_namespace_prefix = name_space_prefix

    def has_data(self):
        return (
            (self.input is not None and self.input.has_data()) or
            (self.output is not None and self.output.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.input is not None and self.input.has_operation()) or
            (self.output is not None and self.output.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "cisco-bridge-domain:create-parameterized-bridge-domains" + path_buffer

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

        if (child_yang_name == "input"):
            if (self.input is None):
                self.input = CreateParameterizedBridgeDomains.Input()
                self.input.parent = self
                self._children_name_map["input"] = "input"
            return self.input

        if (child_yang_name == "output"):
            if (self.output is None):
                self.output = CreateParameterizedBridgeDomains.Output()
                self.output.parent = self
                self._children_name_map["output"] = "output"
            return self.output

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "input" or name == "output"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CreateParameterizedBridgeDomains()
        return self._top_entity

