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


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BridgeDomainStateTypeEnum(Enum):
    """
    BridgeDomainStateTypeEnum

    Bridge domain states.

    .. data:: up = 0

    	Bridge domain is operationally Up.

    .. data:: down = 1

    	Bridge domain is operationally Down.

    .. data:: admin_down = 2

    	Bridge domain is shutdown by administrator.

    """

    up = 0

    down = 1

    admin_down = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['BridgeDomainStateTypeEnum']



class BridgeDomainConfig(object):
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
        self.bridge_domains = BridgeDomainConfig.BridgeDomains()
        self.bridge_domains.parent = self
        self.bridge_groups = BridgeDomainConfig.BridgeGroups()
        self.bridge_groups.parent = self
        self.global_ = BridgeDomainConfig.Global_()
        self.global_.parent = self


    class Global_(object):
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
            self.parent = None
            self.bd_state_notification_enabled = None
            self.bd_state_notification_rate = None
            self.pbb = BridgeDomainConfig.Global_.Pbb()
            self.pbb.parent = self


        class Pbb(object):
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
                self.parent = None
                self.backbone_src_mac = None

            @property
            def _common_path(self):

                return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:global/cisco-bridge-domain:pbb'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.backbone_src_mac is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainConfig.Global_.Pbb']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:global'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bd_state_notification_enabled is not None:
                return True

            if self.bd_state_notification_rate is not None:
                return True

            if self.pbb is not None and self.pbb._has_data():
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainConfig.Global_']['meta_info']


    class BridgeGroups(object):
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
            self.parent = None
            self.bridge_group = YList()
            self.bridge_group.parent = self
            self.bridge_group.name = 'bridge_group'


        class BridgeGroup(object):
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
                self.parent = None
                self.name = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:bridge-groups/cisco-bridge-domain:bridge-group[cisco-bridge-domain:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.name is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainConfig.BridgeGroups.BridgeGroup']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:bridge-groups'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bridge_group is not None:
                for child_ref in self.bridge_group:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainConfig.BridgeGroups']['meta_info']


    class BridgeDomains(object):
        """
        Collection of bridge domains.
        
        .. attribute:: bridge_domain
        
        	Definition of a bridge\-domain
        	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.bridge_domain = YList()
            self.bridge_domain.parent = self
            self.bridge_domain.name = 'bridge_domain'


        class BridgeDomain(object):
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
            	**type**\:   :py:class:`FloodingModeEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingModeEnum>`
            
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
                self.parent = None
                self.id = None
                self.bd_status_change_notification = None
                self.bridge_group = None
                self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping()
                self.dhcp_ipv4_snooping.parent = self
                self.dynamic_arp_inspection = None
                self.enabled = None
                self.flooding_mode = None
                self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping()
                self.igmp_snooping.parent = self
                self.ip_source_guard = None
                self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac()
                self.mac.parent = self
                self.members = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping()
                self.mld_snooping.parent = self
                self.mtu = None
                self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl()
                self.storm_control.parent = self

            class FloodingModeEnum(Enum):
                """
                FloodingModeEnum

                Flood modes for optimization.

                .. data:: convergence_optimized = 0

                	Flood mode optimized for convergence.

                .. data:: resilience_optimized = 1

                	Flood mode optimized for resiliency

                """

                convergence_optimized = 0

                resilience_optimized = 1


                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingModeEnum']



            class Members(object):
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
                    self.parent = None
                    self.ac_member = YList()
                    self.ac_member.parent = self
                    self.ac_member.name = 'ac_member'
                    self.access_pw_member = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember()
                    self.access_pw_member.parent = self
                    self.vfi_member = YList()
                    self.vfi_member.parent = self
                    self.vfi_member.name = 'vfi_member'


                class AcMember(object):
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
                        self.parent = None
                        self.interface = None
                        self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping()
                        self.dhcp_ipv4_snooping.parent = self
                        self.dynamic_arp_inspection = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection()
                        self.dynamic_arp_inspection.parent = self
                        self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding()
                        self.flooding.parent = self
                        self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping()
                        self.igmp_snooping.parent = self
                        self.ip_source_guard = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard()
                        self.ip_source_guard.parent = self
                        self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac()
                        self.mac.parent = self
                        self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping()
                        self.mld_snooping.parent = self
                        self.split_horizon_group = None
                        self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                        self.storm_control.parent = self


                    class SplitHorizonGroup(object):
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
                        
                        .. attribute:: _is_presence
                        
                        	Is present if this instance represents presence container else not
                        	**type**\: bool
                        
                        

                        This class is a :ref:`presence class<presence-class>`

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            self.parent = None
                            self._is_presence = True
                            self.id = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:split-horizon-group'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self._is_presence:
                                return True
                            if self.id is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup']['meta_info']


                    class Mac(object):
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
                            self.parent = None
                            self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging()
                            self.aging.parent = self
                            self.learning_enabled = None
                            self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit()
                            self.limit.parent = self
                            self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown()
                            self.port_down.parent = self
                            self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure()
                            self.secure.parent = self


                        class Limit(object):
                            """
                            MAC table learning limit.
                            
                            .. attribute:: action
                            
                            	MAC limit violation actions
                            	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitActionEnum>`
                            
                            .. attribute:: maximum
                            
                            	Maximum number of mac addresses that can be learnt
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: notification
                            
                            	MAC limit violation notifications
                            	**type**\:   :py:class:`MacLimitNotificationTypeIdentity <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationTypeIdentity>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self.action = None
                                self.maximum = None
                                self.notification = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:limit'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.action is not None:
                                    return True

                                if self.maximum is not None:
                                    return True

                                if self.notification is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit']['meta_info']


                        class Aging(object):
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
                            	**type**\:   :py:class:`MacAgingTypeEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingTypeEnum>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self.time = None
                                self.type = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:aging'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.time is not None:
                                    return True

                                if self.type is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging']['meta_info']


                        class PortDown(object):
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
                                self.parent = None
                                self.flush = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:port-down'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.flush is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown']['meta_info']


                        class Secure(object):
                            """
                            MAC secure parameters.
                            
                            .. attribute:: action
                            
                            	MAC secure action for violating packets
                            	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureActionEnum>`
                            
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
                                self.parent = None
                                self.action = None
                                self.enabled = None
                                self.logging = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:secure'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.action is not None:
                                    return True

                                if self.enabled is not None:
                                    return True

                                if self.logging is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:mac'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.aging is not None and self.aging._has_data():
                                return True

                            if self.learning_enabled is not None:
                                return True

                            if self.limit is not None and self.limit._has_data():
                                return True

                            if self.port_down is not None and self.port_down._has_data():
                                return True

                            if self.secure is not None and self.secure._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info']


                    class IgmpSnooping(object):
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
                            self.parent = None
                            self.profile_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:igmp-snooping'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping']['meta_info']


                    class MldSnooping(object):
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
                            self.parent = None
                            self.profile_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:mld-snooping'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping']['meta_info']


                    class DhcpIpv4Snooping(object):
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
                            self.parent = None
                            self.profile_name = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:dhcp-ipv4-snooping'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.profile_name is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping']['meta_info']


                    class Flooding(object):
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
                            self.parent = None
                            self.disabled = None
                            self.disabled_unknown_unicast = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:flooding'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.disabled is not None:
                                return True

                            if self.disabled_unknown_unicast is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding']['meta_info']


                    class StormControl(object):
                        """
                        A collection of storm control threshold and action
                        configurations.
                        
                        .. attribute:: action
                        
                        	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                        	**type**\:   :py:class:`StormControlActionIdentity <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlActionIdentity>`
                        
                        .. attribute:: thresholds
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            self.parent = None
                            self.action = None
                            self.thresholds = YList()
                            self.thresholds.parent = self
                            self.thresholds.name = 'thresholds'


                        class Thresholds(object):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                            	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                            
                            .. attribute:: unit
                            
                            	This enumeration define unit of the traffic threshold value
                            	**type**\:   :py:class:`UnitEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.UnitEnum>`
                            
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
                                self.parent = None
                                self.traffic_class = None
                                self.unit = None
                                self.value = None

                            class UnitEnum(Enum):
                                """
                                UnitEnum

                                This enumeration define unit of the traffic threshold

                                value.

                                .. data:: bps = 0

                                	Bits per second.

                                .. data:: kbps = 1

                                	Kilobits per second.

                                .. data:: pps = 2

                                	Packets per seconds.

                                """

                                bps = 0

                                kbps = 1

                                pps = 2


                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.UnitEnum']


                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.traffic_class is None:
                                    raise YPYModelError('Key property traffic_class is None')

                                return self.parent._common_path +'/cisco-bridge-domain:thresholds[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.traffic_class is not None:
                                    return True

                                if self.unit is not None:
                                    return True

                                if self.value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:storm-control'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.action is not None:
                                return True

                            if self.thresholds is not None:
                                for child_ref in self.thresholds:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info']


                    class DynamicArpInspection(object):
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
                            self.parent = None
                            self.address_validation = None
                            self.enable = None
                            self.logging = None


                        class AddressValidation(object):
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
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.dst_mac = None
                                self.ipv4 = None
                                self.src_mac = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:address-validation'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.dst_mac is not None:
                                    return True

                                if self.ipv4 is not None:
                                    return True

                                if self.src_mac is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:dynamic-arp-inspection'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.address_validation is not None and self.address_validation._has_data():
                                return True

                            if self.enable is not None:
                                return True

                            if self.logging is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection']['meta_info']


                    class IpSourceGuard(object):
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
                            self.parent = None
                            self.enable = None
                            self.logging = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:ip-source-guard'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.enable is not None:
                                return True

                            if self.logging is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/cisco-bridge-domain:ac-member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping._has_data():
                            return True

                        if self.dynamic_arp_inspection is not None and self.dynamic_arp_inspection._has_data():
                            return True

                        if self.flooding is not None and self.flooding._has_data():
                            return True

                        if self.igmp_snooping is not None and self.igmp_snooping._has_data():
                            return True

                        if self.ip_source_guard is not None and self.ip_source_guard._has_data():
                            return True

                        if self.mac is not None and self.mac._has_data():
                            return True

                        if self.mld_snooping is not None and self.mld_snooping._has_data():
                            return True

                        if self.split_horizon_group is not None and self.split_horizon_group._has_data():
                            return True

                        if self.storm_control is not None and self.storm_control._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']


                class VfiMember(object):
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
                        self.parent = None
                        self.interface = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/cisco-bridge-domain:vfi-member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember']['meta_info']


                class AccessPwMember(object):
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
                        self.parent = None
                        self.access_pw_if_member = YList()
                        self.access_pw_if_member.parent = self
                        self.access_pw_if_member.name = 'access_pw_if_member'
                        self.pw_neighbor_spec = YList()
                        self.pw_neighbor_spec.parent = self
                        self.pw_neighbor_spec.name = 'pw_neighbor_spec'


                    class AccessPwIfMember(object):
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
                            self.parent = None
                            self.interface = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.interface is None:
                                raise YPYModelError('Key property interface is None')

                            return self.parent._common_path +'/cisco-bridge-domain:access-pw-if-member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.interface is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember']['meta_info']


                    class PwNeighborSpec(object):
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
                        	**type**\:   :py:class:`PwEncapsulationTypeIdentity <ydk.models.cisco_ios_xe.cisco_pw.PwEncapsulationTypeIdentity>`
                        
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
                            self.parent = None
                            self.neighbor_ip_address = None
                            self.vc_id = None
                            self.backup = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup()
                            self.backup.parent = self
                            self.dhcp_ipv4_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping()
                            self.dhcp_ipv4_snooping.parent = self
                            self.encap_type = None
                            self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding()
                            self.flooding.parent = self
                            self.igmp_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping()
                            self.igmp_snooping.parent = self
                            self.mac = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac()
                            self.mac.parent = self
                            self.mld_snooping = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping()
                            self.mld_snooping.parent = self
                            self.pw_class_template = None
                            self.source_ipv6 = None
                            self.split_horizon_group = None
                            self.static_label = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel()
                            self.static_label.parent = self
                            self.storm_control = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl()
                            self.storm_control.parent = self
                            self.tag_impose_vlan = None


                        class StaticLabel(object):
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
                                self.parent = None
                                self.local_label = None
                                self.remote_label = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:static-label'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.local_label is not None:
                                    return True

                                if self.remote_label is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel']['meta_info']


                        class SplitHorizonGroup(object):
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
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:split-horizon-group'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self._is_presence:
                                    return True
                                if self.id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup']['meta_info']


                        class Mac(object):
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
                                self.parent = None
                                self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging()
                                self.aging.parent = self
                                self.learning_enabled = None
                                self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit()
                                self.limit.parent = self
                                self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown()
                                self.port_down.parent = self
                                self.secure = BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure()
                                self.secure.parent = self


                            class Limit(object):
                                """
                                MAC table learning limit.
                                
                                .. attribute:: action
                                
                                	MAC limit violation actions
                                	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitActionEnum>`
                                
                                .. attribute:: maximum
                                
                                	Maximum number of mac addresses that can be learnt
                                	**type**\:  int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: notification
                                
                                	MAC limit violation notifications
                                	**type**\:   :py:class:`MacLimitNotificationTypeIdentity <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationTypeIdentity>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    self.parent = None
                                    self.action = None
                                    self.maximum = None
                                    self.notification = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/cisco-bridge-domain:limit'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.action is not None:
                                        return True

                                    if self.maximum is not None:
                                        return True

                                    if self.notification is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit']['meta_info']


                            class Aging(object):
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
                                	**type**\:   :py:class:`MacAgingTypeEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingTypeEnum>`
                                
                                

                                """

                                _prefix = 'bd'
                                _revision = '2016-12-14'

                                def __init__(self):
                                    self.parent = None
                                    self.time = None
                                    self.type = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/cisco-bridge-domain:aging'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.time is not None:
                                        return True

                                    if self.type is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging']['meta_info']


                            class PortDown(object):
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
                                    self.parent = None
                                    self.flush = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/cisco-bridge-domain:port-down'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.flush is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown']['meta_info']


                            class Secure(object):
                                """
                                MAC secure parameters.
                                
                                .. attribute:: action
                                
                                	MAC secure action for violating packets
                                	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureActionEnum>`
                                
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
                                    self.parent = None
                                    self.action = None
                                    self.enabled = None
                                    self.logging = None

                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')

                                    return self.parent._common_path +'/cisco-bridge-domain:secure'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.action is not None:
                                        return True

                                    if self.enabled is not None:
                                        return True

                                    if self.logging is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:mac'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.aging is not None and self.aging._has_data():
                                    return True

                                if self.learning_enabled is not None:
                                    return True

                                if self.limit is not None and self.limit._has_data():
                                    return True

                                if self.port_down is not None and self.port_down._has_data():
                                    return True

                                if self.secure is not None and self.secure._has_data():
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info']


                        class IgmpSnooping(object):
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
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:igmp-snooping'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping']['meta_info']


                        class MldSnooping(object):
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
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:mld-snooping'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping']['meta_info']


                        class DhcpIpv4Snooping(object):
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
                                self.parent = None
                                self.profile_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:dhcp-ipv4-snooping'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.profile_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping']['meta_info']


                        class Flooding(object):
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
                                self.parent = None
                                self.disabled = None
                                self.disabled_unknown_unicast = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:flooding'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.disabled is not None:
                                    return True

                                if self.disabled_unknown_unicast is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding']['meta_info']


                        class StormControl(object):
                            """
                            A collection of storm control threshold and action
                            configurations.
                            
                            .. attribute:: action
                            
                            	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                            	**type**\:   :py:class:`StormControlActionIdentity <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlActionIdentity>`
                            
                            .. attribute:: thresholds
                            
                            	A collection of storm control threshold configuration entries
                            	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds>`
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self.action = None
                                self.thresholds = YList()
                                self.thresholds.parent = self
                                self.thresholds.name = 'thresholds'


                            class Thresholds(object):
                                """
                                A collection of storm control threshold configuration
                                entries.
                                
                                .. attribute:: traffic_class  <key>
                                
                                	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                                	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                                
                                .. attribute:: unit
                                
                                	This enumeration define unit of the traffic threshold value
                                	**type**\:   :py:class:`UnitEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.UnitEnum>`
                                
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
                                    self.parent = None
                                    self.traffic_class = None
                                    self.unit = None
                                    self.value = None

                                class UnitEnum(Enum):
                                    """
                                    UnitEnum

                                    This enumeration define unit of the traffic threshold

                                    value.

                                    .. data:: bps = 0

                                    	Bits per second.

                                    .. data:: kbps = 1

                                    	Kilobits per second.

                                    .. data:: pps = 2

                                    	Packets per seconds.

                                    """

                                    bps = 0

                                    kbps = 1

                                    pps = 2


                                    @staticmethod
                                    def _meta_info():
                                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.UnitEnum']


                                @property
                                def _common_path(self):
                                    if self.parent is None:
                                        raise YPYModelError('parent is not set . Cannot derive path.')
                                    if self.traffic_class is None:
                                        raise YPYModelError('Key property traffic_class is None')

                                    return self.parent._common_path +'/cisco-bridge-domain:thresholds[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                                def is_config(self):
                                    ''' Returns True if this instance represents config data else returns False '''
                                    return True

                                def _has_data(self):
                                    if self.traffic_class is not None:
                                        return True

                                    if self.unit is not None:
                                        return True

                                    if self.value is not None:
                                        return True

                                    return False

                                @staticmethod
                                def _meta_info():
                                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds']['meta_info']

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:storm-control'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.action is not None:
                                    return True

                                if self.thresholds is not None:
                                    for child_ref in self.thresholds:
                                        if child_ref._has_data():
                                            return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl']['meta_info']


                        class Backup(object):
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
                                self.parent = None
                                self.neighbor_ip_address = None
                                self.pw_class_template = None
                                self.vc_id = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/cisco-bridge-domain:backup'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if self.neighbor_ip_address is not None:
                                    return True

                                if self.pw_class_template is not None:
                                    return True

                                if self.vc_id is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.neighbor_ip_address is None:
                                raise YPYModelError('Key property neighbor_ip_address is None')
                            if self.vc_id is None:
                                raise YPYModelError('Key property vc_id is None')

                            return self.parent._common_path +'/cisco-bridge-domain:pw-neighbor-spec[cisco-bridge-domain:neighbor-ip-address = ' + str(self.neighbor_ip_address) + '][cisco-bridge-domain:vc-id = ' + str(self.vc_id) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.neighbor_ip_address is not None:
                                return True

                            if self.vc_id is not None:
                                return True

                            if self.backup is not None and self.backup._has_data():
                                return True

                            if self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping._has_data():
                                return True

                            if self.encap_type is not None:
                                return True

                            if self.flooding is not None and self.flooding._has_data():
                                return True

                            if self.igmp_snooping is not None and self.igmp_snooping._has_data():
                                return True

                            if self.mac is not None and self.mac._has_data():
                                return True

                            if self.mld_snooping is not None and self.mld_snooping._has_data():
                                return True

                            if self.pw_class_template is not None:
                                return True

                            if self.source_ipv6 is not None:
                                return True

                            if self.split_horizon_group is not None and self.split_horizon_group._has_data():
                                return True

                            if self.static_label is not None and self.static_label._has_data():
                                return True

                            if self.storm_control is not None and self.storm_control._has_data():
                                return True

                            if self.tag_impose_vlan is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:access-pw-member'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.access_pw_if_member is not None:
                            for child_ref in self.access_pw_if_member:
                                if child_ref._has_data():
                                    return True

                        if self.pw_neighbor_spec is not None:
                            for child_ref in self.pw_neighbor_spec:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:members'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.ac_member is not None:
                        for child_ref in self.ac_member:
                            if child_ref._has_data():
                                return True

                    if self.access_pw_member is not None and self.access_pw_member._has_data():
                        return True

                    if self.vfi_member is not None:
                        for child_ref in self.vfi_member:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members']['meta_info']


            class Mac(object):
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
                    self.parent = None
                    self.aging = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging()
                    self.aging.parent = self
                    self.flooding = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding()
                    self.flooding.parent = self
                    self.learning_enabled = None
                    self.limit = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit()
                    self.limit.parent = self
                    self.port_down = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown()
                    self.port_down.parent = self
                    self.secure = None
                    self.static = BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static()
                    self.static.parent = self


                class Limit(object):
                    """
                    MAC table learning limit.
                    
                    .. attribute:: action
                    
                    	MAC limit violation actions
                    	**type**\:   :py:class:`MacLimitActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitActionEnum>`
                    
                    .. attribute:: maximum
                    
                    	Maximum number of mac addresses that can be learnt
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notification
                    
                    	MAC limit violation notifications
                    	**type**\:   :py:class:`MacLimitNotificationTypeIdentity <ydk.models.cisco_ios_xe.cisco_bridge_common.MacLimitNotificationTypeIdentity>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        self.parent = None
                        self.action = None
                        self.maximum = None
                        self.notification = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.action is not None:
                            return True

                        if self.maximum is not None:
                            return True

                        if self.notification is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit']['meta_info']


                class Aging(object):
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
                    	**type**\:   :py:class:`MacAgingTypeEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacAgingTypeEnum>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        self.parent = None
                        self.time = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:aging'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.time is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging']['meta_info']


                class PortDown(object):
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
                        self.parent = None
                        self.flush = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:port-down'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.flush is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown']['meta_info']


                class Flooding(object):
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
                        self.parent = None
                        self.disabled = None
                        self.disabled_unknown_unicast = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:flooding'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.disabled is not None:
                            return True

                        if self.disabled_unknown_unicast is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding']['meta_info']


                class Secure(object):
                    """
                    MAC secure parameters.
                    
                    .. attribute:: action
                    
                    	MAC secure action for violating packets
                    	**type**\:   :py:class:`MacSecureActionEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.MacSecureActionEnum>`
                    
                    	**default value**\: restrict
                    
                    .. attribute:: logging
                    
                    	Enable/Disable logging
                    	**type**\:  bool
                    
                    	**default value**\: false
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.action = None
                        self.logging = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:secure'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.action is not None:
                            return True

                        if self.logging is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure']['meta_info']


                class Static(object):
                    """
                    Static mac address list parameters.
                    
                    .. attribute:: mac_addresses
                    
                    	MAC address entry
                    	**type**\: list of    :py:class:`MacAddresses <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses>`
                    
                    

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        self.parent = None
                        self.mac_addresses = YList()
                        self.mac_addresses.parent = self
                        self.mac_addresses.name = 'mac_addresses'


                    class MacAddresses(object):
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
                            self.parent = None
                            self.mac_addr = None
                            self.drop = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.mac_addr is None:
                                raise YPYModelError('Key property mac_addr is None')

                            return self.parent._common_path +'/cisco-bridge-domain:mac-addresses[cisco-bridge-domain:mac-addr = ' + str(self.mac_addr) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if self.mac_addr is not None:
                                return True

                            if self.drop is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:static'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.mac_addresses is not None:
                            for child_ref in self.mac_addresses:
                                if child_ref._has_data():
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:mac'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.aging is not None and self.aging._has_data():
                        return True

                    if self.flooding is not None and self.flooding._has_data():
                        return True

                    if self.learning_enabled is not None:
                        return True

                    if self.limit is not None and self.limit._has_data():
                        return True

                    if self.port_down is not None and self.port_down._has_data():
                        return True

                    if self.secure is not None and self.secure._has_data():
                        return True

                    if self.static is not None and self.static._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']


            class DynamicArpInspection(object):
                """
                Dynamic ARP Inspection (DAI) configurations.
                
                .. attribute:: address_validation
                
                	Enable address validation
                	**type**\:   :py:class:`AddressValidation <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation>`
                
                	**presence node**\: True
                
                .. attribute:: logging
                
                	Enable DAI logging
                	**type**\:  bool
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.address_validation = None
                    self.logging = None


                class AddressValidation(object):
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
                    
                    .. attribute:: _is_presence
                    
                    	Is present if this instance represents presence container else not
                    	**type**\: bool
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'bd'
                    _revision = '2016-12-14'

                    def __init__(self):
                        self.parent = None
                        self._is_presence = True
                        self.dst_mac = None
                        self.ipv4 = None
                        self.src_mac = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/cisco-bridge-domain:address-validation'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self._is_presence:
                            return True
                        if self.dst_mac is not None:
                            return True

                        if self.ipv4 is not None:
                            return True

                        if self.src_mac is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:dynamic-arp-inspection'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.address_validation is not None and self.address_validation._has_data():
                        return True

                    if self.logging is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection']['meta_info']


            class IpSourceGuard(object):
                """
                IP source guard (IPSG) configurations.
                
                .. attribute:: logging
                
                	Enable IPSG logging
                	**type**\:  bool
                
                	**default value**\: false
                
                .. attribute:: _is_presence
                
                	Is present if this instance represents presence container else not
                	**type**\: bool
                
                

                This class is a :ref:`presence class<presence-class>`

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    self.parent = None
                    self._is_presence = True
                    self.logging = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:ip-source-guard'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self._is_presence:
                        return True
                    if self.logging is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard']['meta_info']


            class StormControl(object):
                """
                A collection of storm control threshold and action
                configurations.
                
                .. attribute:: action
                
                	This leaf represents the storm control action taken when the traffic of a particular type exceeds the configured threshold values
                	**type**\:   :py:class:`StormControlActionIdentity <ydk.models.cisco_ios_xe.cisco_storm_control.StormControlActionIdentity>`
                
                .. attribute:: thresholds
                
                	A collection of storm control threshold configuration entries
                	**type**\: list of    :py:class:`Thresholds <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds>`
                
                

                """

                _prefix = 'bd'
                _revision = '2016-12-14'

                def __init__(self):
                    self.parent = None
                    self.action = None
                    self.thresholds = YList()
                    self.thresholds.parent = self
                    self.thresholds.name = 'thresholds'


                class Thresholds(object):
                    """
                    A collection of storm control threshold configuration
                    entries.
                    
                    .. attribute:: traffic_class  <key>
                    
                    	This leaf identifies a ethernet traffic type for which an administrator desires to configure storm control
                    	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                    
                    .. attribute:: unit
                    
                    	This enumeration define unit of the traffic threshold value
                    	**type**\:   :py:class:`UnitEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.UnitEnum>`
                    
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
                        self.parent = None
                        self.traffic_class = None
                        self.unit = None
                        self.value = None

                    class UnitEnum(Enum):
                        """
                        UnitEnum

                        This enumeration define unit of the traffic threshold

                        value.

                        .. data:: bps = 0

                        	Bits per second.

                        .. data:: kbps = 1

                        	Kilobits per second.

                        .. data:: pps = 2

                        	Packets per seconds.

                        """

                        bps = 0

                        kbps = 1

                        pps = 2


                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.UnitEnum']


                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.traffic_class is None:
                            raise YPYModelError('Key property traffic_class is None')

                        return self.parent._common_path +'/cisco-bridge-domain:thresholds[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if self.traffic_class is not None:
                            return True

                        if self.unit is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:storm-control'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.action is not None:
                        return True

                    if self.thresholds is not None:
                        for child_ref in self.thresholds:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl']['meta_info']


            class IgmpSnooping(object):
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
                    self.parent = None
                    self.disabled = None
                    self.profile_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:igmp-snooping'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.disabled is not None:
                        return True

                    if self.profile_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping']['meta_info']


            class MldSnooping(object):
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
                    self.parent = None
                    self.profile_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:mld-snooping'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping']['meta_info']


            class DhcpIpv4Snooping(object):
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
                    self.parent = None
                    self.profile_name = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:dhcp-ipv4-snooping'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if self.profile_name is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:bridge-domains/cisco-bridge-domain:bridge-domain[cisco-bridge-domain:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if self.id is not None:
                    return True

                if self.bd_status_change_notification is not None:
                    return True

                if self.bridge_group is not None:
                    return True

                if self.dhcp_ipv4_snooping is not None and self.dhcp_ipv4_snooping._has_data():
                    return True

                if self.dynamic_arp_inspection is not None and self.dynamic_arp_inspection._has_data():
                    return True

                if self.enabled is not None:
                    return True

                if self.flooding_mode is not None:
                    return True

                if self.igmp_snooping is not None and self.igmp_snooping._has_data():
                    return True

                if self.ip_source_guard is not None and self.ip_source_guard._has_data():
                    return True

                if self.mac is not None and self.mac._has_data():
                    return True

                if self.members is not None and self.members._has_data():
                    return True

                if self.mld_snooping is not None and self.mld_snooping._has_data():
                    return True

                if self.mtu is not None:
                    return True

                if self.storm_control is not None and self.storm_control._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-config/cisco-bridge-domain:bridge-domains'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if self.bridge_domain is not None:
                for child_ref in self.bridge_domain:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainConfig.BridgeDomains']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-bridge-domain:bridge-domain-config'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.bridge_domains is not None and self.bridge_domains._has_data():
            return True

        if self.bridge_groups is not None and self.bridge_groups._has_data():
            return True

        if self.global_ is not None and self.global_._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['BridgeDomainConfig']['meta_info']


class BridgeDomainState(object):
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
        self.bridge_domains = BridgeDomainState.BridgeDomains()
        self.bridge_domains.parent = self
        self.mac_table = YList()
        self.mac_table.parent = self
        self.mac_table.name = 'mac_table'
        self.module_capabilities = BridgeDomainState.ModuleCapabilities()
        self.module_capabilities.parent = self
        self.system_capabilities = BridgeDomainState.SystemCapabilities()
        self.system_capabilities.parent = self


    class SystemCapabilities(object):
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
            self.parent = None
            self.max_ac_per_bd = None
            self.max_bd = None
            self.max_interflex_if_per_bd = None
            self.max_pw_per_bd = None
            self.max_sh_group_per_bd = None
            self.max_vfi_per_bd = None

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:system-capabilities'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.max_ac_per_bd is not None:
                return True

            if self.max_bd is not None:
                return True

            if self.max_interflex_if_per_bd is not None:
                return True

            if self.max_pw_per_bd is not None:
                return True

            if self.max_sh_group_per_bd is not None:
                return True

            if self.max_vfi_per_bd is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainState.SystemCapabilities']['meta_info']


    class ModuleCapabilities(object):
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
            self.parent = None
            self.modules = YList()
            self.modules.parent = self
            self.modules.name = 'modules'


        class Modules(object):
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
                self.parent = None
                self.name = None
                self.max_ac_per_bd = None
                self.max_bd = None
                self.max_mac_per_bd = None
                self.max_pdd_edge_bd = None
                self.max_pw_per_bd = None
                self.max_sh_group_per_bd = None
                self.max_vfi_per_bd = None

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')

                return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:module-capabilities/cisco-bridge-domain:modules[cisco-bridge-domain:name = ' + str(self.name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.name is not None:
                    return True

                if self.max_ac_per_bd is not None:
                    return True

                if self.max_bd is not None:
                    return True

                if self.max_mac_per_bd is not None:
                    return True

                if self.max_pdd_edge_bd is not None:
                    return True

                if self.max_pw_per_bd is not None:
                    return True

                if self.max_sh_group_per_bd is not None:
                    return True

                if self.max_vfi_per_bd is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainState.ModuleCapabilities.Modules']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:module-capabilities'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.modules is not None:
                for child_ref in self.modules:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainState.ModuleCapabilities']['meta_info']


    class BridgeDomains(object):
        """
        Bridge domain state data.
        
        .. attribute:: bridge_domain
        
        	Collection of bridge\-domain state data
        	**type**\: list of    :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.bridge_domain = YList()
            self.bridge_domain.parent = self
            self.bridge_domain.name = 'bridge_domain'


        class BridgeDomain(object):
            """
            Collection of bridge\-domain state data.
            
            .. attribute:: id  <key>
            
            	Bridge domain name or number
            	**type**\:  str
            
            .. attribute:: bd_state
            
            	Bridge domain operational/admin status
            	**type**\:   :py:class:`BridgeDomainStateTypeEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainStateTypeEnum>`
            
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
                self.parent = None
                self.id = None
                self.bd_state = None
                self.create_time = None
                self.last_status_change = None
                self.mac_limit_reached = None
                self.members = BridgeDomainState.BridgeDomains.BridgeDomain.Members()
                self.members.parent = self
                self.p2mp_pw_disabled = None


            class Members(object):
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
                    self.parent = None
                    self.ac_member = YList()
                    self.ac_member.parent = self
                    self.ac_member.name = 'ac_member'
                    self.access_pw_member = YList()
                    self.access_pw_member.parent = self
                    self.access_pw_member.name = 'access_pw_member'
                    self.vfi_member = YList()
                    self.vfi_member.parent = self
                    self.vfi_member.name = 'vfi_member'


                class AcMember(object):
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
                        self.parent = None
                        self.interface = None
                        self.dai_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats()
                        self.dai_stats.parent = self
                        self.ipsg_stats = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats()
                        self.ipsg_stats.parent = self
                        self.static_mac_count = None
                        self.storm_control = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl()
                        self.storm_control.parent = self


                    class DaiStats(object):
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
                            self.parent = None
                            self.byte_drops = None
                            self.packet_drops = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:dai-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.byte_drops is not None:
                                return True

                            if self.packet_drops is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats']['meta_info']


                    class IpsgStats(object):
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
                            self.parent = None
                            self.byte_drops = None
                            self.packet_drops = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:ipsg-stats'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.byte_drops is not None:
                                return True

                            if self.packet_drops is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats']['meta_info']


                    class StormControl(object):
                        """
                        Storm control statistics.
                        
                        .. attribute:: drop_counter
                        
                        	Collection of packet drop statistics for ethernet traffic clasess
                        	**type**\: list of    :py:class:`DropCounter <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            self.parent = None
                            self.drop_counter = YList()
                            self.drop_counter.parent = self
                            self.drop_counter.name = 'drop_counter'


                        class DropCounter(object):
                            """
                            Collection of packet drop statistics for ethernet traffic
                            clasess.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	Ethernet traffic class i.e. broadcast, multicast or unknown unicast
                            	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                            
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
                                self.parent = None
                                self.traffic_class = None
                                self.octate_drops = None
                                self.packet_drops = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.traffic_class is None:
                                    raise YPYModelError('Key property traffic_class is None')

                                return self.parent._common_path +'/cisco-bridge-domain:drop-counter[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.traffic_class is not None:
                                    return True

                                if self.octate_drops is not None:
                                    return True

                                if self.packet_drops is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:storm-control'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.drop_counter is not None:
                                for child_ref in self.drop_counter:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/cisco-bridge-domain:ac-member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.dai_stats is not None and self.dai_stats._has_data():
                            return True

                        if self.ipsg_stats is not None and self.ipsg_stats._has_data():
                            return True

                        if self.static_mac_count is not None:
                            return True

                        if self.storm_control is not None and self.storm_control._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']


                class VfiMember(object):
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
                        self.parent = None
                        self.interface = None
                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding()
                        self.flooding.parent = self


                    class Flooding(object):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            self.parent = None
                            self.status = YList()
                            self.status.parent = self
                            self.status.name = 'status'


                        class Status(object):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self.traffic_class = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.traffic_class is None:
                                    raise YPYModelError('Key property traffic_class is None')

                                return self.parent._common_path +'/cisco-bridge-domain:status[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.traffic_class is not None:
                                    return True

                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:flooding'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.status is not None:
                                for child_ref in self.status:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.interface is None:
                            raise YPYModelError('Key property interface is None')

                        return self.parent._common_path +'/cisco-bridge-domain:vfi-member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.interface is not None:
                            return True

                        if self.flooding is not None and self.flooding._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember']['meta_info']


                class AccessPwMember(object):
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
                        self.parent = None
                        self.vc_peer_address = None
                        self.vc_id = None
                        self.flooding = BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding()
                        self.flooding.parent = self


                    class Flooding(object):
                        """
                        Flooding operational status
                        
                        .. attribute:: status
                        
                        	A collection of storm control threshold configuration entries
                        	**type**\: list of    :py:class:`Status <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status>`
                        
                        

                        """

                        _prefix = 'bd'
                        _revision = '2016-12-14'

                        def __init__(self):
                            self.parent = None
                            self.status = YList()
                            self.status.parent = self
                            self.status.name = 'status'


                        class Status(object):
                            """
                            A collection of storm control threshold configuration
                            entries.
                            
                            .. attribute:: traffic_class  <key>
                            
                            	This leaf identifies a ethernet traffic type
                            	**type**\:   :py:class:`EthTrafficClassEnum <ydk.models.cisco_ios_xe.cisco_bridge_common.EthTrafficClassEnum>`
                            
                            .. attribute:: enabled
                            
                            	This leaf indicates if flooding is enabled for corresponding traffic class
                            	**type**\:  bool
                            
                            

                            """

                            _prefix = 'bd'
                            _revision = '2016-12-14'

                            def __init__(self):
                                self.parent = None
                                self.traffic_class = None
                                self.enabled = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')
                                if self.traffic_class is None:
                                    raise YPYModelError('Key property traffic_class is None')

                                return self.parent._common_path +'/cisco-bridge-domain:status[cisco-bridge-domain:traffic-class = ' + str(self.traffic_class) + ']'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return False

                            def _has_data(self):
                                if self.traffic_class is not None:
                                    return True

                                if self.enabled is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                                return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/cisco-bridge-domain:flooding'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return False

                        def _has_data(self):
                            if self.status is not None:
                                for child_ref in self.status:
                                    if child_ref._has_data():
                                        return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                            return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.vc_peer_address is None:
                            raise YPYModelError('Key property vc_peer_address is None')
                        if self.vc_id is None:
                            raise YPYModelError('Key property vc_id is None')

                        return self.parent._common_path +'/cisco-bridge-domain:access-pw-member[cisco-bridge-domain:vc-peer-address = ' + str(self.vc_peer_address) + '][cisco-bridge-domain:vc-id = ' + str(self.vc_id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.vc_peer_address is not None:
                            return True

                        if self.vc_id is not None:
                            return True

                        if self.flooding is not None and self.flooding._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                        return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/cisco-bridge-domain:members'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.ac_member is not None:
                        for child_ref in self.ac_member:
                            if child_ref._has_data():
                                return True

                    if self.access_pw_member is not None:
                        for child_ref in self.access_pw_member:
                            if child_ref._has_data():
                                return True

                    if self.vfi_member is not None:
                        for child_ref in self.vfi_member:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                    return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members']['meta_info']

            @property
            def _common_path(self):
                if self.id is None:
                    raise YPYModelError('Key property id is None')

                return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:bridge-domains/cisco-bridge-domain:bridge-domain[cisco-bridge-domain:id = ' + str(self.id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.id is not None:
                    return True

                if self.bd_state is not None:
                    return True

                if self.create_time is not None:
                    return True

                if self.last_status_change is not None:
                    return True

                if self.mac_limit_reached is not None:
                    return True

                if self.members is not None and self.members._has_data():
                    return True

                if self.p2mp_pw_disabled is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainState.BridgeDomains.BridgeDomain']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:bridge-domains'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bridge_domain is not None:
                for child_ref in self.bridge_domain:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainState.BridgeDomains']['meta_info']


    class MacTable(object):
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
        	**type**\:   :py:class:`MacTypeEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.BridgeDomainState.MacTable.MacTypeEnum>`
        
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
            self.parent = None
            self.bd_id = None
            self.mac_address = None
            self.age = None
            self.interface = None
            self.location = None
            self.mac_type = None
            self.ntfy_mac = None
            self.secure_mac = None

        class MacTypeEnum(Enum):
            """
            MacTypeEnum

            MAC address type.

            .. data:: static = 0

            	MAC address is configured statically.

            .. data:: dynamic = 1

            	MAC address is learnt dynamicaly.

            """

            static = 0

            dynamic = 1


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['BridgeDomainState.MacTable.MacTypeEnum']


        @property
        def _common_path(self):
            if self.bd_id is None:
                raise YPYModelError('Key property bd_id is None')
            if self.mac_address is None:
                raise YPYModelError('Key property mac_address is None')

            return '/cisco-bridge-domain:bridge-domain-state/cisco-bridge-domain:mac-table[cisco-bridge-domain:bd-id = ' + str(self.bd_id) + '][cisco-bridge-domain:mac-address = ' + str(self.mac_address) + ']'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.bd_id is not None:
                return True

            if self.mac_address is not None:
                return True

            if self.age is not None:
                return True

            if self.interface is not None:
                return True

            if self.location is not None:
                return True

            if self.mac_type is not None:
                return True

            if self.ntfy_mac is not None:
                return True

            if self.secure_mac is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['BridgeDomainState.MacTable']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-bridge-domain:bridge-domain-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.bridge_domains is not None and self.bridge_domains._has_data():
            return True

        if self.mac_table is not None:
            for child_ref in self.mac_table:
                if child_ref._has_data():
                    return True

        if self.module_capabilities is not None and self.module_capabilities._has_data():
            return True

        if self.system_capabilities is not None and self.system_capabilities._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['BridgeDomainState']['meta_info']


class ClearBridgeDomainRpc(object):
    """
    Clear mac\-address table for bridge\-domain and allows a bridge
    to forward again after it was put in shutdown state as a
    result of exceeding the configured MAC limit.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomainRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearBridgeDomainRpc.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        self.input = ClearBridgeDomainRpc.Input()
        self.input.parent = self
        self.output = ClearBridgeDomainRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
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
            self.parent = None
            self.all = None
            self.bd_id = None
            self.bg_id = None

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:clear-bridge-domain/cisco-bridge-domain:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.all is not None:
                return True

            if self.bd_id is not None:
                return True

            if self.bg_id is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['ClearBridgeDomainRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.errstr = None

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:clear-bridge-domain/cisco-bridge-domain:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.errstr is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['ClearBridgeDomainRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-bridge-domain:clear-bridge-domain'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['ClearBridgeDomainRpc']['meta_info']


class ClearMacAddressRpc(object):
    """
    This RPC allows to clear dynamically learnt mac\-address
    entries from the mac\-address table.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddressRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddressRpc.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        self.input = ClearMacAddressRpc.Input()
        self.input.parent = self
        self.output = ClearMacAddressRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: bridge_domain
        
        	Clear mac\-address entries for given bridge\-domain(s)
        	**type**\:   :py:class:`BridgeDomain <ydk.models.cisco_ios_xe.cisco_bridge_domain.ClearMacAddressRpc.Input.BridgeDomain>`
        
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
            self.parent = None
            self.bridge_domain = ClearMacAddressRpc.Input.BridgeDomain()
            self.bridge_domain.parent = self
            self.interface = None
            self.mac_address = None


        class BridgeDomain(object):
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
                self.parent = None
                self.bd_id = None
                self.bg_id = None

            @property
            def _common_path(self):

                return '/cisco-bridge-domain:clear-mac-address/cisco-bridge-domain:input/cisco-bridge-domain:bridge-domain'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.bd_id is not None:
                    return True

                if self.bg_id is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['ClearMacAddressRpc.Input.BridgeDomain']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:clear-mac-address/cisco-bridge-domain:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.bridge_domain is not None and self.bridge_domain._has_data():
                return True

            if self.interface is not None:
                return True

            if self.mac_address is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['ClearMacAddressRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.errstr = None

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:clear-mac-address/cisco-bridge-domain:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.errstr is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['ClearMacAddressRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-bridge-domain:clear-mac-address'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['ClearMacAddressRpc']['meta_info']


class CreateParameterizedBridgeDomainsRpc(object):
    """
    Create bridge domains automatically from user defined
    parameters.
    
    .. attribute:: input
    
    	
    	**type**\:   :py:class:`Input <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomainsRpc.Input>`
    
    .. attribute:: output
    
    	
    	**type**\:   :py:class:`Output <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomainsRpc.Output>`
    
    

    """

    _prefix = 'bd'
    _revision = '2016-12-14'

    def __init__(self):
        self.input = CreateParameterizedBridgeDomainsRpc.Input()
        self.input.parent = self
        self.output = CreateParameterizedBridgeDomainsRpc.Output()
        self.output.parent = self

        self.is_rpc = True


    class Input(object):
        """
        
        
        .. attribute:: member
        
        	Bridge\-domain member interface
        	**type**\: list of    :py:class:`Member <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomainsRpc.Input.Member>`
        
        .. attribute:: parameter
        
        	Parameter for automatic bridge domain creation
        	**type**\:   :py:class:`ParameterEnum <ydk.models.cisco_ios_xe.cisco_bridge_domain.CreateParameterizedBridgeDomainsRpc.Input.ParameterEnum>`
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.member = YList()
            self.member.parent = self
            self.member.name = 'member'
            self.parameter = None

        class ParameterEnum(Enum):
            """
            ParameterEnum

            Parameter for automatic bridge domain creation.

            .. data:: vlan = 0

            	Create bridge-domains from vlan encapsulations of the

            	member interfaces.

            """

            vlan = 0


            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['CreateParameterizedBridgeDomainsRpc.Input.ParameterEnum']



        class Member(object):
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
                self.parent = None
                self.interface = None

            @property
            def _common_path(self):
                if self.interface is None:
                    raise YPYModelError('Key property interface is None')

                return '/cisco-bridge-domain:create-parameterized-bridge-domains/cisco-bridge-domain:input/cisco-bridge-domain:member[cisco-bridge-domain:interface = ' + str(self.interface) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                if self.parent is None:
                    raise YPYError('Parent reference is needed to determine if entity has configuration data')
                return self.parent.is_config()

            def _has_data(self):
                if self.interface is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
                return meta._meta_table['CreateParameterizedBridgeDomainsRpc.Input.Member']['meta_info']

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:create-parameterized-bridge-domains/cisco-bridge-domain:input'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.member is not None:
                for child_ref in self.member:
                    if child_ref._has_data():
                        return True

            if self.parameter is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['CreateParameterizedBridgeDomainsRpc.Input']['meta_info']


    class Output(object):
        """
        
        
        .. attribute:: errstr
        
        	Error message from the device if RPC failed
        	**type**\:  str
        
        

        """

        _prefix = 'bd'
        _revision = '2016-12-14'

        def __init__(self):
            self.parent = None
            self.errstr = None

        @property
        def _common_path(self):

            return '/cisco-bridge-domain:create-parameterized-bridge-domains/cisco-bridge-domain:output'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            if self.parent is None:
                raise YPYError('Parent reference is needed to determine if entity has configuration data')
            return self.parent.is_config()

        def _has_data(self):
            if self.errstr is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
            return meta._meta_table['CreateParameterizedBridgeDomainsRpc.Output']['meta_info']

    @property
    def _common_path(self):

        return '/cisco-bridge-domain:create-parameterized-bridge-domains'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if self.input is not None and self.input._has_data():
            return True

        if self.output is not None and self.output._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _cisco_bridge_domain as meta
        return meta._meta_table['CreateParameterizedBridgeDomainsRpc']['meta_info']


