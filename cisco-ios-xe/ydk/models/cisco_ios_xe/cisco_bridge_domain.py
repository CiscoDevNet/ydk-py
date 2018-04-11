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
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BridgeDomainStateType(Enum):
    """
    BridgeDomainStateType (Enum Class)

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
    
    .. attribute:: global_
    
    	Global configurations for bridge\-domains
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.Global>`
    
    .. attribute:: bridge_groups
    
    	Collection of bridge\-groups.  A Bridge\-group is logical grouping construct for bridge domains. It defines grouping of bridge\-domains under a named bridge\-group. For example all bridge\-domains belonging to a single customer can be grouped under a bridge \-group
    	**type**\:  :py:class:`BridgeGroups <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups>`
    
    .. attribute:: bridge_domains
    
    	Collection of bridge domains
    	**type**\:  :py:class:`BridgeDomains <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(BridgeDomainConfig, self).__init__()
        self._top_entity = None

        self.yang_name = "bridge-domain-config"
        self.yang_parent_name = "cisco-bridge-domain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("global", ("global_", BridgeDomainConfig.Global)), ("bridge-groups", ("bridge_groups", BridgeDomainConfig.BridgeGroups)), ("bridge-domains", ("bridge_domains", BridgeDomainConfig.BridgeDomains))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.global_ = BridgeDomainConfig.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.bridge_groups = BridgeDomainConfig.BridgeGroups()
        self.bridge_groups.parent = self
        self._children_name_map["bridge_groups"] = "bridge-groups"
        self._children_yang_names.add("bridge-groups")

        self.bridge_domains = BridgeDomainConfig.BridgeDomains()
        self.bridge_domains.parent = self
        self._children_name_map["bridge_domains"] = "bridge-domains"
        self._children_yang_names.add("bridge-domains")
        self._segment_path = lambda: "cisco-bridge-domain:bridge-domain-config"


    class Global(Entity):
        """
        Global configurations for bridge\-domains.
        
        .. attribute:: bd_state_notification_enabled
        
        	If this leaf is set to true, then it enables the emission of 'bd\-state\-notification'; otherwise these notifications are not emitted
        	**type**\: bool
        
        .. attribute:: bd_state_notification_rate
        
        	This leaf defines the maximum number of 'bd\-state\- notification' that can be emitted from the device per second
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: pbb
        
        	Provider Backbone Bridging (PBB) related global configurations
        	**type**\:  :py:class:`Pbb <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.Global.Pbb>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "bridge-domain-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("pbb", ("pbb", BridgeDomainConfig.Global.Pbb))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bd_state_notification_enabled', YLeaf(YType.boolean, 'bd-state-notification-enabled')),
                ('bd_state_notification_rate', YLeaf(YType.uint32, 'bd-state-notification-rate')),
            ])
            self.bd_state_notification_enabled = None
            self.bd_state_notification_rate = None

            self.pbb = BridgeDomainConfig.Global.Pbb()
            self.pbb.parent = self
            self._children_name_map["pbb"] = "pbb"
            self._children_yang_names.add("pbb")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainConfig.Global, ['bd_state_notification_enabled', 'bd_state_notification_rate'], name, value)


        class Pbb(Entity):
            """
            Provider Backbone Bridging (PBB) related global
            configurations.
            
            .. attribute:: backbone_src_mac
            
            	Backbone source mac address configuration for Provider Backbone Bridging (PBB)
            	**type**\: str
            
            	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.Global.Pbb, self).__init__()

                self.yang_name = "pbb"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('backbone_src_mac', YLeaf(YType.str, 'backbone-src-mac')),
                ])
                self.backbone_src_mac = None
                self._segment_path = lambda: "pbb"
                self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeDomainConfig.Global.Pbb, ['backbone_src_mac'], name, value)


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
        	**type**\: list of  		 :py:class:`BridgeGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups.BridgeGroup>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.BridgeGroups, self).__init__()

            self.yang_name = "bridge-groups"
            self.yang_parent_name = "bridge-domain-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bridge-group", ("bridge_group", BridgeDomainConfig.BridgeGroups.BridgeGroup))])
            self._leafs = OrderedDict()

            self.bridge_group = YList(self)
            self._segment_path = lambda: "bridge-groups"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainConfig.BridgeGroups, [], name, value)


        class BridgeGroup(Entity):
            """
            Bridge\-group configuration.
            
            .. attribute:: name  (key)
            
            	Bridge\-group name
            	**type**\: str
            
            	**length:** 1..32
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.BridgeGroups.BridgeGroup, self).__init__()

                self.yang_name = "bridge-group"
                self.yang_parent_name = "bridge-groups"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                ])
                self.name = None
                self._segment_path = lambda: "bridge-group" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/bridge-groups/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeDomainConfig.BridgeGroups.BridgeGroup, ['name'], name, value)


    class BridgeDomains(Entity):
        """
        Collection of bridge domains.
        
        .. attribute:: bridge_domain
        
        	Definition of a bridge\-domain
        	**type**\: list of  		 :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainConfig.BridgeDomains, self).__init__()

            self.yang_name = "bridge-domains"
            self.yang_parent_name = "bridge-domain-config"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bridge-domain", ("bridge_domain", BridgeDomainConfig.BridgeDomains.BridgeDomain))])
            self._leafs = OrderedDict()

            self.bridge_domain = YList(self)
            self._segment_path = lambda: "bridge-domains"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainConfig.BridgeDomains, [], name, value)


        class BridgeDomain(Entity):
            """
            Definition of a bridge\-domain.
            
            .. attribute:: id  (key)
            
            	Bridge domain name or number
            	**type**\: str
            
            .. attribute:: bridge_group
            
            	Reference to bridge\-group name. If bridge\-groups are supported, referred bridge\-group MUST be created first
            	**type**\: str
            
            	**length:** 1..32
            
            	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeGroups.BridgeGroup>`
            
            	**mandatory**\: True
            
            .. attribute:: enabled
            
            	This leaf represents configured admin status of the bridge domain
            	**type**\: bool
            
            	**default value**\: true
            
            .. attribute:: bd_status_change_notification
            
            	Enable/disable bridge\-domain status change notification.  If true, any change in bridge\-domain operational status will be notified to client via 'bd\-status\-change' notification
            	**type**\: bool
            
            .. attribute:: members
            
            	Collection of bridge\-domain members
            	**type**\:  :py:class:`Members <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members>`
            
            .. attribute:: mtu
            
            	The MTU size for bridge domain. All bridge domain members must have same MTU size to be operational in the domain
            	**type**\: int
            
            	**range:** 46..65535
            
            .. attribute:: flooding_mode
            
            	Flood modes for optimization
            	**type**\:  :py:class:`FloodingMode <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingMode>`
            
            .. attribute:: mac
            
            	MAC features for bridge domain
            	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac>`
            
            .. attribute:: dynamic_arp_inspection
            
            	Dynamic ARP Inspection (DAI) configurations
            	**type**\:  :py:class:`DynamicArpInspection <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection>`
            
            	**presence node**\: True
            
            .. attribute:: ip_source_guard
            
            	IP source guard (IPSG) configurations
            	**type**\:  :py:class:`IpSourceGuard <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard>`
            
            	**presence node**\: True
            
            .. attribute:: storm_control
            
            	A collection of storm control threshold and action configurations
            	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl>`
            
            .. attribute:: igmp_snooping
            
            	Enable IGMP snooping
            	**type**\:  :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping>`
            
            .. attribute:: mld_snooping
            
            	Enable MLD snooping
            	**type**\:  :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping>`
            
            .. attribute:: dhcp_ipv4_snooping
            
            	Enable DHCP IPv4 snooping
            	**type**\:  :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping>`
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainConfig.BridgeDomains.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "bridge-domains"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_container_classes = OrderedDict([("members", ("members", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members)), ("mac", ("mac", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac)), ("dynamic-arp-inspection", ("dynamic_arp_inspection", BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection)), ("ip-source-guard", ("ip_source_guard", BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard)), ("storm-control", ("storm_control", BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl)), ("igmp-snooping", ("igmp_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping)), ("mld-snooping", ("mld_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping)), ("dhcp-ipv4-snooping", ("dhcp_ipv4_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id', YLeaf(YType.str, 'id')),
                    ('bridge_group', YLeaf(YType.str, 'bridge-group')),
                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                    ('bd_status_change_notification', YLeaf(YType.boolean, 'bd-status-change-notification')),
                    ('mtu', YLeaf(YType.uint16, 'mtu')),
                    ('flooding_mode', YLeaf(YType.enumeration, 'flooding-mode')),
                ])
                self.id = None
                self.bridge_group = None
                self.enabled = None
                self.bd_status_change_notification = None
                self.mtu = None
                self.flooding_mode = None

                self.members = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")

                self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac()
                self.mac.parent = self
                self._children_name_map["mac"] = "mac"
                self._children_yang_names.add("mac")

                self.dynamic_arp_inspection = None
                self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                self._children_yang_names.add("dynamic-arp-inspection")

                self.ip_source_guard = None
                self._children_name_map["ip_source_guard"] = "ip-source-guard"
                self._children_yang_names.add("ip-source-guard")

                self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl()
                self.storm_control.parent = self
                self._children_name_map["storm_control"] = "storm-control"
                self._children_yang_names.add("storm-control")

                self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping()
                self.igmp_snooping.parent = self
                self._children_name_map["igmp_snooping"] = "igmp-snooping"
                self._children_yang_names.add("igmp-snooping")

                self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping()
                self.mld_snooping.parent = self
                self._children_name_map["mld_snooping"] = "mld-snooping"
                self._children_yang_names.add("mld-snooping")

                self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping()
                self.dhcp_ipv4_snooping.parent = self
                self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                self._children_yang_names.add("dhcp-ipv4-snooping")
                self._segment_path = lambda: "bridge-domain" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-config/bridge-domains/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain, ['id', 'bridge_group', 'enabled', 'bd_status_change_notification', 'mtu', 'flooding_mode'], name, value)

            class FloodingMode(Enum):
                """
                FloodingMode (Enum Class)

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
                	**type**\: list of  		 :py:class:`AcMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember>`
                
                .. attribute:: vfi_member
                
                	List of Virtual Forrwarding Interfaces for current bridge\-domain
                	**type**\: list of  		 :py:class:`VfiMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember>`
                
                .. attribute:: access_pw_member
                
                	Collection of access pseudowire members.  A Pseudowires can be a regular interface with ifType 'ifPwType' or it can represented as a non\-interface context. This container provides model definition for both types of the pseudowires
                	**type**\:  :py:class:`AccessPwMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("access-pw-member", ("access_pw_member", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember))])
                    self._child_list_classes = OrderedDict([("ac-member", ("ac_member", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember)), ("vfi-member", ("vfi_member", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember))])
                    self._leafs = OrderedDict()

                    self.access_pw_member = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember()
                    self.access_pw_member.parent = self
                    self._children_name_map["access_pw_member"] = "access-pw-member"
                    self._children_yang_names.add("access-pw-member")

                    self.ac_member = YList(self)
                    self.vfi_member = YList(self)
                    self._segment_path = lambda: "members"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members, [], name, value)


                class AcMember(Entity):
                    """
                    List of Attachment circuits for current
                    bridge\-domain.
                    
                    .. attribute:: interface  (key)
                    
                    	Reference to an attchment circuit interface instance which is configured to be part of this bridge\-domain
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    .. attribute:: split_horizon_group
                    
                    	Bridge domain aggregates attachment circuits (ACs) and pseudowires (PWs) in one or more groups called Split Horizon Groups. When applied to bridge domains, Split Horizon refers to the flooding and forwarding behavior between members of a Split Horizon group. In general, frames received on one member of a split horizon group are not flooded out to the other members
                    	**type**\:  :py:class:`SplitHorizonGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup>`
                    
                    	**presence node**\: True
                    
                    .. attribute:: mac
                    
                    	MAC features for bridge domain
                    	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac>`
                    
                    .. attribute:: igmp_snooping
                    
                    	Enable IGMP snooping
                    	**type**\:  :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping>`
                    
                    .. attribute:: mld_snooping
                    
                    	Enable MLD snooping
                    	**type**\:  :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping>`
                    
                    .. attribute:: dhcp_ipv4_snooping
                    
                    	Enable DHCP IPv4 snooping
                    	**type**\:  :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping>`
                    
                    .. attribute:: flooding
                    
                    	Flooding configurations
                    	**type**\:  :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding>`
                    
                    .. attribute:: storm_control
                    
                    	A collection of storm control threshold and action configurations
                    	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl>`
                    
                    .. attribute:: dynamic_arp_inspection
                    
                    	Dynamic ARP Inspection (DAI) configurations
                    	**type**\:  :py:class:`DynamicArpInspection <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection>`
                    
                    .. attribute:: ip_source_guard
                    
                    	IP source guard (IPSG) configurations
                    	**type**\:  :py:class:`IpSourceGuard <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember, self).__init__()

                        self.yang_name = "ac-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([("split-horizon-group", ("split_horizon_group", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup)), ("mac", ("mac", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac)), ("igmp-snooping", ("igmp_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping)), ("mld-snooping", ("mld_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping)), ("dhcp-ipv4-snooping", ("dhcp_ipv4_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping)), ("flooding", ("flooding", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding)), ("storm-control", ("storm_control", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl)), ("dynamic-arp-inspection", ("dynamic_arp_inspection", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection)), ("ip-source-guard", ("ip_source_guard", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                        ])
                        self.interface = None

                        self.split_horizon_group = None
                        self._children_name_map["split_horizon_group"] = "split-horizon-group"
                        self._children_yang_names.add("split-horizon-group")

                        self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac()
                        self.mac.parent = self
                        self._children_name_map["mac"] = "mac"
                        self._children_yang_names.add("mac")

                        self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping()
                        self.igmp_snooping.parent = self
                        self._children_name_map["igmp_snooping"] = "igmp-snooping"
                        self._children_yang_names.add("igmp-snooping")

                        self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping()
                        self.mld_snooping.parent = self
                        self._children_name_map["mld_snooping"] = "mld-snooping"
                        self._children_yang_names.add("mld-snooping")

                        self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping()
                        self.dhcp_ipv4_snooping.parent = self
                        self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                        self._children_yang_names.add("dhcp-ipv4-snooping")

                        self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")

                        self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                        self.storm_control.parent = self
                        self._children_name_map["storm_control"] = "storm-control"
                        self._children_yang_names.add("storm-control")

                        self.dynamic_arp_inspection = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection()
                        self.dynamic_arp_inspection.parent = self
                        self._children_name_map["dynamic_arp_inspection"] = "dynamic-arp-inspection"
                        self._children_yang_names.add("dynamic-arp-inspection")

                        self.ip_source_guard = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard()
                        self.ip_source_guard.parent = self
                        self._children_name_map["ip_source_guard"] = "ip-source-guard"
                        self._children_yang_names.add("ip-source-guard")
                        self._segment_path = lambda: "ac-member" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember, ['interface'], name, value)


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
                        	**type**\: int
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self.is_presence_container = True
                            self._leafs = OrderedDict([
                                ('id', YLeaf(YType.uint16, 'id')),
                            ])
                            self.id = None
                            self._segment_path = lambda: "split-horizon-group"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup, ['id'], name, value)


                    class Mac(Entity):
                        """
                        MAC features for bridge domain.
                        
                        .. attribute:: learning_enabled
                        
                        	Enable disable mac learning
                        	**type**\: bool
                        
                        	**default value**\: true
                        
                        .. attribute:: limit
                        
                        	MAC table learning limit
                        	**type**\:  :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit>`
                        
                        .. attribute:: aging
                        
                        	MAC aging configurations
                        	**type**\:  :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging>`
                        
                        .. attribute:: port_down
                        
                        	Port down event
                        	**type**\:  :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown>`
                        
                        .. attribute:: secure
                        
                        	MAC secure parameters
                        	**type**\:  :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac, self).__init__()

                            self.yang_name = "mac"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("limit", ("limit", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit)), ("aging", ("aging", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging)), ("port-down", ("port_down", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown)), ("secure", ("secure", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('learning_enabled', YLeaf(YType.boolean, 'learning-enabled')),
                            ])
                            self.learning_enabled = None

                            self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit()
                            self.limit.parent = self
                            self._children_name_map["limit"] = "limit"
                            self._children_yang_names.add("limit")

                            self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging()
                            self.aging.parent = self
                            self._children_name_map["aging"] = "aging"
                            self._children_yang_names.add("aging")

                            self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown()
                            self.port_down.parent = self
                            self._children_name_map["port_down"] = "port-down"
                            self._children_yang_names.add("port-down")

                            self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure()
                            self.secure.parent = self
                            self._children_name_map["secure"] = "secure"
                            self._children_yang_names.add("secure")
                            self._segment_path = lambda: "mac"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac, ['learning_enabled'], name, value)


                        class Limit(Entity):
                            """
                            MAC table learning limit.
                            
                            .. attribute:: maximum
                            
                            	Maximum number of mac addresses that can be learnt
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: action
                            
                            	MAC limit violation actions
                            	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                            
                            .. attribute:: notification
                            
                            	MAC limit violation notifications
                            	**type**\:  :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit, self).__init__()

                                self.yang_name = "limit"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('maximum', YLeaf(YType.uint32, 'maximum')),
                                    ('action', YLeaf(YType.enumeration, 'action')),
                                    ('notification', YLeaf(YType.identityref, 'notification')),
                                ])
                                self.maximum = None
                                self.action = None
                                self.notification = None
                                self._segment_path = lambda: "limit"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit, ['maximum', 'action', 'notification'], name, value)


                        class Aging(Entity):
                            """
                            MAC aging configurations.
                            
                            .. attribute:: time
                            
                            	The timeout period in seconds for aging out dynamically learned forwarding information
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: seconds
                            
                            	**default value**\: 300
                            
                            .. attribute:: type
                            
                            	MAC aging type
                            	**type**\:  :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging, self).__init__()

                                self.yang_name = "aging"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('time', YLeaf(YType.uint32, 'time')),
                                    ('type', YLeaf(YType.enumeration, 'type')),
                                ])
                                self.time = None
                                self.type = None
                                self._segment_path = lambda: "aging"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging, ['time', 'type'], name, value)


                        class PortDown(Entity):
                            """
                            Port down event
                            
                            .. attribute:: flush
                            
                            	Enable/Disable mac table flush when port moves to down state
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown, self).__init__()

                                self.yang_name = "port-down"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('flush', YLeaf(YType.boolean, 'flush')),
                                ])
                                self.flush = None
                                self._segment_path = lambda: "port-down"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown, ['flush'], name, value)


                        class Secure(Entity):
                            """
                            MAC secure parameters.
                            
                            .. attribute:: action
                            
                            	MAC secure action for violating packets
                            	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                            
                            	**default value**\: restrict
                            
                            .. attribute:: logging
                            
                            	Enable/Disable logging
                            	**type**\: bool
                            
                            	**default value**\: false
                            
                            .. attribute:: enabled
                            
                            	Enable or disable mac secure feature
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure, self).__init__()

                                self.yang_name = "secure"
                                self.yang_parent_name = "mac"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('action', YLeaf(YType.enumeration, 'action')),
                                    ('logging', YLeaf(YType.boolean, 'logging')),
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.action = None
                                self.logging = None
                                self.enabled = None
                                self._segment_path = lambda: "secure"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure, ['action', 'logging', 'enabled'], name, value)


                    class IgmpSnooping(Entity):
                        """
                        Enable IGMP snooping.
                        
                        .. attribute:: profile_name
                        
                        	IGMP snooping profile name
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping, self).__init__()

                            self.yang_name = "igmp-snooping"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                            ])
                            self.profile_name = None
                            self._segment_path = lambda: "igmp-snooping"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping, ['profile_name'], name, value)


                    class MldSnooping(Entity):
                        """
                        Enable MLD snooping
                        
                        .. attribute:: profile_name
                        
                        	MLD snooping profile name
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping, self).__init__()

                            self.yang_name = "mld-snooping"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                            ])
                            self.profile_name = None
                            self._segment_path = lambda: "mld-snooping"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping, ['profile_name'], name, value)


                    class DhcpIpv4Snooping(Entity):
                        """
                        Enable DHCP IPv4 snooping.
                        
                        .. attribute:: profile_name
                        
                        	DHCPv4 snooping profile name
                        	**type**\: str
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping, self).__init__()

                            self.yang_name = "dhcp-ipv4-snooping"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('profile_name', YLeaf(YType.str, 'profile-name')),
                            ])
                            self.profile_name = None
                            self._segment_path = lambda: "dhcp-ipv4-snooping"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping, ['profile_name'], name, value)


                    class Flooding(Entity):
                        """
                        Flooding configurations.
                        
                        .. attribute:: disabled
                        
                        	Disable flooding
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: disabled_unknown_unicast
                        
                        	Disable unknown unicast flooding
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('disabled', YLeaf(YType.empty, 'disabled')),
                                ('disabled_unknown_unicast', YLeaf(YType.empty, 'disabled-unknown-unicast')),
                            ])
                            self.disabled = None
                            self.disabled_unknown_unicast = None
                            self._segment_path = lambda: "flooding"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding, ['disabled', 'disabled_unknown_unicast'], name, value)


                    class StormControl(Entity):
                        """
                        A collection of storm control threshold and action
                        configurations.
                        
                        .. attribute:: thresholds
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of  		 :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds>`
                        
                        .. attribute:: action
                        
                        	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                        	**type**\:  :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__init__()

                            self.yang_name = "storm-control"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("thresholds", ("thresholds", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds))])
                            self._leafs = OrderedDict([
                                ('action', YLeaf(YType.identityref, 'action')),
                            ])
                            self.action = None

                            self.thresholds = YList(self)
                            self._segment_path = lambda: "storm-control"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, ['action'], name, value)


                        class Thresholds(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  (key)
                            
                            	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                            	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: value
                            
                            	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            .. attribute:: unit
                            
                            	This enumeration define unit of the traffic threshold value
                            	**type**\:  :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.Unit>`
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds, self).__init__()

                                self.yang_name = "thresholds"
                                self.yang_parent_name = "storm-control"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['traffic_class']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                                    ('value', YLeaf(YType.uint32, 'value')),
                                    ('unit', YLeaf(YType.enumeration, 'unit')),
                                ])
                                self.traffic_class = None
                                self.value = None
                                self.unit = None
                                self._segment_path = lambda: "thresholds" + "[traffic-class='" + str(self.traffic_class) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds, ['traffic_class', 'value', 'unit'], name, value)

                            class Unit(Enum):
                                """
                                Unit (Enum Class)

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



                    class DynamicArpInspection(Entity):
                        """
                        Dynamic ARP Inspection (DAI) configurations.
                        
                        .. attribute:: address_validation
                        
                        	Enable address validation
                        	**type**\:  :py:class:`AddressValidation <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: logging
                        
                        	Enable DAI logging
                        	**type**\: bool
                        
                        .. attribute:: enable
                        
                        	Enable or disable Dynamic ARP Inspection
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection, self).__init__()

                            self.yang_name = "dynamic-arp-inspection"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([("address-validation", ("address_validation", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('logging', YLeaf(YType.boolean, 'logging')),
                                ('enable', YLeaf(YType.boolean, 'enable')),
                            ])
                            self.logging = None
                            self.enable = None

                            self.address_validation = None
                            self._children_name_map["address_validation"] = "address-validation"
                            self._children_yang_names.add("address-validation")
                            self._segment_path = lambda: "dynamic-arp-inspection"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection, ['logging', 'enable'], name, value)


                        class AddressValidation(Entity):
                            """
                            Enable address validation.
                            
                            .. attribute:: dst_mac
                            
                            	Match Destination MAC Address
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: src_mac
                            
                            	Match Source MAC Address
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: ipv4
                            
                            	Match IPv4 Address
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation, self).__init__()

                                self.yang_name = "address-validation"
                                self.yang_parent_name = "dynamic-arp-inspection"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('dst_mac', YLeaf(YType.empty, 'dst-mac')),
                                    ('src_mac', YLeaf(YType.empty, 'src-mac')),
                                    ('ipv4', YLeaf(YType.empty, 'ipv4')),
                                ])
                                self.dst_mac = None
                                self.src_mac = None
                                self.ipv4 = None
                                self._segment_path = lambda: "address-validation"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation, ['dst_mac', 'src_mac', 'ipv4'], name, value)


                    class IpSourceGuard(Entity):
                        """
                        IP source guard (IPSG) configurations.
                        
                        .. attribute:: logging
                        
                        	Enable IPSG logging
                        	**type**\: bool
                        
                        	**default value**\: false
                        
                        .. attribute:: enable
                        
                        	Enable or disable IP source guard feature
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard, self).__init__()

                            self.yang_name = "ip-source-guard"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('logging', YLeaf(YType.boolean, 'logging')),
                                ('enable', YLeaf(YType.boolean, 'enable')),
                            ])
                            self.logging = None
                            self.enable = None
                            self._segment_path = lambda: "ip-source-guard"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard, ['logging', 'enable'], name, value)


                class VfiMember(Entity):
                    """
                    List of Virtual Forrwarding Interfaces for current
                    bridge\-domain.
                    
                    .. attribute:: interface  (key)
                    
                    	Reference to an Virtual Forwarding Interface instance which is configured to be part of this bridge\-domain
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember, self).__init__()

                        self.yang_name = "vfi-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                        ])
                        self.interface = None
                        self._segment_path = lambda: "vfi-member" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember, ['interface'], name, value)


                class AccessPwMember(Entity):
                    """
                    Collection of access pseudowire members.
                    
                    A Pseudowires can be a regular interface with ifType
                    'ifPwType' or it can represented as a non\-interface
                    context. This container provides model definition for
                    both types of the pseudowires.
                    
                    .. attribute:: access_pw_if_member
                    
                    	List of interface based access pseudowires for current bridge\-domain
                    	**type**\: list of  		 :py:class:`AccessPwIfMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember>`
                    
                    .. attribute:: pw_neighbor_spec
                    
                    	Collection of neighbor specification based pseudo\-wires
                    	**type**\: list of  		 :py:class:`PwNeighborSpec <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__init__()

                        self.yang_name = "access-pw-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("access-pw-if-member", ("access_pw_if_member", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember)), ("pw-neighbor-spec", ("pw_neighbor_spec", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec))])
                        self._leafs = OrderedDict()

                        self.access_pw_if_member = YList(self)
                        self.pw_neighbor_spec = YList(self)
                        self._segment_path = lambda: "access-pw-member"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember, [], name, value)


                    class AccessPwIfMember(Entity):
                        """
                        List of interface based access pseudowires for
                        current bridge\-domain.
                        
                        .. attribute:: interface  (key)
                        
                        	Reference to an access pseudo\-wire interface instance which is configured to be part of this bridge domain
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember, self).__init__()

                            self.yang_name = "access-pw-if-member"
                            self.yang_parent_name = "access-pw-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface', YLeaf(YType.str, 'interface')),
                            ])
                            self.interface = None
                            self._segment_path = lambda: "access-pw-if-member" + "[interface='" + str(self.interface) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember, ['interface'], name, value)


                    class PwNeighborSpec(Entity):
                        """
                        Collection of neighbor specification based
                        pseudo\-wires.
                        
                        .. attribute:: neighbor_ip_address  (key)
                        
                        	IPv4 or IPv6 address of the neighbor
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vc_id  (key)
                        
                        	Pseudowire VC ID
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: static_label
                        
                        	Statically configured labels, signalling should be none
                        	**type**\:  :py:class:`StaticLabel <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel>`
                        
                        .. attribute:: pw_class_template
                        
                        	Reference to a pseudowire template
                        	**type**\: str
                        
                        	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
                        
                        .. attribute:: encap_type
                        
                        	Encapsulation configuration for this neighbor
                        	**type**\:  :py:class:`PwEncapsulationType <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationType>`
                        
                        .. attribute:: tag_impose_vlan
                        
                        	Specify a tag for a VLAN ID for the pseudowire
                        	**type**\: int
                        
                        	**range:** 1..4094
                        
                        .. attribute:: source_ipv6
                        
                        	The local source IPv6 address. Note this should only be configured when neighbor address is IPv6 type
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: split_horizon_group
                        
                        	Bridge domain aggregates attachment circuits (ACs) and pseudowires (PWs) in one or more groups called Split Horizon Groups. When applied to bridge domains, Split Horizon refers to the flooding and forwarding behavior between members of a Split Horizon group. In general, frames received on one member of a split horizon group are not flooded out to the other members
                        	**type**\:  :py:class:`SplitHorizonGroup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: mac
                        
                        	MAC features for bridge domain
                        	**type**\:  :py:class:`Mac <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac>`
                        
                        .. attribute:: igmp_snooping
                        
                        	Enable IGMP snooping
                        	**type**\:  :py:class:`IgmpSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping>`
                        
                        .. attribute:: mld_snooping
                        
                        	Enable MLD snooping
                        	**type**\:  :py:class:`MldSnooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping>`
                        
                        .. attribute:: dhcp_ipv4_snooping
                        
                        	Enable DHCP IPv4 snooping
                        	**type**\:  :py:class:`DhcpIpv4Snooping <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping>`
                        
                        .. attribute:: flooding
                        
                        	Flooding configurations
                        	**type**\:  :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding>`
                        
                        .. attribute:: storm_control
                        
                        	A collection of storm control threshold and action configurations
                        	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl>`
                        
                        .. attribute:: backup
                        
                        	Backup pseudo\-wire
                        	**type**\:  :py:class:`Backup <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec, self).__init__()

                            self.yang_name = "pw-neighbor-spec"
                            self.yang_parent_name = "access-pw-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['neighbor_ip_address','vc_id']
                            self._child_container_classes = OrderedDict([("static-label", ("static_label", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel)), ("split-horizon-group", ("split_horizon_group", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup)), ("mac", ("mac", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac)), ("igmp-snooping", ("igmp_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping)), ("mld-snooping", ("mld_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping)), ("dhcp-ipv4-snooping", ("dhcp_ipv4_snooping", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping)), ("flooding", ("flooding", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding)), ("storm-control", ("storm_control", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl)), ("backup", ("backup", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('neighbor_ip_address', YLeaf(YType.str, 'neighbor-ip-address')),
                                ('vc_id', YLeaf(YType.uint32, 'vc-id')),
                                ('pw_class_template', YLeaf(YType.str, 'pw-class-template')),
                                ('encap_type', YLeaf(YType.identityref, 'encap-type')),
                                ('tag_impose_vlan', YLeaf(YType.uint16, 'tag-impose-vlan')),
                                ('source_ipv6', YLeaf(YType.str, 'source-ipv6')),
                            ])
                            self.neighbor_ip_address = None
                            self.vc_id = None
                            self.pw_class_template = None
                            self.encap_type = None
                            self.tag_impose_vlan = None
                            self.source_ipv6 = None

                            self.static_label = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel()
                            self.static_label.parent = self
                            self._children_name_map["static_label"] = "static-label"
                            self._children_yang_names.add("static-label")

                            self.split_horizon_group = None
                            self._children_name_map["split_horizon_group"] = "split-horizon-group"
                            self._children_yang_names.add("split-horizon-group")

                            self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac()
                            self.mac.parent = self
                            self._children_name_map["mac"] = "mac"
                            self._children_yang_names.add("mac")

                            self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping()
                            self.igmp_snooping.parent = self
                            self._children_name_map["igmp_snooping"] = "igmp-snooping"
                            self._children_yang_names.add("igmp-snooping")

                            self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping()
                            self.mld_snooping.parent = self
                            self._children_name_map["mld_snooping"] = "mld-snooping"
                            self._children_yang_names.add("mld-snooping")

                            self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping()
                            self.dhcp_ipv4_snooping.parent = self
                            self._children_name_map["dhcp_ipv4_snooping"] = "dhcp-ipv4-snooping"
                            self._children_yang_names.add("dhcp-ipv4-snooping")

                            self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding()
                            self.flooding.parent = self
                            self._children_name_map["flooding"] = "flooding"
                            self._children_yang_names.add("flooding")

                            self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl()
                            self.storm_control.parent = self
                            self._children_name_map["storm_control"] = "storm-control"
                            self._children_yang_names.add("storm-control")

                            self.backup = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup()
                            self.backup.parent = self
                            self._children_name_map["backup"] = "backup"
                            self._children_yang_names.add("backup")
                            self._segment_path = lambda: "pw-neighbor-spec" + "[neighbor-ip-address='" + str(self.neighbor_ip_address) + "']" + "[vc-id='" + str(self.vc_id) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec, ['neighbor_ip_address', 'vc_id', 'pw_class_template', 'encap_type', 'tag_impose_vlan', 'source_ipv6'], name, value)


                        class StaticLabel(Entity):
                            """
                            Statically configured labels, signalling should be none
                            
                            .. attribute:: local_label
                            
                            	Local MPLS label ID
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            .. attribute:: remote_label
                            
                            	Remote MPLS label ID
                            	**type**\: int
                            
                            	**range:** 16..1048575
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel, self).__init__()

                                self.yang_name = "static-label"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('local_label', YLeaf(YType.uint32, 'local-label')),
                                    ('remote_label', YLeaf(YType.uint32, 'remote-label')),
                                ])
                                self.local_label = None
                                self.remote_label = None
                                self._segment_path = lambda: "static-label"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel, ['local_label', 'remote_label'], name, value)


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
                            	**type**\: int
                            
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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('id', YLeaf(YType.uint16, 'id')),
                                ])
                                self.id = None
                                self._segment_path = lambda: "split-horizon-group"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup, ['id'], name, value)


                        class Mac(Entity):
                            """
                            MAC features for bridge domain.
                            
                            .. attribute:: learning_enabled
                            
                            	Enable disable mac learning
                            	**type**\: bool
                            
                            	**default value**\: true
                            
                            .. attribute:: limit
                            
                            	MAC table learning limit
                            	**type**\:  :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit>`
                            
                            .. attribute:: aging
                            
                            	MAC aging configurations
                            	**type**\:  :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging>`
                            
                            .. attribute:: port_down
                            
                            	Port down event
                            	**type**\:  :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown>`
                            
                            .. attribute:: secure
                            
                            	MAC secure parameters
                            	**type**\:  :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac, self).__init__()

                                self.yang_name = "mac"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([("limit", ("limit", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit)), ("aging", ("aging", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging)), ("port-down", ("port_down", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown)), ("secure", ("secure", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('learning_enabled', YLeaf(YType.boolean, 'learning-enabled')),
                                ])
                                self.learning_enabled = None

                                self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit()
                                self.limit.parent = self
                                self._children_name_map["limit"] = "limit"
                                self._children_yang_names.add("limit")

                                self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging()
                                self.aging.parent = self
                                self._children_name_map["aging"] = "aging"
                                self._children_yang_names.add("aging")

                                self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown()
                                self.port_down.parent = self
                                self._children_name_map["port_down"] = "port-down"
                                self._children_yang_names.add("port-down")

                                self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure()
                                self.secure.parent = self
                                self._children_name_map["secure"] = "secure"
                                self._children_yang_names.add("secure")
                                self._segment_path = lambda: "mac"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac, ['learning_enabled'], name, value)


                            class Limit(Entity):
                                """
                                MAC table learning limit.
                                
                                .. attribute:: maximum
                                
                                	Maximum number of mac addresses that can be learnt
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: action
                                
                                	MAC limit violation actions
                                	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                                
                                .. attribute:: notification
                                
                                	MAC limit violation notifications
                                	**type**\:  :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit, self).__init__()

                                    self.yang_name = "limit"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('maximum', YLeaf(YType.uint32, 'maximum')),
                                        ('action', YLeaf(YType.enumeration, 'action')),
                                        ('notification', YLeaf(YType.identityref, 'notification')),
                                    ])
                                    self.maximum = None
                                    self.action = None
                                    self.notification = None
                                    self._segment_path = lambda: "limit"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit, ['maximum', 'action', 'notification'], name, value)


                            class Aging(Entity):
                                """
                                MAC aging configurations.
                                
                                .. attribute:: time
                                
                                	The timeout period in seconds for aging out dynamically learned forwarding information
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: seconds
                                
                                	**default value**\: 300
                                
                                .. attribute:: type
                                
                                	MAC aging type
                                	**type**\:  :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging, self).__init__()

                                    self.yang_name = "aging"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('time', YLeaf(YType.uint32, 'time')),
                                        ('type', YLeaf(YType.enumeration, 'type')),
                                    ])
                                    self.time = None
                                    self.type = None
                                    self._segment_path = lambda: "aging"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging, ['time', 'type'], name, value)


                            class PortDown(Entity):
                                """
                                Port down event
                                
                                .. attribute:: flush
                                
                                	Enable/Disable mac table flush when port moves to down state
                                	**type**\: bool
                                
                                	**default value**\: true
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown, self).__init__()

                                    self.yang_name = "port-down"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('flush', YLeaf(YType.boolean, 'flush')),
                                    ])
                                    self.flush = None
                                    self._segment_path = lambda: "port-down"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown, ['flush'], name, value)


                            class Secure(Entity):
                                """
                                MAC secure parameters.
                                
                                .. attribute:: action
                                
                                	MAC secure action for violating packets
                                	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                                
                                	**default value**\: restrict
                                
                                .. attribute:: logging
                                
                                	Enable/Disable logging
                                	**type**\: bool
                                
                                	**default value**\: false
                                
                                .. attribute:: enabled
                                
                                	Enable or disable mac secure feature
                                	**type**\: bool
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure, self).__init__()

                                    self.yang_name = "secure"
                                    self.yang_parent_name = "mac"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('action', YLeaf(YType.enumeration, 'action')),
                                        ('logging', YLeaf(YType.boolean, 'logging')),
                                        ('enabled', YLeaf(YType.boolean, 'enabled')),
                                    ])
                                    self.action = None
                                    self.logging = None
                                    self.enabled = None
                                    self._segment_path = lambda: "secure"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure, ['action', 'logging', 'enabled'], name, value)


                        class IgmpSnooping(Entity):
                            """
                            Enable IGMP snooping.
                            
                            .. attribute:: profile_name
                            
                            	IGMP snooping profile name
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping, self).__init__()

                                self.yang_name = "igmp-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "igmp-snooping"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping, ['profile_name'], name, value)


                        class MldSnooping(Entity):
                            """
                            Enable MLD snooping
                            
                            .. attribute:: profile_name
                            
                            	MLD snooping profile name
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping, self).__init__()

                                self.yang_name = "mld-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "mld-snooping"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping, ['profile_name'], name, value)


                        class DhcpIpv4Snooping(Entity):
                            """
                            Enable DHCP IPv4 snooping.
                            
                            .. attribute:: profile_name
                            
                            	DHCPv4 snooping profile name
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping, self).__init__()

                                self.yang_name = "dhcp-ipv4-snooping"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('profile_name', YLeaf(YType.str, 'profile-name')),
                                ])
                                self.profile_name = None
                                self._segment_path = lambda: "dhcp-ipv4-snooping"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping, ['profile_name'], name, value)


                        class Flooding(Entity):
                            """
                            Flooding configurations.
                            
                            .. attribute:: disabled
                            
                            	Disable flooding
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: disabled_unknown_unicast
                            
                            	Disable unknown unicast flooding
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding, self).__init__()

                                self.yang_name = "flooding"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('disabled', YLeaf(YType.empty, 'disabled')),
                                    ('disabled_unknown_unicast', YLeaf(YType.empty, 'disabled-unknown-unicast')),
                                ])
                                self.disabled = None
                                self.disabled_unknown_unicast = None
                                self._segment_path = lambda: "flooding"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding, ['disabled', 'disabled_unknown_unicast'], name, value)


                        class StormControl(Entity):
                            """
                            A collection of storm control threshold and action
                            configurations.
                            
                            .. attribute:: thresholds
                            
                            	A collection of storm control threshold configuration entries
                            	**type**\: list of  		 :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds>`
                            
                            .. attribute:: action
                            
                            	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                            	**type**\:  :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl, self).__init__()

                                self.yang_name = "storm-control"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([("thresholds", ("thresholds", BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds))])
                                self._leafs = OrderedDict([
                                    ('action', YLeaf(YType.identityref, 'action')),
                                ])
                                self.action = None

                                self.thresholds = YList(self)
                                self._segment_path = lambda: "storm-control"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl, ['action'], name, value)


                            class Thresholds(Entity):
                                """
                                A collection of storm control threshold configuration
                                entries.
                                
                                .. attribute:: traffic_class  (key)
                                
                                	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                                	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                                
                                .. attribute:: value
                                
                                	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**mandatory**\: True
                                
                                .. attribute:: unit
                                
                                	This enumeration define unit of the traffic threshold value
                                	**type**\:  :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.Unit>`
                                
                                	**mandatory**\: True
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds, self).__init__()

                                    self.yang_name = "thresholds"
                                    self.yang_parent_name = "storm-control"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = ['traffic_class']
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                                        ('value', YLeaf(YType.uint32, 'value')),
                                        ('unit', YLeaf(YType.enumeration, 'unit')),
                                    ])
                                    self.traffic_class = None
                                    self.value = None
                                    self.unit = None
                                    self._segment_path = lambda: "thresholds" + "[traffic-class='" + str(self.traffic_class) + "']"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds, ['traffic_class', 'value', 'unit'], name, value)

                                class Unit(Enum):
                                    """
                                    Unit (Enum Class)

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



                        class Backup(Entity):
                            """
                            Backup pseudo\-wire.
                            
                            .. attribute:: neighbor_ip_address
                            
                            	IPv4 or IPv6 address of the neighbor
                            	**type**\: union of the below types:
                            
                            		**type**\: str
                            
                            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            		**type**\: str
                            
                            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vc_id
                            
                            	Pseudowire VC ID
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: pw_class_template
                            
                            	Reference to a pseudowire template
                            	**type**\: str
                            
                            	**refers to**\:  :py:class:`name <ydk.models.cisco_ios_xe.cisco_pw.PseudowireConfig.PwTemplates.PwTemplate>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup, self).__init__()

                                self.yang_name = "backup"
                                self.yang_parent_name = "pw-neighbor-spec"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('neighbor_ip_address', YLeaf(YType.str, 'neighbor-ip-address')),
                                    ('vc_id', YLeaf(YType.uint32, 'vc-id')),
                                    ('pw_class_template', YLeaf(YType.str, 'pw-class-template')),
                                ])
                                self.neighbor_ip_address = None
                                self.vc_id = None
                                self.pw_class_template = None
                                self._segment_path = lambda: "backup"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup, ['neighbor_ip_address', 'vc_id', 'pw_class_template'], name, value)


            class Mac(Entity):
                """
                MAC features for bridge domain.
                
                .. attribute:: learning_enabled
                
                	Enable disable mac learning
                	**type**\: bool
                
                	**default value**\: true
                
                .. attribute:: limit
                
                	MAC table learning limit
                	**type**\:  :py:class:`Limit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit>`
                
                .. attribute:: aging
                
                	MAC aging configurations
                	**type**\:  :py:class:`Aging <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging>`
                
                .. attribute:: port_down
                
                	Port down event
                	**type**\:  :py:class:`PortDown <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown>`
                
                .. attribute:: flooding
                
                	Flooding configurations
                	**type**\:  :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding>`
                
                .. attribute:: secure
                
                	MAC secure parameters
                	**type**\:  :py:class:`Secure <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure>`
                
                	**presence node**\: True
                
                .. attribute:: static
                
                	Static mac address list parameters
                	**type**\:  :py:class:`Static <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac, self).__init__()

                    self.yang_name = "mac"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("limit", ("limit", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit)), ("aging", ("aging", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging)), ("port-down", ("port_down", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown)), ("flooding", ("flooding", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding)), ("secure", ("secure", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure)), ("static", ("static", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('learning_enabled', YLeaf(YType.boolean, 'learning-enabled')),
                    ])
                    self.learning_enabled = None

                    self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit()
                    self.limit.parent = self
                    self._children_name_map["limit"] = "limit"
                    self._children_yang_names.add("limit")

                    self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging()
                    self.aging.parent = self
                    self._children_name_map["aging"] = "aging"
                    self._children_yang_names.add("aging")

                    self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown()
                    self.port_down.parent = self
                    self._children_name_map["port_down"] = "port-down"
                    self._children_yang_names.add("port-down")

                    self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding()
                    self.flooding.parent = self
                    self._children_name_map["flooding"] = "flooding"
                    self._children_yang_names.add("flooding")

                    self.secure = None
                    self._children_name_map["secure"] = "secure"
                    self._children_yang_names.add("secure")

                    self.static = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static()
                    self.static.parent = self
                    self._children_name_map["static"] = "static"
                    self._children_yang_names.add("static")
                    self._segment_path = lambda: "mac"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac, ['learning_enabled'], name, value)


                class Limit(Entity):
                    """
                    MAC table learning limit.
                    
                    .. attribute:: maximum
                    
                    	Maximum number of mac addresses that can be learnt
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: action
                    
                    	MAC limit violation actions
                    	**type**\:  :py:class:`MacLimitAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitAction>`
                    
                    .. attribute:: notification
                    
                    	MAC limit violation notifications
                    	**type**\:  :py:class:`MacLimitNotificationType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationType>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit, self).__init__()

                        self.yang_name = "limit"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('maximum', YLeaf(YType.uint32, 'maximum')),
                            ('action', YLeaf(YType.enumeration, 'action')),
                            ('notification', YLeaf(YType.identityref, 'notification')),
                        ])
                        self.maximum = None
                        self.action = None
                        self.notification = None
                        self._segment_path = lambda: "limit"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit, ['maximum', 'action', 'notification'], name, value)


                class Aging(Entity):
                    """
                    MAC aging configurations.
                    
                    .. attribute:: time
                    
                    	The timeout period in seconds for aging out dynamically learned forwarding information
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    	**default value**\: 300
                    
                    .. attribute:: type
                    
                    	MAC aging type
                    	**type**\:  :py:class:`MacAgingType <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingType>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging, self).__init__()

                        self.yang_name = "aging"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('time', YLeaf(YType.uint32, 'time')),
                            ('type', YLeaf(YType.enumeration, 'type')),
                        ])
                        self.time = None
                        self.type = None
                        self._segment_path = lambda: "aging"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging, ['time', 'type'], name, value)


                class PortDown(Entity):
                    """
                    Port down event
                    
                    .. attribute:: flush
                    
                    	Enable/Disable mac table flush when port moves to down state
                    	**type**\: bool
                    
                    	**default value**\: true
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown, self).__init__()

                        self.yang_name = "port-down"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('flush', YLeaf(YType.boolean, 'flush')),
                        ])
                        self.flush = None
                        self._segment_path = lambda: "port-down"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown, ['flush'], name, value)


                class Flooding(Entity):
                    """
                    Flooding configurations.
                    
                    .. attribute:: disabled
                    
                    	Disable flooding
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: disabled_unknown_unicast
                    
                    	Disable unknown unicast flooding
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding, self).__init__()

                        self.yang_name = "flooding"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('disabled', YLeaf(YType.empty, 'disabled')),
                            ('disabled_unknown_unicast', YLeaf(YType.empty, 'disabled-unknown-unicast')),
                        ])
                        self.disabled = None
                        self.disabled_unknown_unicast = None
                        self._segment_path = lambda: "flooding"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding, ['disabled', 'disabled_unknown_unicast'], name, value)


                class Secure(Entity):
                    """
                    MAC secure parameters.
                    
                    .. attribute:: action
                    
                    	MAC secure action for violating packets
                    	**type**\:  :py:class:`MacSecureAction <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureAction>`
                    
                    	**default value**\: restrict
                    
                    .. attribute:: logging
                    
                    	Enable/Disable logging
                    	**type**\: bool
                    
                    	**default value**\: false
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure, self).__init__()

                        self.yang_name = "secure"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('action', YLeaf(YType.enumeration, 'action')),
                            ('logging', YLeaf(YType.boolean, 'logging')),
                        ])
                        self.action = None
                        self.logging = None
                        self._segment_path = lambda: "secure"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure, ['action', 'logging'], name, value)


                class Static(Entity):
                    """
                    Static mac address list parameters.
                    
                    .. attribute:: mac_addresses
                    
                    	MAC address entry
                    	**type**\: list of  		 :py:class:`MacAddresses <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static, self).__init__()

                        self.yang_name = "static"
                        self.yang_parent_name = "mac"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("mac-addresses", ("mac_addresses", BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses))])
                        self._leafs = OrderedDict()

                        self.mac_addresses = YList(self)
                        self._segment_path = lambda: "static"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static, [], name, value)


                    class MacAddresses(Entity):
                        """
                        MAC address entry.
                        
                        .. attribute:: mac_addr  (key)
                        
                        	Static MAC address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: drop
                        
                        	Drop packet
                        	**type**\: bool
                        
                        	**mandatory**\: True
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses, self).__init__()

                            self.yang_name = "mac-addresses"
                            self.yang_parent_name = "static"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['mac_addr']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('mac_addr', YLeaf(YType.str, 'mac-addr')),
                                ('drop', YLeaf(YType.boolean, 'drop')),
                            ])
                            self.mac_addr = None
                            self.drop = None
                            self._segment_path = lambda: "mac-addresses" + "[mac-addr='" + str(self.mac_addr) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses, ['mac_addr', 'drop'], name, value)


            class DynamicArpInspection(Entity):
                """
                Dynamic ARP Inspection (DAI) configurations.
                
                .. attribute:: address_validation
                
                	Enable address validation
                	**type**\:  :py:class:`AddressValidation <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation>`
                
                	**presence node**\: True
                
                .. attribute:: logging
                
                	Enable DAI logging
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection, self).__init__()

                    self.yang_name = "dynamic-arp-inspection"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("address-validation", ("address_validation", BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation))])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('logging', YLeaf(YType.boolean, 'logging')),
                    ])
                    self.logging = None

                    self.address_validation = None
                    self._children_name_map["address_validation"] = "address-validation"
                    self._children_yang_names.add("address-validation")
                    self._segment_path = lambda: "dynamic-arp-inspection"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection, ['logging'], name, value)


                class AddressValidation(Entity):
                    """
                    Enable address validation.
                    
                    .. attribute:: dst_mac
                    
                    	Match Destination MAC Address
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: src_mac
                    
                    	Match Source MAC Address
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: ipv4
                    
                    	Match IPv4 Address
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation, self).__init__()

                        self.yang_name = "address-validation"
                        self.yang_parent_name = "dynamic-arp-inspection"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('dst_mac', YLeaf(YType.empty, 'dst-mac')),
                            ('src_mac', YLeaf(YType.empty, 'src-mac')),
                            ('ipv4', YLeaf(YType.empty, 'ipv4')),
                        ])
                        self.dst_mac = None
                        self.src_mac = None
                        self.ipv4 = None
                        self._segment_path = lambda: "address-validation"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation, ['dst_mac', 'src_mac', 'ipv4'], name, value)


            class IpSourceGuard(Entity):
                """
                IP source guard (IPSG) configurations.
                
                .. attribute:: logging
                
                	Enable IPSG logging
                	**type**\: bool
                
                	**default value**\: false
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard, self).__init__()

                    self.yang_name = "ip-source-guard"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self.is_presence_container = True
                    self._leafs = OrderedDict([
                        ('logging', YLeaf(YType.boolean, 'logging')),
                    ])
                    self.logging = None
                    self._segment_path = lambda: "ip-source-guard"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard, ['logging'], name, value)


            class StormControl(Entity):
                """
                A collection of storm control threshold and action
                configurations.
                
                .. attribute:: thresholds
                
                	A collection of storm control threshold configuration entries
                	**type**\: list of  		 :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds>`
                
                .. attribute:: action
                
                	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                	**type**\:  :py:class:`StormControlAction <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlAction>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl, self).__init__()

                    self.yang_name = "storm-control"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("thresholds", ("thresholds", BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds))])
                    self._leafs = OrderedDict([
                        ('action', YLeaf(YType.identityref, 'action')),
                    ])
                    self.action = None

                    self.thresholds = YList(self)
                    self._segment_path = lambda: "storm-control"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl, ['action'], name, value)


                class Thresholds(Entity):
                    """
                    A collection of storm control threshold configuration
                    entries.
                    
                    .. attribute:: traffic_class  (key)
                    
                    	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                    	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                    
                    .. attribute:: value
                    
                    	Traffic threshold value. Unit of the value is indicated by leaf 'unit'
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**mandatory**\: True
                    
                    .. attribute:: unit
                    
                    	This enumeration define unit of the traffic threshold value
                    	**type**\:  :py:class:`Unit <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.Unit>`
                    
                    	**mandatory**\: True
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds, self).__init__()

                        self.yang_name = "thresholds"
                        self.yang_parent_name = "storm-control"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['traffic_class']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                            ('value', YLeaf(YType.uint32, 'value')),
                            ('unit', YLeaf(YType.enumeration, 'unit')),
                        ])
                        self.traffic_class = None
                        self.value = None
                        self.unit = None
                        self._segment_path = lambda: "thresholds" + "[traffic-class='" + str(self.traffic_class) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds, ['traffic_class', 'value', 'unit'], name, value)

                    class Unit(Enum):
                        """
                        Unit (Enum Class)

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



            class IgmpSnooping(Entity):
                """
                Enable IGMP snooping.
                
                .. attribute:: profile_name
                
                	IGMP snooping profile name
                	**type**\: str
                
                .. attribute:: disabled
                
                	Disable IGMP snooping
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping, self).__init__()

                    self.yang_name = "igmp-snooping"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile_name', YLeaf(YType.str, 'profile-name')),
                        ('disabled', YLeaf(YType.empty, 'disabled')),
                    ])
                    self.profile_name = None
                    self.disabled = None
                    self._segment_path = lambda: "igmp-snooping"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping, ['profile_name', 'disabled'], name, value)


            class MldSnooping(Entity):
                """
                Enable MLD snooping
                
                .. attribute:: profile_name
                
                	MLD snooping profile name
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping, self).__init__()

                    self.yang_name = "mld-snooping"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile_name', YLeaf(YType.str, 'profile-name')),
                    ])
                    self.profile_name = None
                    self._segment_path = lambda: "mld-snooping"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping, ['profile_name'], name, value)


            class DhcpIpv4Snooping(Entity):
                """
                Enable DHCP IPv4 snooping.
                
                .. attribute:: profile_name
                
                	DHCPv4 snooping profile name
                	**type**\: str
                
                	**mandatory**\: True
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping, self).__init__()

                    self.yang_name = "dhcp-ipv4-snooping"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('profile_name', YLeaf(YType.str, 'profile-name')),
                    ])
                    self.profile_name = None
                    self._segment_path = lambda: "dhcp-ipv4-snooping"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping, ['profile_name'], name, value)

    def clone_ptr(self):
        self._top_entity = BridgeDomainConfig()
        return self._top_entity

class BridgeDomainState(Entity):
    """
    This container defines bridge\-domain operational data.
    
    .. attribute:: system_capabilities
    
    	This container defines system capabilities for bridge domain
    	**type**\:  :py:class:`SystemCapabilities <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.SystemCapabilities>`
    
    .. attribute:: module_capabilities
    
    	This container defines module capabilities for bridge domain
    	**type**\:  :py:class:`ModuleCapabilities <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.ModuleCapabilities>`
    
    .. attribute:: bridge_domains
    
    	Bridge domain state data
    	**type**\:  :py:class:`BridgeDomains <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains>`
    
    .. attribute:: mac_table
    
    	This list contains mac\-address entries for bridge domains
    	**type**\: list of  		 :py:class:`MacTable <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.MacTable>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(BridgeDomainState, self).__init__()
        self._top_entity = None

        self.yang_name = "bridge-domain-state"
        self.yang_parent_name = "cisco-bridge-domain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("system-capabilities", ("system_capabilities", BridgeDomainState.SystemCapabilities)), ("module-capabilities", ("module_capabilities", BridgeDomainState.ModuleCapabilities)), ("bridge-domains", ("bridge_domains", BridgeDomainState.BridgeDomains))])
        self._child_list_classes = OrderedDict([("mac-table", ("mac_table", BridgeDomainState.MacTable))])
        self._leafs = OrderedDict()

        self.system_capabilities = BridgeDomainState.SystemCapabilities()
        self.system_capabilities.parent = self
        self._children_name_map["system_capabilities"] = "system-capabilities"
        self._children_yang_names.add("system-capabilities")

        self.module_capabilities = BridgeDomainState.ModuleCapabilities()
        self.module_capabilities.parent = self
        self._children_name_map["module_capabilities"] = "module-capabilities"
        self._children_yang_names.add("module-capabilities")

        self.bridge_domains = BridgeDomainState.BridgeDomains()
        self.bridge_domains.parent = self
        self._children_name_map["bridge_domains"] = "bridge-domains"
        self._children_yang_names.add("bridge-domains")

        self.mac_table = YList(self)
        self._segment_path = lambda: "cisco-bridge-domain:bridge-domain-state"

    def __setattr__(self, name, value):
        self._perform_setattr(BridgeDomainState, [], name, value)


    class SystemCapabilities(Entity):
        """
        This container defines system capabilities for bridge
        domain.
        
        .. attribute:: max_bd
        
        	Maximum number of bridge\-domains suported
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_ac_per_bd
        
        	Maximum number of attachment circuits per bridge\-domains
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_pw_per_bd
        
        	Maximum number of access pseudowires per bridge\-domains
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_vfi_per_bd
        
        	Maximum number of virtual forwarding instances per bridge\-domains
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_sh_group_per_bd
        
        	Maximum number of Split Horizon groups per bridge\-domains
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: max_interflex_if_per_bd
        
        	Maximum number of Interflex interfaces per bridge\-domains
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.SystemCapabilities, self).__init__()

            self.yang_name = "system-capabilities"
            self.yang_parent_name = "bridge-domain-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('max_bd', YLeaf(YType.uint32, 'max-bd')),
                ('max_ac_per_bd', YLeaf(YType.uint32, 'max-ac-per-bd')),
                ('max_pw_per_bd', YLeaf(YType.uint32, 'max-pw-per-bd')),
                ('max_vfi_per_bd', YLeaf(YType.uint32, 'max-vfi-per-bd')),
                ('max_sh_group_per_bd', YLeaf(YType.uint32, 'max-sh-group-per-bd')),
                ('max_interflex_if_per_bd', YLeaf(YType.uint32, 'max-interflex-if-per-bd')),
            ])
            self.max_bd = None
            self.max_ac_per_bd = None
            self.max_pw_per_bd = None
            self.max_vfi_per_bd = None
            self.max_sh_group_per_bd = None
            self.max_interflex_if_per_bd = None
            self._segment_path = lambda: "system-capabilities"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainState.SystemCapabilities, ['max_bd', 'max_ac_per_bd', 'max_pw_per_bd', 'max_vfi_per_bd', 'max_sh_group_per_bd', 'max_interflex_if_per_bd'], name, value)


    class ModuleCapabilities(Entity):
        """
        This container defines module capabilities for bridge
        domain.
        
        .. attribute:: modules
        
        	Collection of capabillity statements for hardware module in the system
        	**type**\: list of  		 :py:class:`Modules <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.ModuleCapabilities.Modules>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.ModuleCapabilities, self).__init__()

            self.yang_name = "module-capabilities"
            self.yang_parent_name = "bridge-domain-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("modules", ("modules", BridgeDomainState.ModuleCapabilities.Modules))])
            self._leafs = OrderedDict()

            self.modules = YList(self)
            self._segment_path = lambda: "module-capabilities"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainState.ModuleCapabilities, [], name, value)


        class Modules(Entity):
            """
            Collection of capabillity statements for hardware
            module in the system.
            
            .. attribute:: name  (key)
            
            	Name of the hardware module such as linecards, for which capability is described
            	**type**\: str
            
            .. attribute:: max_mac_per_bd
            
            	Maximum number of MAC addresses per bridge\-domains supported by this module
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_pdd_edge_bd
            
            	Maximum number of PBB Edge type bridge\-domains supported by this module
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_bd
            
            	Maximum number of bridge\-domains suported
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_ac_per_bd
            
            	Maximum number of attachment circuits per bridge\-domains
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_pw_per_bd
            
            	Maximum number of access pseudowires per bridge\-domains
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_vfi_per_bd
            
            	Maximum number of virtual forwarding instances per bridge\-domains
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: max_sh_group_per_bd
            
            	Maximum number of Split Horizon groups per bridge\-domains
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainState.ModuleCapabilities.Modules, self).__init__()

                self.yang_name = "modules"
                self.yang_parent_name = "module-capabilities"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['name']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('name', YLeaf(YType.str, 'name')),
                    ('max_mac_per_bd', YLeaf(YType.uint32, 'max-mac-per-bd')),
                    ('max_pdd_edge_bd', YLeaf(YType.uint32, 'max-pdd-edge-bd')),
                    ('max_bd', YLeaf(YType.uint32, 'max-bd')),
                    ('max_ac_per_bd', YLeaf(YType.uint32, 'max-ac-per-bd')),
                    ('max_pw_per_bd', YLeaf(YType.uint32, 'max-pw-per-bd')),
                    ('max_vfi_per_bd', YLeaf(YType.uint32, 'max-vfi-per-bd')),
                    ('max_sh_group_per_bd', YLeaf(YType.uint32, 'max-sh-group-per-bd')),
                ])
                self.name = None
                self.max_mac_per_bd = None
                self.max_pdd_edge_bd = None
                self.max_bd = None
                self.max_ac_per_bd = None
                self.max_pw_per_bd = None
                self.max_vfi_per_bd = None
                self.max_sh_group_per_bd = None
                self._segment_path = lambda: "modules" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/module-capabilities/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeDomainState.ModuleCapabilities.Modules, ['name', 'max_mac_per_bd', 'max_pdd_edge_bd', 'max_bd', 'max_ac_per_bd', 'max_pw_per_bd', 'max_vfi_per_bd', 'max_sh_group_per_bd'], name, value)


    class BridgeDomains(Entity):
        """
        Bridge domain state data.
        
        .. attribute:: bridge_domain
        
        	Collection of bridge\-domain state data
        	**type**\: list of  		 :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.BridgeDomains, self).__init__()

            self.yang_name = "bridge-domains"
            self.yang_parent_name = "bridge-domain-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bridge-domain", ("bridge_domain", BridgeDomainState.BridgeDomains.BridgeDomain))])
            self._leafs = OrderedDict()

            self.bridge_domain = YList(self)
            self._segment_path = lambda: "bridge-domains"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainState.BridgeDomains, [], name, value)


        class BridgeDomain(Entity):
            """
            Collection of bridge\-domain state data.
            
            .. attribute:: id  (key)
            
            	Bridge domain name or number
            	**type**\: str
            
            .. attribute:: bd_state
            
            	Bridge domain operational/admin status
            	**type**\:  :py:class:`BridgeDomainStateType <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainStateType>`
            
            	**mandatory**\: True
            
            .. attribute:: create_time
            
            	System time when this bridge\-domain was created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_status_change
            
            	Number of consecutive ticks since bridge\-domain status was changed last time
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: mac_limit_reached
            
            	This leaf indicates if MAC address limit has been reached
            	**type**\: bool
            
            .. attribute:: p2mp_pw_disabled
            
            	Point to Mutipoint pseudowire state
            	**type**\: bool
            
            .. attribute:: members
            
            	Collection of bridge\-domain members
            	**type**\:  :py:class:`Members <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members>`
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(BridgeDomainState.BridgeDomains.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "bridge-domains"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['id']
                self._child_container_classes = OrderedDict([("members", ("members", BridgeDomainState.BridgeDomains.BridgeDomain.Members))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('id', YLeaf(YType.str, 'id')),
                    ('bd_state', YLeaf(YType.enumeration, 'bd-state')),
                    ('create_time', YLeaf(YType.uint32, 'create-time')),
                    ('last_status_change', YLeaf(YType.uint32, 'last-status-change')),
                    ('mac_limit_reached', YLeaf(YType.boolean, 'mac-limit-reached')),
                    ('p2mp_pw_disabled', YLeaf(YType.boolean, 'p2mp-pw-disabled')),
                ])
                self.id = None
                self.bd_state = None
                self.create_time = None
                self.last_status_change = None
                self.mac_limit_reached = None
                self.p2mp_pw_disabled = None

                self.members = BridgeDomainState.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self._children_name_map["members"] = "members"
                self._children_yang_names.add("members")
                self._segment_path = lambda: "bridge-domain" + "[id='" + str(self.id) + "']"
                self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/bridge-domains/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain, ['id', 'bd_state', 'create_time', 'last_status_change', 'mac_limit_reached', 'p2mp_pw_disabled'], name, value)


            class Members(Entity):
                """
                Collection of bridge\-domain members.
                
                .. attribute:: ac_member
                
                	List of attachment circuits for this bridge domains
                	**type**\: list of  		 :py:class:`AcMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember>`
                
                .. attribute:: vfi_member
                
                	Reference to an instance of Bridge domain Virtual Forwarding Instance (VFI) name
                	**type**\: list of  		 :py:class:`VfiMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember>`
                
                .. attribute:: access_pw_member
                
                	Collection of access pseudowire members of the bridge domain
                	**type**\: list of  		 :py:class:`AccessPwMember <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    super(BridgeDomainState.BridgeDomains.BridgeDomain.Members, self).__init__()

                    self.yang_name = "members"
                    self.yang_parent_name = "bridge-domain"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("ac-member", ("ac_member", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember)), ("vfi-member", ("vfi_member", BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember)), ("access-pw-member", ("access_pw_member", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember))])
                    self._leafs = OrderedDict()

                    self.ac_member = YList(self)
                    self.vfi_member = YList(self)
                    self.access_pw_member = YList(self)
                    self._segment_path = lambda: "members"

                def __setattr__(self, name, value):
                    self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members, [], name, value)


                class AcMember(Entity):
                    """
                    List of attachment circuits for this bridge domains
                    
                    .. attribute:: interface  (key)
                    
                    	Reference to an instance of Bridge domain attachment circuit (AC) interface name
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
                    
                    .. attribute:: static_mac_count
                    
                    	Number of static MAC address configured on this bridge\-domain member interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dai_stats
                    
                    	Dynamic ARP Inspection (DAI) statistics
                    	**type**\:  :py:class:`DaiStats <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats>`
                    
                    .. attribute:: ipsg_stats
                    
                    	IPSG stats
                    	**type**\:  :py:class:`IpsgStats <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats>`
                    
                    .. attribute:: storm_control
                    
                    	Storm control statistics
                    	**type**\:  :py:class:`StormControl <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember, self).__init__()

                        self.yang_name = "ac-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([("dai-stats", ("dai_stats", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats)), ("ipsg-stats", ("ipsg_stats", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats)), ("storm-control", ("storm_control", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                            ('static_mac_count', YLeaf(YType.uint32, 'static-mac-count')),
                        ])
                        self.interface = None
                        self.static_mac_count = None

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
                        self._segment_path = lambda: "ac-member" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember, ['interface', 'static_mac_count'], name, value)


                    class DaiStats(Entity):
                        """
                        Dynamic ARP Inspection (DAI) statistics.
                        
                        .. attribute:: packet_drops
                        
                        	Number of packets dropped by interface due to DAI actions
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: byte_drops
                        
                        	Number of bytes dropped by interface due to DAI actions
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats, self).__init__()

                            self.yang_name = "dai-stats"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packet_drops', YLeaf(YType.uint64, 'packet-drops')),
                                ('byte_drops', YLeaf(YType.uint64, 'byte-drops')),
                            ])
                            self.packet_drops = None
                            self.byte_drops = None
                            self._segment_path = lambda: "dai-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats, ['packet_drops', 'byte_drops'], name, value)


                    class IpsgStats(Entity):
                        """
                        IPSG stats.
                        
                        .. attribute:: packet_drops
                        
                        	Number of packets dropped by interface due to IPSG actions
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: byte_drops
                        
                        	Number of bytes dropped by interface due to IPSG actions
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats, self).__init__()

                            self.yang_name = "ipsg-stats"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('packet_drops', YLeaf(YType.uint64, 'packet-drops')),
                                ('byte_drops', YLeaf(YType.uint64, 'byte-drops')),
                            ])
                            self.packet_drops = None
                            self.byte_drops = None
                            self._segment_path = lambda: "ipsg-stats"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats, ['packet_drops', 'byte_drops'], name, value)


                    class StormControl(Entity):
                        """
                        Storm control statistics.
                        
                        .. attribute:: drop_counter
                        
                        	Collection of packet drop statistics for ethernet traffic clasess
                        	**type**\: list of  		 :py:class:`DropCounter <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, self).__init__()

                            self.yang_name = "storm-control"
                            self.yang_parent_name = "ac-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("drop-counter", ("drop_counter", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter))])
                            self._leafs = OrderedDict()

                            self.drop_counter = YList(self)
                            self._segment_path = lambda: "storm-control"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl, [], name, value)


                        class DropCounter(Entity):
                            """
                            Collection of packet drop statistics for ethernet traffic
                            clasess.
                            
                            .. attribute:: traffic_class  (key)
                            
                            	Ethernet traffic class i.e. broadcast, multicast or unknown unicast
                            	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: packet_drops
                            
                            	The total number of dropped packets due to storm control violations
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: octate_drops
                            
                            	The total number of bytes of traffic dropped due to storm control violations
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter, self).__init__()

                                self.yang_name = "drop-counter"
                                self.yang_parent_name = "storm-control"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['traffic_class']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                                    ('packet_drops', YLeaf(YType.uint64, 'packet-drops')),
                                    ('octate_drops', YLeaf(YType.uint64, 'octate-drops')),
                                ])
                                self.traffic_class = None
                                self.packet_drops = None
                                self.octate_drops = None
                                self._segment_path = lambda: "drop-counter" + "[traffic-class='" + str(self.traffic_class) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter, ['traffic_class', 'packet_drops', 'octate_drops'], name, value)


                class VfiMember(Entity):
                    """
                    Reference to an instance of Bridge domain Virtual
                    Forwarding Instance (VFI) name.
                    
                    .. attribute:: interface  (key)
                    
                    	Bridge domain memeber interface name
                    	**type**\: str
                    
                    	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.InterfacesState.Interface>`
                    
                    .. attribute:: flooding
                    
                    	Flooding operational status
                    	**type**\:  :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember, self).__init__()

                        self.yang_name = "vfi-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_container_classes = OrderedDict([("flooding", ("flooding", BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('interface', YLeaf(YType.str, 'interface')),
                        ])
                        self.interface = None

                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")
                        self._segment_path = lambda: "vfi-member" + "[interface='" + str(self.interface) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember, ['interface'], name, value)


                    class Flooding(Entity):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of  		 :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "vfi-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("status", ("status", BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status))])
                            self._leafs = OrderedDict()

                            self.status = YList(self)
                            self._segment_path = lambda: "flooding"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding, [], name, value)


                        class Status(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  (key)
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status, self).__init__()

                                self.yang_name = "status"
                                self.yang_parent_name = "flooding"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['traffic_class']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.traffic_class = None
                                self.enabled = None
                                self._segment_path = lambda: "status" + "[traffic-class='" + str(self.traffic_class) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status, ['traffic_class', 'enabled'], name, value)


                class AccessPwMember(Entity):
                    """
                    Collection of access pseudowire members of the bridge
                    domain.
                    
                    .. attribute:: vc_peer_address  (key)
                    
                    	Reference to peer ip address of a pseudowire instance
                    	**type**\: union of the below types:
                    
                    		**type**\: str
                    
                    			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    		**type**\: str
                    
                    			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    	**refers to**\:  :py:class:`vc_peer_address <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
                    
                    .. attribute:: vc_id  (key)
                    
                    	Reference to vc\-id of a pseudowire instance
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**refers to**\:  :py:class:`vc_id <ydk.models.cisco_ios_xe.cisco_pw.PseudowireState.Pseudowires>`
                    
                    .. attribute:: flooding
                    
                    	Flooding operational status
                    	**type**\:  :py:class:`Flooding <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember, self).__init__()

                        self.yang_name = "access-pw-member"
                        self.yang_parent_name = "members"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['vc_peer_address','vc_id']
                        self._child_container_classes = OrderedDict([("flooding", ("flooding", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('vc_peer_address', YLeaf(YType.str, 'vc-peer-address')),
                            ('vc_id', YLeaf(YType.str, 'vc-id')),
                        ])
                        self.vc_peer_address = None
                        self.vc_id = None

                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding()
                        self.flooding.parent = self
                        self._children_name_map["flooding"] = "flooding"
                        self._children_yang_names.add("flooding")
                        self._segment_path = lambda: "access-pw-member" + "[vc-peer-address='" + str(self.vc_peer_address) + "']" + "[vc-id='" + str(self.vc_id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember, ['vc_peer_address', 'vc_id'], name, value)


                    class Flooding(Entity):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of  		 :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding, self).__init__()

                            self.yang_name = "flooding"
                            self.yang_parent_name = "access-pw-member"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("status", ("status", BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status))])
                            self._leafs = OrderedDict()

                            self.status = YList(self)
                            self._segment_path = lambda: "flooding"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding, [], name, value)


                        class Status(Entity):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  (key)
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:  :py:class:`EthTrafficClass <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClass>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                super(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status, self).__init__()

                                self.yang_name = "status"
                                self.yang_parent_name = "flooding"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['traffic_class']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('traffic_class', YLeaf(YType.enumeration, 'traffic-class')),
                                    ('enabled', YLeaf(YType.boolean, 'enabled')),
                                ])
                                self.traffic_class = None
                                self.enabled = None
                                self._segment_path = lambda: "status" + "[traffic-class='" + str(self.traffic_class) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status, ['traffic_class', 'enabled'], name, value)


    class MacTable(Entity):
        """
        This list contains mac\-address entries for bridge
        domains.
        
        .. attribute:: bd_id  (key)
        
        	Bridge\-domain name where MAC entry is learnt
        	**type**\: str
        
        .. attribute:: mac_address  (key)
        
        	MAC address
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        .. attribute:: mac_type
        
        	MAC address type
        	**type**\:  :py:class:`MacType <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.MacTable.MacType>`
        
        .. attribute:: interface
        
        	Reference to an interface instance where MAC  address is learnt
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        	**mandatory**\: True
        
        .. attribute:: secure_mac
        
        	Secure MAC address
        	**type**\: bool
        
        .. attribute:: ntfy_mac
        
        	TBD ?NTFY?
        	**type**\: bool
        
        .. attribute:: age
        
        	Time since mac address was learnt on the interface
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: location
        
        	Linecard / Module where mac address was learnt
        	**type**\: str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(BridgeDomainState.MacTable, self).__init__()

            self.yang_name = "mac-table"
            self.yang_parent_name = "bridge-domain-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['bd_id','mac_address']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('bd_id', YLeaf(YType.str, 'bd-id')),
                ('mac_address', YLeaf(YType.str, 'mac-address')),
                ('mac_type', YLeaf(YType.enumeration, 'mac-type')),
                ('interface', YLeaf(YType.str, 'interface')),
                ('secure_mac', YLeaf(YType.boolean, 'secure-mac')),
                ('ntfy_mac', YLeaf(YType.boolean, 'ntfy-mac')),
                ('age', YLeaf(YType.uint32, 'age')),
                ('location', YLeaf(YType.str, 'location')),
            ])
            self.bd_id = None
            self.mac_address = None
            self.mac_type = None
            self.interface = None
            self.secure_mac = None
            self.ntfy_mac = None
            self.age = None
            self.location = None
            self._segment_path = lambda: "mac-table" + "[bd-id='" + str(self.bd_id) + "']" + "[mac-address='" + str(self.mac_address) + "']"
            self._absolute_path = lambda: "cisco-bridge-domain:bridge-domain-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BridgeDomainState.MacTable, ['bd_id', 'mac_address', 'mac_type', 'interface', 'secure_mac', 'ntfy_mac', 'age', 'location'], name, value)

        class MacType(Enum):
            """
            MacType (Enum Class)

            MAC address type.

            .. data:: static = 0

            	MAC address is configured statically.

            .. data:: dynamic = 1

            	MAC address is learnt dynamicaly.

            """

            static = Enum.YLeaf(0, "static")

            dynamic = Enum.YLeaf(1, "dynamic")


    def clone_ptr(self):
        self._top_entity = BridgeDomainState()
        return self._top_entity

class ClearBridgeDomain(Entity):
    """
    Clear mac\-address table for bridge\-domain and allows a bridge
    to forward again after it was put in shutdown state as a
    result of exceeding the configured MAC limit.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomain.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomain.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(ClearBridgeDomain, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-bridge-domain"
        self.yang_parent_name = "cisco-bridge-domain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearBridgeDomain.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearBridgeDomain.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-bridge-domain:clear-bridge-domain"


    class Input(Entity):
        """
        
        
        .. attribute:: all
        
        	Clear all bridge\-domains configured on the device
        	**type**\: :py:class:`Empty<ydk.types.Empty>`
        
        .. attribute:: bd_id
        
        	Clear a single bridge\-domain
        	**type**\: str
        
        .. attribute:: bg_id
        
        	Clears all bridge\-domains under this bridge\-group
        	**type**\: str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearBridgeDomain.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-bridge-domain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('all', YLeaf(YType.empty, 'all')),
                ('bd_id', YLeaf(YType.str, 'bd-id')),
                ('bg_id', YLeaf(YType.str, 'bg-id')),
            ])
            self.all = None
            self.bd_id = None
            self.bg_id = None
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-bridge-domain:clear-bridge-domain/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearBridgeDomain.Input, ['all', 'bd_id', 'bg_id'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\: str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearBridgeDomain.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-bridge-domain"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('errstr', YLeaf(YType.str, 'errstr')),
            ])
            self.errstr = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-bridge-domain:clear-bridge-domain/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearBridgeDomain.Output, ['errstr'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearBridgeDomain()
        return self._top_entity

class ClearMacAddress(Entity):
    """
    This RPC allows to clear dynamically learnt mac\-address
    entries from the mac\-address table.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(ClearMacAddress, self).__init__()
        self._top_entity = None

        self.yang_name = "clear-mac-address"
        self.yang_parent_name = "cisco-bridge-domain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = ClearMacAddress.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = ClearMacAddress.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-bridge-domain:clear-mac-address"


    class Input(Entity):
        """
        
        
        .. attribute:: bridge_domain
        
        	Clear mac\-address entries for given bridge\-domain(s)
        	**type**\:  :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddress.Input.BridgeDomain>`
        
        .. attribute:: interface
        
        	Reference to an interface. Clear mac\-addesses learnt by by this interface
        	**type**\: str
        
        	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
        
        .. attribute:: mac_address
        
        	Clear a specific mac\-address entry from the mac\-table
        	**type**\: str
        
        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearMacAddress.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "clear-mac-address"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([("bridge-domain", ("bridge_domain", ClearMacAddress.Input.BridgeDomain))])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('interface', YLeaf(YType.str, 'interface')),
                ('mac_address', YLeaf(YType.str, 'mac-address')),
            ])
            self.interface = None
            self.mac_address = None

            self.bridge_domain = ClearMacAddress.Input.BridgeDomain()
            self.bridge_domain.parent = self
            self._children_name_map["bridge_domain"] = "bridge-domain"
            self._children_yang_names.add("bridge-domain")
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-bridge-domain:clear-mac-address/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearMacAddress.Input, ['interface', 'mac_address'], name, value)


        class BridgeDomain(Entity):
            """
            Clear mac\-address entries for given bridge\-domain(s).
            
            .. attribute:: bd_id
            
            	Bridge\-domain identifier, clear all mac\-address entries dynamically learnt on this bridge\-domain
            	**type**\: str
            
            	**mandatory**\: True
            
            .. attribute:: bg_id
            
            	Bridge\-group identifier, clear all mac\-address entries from all bridge\-domains under this bridge\-group
            	**type**\: str
            
            	**mandatory**\: True
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(ClearMacAddress.Input.BridgeDomain, self).__init__()

                self.yang_name = "bridge-domain"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('bd_id', YLeaf(YType.str, 'bd-id')),
                    ('bg_id', YLeaf(YType.str, 'bg-id')),
                ])
                self.bd_id = None
                self.bg_id = None
                self._segment_path = lambda: "bridge-domain"
                self._absolute_path = lambda: "cisco-bridge-domain:clear-mac-address/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(ClearMacAddress.Input.BridgeDomain, ['bd_id', 'bg_id'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\: str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(ClearMacAddress.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "clear-mac-address"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('errstr', YLeaf(YType.str, 'errstr')),
            ])
            self.errstr = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-bridge-domain:clear-mac-address/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(ClearMacAddress.Output, ['errstr'], name, value)

    def clone_ptr(self):
        self._top_entity = ClearMacAddress()
        return self._top_entity

class CreateParameterizedBridgeDomains(Entity):
    """
    Create bridge domains automatically from user defined
    parameters.
    
    .. attribute:: input
    
    	
    	**type**\:  :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:  :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        super(CreateParameterizedBridgeDomains, self).__init__()
        self._top_entity = None

        self.yang_name = "create-parameterized-bridge-domains"
        self.yang_parent_name = "cisco-bridge-domain"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.input = CreateParameterizedBridgeDomains.Input()
        self.input.parent = self
        self._children_name_map["input"] = "input"
        self._children_yang_names.add("input")

        self.output = CreateParameterizedBridgeDomains.Output()
        self.output.parent = self
        self._children_name_map["output"] = "output"
        self._children_yang_names.add("output")
        self._segment_path = lambda: "cisco-bridge-domain:create-parameterized-bridge-domains"


    class Input(Entity):
        """
        
        
        .. attribute:: parameter
        
        	Parameter for automatic bridge domain creation
        	**type**\:  :py:class:`Parameter <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input.Parameter>`
        
        .. attribute:: member
        
        	Bridge\-domain member interface
        	**type**\: list of  		 :py:class:`Member <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomains.Input.Member>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(CreateParameterizedBridgeDomains.Input, self).__init__()

            self.yang_name = "input"
            self.yang_parent_name = "create-parameterized-bridge-domains"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("member", ("member", CreateParameterizedBridgeDomains.Input.Member))])
            self._leafs = OrderedDict([
                ('parameter', YLeaf(YType.enumeration, 'parameter')),
            ])
            self.parameter = None

            self.member = YList(self)
            self._segment_path = lambda: "input"
            self._absolute_path = lambda: "cisco-bridge-domain:create-parameterized-bridge-domains/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CreateParameterizedBridgeDomains.Input, ['parameter'], name, value)

        class Parameter(Enum):
            """
            Parameter (Enum Class)

            Parameter for automatic bridge domain creation.

            .. data:: vlan = 0

            	Create bridge-domains from vlan encapsulations of the

            	member interfaces.

            """

            vlan = Enum.YLeaf(0, "vlan")



        class Member(Entity):
            """
            Bridge\-domain member interface.
            
            .. attribute:: interface  (key)
            
            	Reference to an interface instance which is configured to be part of this bridge domain
            	**type**\: str
            
            	**refers to**\:  :py:class:`name <ydk.models.ietf.ietf_interfaces.Interfaces.Interface>`
            
            

            """

            _prefix = 'bd'
            _revision = '2016-12-14'

            def __init__(self):
                super(CreateParameterizedBridgeDomains.Input.Member, self).__init__()

                self.yang_name = "member"
                self.yang_parent_name = "input"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['interface']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('interface', YLeaf(YType.str, 'interface')),
                ])
                self.interface = None
                self._segment_path = lambda: "member" + "[interface='" + str(self.interface) + "']"
                self._absolute_path = lambda: "cisco-bridge-domain:create-parameterized-bridge-domains/input/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CreateParameterizedBridgeDomains.Input.Member, ['interface'], name, value)


    class Output(Entity):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\: str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            super(CreateParameterizedBridgeDomains.Output, self).__init__()

            self.yang_name = "output"
            self.yang_parent_name = "create-parameterized-bridge-domains"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('errstr', YLeaf(YType.str, 'errstr')),
            ])
            self.errstr = None
            self._segment_path = lambda: "output"
            self._absolute_path = lambda: "cisco-bridge-domain:create-parameterized-bridge-domains/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CreateParameterizedBridgeDomains.Output, ['errstr'], name, value)

    def clone_ptr(self):
        self._top_entity = CreateParameterizedBridgeDomains()
        return self._top_entity

