""" Cisco_IOS_XR_infra_policymgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ASR9k policy manager configuration.
 
Copyright (c) 2013, 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class AuthorizeIdentifier(Enum):
    """
    AuthorizeIdentifier

    Authorize identifier.

    .. data:: circuit_id = 0

    	Authorize circuit ID.

    .. data:: dhcp_client_id = 1

    	Authorize dhcp client ID.

    .. data:: remote_id = 2

    	Authorize remote ID.

    .. data:: source_address_ipv4 = 3

    	Authorize source IPv4 address.

    .. data:: source_address_ipv6 = 4

    	Authorize source IPv6 address.

    .. data:: source_address_mac = 5

    	Authorize source MAC address.

    .. data:: username = 6

    	Authorize username.

    """

    circuit_id = Enum.YLeaf(0, "circuit-id")

    dhcp_client_id = Enum.YLeaf(1, "dhcp-client-id")

    remote_id = Enum.YLeaf(2, "remote-id")

    source_address_ipv4 = Enum.YLeaf(3, "source-address-ipv4")

    source_address_ipv6 = Enum.YLeaf(4, "source-address-ipv6")

    source_address_mac = Enum.YLeaf(5, "source-address-mac")

    username = Enum.YLeaf(6, "username")


class ClassMapType(Enum):
    """
    ClassMapType

    Policy manager class\-map type.

    .. data:: qos = 1

    	QoS Classmap.

    .. data:: traffic = 3

    	TRAFFIC Classmap.

    .. data:: control = 4

    	Control Subscriber Classmap.

    """

    qos = Enum.YLeaf(1, "qos")

    traffic = Enum.YLeaf(3, "traffic")

    control = Enum.YLeaf(4, "control")


class EventType(Enum):
    """
    EventType

    Event type.

    .. data:: account_logoff = 0

    	Account logoff event.

    .. data:: account_logon = 1

    	Account logon event.

    .. data:: authentication_failure = 2

    	Authentication failure event.

    .. data:: authentication_no_response = 3

    	Authentication no response event.

    .. data:: authorization_failure = 4

    	Authorization failure event.

    .. data:: authorization_no_response = 5

    	Authorization no response event.

    .. data:: credit_exhausted = 6

    	Credit exhaustion event.

    .. data:: exception = 7

    	Exception event.

    .. data:: idle_timeout = 8

    	Idle timeout event.

    .. data:: quota_depleted = 9

    	Quota depletion event.

    .. data:: service_start = 10

    	Service start event.

    .. data:: service_stop = 11

    	Service stop event.

    .. data:: session_activate = 12

    	Session activate event.

    .. data:: session_start = 13

    	Session start event.

    .. data:: session_stop = 14

    	Session stop event.

    .. data:: timer_expiry = 15

    	Timer expiry event.

    """

    account_logoff = Enum.YLeaf(0, "account-logoff")

    account_logon = Enum.YLeaf(1, "account-logon")

    authentication_failure = Enum.YLeaf(2, "authentication-failure")

    authentication_no_response = Enum.YLeaf(3, "authentication-no-response")

    authorization_failure = Enum.YLeaf(4, "authorization-failure")

    authorization_no_response = Enum.YLeaf(5, "authorization-no-response")

    credit_exhausted = Enum.YLeaf(6, "credit-exhausted")

    exception = Enum.YLeaf(7, "exception")

    idle_timeout = Enum.YLeaf(8, "idle-timeout")

    quota_depleted = Enum.YLeaf(9, "quota-depleted")

    service_start = Enum.YLeaf(10, "service-start")

    service_stop = Enum.YLeaf(11, "service-stop")

    session_activate = Enum.YLeaf(12, "session-activate")

    session_start = Enum.YLeaf(13, "session-start")

    session_stop = Enum.YLeaf(14, "session-stop")

    timer_expiry = Enum.YLeaf(15, "timer-expiry")


class ExecutionStrategy(Enum):
    """
    ExecutionStrategy

    Executuion strategy.

    .. data:: do_all = 0

    	Do all actions.

    .. data:: do_until_failure = 1

    	Do all actions until failure.

    .. data:: do_until_success = 2

    	Do all actions until success.

    """

    do_all = Enum.YLeaf(0, "do-all")

    do_until_failure = Enum.YLeaf(1, "do-until-failure")

    do_until_success = Enum.YLeaf(2, "do-until-success")


class PmapClassMapType(Enum):
    """
    PmapClassMapType

    Policy manager class\-map type.

    .. data:: qos = 1

    	QoS Classmap.

    .. data:: traffic = 2

    	TRAFFIC Classmap.

    .. data:: subscriber_control = 3

    	Subscriber Control Classmap.

    """

    qos = Enum.YLeaf(1, "qos")

    traffic = Enum.YLeaf(2, "traffic")

    subscriber_control = Enum.YLeaf(3, "subscriber-control")


class PolicyMapType(Enum):
    """
    PolicyMapType

    Policy manager policy\-map type.

    .. data:: qos = 1

    	QoS Policymap

    .. data:: pbr = 2

    	PBR Policymap

    .. data:: traffic = 3

    	TRAFFIC Policymap

    .. data:: subscriber_control = 4

    	SUBSCRIBER-CONTROL Policymap

    .. data:: redirect = 6

    	REDIRECT Policy map

    .. data:: flow_monitor = 7

    	FLOWMONITOR Policy map

    """

    qos = Enum.YLeaf(1, "qos")

    pbr = Enum.YLeaf(2, "pbr")

    traffic = Enum.YLeaf(3, "traffic")

    subscriber_control = Enum.YLeaf(4, "subscriber-control")

    redirect = Enum.YLeaf(6, "redirect")

    flow_monitor = Enum.YLeaf(7, "flow-monitor")



class PolicyManager(Entity):
    """
    Global Policy Manager configuration.
    
    .. attribute:: class_maps
    
    	Class\-maps configuration
    	**type**\:   :py:class:`ClassMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps>`
    
    .. attribute:: policy_maps
    
    	Policy\-maps configuration
    	**type**\:   :py:class:`PolicyMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps>`
    
    

    """

    _prefix = 'infra-policymgr-cfg'
    _revision = '2017-08-11'

    def __init__(self):
        super(PolicyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "policy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-policymgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"class-maps" : ("class_maps", PolicyManager.ClassMaps), "policy-maps" : ("policy_maps", PolicyManager.PolicyMaps)}
        self._child_list_classes = {}

        self.class_maps = PolicyManager.ClassMaps()
        self.class_maps.parent = self
        self._children_name_map["class_maps"] = "class-maps"
        self._children_yang_names.add("class-maps")

        self.policy_maps = PolicyManager.PolicyMaps()
        self.policy_maps.parent = self
        self._children_name_map["policy_maps"] = "policy-maps"
        self._children_yang_names.add("policy-maps")
        self._segment_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager"


    class ClassMaps(Entity):
        """
        Class\-maps configuration.
        
        .. attribute:: class_map
        
        	Class\-map configuration
        	**type**\: list of    :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2017-08-11'

        def __init__(self):
            super(PolicyManager.ClassMaps, self).__init__()

            self.yang_name = "class-maps"
            self.yang_parent_name = "policy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"class-map" : ("class_map", PolicyManager.ClassMaps.ClassMap)}

            self.class_map = YList(self)
            self._segment_path = lambda: "class-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PolicyManager.ClassMaps, [], name, value)


        class ClassMap(Entity):
            """
            Class\-map configuration.
            
            .. attribute:: type  <key>
            
            	Type of class\-map
            	**type**\:   :py:class:`ClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.ClassMapType>`
            
            .. attribute:: name  <key>
            
            	Name of class\-map
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: class_map_mode_match_all
            
            	Match any match criteria
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: class_map_mode_match_any
            
            	Match all match criteria
            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\:  str
            
            .. attribute:: match
            
            	Match rules
            	**type**\:   :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match>`
            
            .. attribute:: match_not
            
            	Match not rules
            	**type**\:   :py:class:`MatchNot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot>`
            
            

            """

            _prefix = 'infra-policymgr-cfg'
            _revision = '2017-08-11'

            def __init__(self):
                super(PolicyManager.ClassMaps.ClassMap, self).__init__()

                self.yang_name = "class-map"
                self.yang_parent_name = "class-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"match" : ("match", PolicyManager.ClassMaps.ClassMap.Match), "match-not" : ("match_not", PolicyManager.ClassMaps.ClassMap.MatchNot)}
                self._child_list_classes = {}

                self.type = YLeaf(YType.enumeration, "type")

                self.name = YLeaf(YType.str, "name")

                self.class_map_mode_match_all = YLeaf(YType.empty, "class-map-mode-match-all")

                self.class_map_mode_match_any = YLeaf(YType.empty, "class-map-mode-match-any")

                self.description = YLeaf(YType.str, "description")

                self.match = PolicyManager.ClassMaps.ClassMap.Match()
                self.match.parent = self
                self._children_name_map["match"] = "match"
                self._children_yang_names.add("match")

                self.match_not = PolicyManager.ClassMaps.ClassMap.MatchNot()
                self.match_not.parent = self
                self._children_name_map["match_not"] = "match-not"
                self._children_yang_names.add("match-not")
                self._segment_path = lambda: "class-map" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/class-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PolicyManager.ClassMaps.ClassMap, ['type', 'name', 'class_map_mode_match_all', 'class_map_mode_match_any', 'description'], name, value)


            class Match(Entity):
                """
                Match rules.
                
                .. attribute:: atm_clp
                
                	Match ATM CLP bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: atm_oam
                
                	Match ATM OAM
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\:  str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: cac_admit
                
                	Match CAC admitted
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cac_unadmit
                
                	Match CAC unadmitted
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: circuit_id
                
                	Match Circuit ID
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: circuit_id_regex
                
                	Match Circuit id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: dei
                
                	Match DEI bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: dei_inner
                
                	Match DEI INNER  bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of    :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of    :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6>`
                
                .. attribute:: destination_mac
                
                	Match destination MAC address
                	**type**\:  list of str
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: dhcp_client_id
                
                	Match dhcp client ID
                	**type**\: list of    :py:class:`DhcpClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId>`
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\: list of    :py:class:`DhcpClientIdRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex>`
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of    :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DomainName>`
                
                .. attribute:: domain_name_regex
                
                	Match domain name
                	**type**\: list of    :py:class:`DomainNameRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex>`
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ethernet_services_acl
                
                	Match Ethernet Services
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\:  list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
                .. attribute:: flow
                
                	Match flow
                	**type**\:   :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow>`
                
                .. attribute:: flow_tag
                
                	Match flow\-tag. Should be value 1..63 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fr_de
                
                	Set FrameRelay DE bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: fragment_type
                
                	Match fragment type for a packet
                	**type**\:  list of str
                
                	**pattern:** (first\-fragment)\|(is\-fragment)\|(last\-fragment)
                
                .. attribute:: frame_relay_dlci
                
                	Match frame\-relay DLCI value.  Should be value 16..1007 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_code
                
                	Match IPv4 ICMP code.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_type
                
                	Match IPv4 ICMP type.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_code
                
                	Match IPv6 ICMP code.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_type
                
                	Match IPv6 ICMP type.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: inner_cos
                
                	Match inner CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: inner_vlan
                
                	Match inner VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv4_acl
                
                	Match IPv4 ACL
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ipv4_dscp
                
                	Match IPv4 DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv4_packet_length
                
                	Match IPv4 packet length. Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv4_precedence
                
                	Match IPv4 precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: ipv6_acl
                
                	Match IPv6 ACL
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ipv6_dscp
                
                	Match IPv6 DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv6_packet_length
                
                	Match IPv6 packet length.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv6_precedence
                
                	Match IPv6 precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: mpls_disposition_ipv4_access_list
                
                	Match MPLS Label Disposition IPv4 access list
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: mpls_experimental_imposition
                
                	Match MPLS experimental imposition label
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: mpls_experimental_topmost
                
                	Match MPLS experimental topmost label
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: packet_length
                
                	Match packet length.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: precedence
                
                	Match precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: protocol
                
                	Match protocol
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\|(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\\-([1\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5]))\|((ahp)\|(dhcpv4)\|(dhcpv6)\|(eigrp)\|(esp)\|(gre)\|(icmp)\|(igmp)\|(igrp)\|(ipinip)\|(ipv4)\|(ipv6)\|(ipv6icmp)\|(mpls)\|(nos)\|(ospf)\|(pcp)\|(pim)\|(ppp)\|(sctp)\|(tcp)\|(udp))
                
                .. attribute:: qos_group
                
                	Match QoS group. Should be value 0..512 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: remote_id
                
                	Match remote ID
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: remote_id_regex
                
                	Match remote id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of    :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of    :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6>`
                
                .. attribute:: source_mac
                
                	Match source MAC address
                	**type**\:  list of str
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flags
                	**type**\:  int
                
                	**range:** 0..4095
                
                .. attribute:: timer
                
                	Match timer
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: traffic_class
                
                	Match Traffic Class. Should be value 0..63 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: vpls_broadcast
                
                	Match VPLS Broadcast
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_control
                
                	Match VPLS control
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_known
                
                	Match VPLS Known
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_multicast
                
                	Match VPLS Multicast
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_unknown
                
                	Match VPLS Unknown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2017-08-11'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.Match, self).__init__()

                    self.yang_name = "match"
                    self.yang_parent_name = "class-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flow" : ("flow", PolicyManager.ClassMaps.ClassMap.Match.Flow)}
                    self._child_list_classes = {"destination-address-ipv4" : ("destination_address_ipv4", PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4), "destination-address-ipv6" : ("destination_address_ipv6", PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6), "dhcp-client-id" : ("dhcp_client_id", PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId), "dhcp-client-id-regex" : ("dhcp_client_id_regex", PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex), "domain-name" : ("domain_name", PolicyManager.ClassMaps.ClassMap.Match.DomainName), "domain-name-regex" : ("domain_name_regex", PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex), "source-address-ipv4" : ("source_address_ipv4", PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4), "source-address-ipv6" : ("source_address_ipv6", PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6)}

                    self.atm_clp = YLeaf(YType.uint8, "atm-clp")

                    self.atm_oam = YLeaf(YType.empty, "atm-oam")

                    self.authen_status = YLeaf(YType.str, "authen-status")

                    self.cac_admit = YLeaf(YType.empty, "cac-admit")

                    self.cac_unadmit = YLeaf(YType.empty, "cac-unadmit")

                    self.circuit_id = YLeafList(YType.str, "circuit-id")

                    self.circuit_id_regex = YLeafList(YType.str, "circuit-id-regex")

                    self.cos = YLeafList(YType.uint8, "cos")

                    self.dei = YLeaf(YType.uint8, "dei")

                    self.dei_inner = YLeaf(YType.uint8, "dei-inner")

                    self.destination_mac = YLeafList(YType.str, "destination-mac")

                    self.destination_port = YLeafList(YType.str, "destination-port")

                    self.discard_class = YLeafList(YType.uint8, "discard-class")

                    self.dscp = YLeafList(YType.str, "dscp")

                    self.ethernet_services_acl = YLeaf(YType.str, "ethernet-services-acl")

                    self.ethertype = YLeafList(YType.str, "ethertype")

                    self.flow_tag = YLeafList(YType.str, "flow-tag")

                    self.fr_de = YLeaf(YType.uint8, "fr-de")

                    self.fragment_type = YLeafList(YType.str, "fragment-type")

                    self.frame_relay_dlci = YLeafList(YType.str, "frame-relay-dlci")

                    self.icmpv4_code = YLeafList(YType.str, "icmpv4-code")

                    self.icmpv4_type = YLeafList(YType.str, "icmpv4-type")

                    self.icmpv6_code = YLeafList(YType.str, "icmpv6-code")

                    self.icmpv6_type = YLeafList(YType.str, "icmpv6-type")

                    self.inner_cos = YLeafList(YType.uint8, "inner-cos")

                    self.inner_vlan = YLeafList(YType.str, "inner-vlan")

                    self.ipv4_acl = YLeaf(YType.str, "ipv4-acl")

                    self.ipv4_dscp = YLeafList(YType.str, "ipv4-dscp")

                    self.ipv4_packet_length = YLeafList(YType.str, "ipv4-packet-length")

                    self.ipv4_precedence = YLeafList(YType.str, "ipv4-precedence")

                    self.ipv6_acl = YLeaf(YType.str, "ipv6-acl")

                    self.ipv6_dscp = YLeafList(YType.str, "ipv6-dscp")

                    self.ipv6_packet_length = YLeafList(YType.str, "ipv6-packet-length")

                    self.ipv6_precedence = YLeafList(YType.str, "ipv6-precedence")

                    self.mpls_disposition_ipv4_access_list = YLeaf(YType.str, "mpls-disposition-ipv4-access-list")

                    self.mpls_disposition_ipv6_access_list = YLeaf(YType.str, "mpls-disposition-ipv6-access-list")

                    self.mpls_experimental_imposition = YLeafList(YType.uint8, "mpls-experimental-imposition")

                    self.mpls_experimental_topmost = YLeafList(YType.uint8, "mpls-experimental-topmost")

                    self.packet_length = YLeafList(YType.str, "packet-length")

                    self.precedence = YLeafList(YType.str, "precedence")

                    self.protocol = YLeafList(YType.str, "protocol")

                    self.qos_group = YLeafList(YType.str, "qos-group")

                    self.remote_id = YLeafList(YType.str, "remote-id")

                    self.remote_id_regex = YLeafList(YType.str, "remote-id-regex")

                    self.service_name = YLeafList(YType.str, "service-name")

                    self.service_name_regex = YLeafList(YType.str, "service-name-regex")

                    self.source_mac = YLeafList(YType.str, "source-mac")

                    self.source_port = YLeafList(YType.str, "source-port")

                    self.tcp_flag = YLeaf(YType.uint16, "tcp-flag")

                    self.timer = YLeafList(YType.str, "timer")

                    self.timer_regex = YLeafList(YType.str, "timer-regex")

                    self.traffic_class = YLeafList(YType.str, "traffic-class")

                    self.user_name = YLeafList(YType.str, "user-name")

                    self.user_name_regex = YLeafList(YType.str, "user-name-regex")

                    self.vlan = YLeafList(YType.str, "vlan")

                    self.vpls_broadcast = YLeaf(YType.empty, "vpls-broadcast")

                    self.vpls_control = YLeaf(YType.empty, "vpls-control")

                    self.vpls_known = YLeaf(YType.empty, "vpls-known")

                    self.vpls_multicast = YLeaf(YType.empty, "vpls-multicast")

                    self.vpls_unknown = YLeaf(YType.empty, "vpls-unknown")

                    self.flow = PolicyManager.ClassMaps.ClassMap.Match.Flow()
                    self.flow.parent = self
                    self._children_name_map["flow"] = "flow"
                    self._children_yang_names.add("flow")

                    self.destination_address_ipv4 = YList(self)
                    self.destination_address_ipv6 = YList(self)
                    self.dhcp_client_id = YList(self)
                    self.dhcp_client_id_regex = YList(self)
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)
                    self._segment_path = lambda: "match"

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match, ['atm_clp', 'atm_oam', 'authen_status', 'cac_admit', 'cac_unadmit', 'circuit_id', 'circuit_id_regex', 'cos', 'dei', 'dei_inner', 'destination_mac', 'destination_port', 'discard_class', 'dscp', 'ethernet_services_acl', 'ethertype', 'flow_tag', 'fr_de', 'fragment_type', 'frame_relay_dlci', 'icmpv4_code', 'icmpv4_type', 'icmpv6_code', 'icmpv6_type', 'inner_cos', 'inner_vlan', 'ipv4_acl', 'ipv4_dscp', 'ipv4_packet_length', 'ipv4_precedence', 'ipv6_acl', 'ipv6_dscp', 'ipv6_packet_length', 'ipv6_precedence', 'mpls_disposition_ipv4_access_list', 'mpls_disposition_ipv6_access_list', 'mpls_experimental_imposition', 'mpls_experimental_topmost', 'packet_length', 'precedence', 'protocol', 'qos_group', 'remote_id', 'remote_id_regex', 'service_name', 'service_name_regex', 'source_mac', 'source_port', 'tcp_flag', 'timer', 'timer_regex', 'traffic_class', 'user_name', 'user_name_regex', 'vlan', 'vpls_broadcast', 'vpls_control', 'vpls_known', 'vpls_multicast', 'vpls_unknown'], name, value)


                class DestinationAddressIpv4(Entity):
                    """
                    Match destination IPv4 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IPv4 netmask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")
                        self._segment_path = lambda: "destination-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, ['address', 'netmask'], name, value)


                class DestinationAddressIpv6(Entity):
                    """
                    Match destination IPv6 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	IPv6 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "destination-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, ['address', 'prefix_length'], name, value)


                class DhcpClientId(Entity):
                    """
                    Match dhcp client ID.
                    
                    .. attribute:: value  <key>
                    
                    	Dhcp client Id
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  <key>
                    
                    	Dhcp client id Ascii/Hex
                    	**type**\:  str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId, self).__init__()

                        self.yang_name = "dhcp-client-id"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.value = YLeaf(YType.str, "value")

                        self.flag = YLeaf(YType.str, "flag")
                        self._segment_path = lambda: "dhcp-client-id" + "[value='" + self.value.get() + "']" + "[flag='" + self.flag.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId, ['value', 'flag'], name, value)


                class DhcpClientIdRegex(Entity):
                    """
                    Match dhcp client id regex.
                    
                    .. attribute:: value  <key>
                    
                    	Dhcp client id regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  <key>
                    
                    	Dhcp client Id regex Ascii/Hex
                    	**type**\:  str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex, self).__init__()

                        self.yang_name = "dhcp-client-id-regex"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.value = YLeaf(YType.str, "value")

                        self.flag = YLeaf(YType.str, "flag")
                        self._segment_path = lambda: "dhcp-client-id-regex" + "[value='" + self.value.get() + "']" + "[flag='" + self.flag.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex, ['value', 'flag'], name, value)


                class DomainName(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: name  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.format = YLeaf(YType.str, "format")
                        self._segment_path = lambda: "domain-name" + "[name='" + self.name.get() + "']" + "[format='" + self.format.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DomainName, ['name', 'format'], name, value)


                class DomainNameRegex(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: regex  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.regex = YLeaf(YType.str, "regex")

                        self.format = YLeaf(YType.str, "format")
                        self._segment_path = lambda: "domain-name-regex" + "[regex='" + self.regex.get() + "']" + "[format='" + self.format.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, ['regex', 'format'], name, value)


                class Flow(Entity):
                    """
                    Match flow.
                    
                    .. attribute:: flow_cache
                    
                    	Configure the flow\-cache parameters
                    	**type**\:   :py:class:`FlowCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache>`
                    
                    .. attribute:: flow_key
                    
                    	Configure the flow\-key parameters
                    	**type**\:  list of str
                    
                    	**pattern:** (SourceIP)\|(DestinationIP)\|(5Tuple)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"flow-cache" : ("flow_cache", PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache)}
                        self._child_list_classes = {}

                        self.flow_key = YLeafList(YType.str, "flow-key")

                        self.flow_cache = PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache()
                        self.flow_cache.parent = self
                        self._children_name_map["flow_cache"] = "flow-cache"
                        self._children_yang_names.add("flow-cache")
                        self._segment_path = lambda: "flow"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.Flow, ['flow_key'], name, value)


                    class FlowCache(Entity):
                        """
                        Configure the flow\-cache parameters
                        
                        .. attribute:: idle_timeout
                        
                        	Maximum time of inactivity for a flow
                        	**type**\: one of the below types:
                        
                        	**type**\:  int
                        
                        	**range:** 10..2550
                        
                        
                        ----
                        	**type**\:  str
                        
                        	**pattern:** (None)\|(none)
                        
                        
                        ----
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, self).__init__()

                            self.yang_name = "flow-cache"
                            self.yang_parent_name = "flow"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.idle_timeout = YLeaf(YType.str, "idle-timeout")
                            self._segment_path = lambda: "flow-cache"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, ['idle_timeout'], name, value)


                class SourceAddressIpv4(Entity):
                    """
                    Match source IPv4 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IPv4 netmask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")
                        self._segment_path = lambda: "source-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, ['address', 'netmask'], name, value)


                class SourceAddressIpv6(Entity):
                    """
                    Match source IPv6 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	IPv6 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "source-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, ['address', 'prefix_length'], name, value)


            class MatchNot(Entity):
                """
                Match not rules.
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\:  str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: circuit_id
                
                	Match Circuit ID
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: circuit_id_regex
                
                	Match Circuit id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: dei
                
                	Match DEI bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: dei_inner
                
                	Match DEI INNER  bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of    :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of    :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6>`
                
                .. attribute:: destination_mac
                
                	Match destination MAC address
                	**type**\:  list of str
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: dhcp_client_id
                
                	Match dhcp client ID
                	**type**\: list of    :py:class:`DhcpClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId>`
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\: list of    :py:class:`DhcpClientIdRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex>`
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of    :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName>`
                
                .. attribute:: domain_name_regex
                
                	Match domain name
                	**type**\: list of    :py:class:`DomainNameRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex>`
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ethernet_services_acl
                
                	Match Ethernet Services
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\:  list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
                .. attribute:: flow
                
                	Match flow
                	**type**\:   :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.Flow>`
                
                .. attribute:: flow_tag
                
                	Match flow\-tag. Should be value 1..63 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fr_de
                
                	Set FrameRelay DE bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: fragment_type
                
                	Match fragment type for a packet
                	**type**\:  list of str
                
                	**pattern:** (first\-fragment)\|(is\-fragment)\|(last\-fragment)
                
                .. attribute:: frame_relay_dlci
                
                	Match frame\-relay DLCI value.  Should be value 16..1007 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_code
                
                	Match IPv4 ICMP code.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_type
                
                	Match IPv4 ICMP type.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_code
                
                	Match IPv6 ICMP code.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_type
                
                	Match IPv6 ICMP type.  Should be value 0..255 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: inner_cos
                
                	Match inner CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: inner_vlan
                
                	Match inner VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv4_acl
                
                	Match IPv4 ACL
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ipv4_dscp
                
                	Match IPv4 DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv4_packet_length
                
                	Match IPv4 packet length. Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv4_precedence
                
                	Match IPv4 precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: ipv6_acl
                
                	Match IPv6 ACL
                	**type**\:  str
                
                	**length:** 1..64
                
                .. attribute:: ipv6_dscp
                
                	Match IPv6 DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv6_packet_length
                
                	Match IPv6 packet length.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv6_precedence
                
                	Match IPv6 precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: mpls_disposition_ipv4_access_list
                
                	Match MPLS Label Disposition IPv4 access list
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\:  str
                
                	**length:** 1..32
                
                .. attribute:: mpls_experimental_imposition
                
                	Match MPLS experimental imposition label
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: mpls_experimental_topmost
                
                	Match MPLS experimental topmost label
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: packet_length
                
                	Match packet length.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: precedence
                
                	Match precedence
                	**type**\: one of the below types:
                
                	**type**\:  list of int
                
                	**range:** 0..7
                
                
                ----
                	**type**\:  list of str
                
                	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                
                ----
                .. attribute:: protocol
                
                	Match protocol
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\|(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\\-([1\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5]))\|((ahp)\|(dhcpv4)\|(dhcpv6)\|(eigrp)\|(esp)\|(gre)\|(icmp)\|(igmp)\|(igrp)\|(ipinip)\|(ipv4)\|(ipv6)\|(ipv6icmp)\|(mpls)\|(nos)\|(ospf)\|(pcp)\|(pim)\|(ppp)\|(sctp)\|(tcp)\|(udp))
                
                .. attribute:: qos_group
                
                	Match QoS group. Should be value 0..512 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: remote_id
                
                	Match remote ID
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: remote_id_regex
                
                	Match remote id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of    :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of    :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6>`
                
                .. attribute:: source_mac
                
                	Match source MAC address
                	**type**\:  list of str
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flags
                	**type**\:  int
                
                	**range:** 0..4095
                
                .. attribute:: timer
                
                	Match timer
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: traffic_class
                
                	Match Traffic Class. Should be value 0..63 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: vpls_broadcast
                
                	Match VPLS Broadcast
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_control
                
                	Match VPLS control
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_known
                
                	Match VPLS Known
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_multicast
                
                	Match VPLS Multicast
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_unknown
                
                	Match VPLS Unknown
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2017-08-11'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.MatchNot, self).__init__()

                    self.yang_name = "match-not"
                    self.yang_parent_name = "class-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"flow" : ("flow", PolicyManager.ClassMaps.ClassMap.MatchNot.Flow)}
                    self._child_list_classes = {"destination-address-ipv4" : ("destination_address_ipv4", PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4), "destination-address-ipv6" : ("destination_address_ipv6", PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6), "dhcp-client-id" : ("dhcp_client_id", PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId), "dhcp-client-id-regex" : ("dhcp_client_id_regex", PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex), "domain-name" : ("domain_name", PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName), "domain-name-regex" : ("domain_name_regex", PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex), "source-address-ipv4" : ("source_address_ipv4", PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4), "source-address-ipv6" : ("source_address_ipv6", PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6)}

                    self.authen_status = YLeaf(YType.str, "authen-status")

                    self.circuit_id = YLeafList(YType.str, "circuit-id")

                    self.circuit_id_regex = YLeafList(YType.str, "circuit-id-regex")

                    self.cos = YLeafList(YType.uint8, "cos")

                    self.dei = YLeaf(YType.uint8, "dei")

                    self.dei_inner = YLeaf(YType.uint8, "dei-inner")

                    self.destination_mac = YLeafList(YType.str, "destination-mac")

                    self.destination_port = YLeafList(YType.str, "destination-port")

                    self.discard_class = YLeafList(YType.uint8, "discard-class")

                    self.dscp = YLeafList(YType.str, "dscp")

                    self.ethernet_services_acl = YLeaf(YType.str, "ethernet-services-acl")

                    self.ethertype = YLeafList(YType.str, "ethertype")

                    self.flow_tag = YLeafList(YType.str, "flow-tag")

                    self.fr_de = YLeaf(YType.uint8, "fr-de")

                    self.fragment_type = YLeafList(YType.str, "fragment-type")

                    self.frame_relay_dlci = YLeafList(YType.str, "frame-relay-dlci")

                    self.icmpv4_code = YLeafList(YType.str, "icmpv4-code")

                    self.icmpv4_type = YLeafList(YType.str, "icmpv4-type")

                    self.icmpv6_code = YLeafList(YType.str, "icmpv6-code")

                    self.icmpv6_type = YLeafList(YType.str, "icmpv6-type")

                    self.inner_cos = YLeafList(YType.uint8, "inner-cos")

                    self.inner_vlan = YLeafList(YType.str, "inner-vlan")

                    self.ipv4_acl = YLeaf(YType.str, "ipv4-acl")

                    self.ipv4_dscp = YLeafList(YType.str, "ipv4-dscp")

                    self.ipv4_packet_length = YLeafList(YType.str, "ipv4-packet-length")

                    self.ipv4_precedence = YLeafList(YType.str, "ipv4-precedence")

                    self.ipv6_acl = YLeaf(YType.str, "ipv6-acl")

                    self.ipv6_dscp = YLeafList(YType.str, "ipv6-dscp")

                    self.ipv6_packet_length = YLeafList(YType.str, "ipv6-packet-length")

                    self.ipv6_precedence = YLeafList(YType.str, "ipv6-precedence")

                    self.mpls_disposition_ipv4_access_list = YLeaf(YType.str, "mpls-disposition-ipv4-access-list")

                    self.mpls_disposition_ipv6_access_list = YLeaf(YType.str, "mpls-disposition-ipv6-access-list")

                    self.mpls_experimental_imposition = YLeafList(YType.uint8, "mpls-experimental-imposition")

                    self.mpls_experimental_topmost = YLeafList(YType.uint8, "mpls-experimental-topmost")

                    self.packet_length = YLeafList(YType.str, "packet-length")

                    self.precedence = YLeafList(YType.str, "precedence")

                    self.protocol = YLeafList(YType.str, "protocol")

                    self.qos_group = YLeafList(YType.str, "qos-group")

                    self.remote_id = YLeafList(YType.str, "remote-id")

                    self.remote_id_regex = YLeafList(YType.str, "remote-id-regex")

                    self.service_name = YLeafList(YType.str, "service-name")

                    self.service_name_regex = YLeafList(YType.str, "service-name-regex")

                    self.source_mac = YLeafList(YType.str, "source-mac")

                    self.source_port = YLeafList(YType.str, "source-port")

                    self.tcp_flag = YLeaf(YType.uint16, "tcp-flag")

                    self.timer = YLeafList(YType.str, "timer")

                    self.timer_regex = YLeafList(YType.str, "timer-regex")

                    self.traffic_class = YLeafList(YType.str, "traffic-class")

                    self.user_name = YLeafList(YType.str, "user-name")

                    self.user_name_regex = YLeafList(YType.str, "user-name-regex")

                    self.vlan = YLeafList(YType.str, "vlan")

                    self.vpls_broadcast = YLeaf(YType.empty, "vpls-broadcast")

                    self.vpls_control = YLeaf(YType.empty, "vpls-control")

                    self.vpls_known = YLeaf(YType.empty, "vpls-known")

                    self.vpls_multicast = YLeaf(YType.empty, "vpls-multicast")

                    self.vpls_unknown = YLeaf(YType.empty, "vpls-unknown")

                    self.flow = PolicyManager.ClassMaps.ClassMap.MatchNot.Flow()
                    self.flow.parent = self
                    self._children_name_map["flow"] = "flow"
                    self._children_yang_names.add("flow")

                    self.destination_address_ipv4 = YList(self)
                    self.destination_address_ipv6 = YList(self)
                    self.dhcp_client_id = YList(self)
                    self.dhcp_client_id_regex = YList(self)
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)
                    self._segment_path = lambda: "match-not"

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot, ['authen_status', 'circuit_id', 'circuit_id_regex', 'cos', 'dei', 'dei_inner', 'destination_mac', 'destination_port', 'discard_class', 'dscp', 'ethernet_services_acl', 'ethertype', 'flow_tag', 'fr_de', 'fragment_type', 'frame_relay_dlci', 'icmpv4_code', 'icmpv4_type', 'icmpv6_code', 'icmpv6_type', 'inner_cos', 'inner_vlan', 'ipv4_acl', 'ipv4_dscp', 'ipv4_packet_length', 'ipv4_precedence', 'ipv6_acl', 'ipv6_dscp', 'ipv6_packet_length', 'ipv6_precedence', 'mpls_disposition_ipv4_access_list', 'mpls_disposition_ipv6_access_list', 'mpls_experimental_imposition', 'mpls_experimental_topmost', 'packet_length', 'precedence', 'protocol', 'qos_group', 'remote_id', 'remote_id_regex', 'service_name', 'service_name_regex', 'source_mac', 'source_port', 'tcp_flag', 'timer', 'timer_regex', 'traffic_class', 'user_name', 'user_name_regex', 'vlan', 'vpls_broadcast', 'vpls_control', 'vpls_known', 'vpls_multicast', 'vpls_unknown'], name, value)


                class DestinationAddressIpv4(Entity):
                    """
                    Match destination IPv4 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IPv4 netmask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")
                        self._segment_path = lambda: "destination-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, ['address', 'netmask'], name, value)


                class DestinationAddressIpv6(Entity):
                    """
                    Match destination IPv6 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	IPv6 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "destination-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, ['address', 'prefix_length'], name, value)


                class DhcpClientId(Entity):
                    """
                    Match dhcp client ID.
                    
                    .. attribute:: value  <key>
                    
                    	Dhcp client Id
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  <key>
                    
                    	Dhcp client id Ascii/Hex
                    	**type**\:  str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId, self).__init__()

                        self.yang_name = "dhcp-client-id"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.value = YLeaf(YType.str, "value")

                        self.flag = YLeaf(YType.str, "flag")
                        self._segment_path = lambda: "dhcp-client-id" + "[value='" + self.value.get() + "']" + "[flag='" + self.flag.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId, ['value', 'flag'], name, value)


                class DhcpClientIdRegex(Entity):
                    """
                    Match dhcp client id regex.
                    
                    .. attribute:: value  <key>
                    
                    	Dhcp client id regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  <key>
                    
                    	Dhcp client Id regex Ascii/Hex
                    	**type**\:  str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex, self).__init__()

                        self.yang_name = "dhcp-client-id-regex"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.value = YLeaf(YType.str, "value")

                        self.flag = YLeaf(YType.str, "flag")
                        self._segment_path = lambda: "dhcp-client-id-regex" + "[value='" + self.value.get() + "']" + "[flag='" + self.flag.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex, ['value', 'flag'], name, value)


                class DomainName(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: name  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.name = YLeaf(YType.str, "name")

                        self.format = YLeaf(YType.str, "format")
                        self._segment_path = lambda: "domain-name" + "[name='" + self.name.get() + "']" + "[format='" + self.format.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, ['name', 'format'], name, value)


                class DomainNameRegex(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: regex  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.regex = YLeaf(YType.str, "regex")

                        self.format = YLeaf(YType.str, "format")
                        self._segment_path = lambda: "domain-name-regex" + "[regex='" + self.regex.get() + "']" + "[format='" + self.format.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, ['regex', 'format'], name, value)


                class Flow(Entity):
                    """
                    Match flow.
                    
                    .. attribute:: flow_tag
                    
                    	Configure the flow\-tag parameters
                    	**type**\:  list of int
                    
                    	**range:** 1..63
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.flow_tag = YLeafList(YType.uint16, "flow-tag")
                        self._segment_path = lambda: "flow"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, ['flow_tag'], name, value)


                class SourceAddressIpv4(Entity):
                    """
                    Match source IPv4 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  <key>
                    
                    	IPv4 netmask
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")
                        self._segment_path = lambda: "source-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, ['address', 'netmask'], name, value)


                class SourceAddressIpv6(Entity):
                    """
                    Match source IPv6 address.
                    
                    .. attribute:: address  <key>
                    
                    	IPv6 address
                    	**type**\:  str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  <key>
                    
                    	IPv6 prefix length
                    	**type**\:  int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")
                        self._segment_path = lambda: "source-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, ['address', 'prefix_length'], name, value)


    class PolicyMaps(Entity):
        """
        Policy\-maps configuration.
        
        .. attribute:: policy_map
        
        	Policy\-map configuration
        	**type**\: list of    :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2017-08-11'

        def __init__(self):
            super(PolicyManager.PolicyMaps, self).__init__()

            self.yang_name = "policy-maps"
            self.yang_parent_name = "policy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"policy-map" : ("policy_map", PolicyManager.PolicyMaps.PolicyMap)}

            self.policy_map = YList(self)
            self._segment_path = lambda: "policy-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(PolicyManager.PolicyMaps, [], name, value)


        class PolicyMap(Entity):
            """
            Policy\-map configuration.
            
            .. attribute:: type  <key>
            
            	Type of policy\-map
            	**type**\:   :py:class:`PolicyMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyMapType>`
            
            .. attribute:: name  <key>
            
            	Name of policy\-map
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\:  str
            
            .. attribute:: event
            
            	Policy event
            	**type**\: list of    :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event>`
            
            .. attribute:: policy_map_rule
            
            	Class\-map rule
            	**type**\: list of    :py:class:`PolicyMapRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule>`
            
            

            """

            _prefix = 'infra-policymgr-cfg'
            _revision = '2017-08-11'

            def __init__(self):
                super(PolicyManager.PolicyMaps.PolicyMap, self).__init__()

                self.yang_name = "policy-map"
                self.yang_parent_name = "policy-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"event" : ("event", PolicyManager.PolicyMaps.PolicyMap.Event), "policy-map-rule" : ("policy_map_rule", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule)}

                self.type = YLeaf(YType.enumeration, "type")

                self.name = YLeaf(YType.str, "name")

                self.description = YLeaf(YType.str, "description")

                self.event = YList(self)
                self.policy_map_rule = YList(self)
                self._segment_path = lambda: "policy-map" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/policy-maps/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap, ['type', 'name', 'description'], name, value)


            class Event(Entity):
                """
                Policy event.
                
                .. attribute:: event_type  <key>
                
                	Event type
                	**type**\:   :py:class:`EventType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.EventType>`
                
                .. attribute:: class_
                
                	Class\-map rule
                	**type**\: list of    :py:class:`Class_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_>`
                
                .. attribute:: event_mode_match_all
                
                	Execute all the matched classes
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: event_mode_match_first
                
                	Execute only the first matched class
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2017-08-11'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.Event, self).__init__()

                    self.yang_name = "event"
                    self.yang_parent_name = "policy-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"class" : ("class_", PolicyManager.PolicyMaps.PolicyMap.Event.Class_)}

                    self.event_type = YLeaf(YType.enumeration, "event-type")

                    self.event_mode_match_all = YLeaf(YType.empty, "event-mode-match-all")

                    self.event_mode_match_first = YLeaf(YType.empty, "event-mode-match-first")

                    self.class_ = YList(self)
                    self._segment_path = lambda: "event" + "[event-type='" + self.event_type.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event, ['event_type', 'event_mode_match_all', 'event_mode_match_first'], name, value)


                class Class_(Entity):
                    """
                    Class\-map rule.
                    
                    .. attribute:: class_name  <key>
                    
                    	Name of class
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: class_type  <key>
                    
                    	Type of class
                    	**type**\:   :py:class:`PmapClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PmapClassMapType>`
                    
                    .. attribute:: action_rule
                    
                    	Action rule
                    	**type**\: list of    :py:class:`ActionRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule>`
                    
                    .. attribute:: class_execution_strategy
                    
                    	Class execution strategy
                    	**type**\:   :py:class:`ExecutionStrategy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.ExecutionStrategy>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_, self).__init__()

                        self.yang_name = "class"
                        self.yang_parent_name = "event"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {"action-rule" : ("action_rule", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule)}

                        self.class_name = YLeaf(YType.str, "class-name")

                        self.class_type = YLeaf(YType.enumeration, "class-type")

                        self.class_execution_strategy = YLeaf(YType.enumeration, "class-execution-strategy")

                        self.action_rule = YList(self)
                        self._segment_path = lambda: "class" + "[class-name='" + self.class_name.get() + "']" + "[class-type='" + self.class_type.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_, ['class_name', 'class_type', 'class_execution_strategy'], name, value)


                    class ActionRule(Entity):
                        """
                        Action rule.
                        
                        .. attribute:: action_sequence_number  <key>
                        
                        	Sequence number for this action
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: activate_dynamic_template
                        
                        	Activate dynamic templates
                        	**type**\:   :py:class:`ActivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: authenticate
                        
                        	Authentication related configuration
                        	**type**\:   :py:class:`Authenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate>`
                        
                        .. attribute:: authorize
                        
                        	Authorize
                        	**type**\:   :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: deactivate_dynamic_template
                        
                        	Deactivate dynamic templates
                        	**type**\:   :py:class:`DeactivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: disconnect
                        
                        	Disconnect session
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: monitor
                        
                        	Monitor session
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set_timer
                        
                        	Set a timer to execute a rule on its  expiry
                        	**type**\:   :py:class:`SetTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: stop_timer
                        
                        	Disable timer before it expires
                        	**type**\:   :py:class:`StopTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule, self).__init__()

                            self.yang_name = "action-rule"
                            self.yang_parent_name = "class"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"activate-dynamic-template" : ("activate_dynamic_template", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate), "authenticate" : ("authenticate", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate), "authorize" : ("authorize", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize), "deactivate-dynamic-template" : ("deactivate_dynamic_template", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate), "set-timer" : ("set_timer", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer), "stop-timer" : ("stop_timer", PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer)}
                            self._child_list_classes = {}

                            self.action_sequence_number = YLeaf(YType.uint16, "action-sequence-number")

                            self.disconnect = YLeaf(YType.empty, "disconnect")

                            self.monitor = YLeaf(YType.empty, "monitor")

                            self.activate_dynamic_template = None
                            self._children_name_map["activate_dynamic_template"] = "activate-dynamic-template"
                            self._children_yang_names.add("activate-dynamic-template")

                            self.authenticate = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate()
                            self.authenticate.parent = self
                            self._children_name_map["authenticate"] = "authenticate"
                            self._children_yang_names.add("authenticate")

                            self.authorize = None
                            self._children_name_map["authorize"] = "authorize"
                            self._children_yang_names.add("authorize")

                            self.deactivate_dynamic_template = None
                            self._children_name_map["deactivate_dynamic_template"] = "deactivate-dynamic-template"
                            self._children_yang_names.add("deactivate-dynamic-template")

                            self.set_timer = None
                            self._children_name_map["set_timer"] = "set-timer"
                            self._children_yang_names.add("set-timer")

                            self.stop_timer = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer()
                            self.stop_timer.parent = self
                            self._children_name_map["stop_timer"] = "stop-timer"
                            self._children_yang_names.add("stop-timer")
                            self._segment_path = lambda: "action-rule" + "[action-sequence-number='" + self.action_sequence_number.get() + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule, ['action_sequence_number', 'disconnect', 'monitor'], name, value)


                        class ActivateDynamicTemplate(Entity):
                            """
                            Activate dynamic templates.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate, self).__init__()

                                self.yang_name = "activate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

                                self.name = YLeaf(YType.str, "name")
                                self._segment_path = lambda: "activate-dynamic-template"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate, ['aaa_list', 'name'], name, value)


                        class Authenticate(Entity):
                            """
                            Authentication related configuration.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate, self).__init__()

                                self.yang_name = "authenticate"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.aaa_list = YLeaf(YType.str, "aaa-list")
                                self._segment_path = lambda: "authenticate"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate, ['aaa_list'], name, value)


                        class Authorize(Entity):
                            """
                            Authorize.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: format
                            
                            	Specify an Authorize format name
                            	**type**\:  str
                            
                            .. attribute:: identifier
                            
                            	Specify an Authorize format name
                            	**type**\:   :py:class:`AuthorizeIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.AuthorizeIdentifier>`
                            
                            .. attribute:: password
                            
                            	Specify a password to be used for AAA request
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize, self).__init__()

                                self.yang_name = "authorize"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

                                self.format = YLeaf(YType.str, "format")

                                self.identifier = YLeaf(YType.enumeration, "identifier")

                                self.password = YLeaf(YType.str, "password")
                                self._segment_path = lambda: "authorize"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize, ['aaa_list', 'format', 'identifier', 'password'], name, value)


                        class DeactivateDynamicTemplate(Entity):
                            """
                            Deactivate dynamic templates.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate, self).__init__()

                                self.yang_name = "deactivate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

                                self.name = YLeaf(YType.str, "name")
                                self._segment_path = lambda: "deactivate-dynamic-template"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate, ['aaa_list', 'name'], name, value)


                        class SetTimer(Entity):
                            """
                            Set a timer to execute a rule on its 
                            expiry
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: timer_value
                            
                            	Timer value in minutes
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: minutes
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer, self).__init__()

                                self.yang_name = "set-timer"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}
                                self.is_presence_container = True

                                self.timer_name = YLeaf(YType.str, "timer-name")

                                self.timer_value = YLeaf(YType.uint32, "timer-value")
                                self._segment_path = lambda: "set-timer"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer, ['timer_name', 'timer_value'], name, value)


                        class StopTimer(Entity):
                            """
                            Disable timer before it expires.
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer, self).__init__()

                                self.yang_name = "stop-timer"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.timer_name = YLeaf(YType.str, "timer-name")
                                self._segment_path = lambda: "stop-timer"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer, ['timer_name'], name, value)


            class PolicyMapRule(Entity):
                """
                Class\-map rule.
                
                .. attribute:: class_name  <key>
                
                	Name of class\-map
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                
                .. attribute:: class_type  <key>
                
                	Type of class\-map
                	**type**\:   :py:class:`PmapClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PmapClassMapType>`
                
                .. attribute:: bandwidth_remaining
                
                	Policy action bandwidth remaining queue
                	**type**\:   :py:class:`BandwidthRemaining <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining>`
                
                .. attribute:: cac_local
                
                	Policy action CAC
                	**type**\:   :py:class:`CacLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal>`
                
                .. attribute:: decap_gre
                
                	Policy action DECAP GRE
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: default_red
                
                	Default random early detection
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ecn_red
                
                	ECN based random early detection
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: flow_params
                
                	Policy flow monitoring action
                	**type**\:   :py:class:`FlowParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams>`
                
                .. attribute:: fragment
                
                	Policy action fragment. Fragment name
                	**type**\:  str
                
                .. attribute:: http_redirect
                
                	Policy action http redirect. Redirect to this url
                	**type**\:  str
                
                .. attribute:: metrics_ipcbr
                
                	Policy IP\-CBR metric action
                	**type**\:   :py:class:`MetricsIpcbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr>`
                
                .. attribute:: min_bandwidth
                
                	Policy action minimum bandwidth queue
                	**type**\:   :py:class:`MinBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth>`
                
                .. attribute:: pbr_drop
                
                	Policy action PBR drop
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: pbr_forward
                
                	Policy action PBR forward
                	**type**\:   :py:class:`PbrForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward>`
                
                .. attribute:: pbr_redirect
                
                	Policy action redirect
                	**type**\:   :py:class:`PbrRedirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect>`
                
                .. attribute:: pbr_transmit
                
                	Policy action PBR transmit
                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: pfc
                
                	Policy action pfc
                	**type**\:   :py:class:`Pfc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc>`
                
                .. attribute:: police
                
                	Configures traffic policing action
                	**type**\:   :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police>`
                
                .. attribute:: priority_level
                
                	Priority level
                	**type**\:  int
                
                	**range:** 1..7
                
                .. attribute:: queue_limit
                
                	Policy action queue limit
                	**type**\:   :py:class:`QueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit>`
                
                .. attribute:: random_detect
                
                	Random early detection. All RED profiles in a class must be based on the same field
                	**type**\: list of    :py:class:`RandomDetect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect>`
                
                .. attribute:: react
                
                	Policy action react
                	**type**\:   :py:class:`React <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React>`
                
                .. attribute:: service_fragment
                
                	Policy action service fragment.  Service fragment name
                	**type**\:  str
                
                .. attribute:: service_function_path
                
                	Policy action service function path
                	**type**\:   :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath>`
                
                	**presence node**\: True
                
                .. attribute:: service_policy
                
                	Configure a child service policy
                	**type**\:   :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy>`
                
                .. attribute:: set
                
                	Policy action packet marking
                	**type**\:   :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set>`
                
                .. attribute:: shape
                
                	Policy action shape
                	**type**\:   :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2017-08-11'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, self).__init__()

                    self.yang_name = "policy-map-rule"
                    self.yang_parent_name = "policy-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"bandwidth-remaining" : ("bandwidth_remaining", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining), "cac-local" : ("cac_local", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal), "flow-params" : ("flow_params", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams), "metrics-ipcbr" : ("metrics_ipcbr", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr), "min-bandwidth" : ("min_bandwidth", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth), "pbr-forward" : ("pbr_forward", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward), "pbr-redirect" : ("pbr_redirect", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect), "pfc" : ("pfc", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc), "police" : ("police", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police), "queue-limit" : ("queue_limit", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit), "react" : ("react", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React), "service-function-path" : ("service_function_path", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath), "service-policy" : ("service_policy", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy), "set" : ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set), "shape" : ("shape", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape)}
                    self._child_list_classes = {"random-detect" : ("random_detect", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect)}

                    self.class_name = YLeaf(YType.str, "class-name")

                    self.class_type = YLeaf(YType.enumeration, "class-type")

                    self.decap_gre = YLeaf(YType.empty, "decap-gre")

                    self.default_red = YLeaf(YType.empty, "default-red")

                    self.ecn_red = YLeaf(YType.empty, "ecn-red")

                    self.fragment = YLeaf(YType.str, "fragment")

                    self.http_redirect = YLeaf(YType.str, "http-redirect")

                    self.pbr_drop = YLeaf(YType.empty, "pbr-drop")

                    self.pbr_transmit = YLeaf(YType.empty, "pbr-transmit")

                    self.priority_level = YLeaf(YType.uint8, "priority-level")

                    self.service_fragment = YLeaf(YType.str, "service-fragment")

                    self.bandwidth_remaining = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining()
                    self.bandwidth_remaining.parent = self
                    self._children_name_map["bandwidth_remaining"] = "bandwidth-remaining"
                    self._children_yang_names.add("bandwidth-remaining")

                    self.cac_local = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal()
                    self.cac_local.parent = self
                    self._children_name_map["cac_local"] = "cac-local"
                    self._children_yang_names.add("cac-local")

                    self.flow_params = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams()
                    self.flow_params.parent = self
                    self._children_name_map["flow_params"] = "flow-params"
                    self._children_yang_names.add("flow-params")

                    self.metrics_ipcbr = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr()
                    self.metrics_ipcbr.parent = self
                    self._children_name_map["metrics_ipcbr"] = "metrics-ipcbr"
                    self._children_yang_names.add("metrics-ipcbr")

                    self.min_bandwidth = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth()
                    self.min_bandwidth.parent = self
                    self._children_name_map["min_bandwidth"] = "min-bandwidth"
                    self._children_yang_names.add("min-bandwidth")

                    self.pbr_forward = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward()
                    self.pbr_forward.parent = self
                    self._children_name_map["pbr_forward"] = "pbr-forward"
                    self._children_yang_names.add("pbr-forward")

                    self.pbr_redirect = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect()
                    self.pbr_redirect.parent = self
                    self._children_name_map["pbr_redirect"] = "pbr-redirect"
                    self._children_yang_names.add("pbr-redirect")

                    self.pfc = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc()
                    self.pfc.parent = self
                    self._children_name_map["pfc"] = "pfc"
                    self._children_yang_names.add("pfc")

                    self.police = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police()
                    self.police.parent = self
                    self._children_name_map["police"] = "police"
                    self._children_yang_names.add("police")

                    self.queue_limit = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit()
                    self.queue_limit.parent = self
                    self._children_name_map["queue_limit"] = "queue-limit"
                    self._children_yang_names.add("queue-limit")

                    self.react = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React()
                    self.react.parent = self
                    self._children_name_map["react"] = "react"
                    self._children_yang_names.add("react")

                    self.service_function_path = None
                    self._children_name_map["service_function_path"] = "service-function-path"
                    self._children_yang_names.add("service-function-path")

                    self.service_policy = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"
                    self._children_yang_names.add("service-policy")

                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set()
                    self.set.parent = self
                    self._children_name_map["set"] = "set"
                    self._children_yang_names.add("set")

                    self.shape = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape()
                    self.shape.parent = self
                    self._children_name_map["shape"] = "shape"
                    self._children_yang_names.add("shape")

                    self.random_detect = YList(self)
                    self._segment_path = lambda: "policy-map-rule" + "[class-name='" + self.class_name.get() + "']" + "[class-type='" + self.class_type.get() + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, ['class_name', 'class_type', 'decap_gre', 'default_red', 'ecn_red', 'fragment', 'http_redirect', 'pbr_drop', 'pbr_transmit', 'priority_level', 'service_fragment'], name, value)


                class BandwidthRemaining(Entity):
                    """
                    Policy action bandwidth remaining queue.
                    
                    .. attribute:: unit
                    
                    	Remaining bandwidth units
                    	**type**\:  str
                    
                    	**pattern:** (percent)\|(ratio)
                    
                    .. attribute:: value
                    
                    	Remaining bandwidth value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, self).__init__()

                        self.yang_name = "bandwidth-remaining"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.unit = YLeaf(YType.str, "unit")

                        self.value = YLeaf(YType.uint32, "value")
                        self._segment_path = lambda: "bandwidth-remaining"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, ['unit', 'value'], name, value)


                class CacLocal(Entity):
                    """
                    Policy action CAC.
                    
                    .. attribute:: flow_idle_timeout
                    
                    	The interval after which a flow is removed,  if there is no activity. If timeout is 0 this flow does not expire
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 10..2550
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (None)\|(none)
                    
                    
                    ----
                    .. attribute:: flow_rate
                    
                    	The rate allocated per flow
                    	**type**\:   :py:class:`FlowRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate>`
                    
                    .. attribute:: rate
                    
                    	The rate allocated for all flows
                    	**type**\:   :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, self).__init__()

                        self.yang_name = "cac-local"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"flow-rate" : ("flow_rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate), "rate" : ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate)}
                        self._child_list_classes = {}

                        self.flow_idle_timeout = YLeaf(YType.str, "flow-idle-timeout")

                        self.flow_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate()
                        self.flow_rate.parent = self
                        self._children_name_map["flow_rate"] = "flow-rate"
                        self._children_yang_names.add("flow-rate")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")
                        self._segment_path = lambda: "cac-local"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, ['flow_idle_timeout'], name, value)


                    class FlowRate(Entity):
                        """
                        The rate allocated per flow.
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(cellsps)
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, self).__init__()

                            self.yang_name = "flow-rate"
                            self.yang_parent_name = "cac-local"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "flow-rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, ['units', 'value'], name, value)


                    class Rate(Entity):
                        """
                        The rate allocated for all flows.
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(cellsps)
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 1..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "cac-local"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, ['units', 'value'], name, value)


                class FlowParams(Entity):
                    """
                    Policy flow monitoring action.
                    
                    .. attribute:: history
                    
                    	Keep stats/metrics on box for so many intervals
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: interval_duration
                    
                    	Monitored interval duration
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: max_flow
                    
                    	Max simultaneous flows monitored per policy class
                    	**type**\:  int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: timeout
                    
                    	Declare a flow dead if no packets received in so much time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, self).__init__()

                        self.yang_name = "flow-params"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.history = YLeaf(YType.uint32, "history")

                        self.interval_duration = YLeaf(YType.uint32, "interval-duration")

                        self.max_flow = YLeaf(YType.uint16, "max-flow")

                        self.timeout = YLeaf(YType.uint32, "timeout")
                        self._segment_path = lambda: "flow-params"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, ['history', 'interval_duration', 'max_flow', 'timeout'], name, value)


                class MetricsIpcbr(Entity):
                    """
                    Policy IP\-CBR metric action.
                    
                    .. attribute:: media_packet
                    
                    	Media\-packet structure
                    	**type**\:   :py:class:`MediaPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket>`
                    
                    .. attribute:: rate
                    
                    	Nominal per\-flow data rate
                    	**type**\:   :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr, self).__init__()

                        self.yang_name = "metrics-ipcbr"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"media-packet" : ("media_packet", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket), "rate" : ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate)}
                        self._child_list_classes = {}

                        self.media_packet = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket()
                        self.media_packet.parent = self
                        self._children_name_map["media_packet"] = "media-packet"
                        self._children_yang_names.add("media-packet")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")
                        self._segment_path = lambda: "metrics-ipcbr"


                    class MediaPacket(Entity):
                        """
                        Media\-packet structure.
                        
                        .. attribute:: count_in_layer3
                        
                        	Nominal number of media packets in an IP payload
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        	**units**\: packets
                        
                        .. attribute:: size
                        
                        	Nominal size of the media\-packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        	**units**\: bytes
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, self).__init__()

                            self.yang_name = "media-packet"
                            self.yang_parent_name = "metrics-ipcbr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.count_in_layer3 = YLeaf(YType.uint8, "count-in-layer3")

                            self.size = YLeaf(YType.uint16, "size")
                            self._segment_path = lambda: "media-packet"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, ['count_in_layer3', 'size'], name, value)


                    class Rate(Entity):
                        """
                        Nominal per\-flow data rate.
                        
                        .. attribute:: layer3
                        
                        	Nominal rate specified at the L3 (IP)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bps
                        
                        .. attribute:: media
                        
                        	Nominal data rate of the media flow (ip payload)
                        	**type**\:  int
                        
                        	**range:** 1..3000000000
                        
                        	**units**\: bps
                        
                        .. attribute:: packet
                        
                        	Nominal IP layer packet rate (in pps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: pps
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "metrics-ipcbr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.layer3 = YLeaf(YType.uint32, "layer3")

                            self.media = YLeaf(YType.uint32, "media")

                            self.packet = YLeaf(YType.uint32, "packet")
                            self._segment_path = lambda: "rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, ['layer3', 'media', 'packet'], name, value)


                class MinBandwidth(Entity):
                    """
                    Policy action minimum bandwidth queue.
                    
                    .. attribute:: unit
                    
                    	Minimum bandwidth units
                    	**type**\:  str
                    
                    	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(percent)\|(per\-million)\|(per\-thousand)
                    
                    .. attribute:: value
                    
                    	Minimum bandwidth value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, self).__init__()

                        self.yang_name = "min-bandwidth"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.unit = YLeaf(YType.str, "unit")

                        self.value = YLeaf(YType.uint32, "value")
                        self._segment_path = lambda: "min-bandwidth"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, ['unit', 'value'], name, value)


                class PbrForward(Entity):
                    """
                    Policy action PBR forward.
                    
                    .. attribute:: default
                    
                    	Use system default routing table
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: next_hop
                    
                    	Use specific next\-hop. Here we present 5 different combination  for the pbf next\-hop.  1. vrf with v6 address  2. vrf with v4 address  3. vrf   4. v4 address  5. v6 address
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, self).__init__()

                        self.yang_name = "pbr-forward"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"next-hop" : ("next_hop", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop)}
                        self._child_list_classes = {}

                        self.default = YLeaf(YType.empty, "default")

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")
                        self._segment_path = lambda: "pbr-forward"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, ['default'], name, value)


                    class NextHop(Entity):
                        """
                        Use specific next\-hop.
                        Here we present 5 different combination 
                        for the pbf next\-hop.
                         1. vrf with v6 address
                         2. vrf with v4 address
                         3. vrf 
                         4. v4 address
                         5. v6 address
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-forward"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf = YLeaf(YType.str, "vrf")
                            self._segment_path = lambda: "next-hop"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, ['ipv4_address', 'ipv6_address', 'vrf'], name, value)


                class PbrRedirect(Entity):
                    """
                    Policy action redirect
                    
                    .. attribute:: ipv4
                    
                    	Policy action redirect IPv4
                    	**type**\:   :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	Policy action redirect IPv6
                    	**type**\:   :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6>`
                    
                    .. attribute:: next_hop
                    
                    	Next hop address
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect, self).__init__()

                        self.yang_name = "pbr-redirect"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv4" : ("ipv4", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4), "ipv6" : ("ipv6", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6), "next-hop" : ("next_hop", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop)}
                        self._child_list_classes = {}

                        self.ipv4 = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"
                        self._children_yang_names.add("ipv4")

                        self.ipv6 = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"
                        self._children_yang_names.add("ipv6")

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")
                        self._segment_path = lambda: "pbr-redirect"


                    class Ipv4(Entity):
                        """
                        Policy action redirect IPv4
                        
                        .. attribute:: ipv4_next_hop
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf
                        
                        	IPv4 VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv4_next_hop = YLeaf(YType.str, "ipv4-next-hop")

                            self.vrf = YLeaf(YType.str, "vrf")
                            self._segment_path = lambda: "ipv4"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4, ['ipv4_next_hop', 'vrf'], name, value)


                    class Ipv6(Entity):
                        """
                        Policy action redirect IPv6
                        
                        .. attribute:: ipv6_next_hop
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf
                        
                        	IPv6 VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_next_hop = YLeaf(YType.str, "ipv6-next-hop")

                            self.vrf = YLeaf(YType.str, "vrf")
                            self._segment_path = lambda: "ipv6"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6, ['ipv6_next_hop', 'vrf'], name, value)


                    class NextHop(Entity):
                        """
                        Next hop address.
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:   :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"route-target" : ("route_target", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget)}
                            self._child_list_classes = {}

                            self.route_target = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget()
                            self.route_target.parent = self
                            self._children_name_map["route_target"] = "route-target"
                            self._children_yang_names.add("route-target")
                            self._segment_path = lambda: "next-hop"


                        class RouteTarget(Entity):
                            """
                            Route Target
                            
                            .. attribute:: as_number
                            
                            	2\-byte/4\-byte AS number
                            	**type**\:  int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: index
                            
                            	ASN2\:index 2/4 byte (hex or decimal format)
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:   :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address>`
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipv4-address" : ("ipv4_address", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address)}
                                self._child_list_classes = {}

                                self.as_number = YLeaf(YType.uint32, "as-number")

                                self.index = YLeaf(YType.uint32, "index")

                                self.ipv4_address = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address()
                                self.ipv4_address.parent = self
                                self._children_name_map["ipv4_address"] = "ipv4-address"
                                self._children_yang_names.add("ipv4-address")
                                self._segment_path = lambda: "route-target"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, ['as_number', 'index'], name, value)


                            class Ipv4Address(Entity):
                                """
                                IPv4 address.
                                
                                .. attribute:: address
                                
                                	IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: netmask
                                
                                	IPv4 netmask
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'infra-policymgr-cfg'
                                _revision = '2017-08-11'

                                def __init__(self):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, self).__init__()

                                    self.yang_name = "ipv4-address"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.address = YLeaf(YType.str, "address")

                                    self.netmask = YLeaf(YType.str, "netmask")
                                    self._segment_path = lambda: "ipv4-address"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, ['address', 'netmask'], name, value)


                class Pfc(Entity):
                    """
                    Policy action pfc.
                    
                    .. attribute:: pfc_buffer_size
                    
                    	
                    	**type**\:   :py:class:`PfcBufferSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize>`
                    
                    .. attribute:: pfc_pause_set
                    
                    	Pfc Pause set value
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: pfc_pause_threshold
                    
                    	
                    	**type**\:   :py:class:`PfcPauseThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold>`
                    
                    .. attribute:: pfc_resume_threshold
                    
                    	
                    	**type**\:   :py:class:`PfcResumeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, self).__init__()

                        self.yang_name = "pfc"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"pfc-buffer-size" : ("pfc_buffer_size", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize), "pfc-pause-threshold" : ("pfc_pause_threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold), "pfc-resume-threshold" : ("pfc_resume_threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold)}
                        self._child_list_classes = {}

                        self.pfc_pause_set = YLeaf(YType.empty, "pfc-pause-set")

                        self.pfc_buffer_size = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize()
                        self.pfc_buffer_size.parent = self
                        self._children_name_map["pfc_buffer_size"] = "pfc-buffer-size"
                        self._children_yang_names.add("pfc-buffer-size")

                        self.pfc_pause_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold()
                        self.pfc_pause_threshold.parent = self
                        self._children_name_map["pfc_pause_threshold"] = "pfc-pause-threshold"
                        self._children_yang_names.add("pfc-pause-threshold")

                        self.pfc_resume_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold()
                        self.pfc_resume_threshold.parent = self
                        self._children_name_map["pfc_resume_threshold"] = "pfc-resume-threshold"
                        self._children_yang_names.add("pfc-resume-threshold")
                        self._segment_path = lambda: "pfc"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, ['pfc_pause_set'], name, value)


                    class PfcBufferSize(Entity):
                        """
                        
                        
                        .. attribute:: unit
                        
                        	Pfc buffer size units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Pfc buffer size value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, self).__init__()

                            self.yang_name = "pfc-buffer-size"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unit = YLeaf(YType.str, "unit")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "pfc-buffer-size"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, ['unit', 'value'], name, value)


                    class PfcPauseThreshold(Entity):
                        """
                        
                        
                        .. attribute:: unit
                        
                        	Pfc pause threshold units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Pfc pause threshold value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, self).__init__()

                            self.yang_name = "pfc-pause-threshold"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unit = YLeaf(YType.str, "unit")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "pfc-pause-threshold"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, ['unit', 'value'], name, value)


                    class PfcResumeThreshold(Entity):
                        """
                        
                        
                        .. attribute:: unit
                        
                        	Pfc resume threshold units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Pfc resume threshold value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, self).__init__()

                            self.yang_name = "pfc-resume-threshold"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unit = YLeaf(YType.str, "unit")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "pfc-resume-threshold"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, ['unit', 'value'], name, value)


                class Police(Entity):
                    """
                    Configures traffic policing action.
                    
                    .. attribute:: burst
                    
                    	Burst configuration
                    	**type**\:   :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst>`
                    
                    .. attribute:: conform_action
                    
                    	Configures the action to take on packets that conform  to the rate limit
                    	**type**\:   :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction>`
                    
                    .. attribute:: exceed_action
                    
                    	Configures the action to take on packets that exceed  the rate limit
                    	**type**\:   :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction>`
                    
                    .. attribute:: peak_burst
                    
                    	Peak burst configuration
                    	**type**\:   :py:class:`PeakBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst>`
                    
                    .. attribute:: peak_rate
                    
                    	Peak rate configuration
                    	**type**\:   :py:class:`PeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate>`
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:   :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate>`
                    
                    .. attribute:: violate_action
                    
                    	Configures the action to take on packets that violate the rate limit
                    	**type**\:   :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"burst" : ("burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst), "conform-action" : ("conform_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction), "exceed-action" : ("exceed_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction), "peak-burst" : ("peak_burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst), "peak-rate" : ("peak_rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate), "rate" : ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate), "violate-action" : ("violate_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction)}
                        self._child_list_classes = {}

                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst()
                        self.burst.parent = self
                        self._children_name_map["burst"] = "burst"
                        self._children_yang_names.add("burst")

                        self.conform_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction()
                        self.conform_action.parent = self
                        self._children_name_map["conform_action"] = "conform-action"
                        self._children_yang_names.add("conform-action")

                        self.exceed_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction()
                        self.exceed_action.parent = self
                        self._children_name_map["exceed_action"] = "exceed-action"
                        self._children_yang_names.add("exceed-action")

                        self.peak_burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst()
                        self.peak_burst.parent = self
                        self._children_name_map["peak_burst"] = "peak-burst"
                        self._children_yang_names.add("peak-burst")

                        self.peak_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate()
                        self.peak_rate.parent = self
                        self._children_name_map["peak_rate"] = "peak-rate"
                        self._children_yang_names.add("peak-rate")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")

                        self.violate_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction()
                        self.violate_action.parent = self
                        self._children_name_map["violate_action"] = "violate-action"
                        self._children_yang_names.add("violate-action")
                        self._segment_path = lambda: "police"


                    class Burst(Entity):
                        """
                        Burst configuration.
                        
                        .. attribute:: units
                        
                        	Burst units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Burst value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "burst"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, ['units', 'value'], name, value)


                    class ConformAction(Entity):
                        """
                        Configures the action to take on packets that conform 
                        to the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:   :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, self).__init__()

                            self.yang_name = "conform-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"set" : ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set)}
                            self._child_list_classes = {}

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")
                            self._segment_path = lambda: "conform-action"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, ['drop', 'transmit'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..512
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "conform-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.dei = YLeaf(YType.uint8, "dei")

                                self.dei_imposition = YLeaf(YType.uint8, "dei-imposition")

                                self.destination_address = YLeaf(YType.str, "destination-address")

                                self.df = YLeaf(YType.uint8, "df")

                                self.discard_class = YLeaf(YType.uint8, "discard-class")

                                self.dscp = YLeaf(YType.str, "dscp")

                                self.forward_class = YLeaf(YType.uint8, "forward-class")

                                self.fr_de = YLeaf(YType.uint8, "fr-de")

                                self.inner_cos = YLeaf(YType.uint8, "inner-cos")

                                self.mpls_experimental_imposition = YLeaf(YType.uint8, "mpls-experimental-imposition")

                                self.mpls_experimental_top_most = YLeaf(YType.uint8, "mpls-experimental-top-most")

                                self.precedence = YLeaf(YType.str, "precedence")

                                self.precedence_tunnel = YLeaf(YType.str, "precedence-tunnel")

                                self.qos_group = YLeaf(YType.uint16, "qos-group")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.srp_priority = YLeaf(YType.uint8, "srp-priority")

                                self.traffic_class = YLeaf(YType.uint8, "traffic-class")
                                self._segment_path = lambda: "set"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, ['cos', 'dei', 'dei_imposition', 'destination_address', 'df', 'discard_class', 'dscp', 'forward_class', 'fr_de', 'inner_cos', 'mpls_experimental_imposition', 'mpls_experimental_top_most', 'precedence', 'precedence_tunnel', 'qos_group', 'source_address', 'srp_priority', 'traffic_class'], name, value)


                    class ExceedAction(Entity):
                        """
                        Configures the action to take on packets that exceed 
                        the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:   :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, self).__init__()

                            self.yang_name = "exceed-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"set" : ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set)}
                            self._child_list_classes = {}

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")
                            self._segment_path = lambda: "exceed-action"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, ['drop', 'transmit'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..512
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "exceed-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.dei = YLeaf(YType.uint8, "dei")

                                self.dei_imposition = YLeaf(YType.uint8, "dei-imposition")

                                self.destination_address = YLeaf(YType.str, "destination-address")

                                self.df = YLeaf(YType.uint8, "df")

                                self.discard_class = YLeaf(YType.uint8, "discard-class")

                                self.dscp = YLeaf(YType.str, "dscp")

                                self.forward_class = YLeaf(YType.uint8, "forward-class")

                                self.fr_de = YLeaf(YType.uint8, "fr-de")

                                self.inner_cos = YLeaf(YType.uint8, "inner-cos")

                                self.mpls_experimental_imposition = YLeaf(YType.uint8, "mpls-experimental-imposition")

                                self.mpls_experimental_top_most = YLeaf(YType.uint8, "mpls-experimental-top-most")

                                self.precedence = YLeaf(YType.str, "precedence")

                                self.precedence_tunnel = YLeaf(YType.str, "precedence-tunnel")

                                self.qos_group = YLeaf(YType.uint16, "qos-group")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.srp_priority = YLeaf(YType.uint8, "srp-priority")

                                self.traffic_class = YLeaf(YType.uint8, "traffic-class")
                                self._segment_path = lambda: "set"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, ['cos', 'dei', 'dei_imposition', 'destination_address', 'df', 'discard_class', 'dscp', 'forward_class', 'fr_de', 'inner_cos', 'mpls_experimental_imposition', 'mpls_experimental_top_most', 'precedence', 'precedence_tunnel', 'qos_group', 'source_address', 'srp_priority', 'traffic_class'], name, value)


                    class PeakBurst(Entity):
                        """
                        Peak burst configuration.
                        
                        .. attribute:: units
                        
                        	Peak burst units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Peak burst value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, self).__init__()

                            self.yang_name = "peak-burst"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "peak-burst"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, ['units', 'value'], name, value)


                    class PeakRate(Entity):
                        """
                        Peak rate configuration.
                        
                        .. attribute:: units
                        
                        	Peak rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)\|(cellsps)
                        
                        .. attribute:: value
                        
                        	Peak rate value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, self).__init__()

                            self.yang_name = "peak-rate"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "peak-rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, ['units', 'value'], name, value)


                    class Rate(Entity):
                        """
                        Rate configuration.
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)\|(cellsps)
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, ['units', 'value'], name, value)


                    class ViolateAction(Entity):
                        """
                        Configures the action to take on packets that violate
                        the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:   :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, self).__init__()

                            self.yang_name = "violate-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"set" : ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set)}
                            self._child_list_classes = {}

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")
                            self._segment_path = lambda: "violate-action"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, ['drop', 'transmit'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\:  str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\:  int
                            
                            	**range:** 0..1
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: one of the below types:
                            
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            
                            ----
                            	**type**\:  str
                            
                            	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            
                            ----
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\:  int
                            
                            	**range:** 0..512
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\:  int
                            
                            	**range:** 0..63
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "violate-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.cos = YLeaf(YType.uint8, "cos")

                                self.dei = YLeaf(YType.uint8, "dei")

                                self.dei_imposition = YLeaf(YType.uint8, "dei-imposition")

                                self.destination_address = YLeaf(YType.str, "destination-address")

                                self.df = YLeaf(YType.uint8, "df")

                                self.discard_class = YLeaf(YType.uint8, "discard-class")

                                self.dscp = YLeaf(YType.str, "dscp")

                                self.forward_class = YLeaf(YType.uint8, "forward-class")

                                self.fr_de = YLeaf(YType.uint8, "fr-de")

                                self.inner_cos = YLeaf(YType.uint8, "inner-cos")

                                self.mpls_experimental_imposition = YLeaf(YType.uint8, "mpls-experimental-imposition")

                                self.mpls_experimental_top_most = YLeaf(YType.uint8, "mpls-experimental-top-most")

                                self.precedence = YLeaf(YType.str, "precedence")

                                self.precedence_tunnel = YLeaf(YType.str, "precedence-tunnel")

                                self.qos_group = YLeaf(YType.uint16, "qos-group")

                                self.source_address = YLeaf(YType.str, "source-address")

                                self.srp_priority = YLeaf(YType.uint8, "srp-priority")

                                self.traffic_class = YLeaf(YType.uint8, "traffic-class")
                                self._segment_path = lambda: "set"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, ['cos', 'dei', 'dei_imposition', 'destination_address', 'df', 'discard_class', 'dscp', 'forward_class', 'fr_de', 'inner_cos', 'mpls_experimental_imposition', 'mpls_experimental_top_most', 'precedence', 'precedence_tunnel', 'qos_group', 'source_address', 'srp_priority', 'traffic_class'], name, value)


                class QueueLimit(Entity):
                    """
                    Policy action queue limit.
                    
                    .. attribute:: unit
                    
                    	Remaining bandwidth units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)\|(percent)
                    
                    .. attribute:: value
                    
                    	Remaining bandwidth value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, self).__init__()

                        self.yang_name = "queue-limit"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.unit = YLeaf(YType.str, "unit")

                        self.value = YLeaf(YType.uint32, "value")
                        self._segment_path = lambda: "queue-limit"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, ['unit', 'value'], name, value)


                class RandomDetect(Entity):
                    """
                    Random early detection.
                    All RED profiles in a class must be based
                    on the same field.
                    
                    .. attribute:: threshold_min_value  <key>
                    
                    	Minimum RED threshold value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: threshold_min_units  <key>
                    
                    	Minimum RED threshold units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: threshold_max_value  <key>
                    
                    	Maximum RED threshold value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: threshold_max_units  <key>
                    
                    	Maximum RED threshold units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: cos
                    
                    	WRED based on CoS
                    	**type**\:  list of str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: dei
                    
                    	DEI based WRED
                    	**type**\:  int
                    
                    	**range:** 0..1
                    
                    .. attribute:: discard_class
                    
                    	WRED based on discard class
                    	**type**\:  list of int
                    
                    	**range:** 0..7
                    
                    .. attribute:: dscp
                    
                    	WRED based on DSCP
                    	**type**\:  list of str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: ecn
                    
                    	ECN based WRED
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: mpls_exp
                    
                    	MPLS Experimental value based WRED
                    	**type**\:  list of int
                    
                    	**range:** 0..7
                    
                    .. attribute:: precedence
                    
                    	WRED based on precedence
                    	**type**\: one of the below types:
                    
                    	**type**\:  list of int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    	**type**\:  list of str
                    
                    	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    
                    ----
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, self).__init__()

                        self.yang_name = "random-detect"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.threshold_min_value = YLeaf(YType.uint32, "threshold-min-value")

                        self.threshold_min_units = YLeaf(YType.str, "threshold-min-units")

                        self.threshold_max_value = YLeaf(YType.uint32, "threshold-max-value")

                        self.threshold_max_units = YLeaf(YType.str, "threshold-max-units")

                        self.cos = YLeafList(YType.str, "cos")

                        self.dei = YLeaf(YType.uint8, "dei")

                        self.discard_class = YLeafList(YType.uint8, "discard-class")

                        self.dscp = YLeafList(YType.str, "dscp")

                        self.ecn = YLeaf(YType.empty, "ecn")

                        self.mpls_exp = YLeafList(YType.uint8, "mpls-exp")

                        self.precedence = YLeafList(YType.str, "precedence")
                        self._segment_path = lambda: "random-detect" + "[threshold-min-value='" + self.threshold_min_value.get() + "']" + "[threshold-min-units='" + self.threshold_min_units.get() + "']" + "[threshold-max-value='" + self.threshold_max_value.get() + "']" + "[threshold-max-units='" + self.threshold_max_units.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, ['threshold_min_value', 'threshold_min_units', 'threshold_max_value', 'threshold_max_units', 'cos', 'dei', 'discard_class', 'dscp', 'ecn', 'mpls_exp', 'precedence'], name, value)


                class React(Entity):
                    """
                    Policy action react.
                    
                    .. attribute:: action
                    
                    	Action on alert
                    	**type**\:   :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action>`
                    
                    .. attribute:: alarm
                    
                    	Alaram settings
                    	**type**\:   :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm>`
                    
                    .. attribute:: criterion_delay_factor
                    
                    	React criterion delay factor
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_flow_count
                    
                    	React criterion flow count
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_media_stop
                    
                    	React criterion media stop
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_mrv
                    
                    	React criterion mrv
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_packet_rate
                    
                    	React criterion packet rate
                    	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: descrition
                    
                    	String describing the react statement
                    	**type**\:  str
                    
                    .. attribute:: threshold
                    
                    	Alarm threshold settings
                    	**type**\:   :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, self).__init__()

                        self.yang_name = "react"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"action" : ("action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action), "alarm" : ("alarm", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm), "threshold" : ("threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold)}
                        self._child_list_classes = {}

                        self.criterion_delay_factor = YLeaf(YType.empty, "criterion-delay-factor")

                        self.criterion_flow_count = YLeaf(YType.empty, "criterion-flow-count")

                        self.criterion_media_stop = YLeaf(YType.empty, "criterion-media-stop")

                        self.criterion_mrv = YLeaf(YType.empty, "criterion-mrv")

                        self.criterion_packet_rate = YLeaf(YType.empty, "criterion-packet-rate")

                        self.descrition = YLeaf(YType.str, "descrition")

                        self.action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action()
                        self.action.parent = self
                        self._children_name_map["action"] = "action"
                        self._children_yang_names.add("action")

                        self.alarm = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm()
                        self.alarm.parent = self
                        self._children_name_map["alarm"] = "alarm"
                        self._children_yang_names.add("alarm")

                        self.threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold()
                        self.threshold.parent = self
                        self._children_name_map["threshold"] = "threshold"
                        self._children_yang_names.add("threshold")
                        self._segment_path = lambda: "react"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, ['criterion_delay_factor', 'criterion_flow_count', 'criterion_media_stop', 'criterion_mrv', 'criterion_packet_rate', 'descrition'], name, value)


                    class Action(Entity):
                        """
                        Action on alert.
                        
                        .. attribute:: snmp
                        
                        	SNMP
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: syslog
                        
                        	Syslog
                        	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, self).__init__()

                            self.yang_name = "action"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.snmp = YLeaf(YType.empty, "snmp")

                            self.syslog = YLeaf(YType.empty, "syslog")
                            self._segment_path = lambda: "action"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, ['snmp', 'syslog'], name, value)


                    class Alarm(Entity):
                        """
                        Alaram settings.
                        
                        .. attribute:: severity
                        
                        	Severity of the alarm
                        	**type**\:  str
                        
                        	**pattern:** (informational)\|(notification)\|(warning)\|(error)\|(critical)\|(alert)\|(emergency)
                        
                        .. attribute:: type
                        
                        	Alarm type
                        	**type**\:   :py:class:`Type <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, self).__init__()

                            self.yang_name = "alarm"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"type" : ("type", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type)}
                            self._child_list_classes = {}

                            self.severity = YLeaf(YType.str, "severity")

                            self.type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type()
                            self.type.parent = self
                            self._children_name_map["type"] = "type"
                            self._children_yang_names.add("type")
                            self._segment_path = lambda: "alarm"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, ['severity'], name, value)


                        class Type(Entity):
                            """
                            Alarm type.
                            
                            .. attribute:: discrete
                            
                            	Discrete alarm type
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: group_count
                            
                            	Number of flows to reach before  triggering alarm
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**units**\: number of flows
                            
                            .. attribute:: group_percent
                            
                            	Percent to reach before triggering alarm
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, self).__init__()

                                self.yang_name = "type"
                                self.yang_parent_name = "alarm"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.discrete = YLeaf(YType.empty, "discrete")

                                self.group_count = YLeaf(YType.uint16, "group-count")

                                self.group_percent = YLeaf(YType.uint16, "group-percent")
                                self._segment_path = lambda: "type"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, ['discrete', 'group_count', 'group_percent'], name, value)


                    class Threshold(Entity):
                        """
                        Alarm threshold settings.
                        
                        .. attribute:: trigger_type
                        
                        	Alarm trigger type settings
                        	**type**\:   :py:class:`TriggerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType>`
                        
                        .. attribute:: trigger_value
                        
                        	Alarm trigger value settings
                        	**type**\:   :py:class:`TriggerValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold, self).__init__()

                            self.yang_name = "threshold"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"trigger-type" : ("trigger_type", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType), "trigger-value" : ("trigger_value", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue)}
                            self._child_list_classes = {}

                            self.trigger_type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType()
                            self.trigger_type.parent = self
                            self._children_name_map["trigger_type"] = "trigger-type"
                            self._children_yang_names.add("trigger-type")

                            self.trigger_value = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue()
                            self.trigger_value.parent = self
                            self._children_name_map["trigger_value"] = "trigger-value"
                            self._children_yang_names.add("trigger-value")
                            self._segment_path = lambda: "threshold"


                        class TriggerType(Entity):
                            """
                            Alarm trigger type settings.
                            
                            .. attribute:: average
                            
                            	Trigger averaged over N intervals
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: immediate
                            
                            	Immediate trigger
                            	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, self).__init__()

                                self.yang_name = "trigger-type"
                                self.yang_parent_name = "threshold"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.average = YLeaf(YType.uint32, "average")

                                self.immediate = YLeaf(YType.empty, "immediate")
                                self._segment_path = lambda: "trigger-type"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, ['average', 'immediate'], name, value)


                        class TriggerValue(Entity):
                            """
                            Alarm trigger value settings.
                            
                            .. attribute:: greater_than
                            
                            	Greater than
                            	**type**\:  str
                            
                            .. attribute:: greater_than_equal
                            
                            	Greater than equal
                            	**type**\:  str
                            
                            .. attribute:: less_than
                            
                            	Less than
                            	**type**\:  str
                            
                            .. attribute:: less_than_equal
                            
                            	Less than equal
                            	**type**\:  str
                            
                            .. attribute:: range
                            
                            	Range
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-08-11'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, self).__init__()

                                self.yang_name = "trigger-value"
                                self.yang_parent_name = "threshold"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.greater_than = YLeaf(YType.str, "greater-than")

                                self.greater_than_equal = YLeaf(YType.str, "greater-than-equal")

                                self.less_than = YLeaf(YType.str, "less-than")

                                self.less_than_equal = YLeaf(YType.str, "less-than-equal")

                                self.range = YLeaf(YType.str, "range")
                                self._segment_path = lambda: "trigger-value"

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, ['greater_than', 'greater_than_equal', 'less_than', 'less_than_equal', 'range'], name, value)


                class ServiceFunctionPath(Entity):
                    """
                    Policy action service function path.
                    
                    .. attribute:: index
                    
                    	Service function path index
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    .. attribute:: metadata
                    
                    	Service function path metadata name
                    	**type**\:  str
                    
                    .. attribute:: path_id
                    
                    	Service function path id
                    	**type**\:  int
                    
                    	**range:** 1..16777215
                    
                    	**mandatory**\: True
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, self).__init__()

                        self.yang_name = "service-function-path"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}
                        self.is_presence_container = True

                        self.index = YLeaf(YType.uint8, "index")

                        self.metadata = YLeaf(YType.str, "metadata")

                        self.path_id = YLeaf(YType.uint32, "path-id")
                        self._segment_path = lambda: "service-function-path"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, ['index', 'metadata', 'path_id'], name, value)


                class ServicePolicy(Entity):
                    """
                    Configure a child service policy.
                    
                    .. attribute:: policy_name
                    
                    	Name of service\-policy
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: type
                    
                    	Type of service\-policy
                    	**type**\:  str
                    
                    	**pattern:** (PBR)\|(QOS)\|(REDIRECT)\|(TRAFFIC)\|(pbr)\|(qos)\|(redirect)\|(traffic)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.policy_name = YLeaf(YType.str, "policy-name")

                        self.type = YLeaf(YType.str, "type")
                        self._segment_path = lambda: "service-policy"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, ['policy_name', 'type'], name, value)


                class Set(Entity):
                    """
                    Policy action packet marking.
                    
                    .. attribute:: cos
                    
                    	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: dei
                    
                    	Set DEI bit
                    	**type**\:  int
                    
                    	**range:** 0..1
                    
                    .. attribute:: dei_imposition
                    
                    	Set DEI imposition bit
                    	**type**\:  int
                    
                    	**range:** 0..1
                    
                    .. attribute:: destination_address
                    
                    	Destination IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: df
                    
                    	Set DF bit
                    	**type**\:  int
                    
                    	**range:** 0..1
                    
                    .. attribute:: discard_class
                    
                    	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: dscp
                    
                    	Marks a packet by setting the DSCP in the ToS byte
                    	**type**\:  str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: forward_class
                    
                    	Sets the forward class
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: fr_de
                    
                    	Set FrameRelay DE bit
                    	**type**\:  int
                    
                    	**range:** 0..1
                    
                    .. attribute:: inner_cos
                    
                    	Set inner cos
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mpls_experimental_imposition
                    
                    	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mpls_experimental_top_most
                    
                    	Sets the experimental value of the MPLS packet top\-most labels
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: precedence
                    
                    	Sets the precedence value in the IP header
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    
                    ----
                    .. attribute:: precedence_tunnel
                    
                    	Sets the precedence tunnel value for ipsec
                    	**type**\: one of the below types:
                    
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    
                    ----
                    	**type**\:  str
                    
                    	**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    
                    ----
                    .. attribute:: qos_group
                    
                    	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                    	**type**\:  int
                    
                    	**range:** 0..512
                    
                    .. attribute:: source_address
                    
                    	Source IPv4 address
                    	**type**\:  str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: srp_priority
                    
                    	Sets the spatial reuse protocol priority value of an  outgoing packet
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    .. attribute:: traffic_class
                    
                    	Sets the Traffic class identifiers on IPv4 or MPLS packets
                    	**type**\:  int
                    
                    	**range:** 0..63
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.cos = YLeaf(YType.uint8, "cos")

                        self.dei = YLeaf(YType.uint8, "dei")

                        self.dei_imposition = YLeaf(YType.uint8, "dei-imposition")

                        self.destination_address = YLeaf(YType.str, "destination-address")

                        self.df = YLeaf(YType.uint8, "df")

                        self.discard_class = YLeaf(YType.uint8, "discard-class")

                        self.dscp = YLeaf(YType.str, "dscp")

                        self.forward_class = YLeaf(YType.uint8, "forward-class")

                        self.fr_de = YLeaf(YType.uint8, "fr-de")

                        self.inner_cos = YLeaf(YType.uint8, "inner-cos")

                        self.mpls_experimental_imposition = YLeaf(YType.uint8, "mpls-experimental-imposition")

                        self.mpls_experimental_top_most = YLeaf(YType.uint8, "mpls-experimental-top-most")

                        self.precedence = YLeaf(YType.str, "precedence")

                        self.precedence_tunnel = YLeaf(YType.str, "precedence-tunnel")

                        self.qos_group = YLeaf(YType.uint16, "qos-group")

                        self.source_address = YLeaf(YType.str, "source-address")

                        self.srp_priority = YLeaf(YType.uint8, "srp-priority")

                        self.traffic_class = YLeaf(YType.uint8, "traffic-class")
                        self._segment_path = lambda: "set"

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, ['cos', 'dei', 'dei_imposition', 'destination_address', 'df', 'discard_class', 'dscp', 'forward_class', 'fr_de', 'inner_cos', 'mpls_experimental_imposition', 'mpls_experimental_top_most', 'precedence', 'precedence_tunnel', 'qos_group', 'source_address', 'srp_priority', 'traffic_class'], name, value)


                class Shape(Entity):
                    """
                    Policy action shape.
                    
                    .. attribute:: burst
                    
                    	Burst size configuration
                    	**type**\:   :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst>`
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:   :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-08-11'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape, self).__init__()

                        self.yang_name = "shape"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"burst" : ("burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst), "rate" : ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate)}
                        self._child_list_classes = {}

                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst()
                        self.burst.parent = self
                        self._children_name_map["burst"] = "burst"
                        self._children_yang_names.add("burst")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")
                        self._segment_path = lambda: "shape"


                    class Burst(Entity):
                        """
                        Burst size configuration.
                        
                        .. attribute:: units
                        
                        	Burst size units
                        	**type**\:  str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        .. attribute:: value
                        
                        	Burst size value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "shape"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.units = YLeaf(YType.str, "units")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "burst"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, ['units', 'value'], name, value)


                    class Rate(Entity):
                        """
                        Rate configuration.
                        
                        .. attribute:: unit
                        
                        	Shape bandwidth units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(percent)\|(per\-million)\|(per\-thousand)
                        
                        .. attribute:: value
                        
                        	Shape bandwidth value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-08-11'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "shape"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.unit = YLeaf(YType.str, "unit")

                            self.value = YLeaf(YType.uint32, "value")
                            self._segment_path = lambda: "rate"

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, ['unit', 'value'], name, value)

    def clone_ptr(self):
        self._top_entity = PolicyManager()
        return self._top_entity

