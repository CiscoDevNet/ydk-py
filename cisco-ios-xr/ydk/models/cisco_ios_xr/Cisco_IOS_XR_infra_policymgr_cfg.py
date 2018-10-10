""" Cisco_IOS_XR_infra_policymgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ASR9k policy manager configuration.
 
Copyright (c) 2013, 2015\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class AuthorizeIdentifier(Enum):
    """
    AuthorizeIdentifier (Enum Class)

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
    ClassMapType (Enum Class)

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
    EventType (Enum Class)

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
    ExecutionStrategy (Enum Class)

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
    PmapClassMapType (Enum Class)

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
    PolicyMapType (Enum Class)

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
    	**type**\:  :py:class:`ClassMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps>`
    
    .. attribute:: policy_maps
    
    	Policy\-maps configuration
    	**type**\:  :py:class:`PolicyMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps>`
    
    

    """

    _prefix = 'infra-policymgr-cfg'
    _revision = '2018-03-02'

    def __init__(self):
        super(PolicyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "policy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-policymgr-cfg"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("class-maps", ("class_maps", PolicyManager.ClassMaps)), ("policy-maps", ("policy_maps", PolicyManager.PolicyMaps))])
        self._leafs = OrderedDict()

        self.class_maps = PolicyManager.ClassMaps()
        self.class_maps.parent = self
        self._children_name_map["class_maps"] = "class-maps"

        self.policy_maps = PolicyManager.PolicyMaps()
        self.policy_maps.parent = self
        self._children_name_map["policy_maps"] = "policy-maps"
        self._segment_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PolicyManager, [], name, value)


    class ClassMaps(Entity):
        """
        Class\-maps configuration.
        
        .. attribute:: class_map
        
        	Class\-map configuration
        	**type**\: list of  		 :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2018-03-02'

        def __init__(self):
            super(PolicyManager.ClassMaps, self).__init__()

            self.yang_name = "class-maps"
            self.yang_parent_name = "policy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("class-map", ("class_map", PolicyManager.ClassMaps.ClassMap))])
            self._leafs = OrderedDict()

            self.class_map = YList(self)
            self._segment_path = lambda: "class-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PolicyManager.ClassMaps, [], name, value)


        class ClassMap(Entity):
            """
            Class\-map configuration.
            
            .. attribute:: type  (key)
            
            	Type of class\-map
            	**type**\:  :py:class:`ClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.ClassMapType>`
            
            .. attribute:: name  (key)
            
            	Name of class\-map
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: class_map_mode_match_any
            
            	Match all match criteria
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: class_map_mode_match_all
            
            	Match any match criteria
            	**type**\: :py:class:`Empty<ydk.types.Empty>`
            
            .. attribute:: match
            
            	Match rules
            	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match>`
            
            .. attribute:: match_not
            
            	Match not rules
            	**type**\:  :py:class:`MatchNot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot>`
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\: str
            
            

            """

            _prefix = 'infra-policymgr-cfg'
            _revision = '2018-03-02'

            def __init__(self):
                super(PolicyManager.ClassMaps.ClassMap, self).__init__()

                self.yang_name = "class-map"
                self.yang_parent_name = "class-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type','name']
                self._child_classes = OrderedDict([("match", ("match", PolicyManager.ClassMaps.ClassMap.Match)), ("match-not", ("match_not", PolicyManager.ClassMaps.ClassMap.MatchNot))])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'ClassMapType', '')])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('class_map_mode_match_any', (YLeaf(YType.empty, 'class-map-mode-match-any'), ['Empty'])),
                    ('class_map_mode_match_all', (YLeaf(YType.empty, 'class-map-mode-match-all'), ['Empty'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.type = None
                self.name = None
                self.class_map_mode_match_any = None
                self.class_map_mode_match_all = None
                self.description = None

                self.match = PolicyManager.ClassMaps.ClassMap.Match()
                self.match.parent = self
                self._children_name_map["match"] = "match"

                self.match_not = PolicyManager.ClassMaps.ClassMap.MatchNot()
                self.match_not.parent = self
                self._children_name_map["match_not"] = "match-not"
                self._segment_path = lambda: "class-map" + "[type='" + str(self.type) + "']" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/class-maps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PolicyManager.ClassMaps.ClassMap, ['type', 'name', 'class_map_mode_match_any', 'class_map_mode_match_all', 'description'], name, value)


            class Match(Entity):
                """
                Match rules.
                
                .. attribute:: ipv4_dscp
                
                	Match IPv4 DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv6_dscp
                
                	Match IPv6 DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv4_precedence
                
                	Match IPv4 precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: ipv6_precedence
                
                	Match IPv6 precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: precedence
                
                	Match precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: qos_group
                
                	Match QoS group. Should be value 0..512 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: traffic_class
                
                	Match Traffic Class. Should be value 0..63 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: inner_cos
                
                	Match inner CoS
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: dei
                
                	Match DEI bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: dei_inner
                
                	Match DEI INNER  bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: protocol
                
                	Match protocol
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\|(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\\-([1\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5]))\|((ahp)\|(dhcpv4)\|(dhcpv6)\|(eigrp)\|(esp)\|(gre)\|(icmp)\|(igmp)\|(igrp)\|(ipinip)\|(ipv4)\|(ipv6)\|(ipv6icmp)\|(mpls)\|(nos)\|(ospf)\|(pcp)\|(pim)\|(ppp)\|(sctp)\|(tcp)\|(udp))
                
                .. attribute:: ipv4_acl
                
                	Match IPv4 ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: ipv6_acl
                
                	Match IPv6 ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: ethernet_services_acl
                
                	Match Ethernet Services
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: mpls_experimental_topmost
                
                	Match MPLS experimental topmost label
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: mpls_experimental_imposition
                
                	Match MPLS experimental imposition label
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: ipv4_packet_length
                
                	Match IPv4 packet length. Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv6_packet_length
                
                	Match IPv6 packet length.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: packet_length
                
                	Match packet length.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: mpls_disposition_ipv4_access_list
                
                	Match MPLS Label Disposition IPv4 access list
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: inner_vlan
                
                	Match inner VLAN ID
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: flow_tag
                
                	Match flow\-tag. Should be value 1..63 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\: list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of  		 :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of  		 :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6>`
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fragment_type
                
                	Match fragment type for a packet
                	**type**\: list of str
                
                	**pattern:** (first\-fragment)\|(is\-fragment)\|(last\-fragment)
                
                .. attribute:: frame_relay_dlci
                
                	Match frame\-relay DLCI value.  Should be value 16..1007 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fr_de
                
                	Set FrameRelay DE bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: icmpv4_code
                
                	Match IPv4 ICMP code.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_type
                
                	Match IPv4 ICMP type.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_code
                
                	Match IPv6 ICMP code.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_type
                
                	Match IPv6 ICMP type.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of  		 :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of  		 :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6>`
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flags
                	**type**\: int
                
                	**range:** 0..4095
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\: str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: circuit_id
                
                	Match Circuit ID
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: circuit_id_regex
                
                	Match Circuit id regex
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: dhcp_client_id
                
                	Match dhcp client ID
                	**type**\: list of  		 :py:class:`DhcpClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId>`
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\: list of  		 :py:class:`DhcpClientIdRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex>`
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of  		 :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DomainName>`
                
                .. attribute:: domain_name_regex
                
                	Match domain name
                	**type**\: list of  		 :py:class:`DomainNameRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex>`
                
                .. attribute:: remote_id
                
                	Match remote ID
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: remote_id_regex
                
                	Match remote id regex
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: timer
                
                	Match timer
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: source_mac
                
                	Match source MAC address
                	**type**\: list of str
                
                .. attribute:: destination_mac
                
                	Match destination MAC address
                	**type**\: list of str
                
                .. attribute:: vpls_control
                
                	Match VPLS control
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_broadcast
                
                	Match VPLS Broadcast
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_multicast
                
                	Match VPLS Multicast
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_known
                
                	Match VPLS Known
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_unknown
                
                	Match VPLS Unknown
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: atm_clp
                
                	Match ATM CLP bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: atm_oam
                
                	Match ATM OAM
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cac_admit
                
                	Match CAC admitted
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: cac_unadmit
                
                	Match CAC unadmitted
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: flow
                
                	Match flow
                	**type**\:  :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2018-03-02'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.Match, self).__init__()

                    self.yang_name = "match"
                    self.yang_parent_name = "class-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("destination-address-ipv4", ("destination_address_ipv4", PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4)), ("destination-address-ipv6", ("destination_address_ipv6", PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6)), ("source-address-ipv4", ("source_address_ipv4", PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4)), ("source-address-ipv6", ("source_address_ipv6", PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6)), ("dhcp-client-id", ("dhcp_client_id", PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId)), ("dhcp-client-id-regex", ("dhcp_client_id_regex", PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex)), ("domain-name", ("domain_name", PolicyManager.ClassMaps.ClassMap.Match.DomainName)), ("domain-name-regex", ("domain_name_regex", PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex)), ("flow", ("flow", PolicyManager.ClassMaps.ClassMap.Match.Flow))])
                    self._leafs = OrderedDict([
                        ('ipv4_dscp', (YLeafList(YType.str, 'ipv4-dscp'), ['str'])),
                        ('ipv6_dscp', (YLeafList(YType.str, 'ipv6-dscp'), ['str'])),
                        ('dscp', (YLeafList(YType.str, 'dscp'), ['str'])),
                        ('ipv4_precedence', (YLeafList(YType.str, 'ipv4-precedence'), ['int','str'])),
                        ('ipv6_precedence', (YLeafList(YType.str, 'ipv6-precedence'), ['int','str'])),
                        ('precedence', (YLeafList(YType.str, 'precedence'), ['int','str'])),
                        ('qos_group', (YLeafList(YType.str, 'qos-group'), ['str'])),
                        ('traffic_class', (YLeafList(YType.str, 'traffic-class'), ['str'])),
                        ('cos', (YLeafList(YType.uint8, 'cos'), ['int'])),
                        ('inner_cos', (YLeafList(YType.uint8, 'inner-cos'), ['int'])),
                        ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                        ('dei_inner', (YLeaf(YType.uint8, 'dei-inner'), ['int'])),
                        ('protocol', (YLeafList(YType.str, 'protocol'), ['str'])),
                        ('ipv4_acl', (YLeaf(YType.str, 'ipv4-acl'), ['str'])),
                        ('ipv6_acl', (YLeaf(YType.str, 'ipv6-acl'), ['str'])),
                        ('ethernet_services_acl', (YLeaf(YType.str, 'ethernet-services-acl'), ['str'])),
                        ('mpls_experimental_topmost', (YLeafList(YType.uint8, 'mpls-experimental-topmost'), ['int'])),
                        ('mpls_experimental_imposition', (YLeafList(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                        ('discard_class', (YLeafList(YType.uint8, 'discard-class'), ['int'])),
                        ('ipv4_packet_length', (YLeafList(YType.str, 'ipv4-packet-length'), ['str'])),
                        ('ipv6_packet_length', (YLeafList(YType.str, 'ipv6-packet-length'), ['str'])),
                        ('packet_length', (YLeafList(YType.str, 'packet-length'), ['str'])),
                        ('mpls_disposition_ipv4_access_list', (YLeaf(YType.str, 'mpls-disposition-ipv4-access-list'), ['str'])),
                        ('mpls_disposition_ipv6_access_list', (YLeaf(YType.str, 'mpls-disposition-ipv6-access-list'), ['str'])),
                        ('vlan', (YLeafList(YType.str, 'vlan'), ['str'])),
                        ('inner_vlan', (YLeafList(YType.str, 'inner-vlan'), ['str'])),
                        ('flow_tag', (YLeafList(YType.str, 'flow-tag'), ['str'])),
                        ('ethertype', (YLeafList(YType.str, 'ethertype'), ['str'])),
                        ('destination_port', (YLeafList(YType.str, 'destination-port'), ['str'])),
                        ('fragment_type', (YLeafList(YType.str, 'fragment-type'), ['str'])),
                        ('frame_relay_dlci', (YLeafList(YType.str, 'frame-relay-dlci'), ['str'])),
                        ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                        ('icmpv4_code', (YLeafList(YType.str, 'icmpv4-code'), ['str'])),
                        ('icmpv4_type', (YLeafList(YType.str, 'icmpv4-type'), ['str'])),
                        ('icmpv6_code', (YLeafList(YType.str, 'icmpv6-code'), ['str'])),
                        ('icmpv6_type', (YLeafList(YType.str, 'icmpv6-type'), ['str'])),
                        ('source_port', (YLeafList(YType.str, 'source-port'), ['str'])),
                        ('tcp_flag', (YLeaf(YType.uint16, 'tcp-flag'), ['int'])),
                        ('authen_status', (YLeaf(YType.str, 'authen-status'), ['str'])),
                        ('circuit_id', (YLeafList(YType.str, 'circuit-id'), ['str'])),
                        ('circuit_id_regex', (YLeafList(YType.str, 'circuit-id-regex'), ['str'])),
                        ('remote_id', (YLeafList(YType.str, 'remote-id'), ['str'])),
                        ('remote_id_regex', (YLeafList(YType.str, 'remote-id-regex'), ['str'])),
                        ('service_name', (YLeafList(YType.str, 'service-name'), ['str'])),
                        ('service_name_regex', (YLeafList(YType.str, 'service-name-regex'), ['str'])),
                        ('timer', (YLeafList(YType.str, 'timer'), ['str'])),
                        ('timer_regex', (YLeafList(YType.str, 'timer-regex'), ['str'])),
                        ('user_name', (YLeafList(YType.str, 'user-name'), ['str'])),
                        ('user_name_regex', (YLeafList(YType.str, 'user-name-regex'), ['str'])),
                        ('source_mac', (YLeafList(YType.str, 'source-mac'), ['str'])),
                        ('destination_mac', (YLeafList(YType.str, 'destination-mac'), ['str'])),
                        ('vpls_control', (YLeaf(YType.empty, 'vpls-control'), ['Empty'])),
                        ('vpls_broadcast', (YLeaf(YType.empty, 'vpls-broadcast'), ['Empty'])),
                        ('vpls_multicast', (YLeaf(YType.empty, 'vpls-multicast'), ['Empty'])),
                        ('vpls_known', (YLeaf(YType.empty, 'vpls-known'), ['Empty'])),
                        ('vpls_unknown', (YLeaf(YType.empty, 'vpls-unknown'), ['Empty'])),
                        ('atm_clp', (YLeaf(YType.uint8, 'atm-clp'), ['int'])),
                        ('atm_oam', (YLeaf(YType.empty, 'atm-oam'), ['Empty'])),
                        ('cac_admit', (YLeaf(YType.empty, 'cac-admit'), ['Empty'])),
                        ('cac_unadmit', (YLeaf(YType.empty, 'cac-unadmit'), ['Empty'])),
                    ])
                    self.ipv4_dscp = []
                    self.ipv6_dscp = []
                    self.dscp = []
                    self.ipv4_precedence = []
                    self.ipv6_precedence = []
                    self.precedence = []
                    self.qos_group = []
                    self.traffic_class = []
                    self.cos = []
                    self.inner_cos = []
                    self.dei = None
                    self.dei_inner = None
                    self.protocol = []
                    self.ipv4_acl = None
                    self.ipv6_acl = None
                    self.ethernet_services_acl = None
                    self.mpls_experimental_topmost = []
                    self.mpls_experimental_imposition = []
                    self.discard_class = []
                    self.ipv4_packet_length = []
                    self.ipv6_packet_length = []
                    self.packet_length = []
                    self.mpls_disposition_ipv4_access_list = None
                    self.mpls_disposition_ipv6_access_list = None
                    self.vlan = []
                    self.inner_vlan = []
                    self.flow_tag = []
                    self.ethertype = []
                    self.destination_port = []
                    self.fragment_type = []
                    self.frame_relay_dlci = []
                    self.fr_de = None
                    self.icmpv4_code = []
                    self.icmpv4_type = []
                    self.icmpv6_code = []
                    self.icmpv6_type = []
                    self.source_port = []
                    self.tcp_flag = None
                    self.authen_status = None
                    self.circuit_id = []
                    self.circuit_id_regex = []
                    self.remote_id = []
                    self.remote_id_regex = []
                    self.service_name = []
                    self.service_name_regex = []
                    self.timer = []
                    self.timer_regex = []
                    self.user_name = []
                    self.user_name_regex = []
                    self.source_mac = []
                    self.destination_mac = []
                    self.vpls_control = None
                    self.vpls_broadcast = None
                    self.vpls_multicast = None
                    self.vpls_known = None
                    self.vpls_unknown = None
                    self.atm_clp = None
                    self.atm_oam = None
                    self.cac_admit = None
                    self.cac_unadmit = None

                    self.flow = PolicyManager.ClassMaps.ClassMap.Match.Flow()
                    self.flow.parent = self
                    self._children_name_map["flow"] = "flow"

                    self.destination_address_ipv4 = YList(self)
                    self.destination_address_ipv6 = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)
                    self.dhcp_client_id = YList(self)
                    self.dhcp_client_id_regex = YList(self)
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self._segment_path = lambda: "match"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match, ['ipv4_dscp', 'ipv6_dscp', 'dscp', 'ipv4_precedence', 'ipv6_precedence', 'precedence', 'qos_group', 'traffic_class', 'cos', 'inner_cos', 'dei', 'dei_inner', 'protocol', 'ipv4_acl', 'ipv6_acl', 'ethernet_services_acl', 'mpls_experimental_topmost', 'mpls_experimental_imposition', 'discard_class', 'ipv4_packet_length', 'ipv6_packet_length', 'packet_length', 'mpls_disposition_ipv4_access_list', 'mpls_disposition_ipv6_access_list', 'vlan', 'inner_vlan', 'flow_tag', 'ethertype', 'destination_port', 'fragment_type', 'frame_relay_dlci', 'fr_de', 'icmpv4_code', 'icmpv4_type', 'icmpv6_code', 'icmpv6_type', 'source_port', 'tcp_flag', 'authen_status', 'circuit_id', 'circuit_id_regex', 'remote_id', 'remote_id_regex', 'service_name', 'service_name_regex', 'timer', 'timer_regex', 'user_name', 'user_name_regex', 'source_mac', 'destination_mac', 'vpls_control', 'vpls_broadcast', 'vpls_multicast', 'vpls_known', 'vpls_unknown', 'atm_clp', 'atm_oam', 'cac_admit', 'cac_unadmit'], name, value)


                class DestinationAddressIpv4(Entity):
                    """
                    Match destination IPv4 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  (key)
                    
                    	IPv4 netmask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','netmask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                        ])
                        self.address = None
                        self.netmask = None
                        self._segment_path = lambda: "destination-address-ipv4" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, ['address', 'netmask'], name, value)


                class DestinationAddressIpv6(Entity):
                    """
                    Match destination IPv6 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	IPv6 prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self._segment_path = lambda: "destination-address-ipv6" + "[address='" + str(self.address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, ['address', 'prefix_length'], name, value)


                class SourceAddressIpv4(Entity):
                    """
                    Match source IPv4 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  (key)
                    
                    	IPv4 netmask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','netmask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                        ])
                        self.address = None
                        self.netmask = None
                        self._segment_path = lambda: "source-address-ipv4" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, ['address', 'netmask'], name, value)


                class SourceAddressIpv6(Entity):
                    """
                    Match source IPv6 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	IPv6 prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self._segment_path = lambda: "source-address-ipv6" + "[address='" + str(self.address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, ['address', 'prefix_length'], name, value)


                class DhcpClientId(Entity):
                    """
                    Match dhcp client ID.
                    
                    .. attribute:: value  (key)
                    
                    	Dhcp client Id
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  (key)
                    
                    	Dhcp client id Ascii/Hex
                    	**type**\: str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId, self).__init__()

                        self.yang_name = "dhcp-client-id"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['value','flag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('flag', (YLeaf(YType.str, 'flag'), ['str'])),
                        ])
                        self.value = None
                        self.flag = None
                        self._segment_path = lambda: "dhcp-client-id" + "[value='" + str(self.value) + "']" + "[flag='" + str(self.flag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientId, ['value', 'flag'], name, value)


                class DhcpClientIdRegex(Entity):
                    """
                    Match dhcp client id regex.
                    
                    .. attribute:: value  (key)
                    
                    	Dhcp client id regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  (key)
                    
                    	Dhcp client Id regex Ascii/Hex
                    	**type**\: str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex, self).__init__()

                        self.yang_name = "dhcp-client-id-regex"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['value','flag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('flag', (YLeaf(YType.str, 'flag'), ['str'])),
                        ])
                        self.value = None
                        self.flag = None
                        self._segment_path = lambda: "dhcp-client-id-regex" + "[value='" + str(self.value) + "']" + "[flag='" + str(self.flag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DhcpClientIdRegex, ['value', 'flag'], name, value)


                class DomainName(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: name  (key)
                    
                    	Domain name or regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  (key)
                    
                    	Domain\-format name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name','format']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('format', (YLeaf(YType.str, 'format'), ['str'])),
                        ])
                        self.name = None
                        self.format = None
                        self._segment_path = lambda: "domain-name" + "[name='" + str(self.name) + "']" + "[format='" + str(self.format) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DomainName, ['name', 'format'], name, value)


                class DomainNameRegex(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: regex  (key)
                    
                    	Domain name or regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  (key)
                    
                    	Domain\-format name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['regex','format']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('regex', (YLeaf(YType.str, 'regex'), ['str'])),
                            ('format', (YLeaf(YType.str, 'format'), ['str'])),
                        ])
                        self.regex = None
                        self.format = None
                        self._segment_path = lambda: "domain-name-regex" + "[regex='" + str(self.regex) + "']" + "[format='" + str(self.format) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, ['regex', 'format'], name, value)


                class Flow(Entity):
                    """
                    Match flow.
                    
                    .. attribute:: flow_key
                    
                    	Configure the flow\-key parameters
                    	**type**\: list of str
                    
                    	**pattern:** (SourceIP)\|(DestinationIP)\|(5Tuple)
                    
                    .. attribute:: flow_cache
                    
                    	Configure the flow\-cache parameters
                    	**type**\:  :py:class:`FlowCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("flow-cache", ("flow_cache", PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache))])
                        self._leafs = OrderedDict([
                            ('flow_key', (YLeafList(YType.str, 'flow-key'), ['str'])),
                        ])
                        self.flow_key = []

                        self.flow_cache = PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache()
                        self.flow_cache.parent = self
                        self._children_name_map["flow_cache"] = "flow-cache"
                        self._segment_path = lambda: "flow"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.Flow, ['flow_key'], name, value)


                    class FlowCache(Entity):
                        """
                        Configure the flow\-cache parameters
                        
                        .. attribute:: idle_timeout
                        
                        	Maximum time of inactivity for a flow
                        	**type**\: union of the below types:
                        
                        		**type**\: int
                        
                        			**range:** 10..2550
                        
                        		**type**\: str
                        
                        			**pattern:** (None)\|(none)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, self).__init__()

                            self.yang_name = "flow-cache"
                            self.yang_parent_name = "flow"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('idle_timeout', (YLeaf(YType.str, 'idle-timeout'), ['int','str'])),
                            ])
                            self.idle_timeout = None
                            self._segment_path = lambda: "flow-cache"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, ['idle_timeout'], name, value)


            class MatchNot(Entity):
                """
                Match not rules.
                
                .. attribute:: ipv4_dscp
                
                	Match IPv4 DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv6_dscp
                
                	Match IPv6 DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ipv4_precedence
                
                	Match IPv4 precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: ipv6_precedence
                
                	Match IPv6 precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: precedence
                
                	Match precedence
                	**type**\: union of the below types:
                
                		**type**\: list of int
                
                			**range:** 0..7
                
                		**type**\: list of str
                
                			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                
                .. attribute:: qos_group
                
                	Match QoS group. Should be value 0..512 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: traffic_class
                
                	Match Traffic Class. Should be value 0..63 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: inner_cos
                
                	Match inner CoS
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: dei
                
                	Match DEI bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: dei_inner
                
                	Match DEI INNER  bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: protocol
                
                	Match protocol
                	**type**\: list of str
                
                	**pattern:** ([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\|(([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\\-([1\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5]))\|((ahp)\|(dhcpv4)\|(dhcpv6)\|(eigrp)\|(esp)\|(gre)\|(icmp)\|(igmp)\|(igrp)\|(ipinip)\|(ipv4)\|(ipv6)\|(ipv6icmp)\|(mpls)\|(nos)\|(ospf)\|(pcp)\|(pim)\|(ppp)\|(sctp)\|(tcp)\|(udp))
                
                .. attribute:: ipv4_acl
                
                	Match IPv4 ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: ipv6_acl
                
                	Match IPv6 ACL
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: ethernet_services_acl
                
                	Match Ethernet Services
                	**type**\: str
                
                	**length:** 1..64
                
                .. attribute:: mpls_experimental_topmost
                
                	Match MPLS experimental topmost label
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: mpls_experimental_imposition
                
                	Match MPLS experimental imposition label
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\: list of int
                
                	**range:** 0..7
                
                .. attribute:: ipv4_packet_length
                
                	Match IPv4 packet length. Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ipv6_packet_length
                
                	Match IPv6 packet length.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: packet_length
                
                	Match packet length.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: mpls_disposition_ipv4_access_list
                
                	Match MPLS Label Disposition IPv4 access list
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\: str
                
                	**length:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: inner_vlan
                
                	Match inner VLAN ID
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: flow_tag
                
                	Match flow\-tag. Should be value 1..63 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\: list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of  		 :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of  		 :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6>`
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fragment_type
                
                	Match fragment type for a packet
                	**type**\: list of str
                
                	**pattern:** (first\-fragment)\|(is\-fragment)\|(last\-fragment)
                
                .. attribute:: frame_relay_dlci
                
                	Match frame\-relay DLCI value.  Should be value 16..1007 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: fr_de
                
                	Set FrameRelay DE bit
                	**type**\: int
                
                	**range:** 0..1
                
                .. attribute:: icmpv4_code
                
                	Match IPv4 ICMP code.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv4_type
                
                	Match IPv4 ICMP type.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_code
                
                	Match IPv6 ICMP code.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: icmpv6_type
                
                	Match IPv6 ICMP type.  Should be value 0..255 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of  		 :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of  		 :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6>`
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\: list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flags
                	**type**\: int
                
                	**range:** 0..4095
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\: str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: circuit_id
                
                	Match Circuit ID
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: circuit_id_regex
                
                	Match Circuit id regex
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: dhcp_client_id
                
                	Match dhcp client ID
                	**type**\: list of  		 :py:class:`DhcpClientId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId>`
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\: list of  		 :py:class:`DhcpClientIdRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex>`
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of  		 :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName>`
                
                .. attribute:: domain_name_regex
                
                	Match domain name
                	**type**\: list of  		 :py:class:`DomainNameRegex <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex>`
                
                .. attribute:: remote_id
                
                	Match remote ID
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: remote_id_regex
                
                	Match remote id regex
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: timer
                
                	Match timer
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\: list of str
                
                	**length:** 1..32
                
                .. attribute:: source_mac
                
                	Match source MAC address
                	**type**\: list of str
                
                .. attribute:: destination_mac
                
                	Match destination MAC address
                	**type**\: list of str
                
                .. attribute:: vpls_control
                
                	Match VPLS control
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_broadcast
                
                	Match VPLS Broadcast
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_multicast
                
                	Match VPLS Multicast
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_known
                
                	Match VPLS Known
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: vpls_unknown
                
                	Match VPLS Unknown
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: flow
                
                	Match flow
                	**type**\:  :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.Flow>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2018-03-02'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.MatchNot, self).__init__()

                    self.yang_name = "match-not"
                    self.yang_parent_name = "class-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("destination-address-ipv4", ("destination_address_ipv4", PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4)), ("destination-address-ipv6", ("destination_address_ipv6", PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6)), ("source-address-ipv4", ("source_address_ipv4", PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4)), ("source-address-ipv6", ("source_address_ipv6", PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6)), ("dhcp-client-id", ("dhcp_client_id", PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId)), ("dhcp-client-id-regex", ("dhcp_client_id_regex", PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex)), ("domain-name", ("domain_name", PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName)), ("domain-name-regex", ("domain_name_regex", PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex)), ("flow", ("flow", PolicyManager.ClassMaps.ClassMap.MatchNot.Flow))])
                    self._leafs = OrderedDict([
                        ('ipv4_dscp', (YLeafList(YType.str, 'ipv4-dscp'), ['str'])),
                        ('ipv6_dscp', (YLeafList(YType.str, 'ipv6-dscp'), ['str'])),
                        ('dscp', (YLeafList(YType.str, 'dscp'), ['str'])),
                        ('ipv4_precedence', (YLeafList(YType.str, 'ipv4-precedence'), ['int','str'])),
                        ('ipv6_precedence', (YLeafList(YType.str, 'ipv6-precedence'), ['int','str'])),
                        ('precedence', (YLeafList(YType.str, 'precedence'), ['int','str'])),
                        ('qos_group', (YLeafList(YType.str, 'qos-group'), ['str'])),
                        ('traffic_class', (YLeafList(YType.str, 'traffic-class'), ['str'])),
                        ('cos', (YLeafList(YType.uint8, 'cos'), ['int'])),
                        ('inner_cos', (YLeafList(YType.uint8, 'inner-cos'), ['int'])),
                        ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                        ('dei_inner', (YLeaf(YType.uint8, 'dei-inner'), ['int'])),
                        ('protocol', (YLeafList(YType.str, 'protocol'), ['str'])),
                        ('ipv4_acl', (YLeaf(YType.str, 'ipv4-acl'), ['str'])),
                        ('ipv6_acl', (YLeaf(YType.str, 'ipv6-acl'), ['str'])),
                        ('ethernet_services_acl', (YLeaf(YType.str, 'ethernet-services-acl'), ['str'])),
                        ('mpls_experimental_topmost', (YLeafList(YType.uint8, 'mpls-experimental-topmost'), ['int'])),
                        ('mpls_experimental_imposition', (YLeafList(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                        ('discard_class', (YLeafList(YType.uint8, 'discard-class'), ['int'])),
                        ('ipv4_packet_length', (YLeafList(YType.str, 'ipv4-packet-length'), ['str'])),
                        ('ipv6_packet_length', (YLeafList(YType.str, 'ipv6-packet-length'), ['str'])),
                        ('packet_length', (YLeafList(YType.str, 'packet-length'), ['str'])),
                        ('mpls_disposition_ipv4_access_list', (YLeaf(YType.str, 'mpls-disposition-ipv4-access-list'), ['str'])),
                        ('mpls_disposition_ipv6_access_list', (YLeaf(YType.str, 'mpls-disposition-ipv6-access-list'), ['str'])),
                        ('vlan', (YLeafList(YType.str, 'vlan'), ['str'])),
                        ('inner_vlan', (YLeafList(YType.str, 'inner-vlan'), ['str'])),
                        ('flow_tag', (YLeafList(YType.str, 'flow-tag'), ['str'])),
                        ('ethertype', (YLeafList(YType.str, 'ethertype'), ['str'])),
                        ('destination_port', (YLeafList(YType.str, 'destination-port'), ['str'])),
                        ('fragment_type', (YLeafList(YType.str, 'fragment-type'), ['str'])),
                        ('frame_relay_dlci', (YLeafList(YType.str, 'frame-relay-dlci'), ['str'])),
                        ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                        ('icmpv4_code', (YLeafList(YType.str, 'icmpv4-code'), ['str'])),
                        ('icmpv4_type', (YLeafList(YType.str, 'icmpv4-type'), ['str'])),
                        ('icmpv6_code', (YLeafList(YType.str, 'icmpv6-code'), ['str'])),
                        ('icmpv6_type', (YLeafList(YType.str, 'icmpv6-type'), ['str'])),
                        ('source_port', (YLeafList(YType.str, 'source-port'), ['str'])),
                        ('tcp_flag', (YLeaf(YType.uint16, 'tcp-flag'), ['int'])),
                        ('authen_status', (YLeaf(YType.str, 'authen-status'), ['str'])),
                        ('circuit_id', (YLeafList(YType.str, 'circuit-id'), ['str'])),
                        ('circuit_id_regex', (YLeafList(YType.str, 'circuit-id-regex'), ['str'])),
                        ('remote_id', (YLeafList(YType.str, 'remote-id'), ['str'])),
                        ('remote_id_regex', (YLeafList(YType.str, 'remote-id-regex'), ['str'])),
                        ('service_name', (YLeafList(YType.str, 'service-name'), ['str'])),
                        ('service_name_regex', (YLeafList(YType.str, 'service-name-regex'), ['str'])),
                        ('timer', (YLeafList(YType.str, 'timer'), ['str'])),
                        ('timer_regex', (YLeafList(YType.str, 'timer-regex'), ['str'])),
                        ('user_name', (YLeafList(YType.str, 'user-name'), ['str'])),
                        ('user_name_regex', (YLeafList(YType.str, 'user-name-regex'), ['str'])),
                        ('source_mac', (YLeafList(YType.str, 'source-mac'), ['str'])),
                        ('destination_mac', (YLeafList(YType.str, 'destination-mac'), ['str'])),
                        ('vpls_control', (YLeaf(YType.empty, 'vpls-control'), ['Empty'])),
                        ('vpls_broadcast', (YLeaf(YType.empty, 'vpls-broadcast'), ['Empty'])),
                        ('vpls_multicast', (YLeaf(YType.empty, 'vpls-multicast'), ['Empty'])),
                        ('vpls_known', (YLeaf(YType.empty, 'vpls-known'), ['Empty'])),
                        ('vpls_unknown', (YLeaf(YType.empty, 'vpls-unknown'), ['Empty'])),
                    ])
                    self.ipv4_dscp = []
                    self.ipv6_dscp = []
                    self.dscp = []
                    self.ipv4_precedence = []
                    self.ipv6_precedence = []
                    self.precedence = []
                    self.qos_group = []
                    self.traffic_class = []
                    self.cos = []
                    self.inner_cos = []
                    self.dei = None
                    self.dei_inner = None
                    self.protocol = []
                    self.ipv4_acl = None
                    self.ipv6_acl = None
                    self.ethernet_services_acl = None
                    self.mpls_experimental_topmost = []
                    self.mpls_experimental_imposition = []
                    self.discard_class = []
                    self.ipv4_packet_length = []
                    self.ipv6_packet_length = []
                    self.packet_length = []
                    self.mpls_disposition_ipv4_access_list = None
                    self.mpls_disposition_ipv6_access_list = None
                    self.vlan = []
                    self.inner_vlan = []
                    self.flow_tag = []
                    self.ethertype = []
                    self.destination_port = []
                    self.fragment_type = []
                    self.frame_relay_dlci = []
                    self.fr_de = None
                    self.icmpv4_code = []
                    self.icmpv4_type = []
                    self.icmpv6_code = []
                    self.icmpv6_type = []
                    self.source_port = []
                    self.tcp_flag = None
                    self.authen_status = None
                    self.circuit_id = []
                    self.circuit_id_regex = []
                    self.remote_id = []
                    self.remote_id_regex = []
                    self.service_name = []
                    self.service_name_regex = []
                    self.timer = []
                    self.timer_regex = []
                    self.user_name = []
                    self.user_name_regex = []
                    self.source_mac = []
                    self.destination_mac = []
                    self.vpls_control = None
                    self.vpls_broadcast = None
                    self.vpls_multicast = None
                    self.vpls_known = None
                    self.vpls_unknown = None

                    self.flow = PolicyManager.ClassMaps.ClassMap.MatchNot.Flow()
                    self.flow.parent = self
                    self._children_name_map["flow"] = "flow"

                    self.destination_address_ipv4 = YList(self)
                    self.destination_address_ipv6 = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)
                    self.dhcp_client_id = YList(self)
                    self.dhcp_client_id_regex = YList(self)
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self._segment_path = lambda: "match-not"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot, ['ipv4_dscp', 'ipv6_dscp', 'dscp', 'ipv4_precedence', 'ipv6_precedence', 'precedence', 'qos_group', 'traffic_class', 'cos', 'inner_cos', 'dei', 'dei_inner', 'protocol', 'ipv4_acl', 'ipv6_acl', 'ethernet_services_acl', 'mpls_experimental_topmost', 'mpls_experimental_imposition', 'discard_class', 'ipv4_packet_length', 'ipv6_packet_length', 'packet_length', 'mpls_disposition_ipv4_access_list', 'mpls_disposition_ipv6_access_list', 'vlan', 'inner_vlan', 'flow_tag', 'ethertype', 'destination_port', 'fragment_type', 'frame_relay_dlci', 'fr_de', 'icmpv4_code', 'icmpv4_type', 'icmpv6_code', 'icmpv6_type', 'source_port', 'tcp_flag', 'authen_status', 'circuit_id', 'circuit_id_regex', 'remote_id', 'remote_id_regex', 'service_name', 'service_name_regex', 'timer', 'timer_regex', 'user_name', 'user_name_regex', 'source_mac', 'destination_mac', 'vpls_control', 'vpls_broadcast', 'vpls_multicast', 'vpls_known', 'vpls_unknown'], name, value)


                class DestinationAddressIpv4(Entity):
                    """
                    Match destination IPv4 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  (key)
                    
                    	IPv4 netmask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','netmask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                        ])
                        self.address = None
                        self.netmask = None
                        self._segment_path = lambda: "destination-address-ipv4" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, ['address', 'netmask'], name, value)


                class DestinationAddressIpv6(Entity):
                    """
                    Match destination IPv6 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	IPv6 prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self._segment_path = lambda: "destination-address-ipv6" + "[address='" + str(self.address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, ['address', 'prefix_length'], name, value)


                class SourceAddressIpv4(Entity):
                    """
                    Match source IPv4 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: netmask  (key)
                    
                    	IPv4 netmask
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','netmask']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                        ])
                        self.address = None
                        self.netmask = None
                        self._segment_path = lambda: "source-address-ipv4" + "[address='" + str(self.address) + "']" + "[netmask='" + str(self.netmask) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, ['address', 'netmask'], name, value)


                class SourceAddressIpv6(Entity):
                    """
                    Match source IPv6 address.
                    
                    .. attribute:: address  (key)
                    
                    	IPv6 address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: prefix_length  (key)
                    
                    	IPv6 prefix length
                    	**type**\: int
                    
                    	**range:** 0..128
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['address','prefix_length']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('address', (YLeaf(YType.str, 'address'), ['str'])),
                            ('prefix_length', (YLeaf(YType.uint8, 'prefix-length'), ['int'])),
                        ])
                        self.address = None
                        self.prefix_length = None
                        self._segment_path = lambda: "source-address-ipv6" + "[address='" + str(self.address) + "']" + "[prefix-length='" + str(self.prefix_length) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, ['address', 'prefix_length'], name, value)


                class DhcpClientId(Entity):
                    """
                    Match dhcp client ID.
                    
                    .. attribute:: value  (key)
                    
                    	Dhcp client Id
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  (key)
                    
                    	Dhcp client id Ascii/Hex
                    	**type**\: str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId, self).__init__()

                        self.yang_name = "dhcp-client-id"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['value','flag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('flag', (YLeaf(YType.str, 'flag'), ['str'])),
                        ])
                        self.value = None
                        self.flag = None
                        self._segment_path = lambda: "dhcp-client-id" + "[value='" + str(self.value) + "']" + "[flag='" + str(self.flag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientId, ['value', 'flag'], name, value)


                class DhcpClientIdRegex(Entity):
                    """
                    Match dhcp client id regex.
                    
                    .. attribute:: value  (key)
                    
                    	Dhcp client id regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: flag  (key)
                    
                    	Dhcp client Id regex Ascii/Hex
                    	**type**\: str
                    
                    	**pattern:** (none)\|(ascii)\|(hex)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex, self).__init__()

                        self.yang_name = "dhcp-client-id-regex"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['value','flag']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.str, 'value'), ['str'])),
                            ('flag', (YLeaf(YType.str, 'flag'), ['str'])),
                        ])
                        self.value = None
                        self.flag = None
                        self._segment_path = lambda: "dhcp-client-id-regex" + "[value='" + str(self.value) + "']" + "[flag='" + str(self.flag) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DhcpClientIdRegex, ['value', 'flag'], name, value)


                class DomainName(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: name  (key)
                    
                    	Domain name or regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  (key)
                    
                    	Domain\-format name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['name','format']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('format', (YLeaf(YType.str, 'format'), ['str'])),
                        ])
                        self.name = None
                        self.format = None
                        self._segment_path = lambda: "domain-name" + "[name='" + str(self.name) + "']" + "[format='" + str(self.format) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, ['name', 'format'], name, value)


                class DomainNameRegex(Entity):
                    """
                    Match domain name.
                    
                    .. attribute:: regex  (key)
                    
                    	Domain name or regular expression
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    .. attribute:: format  (key)
                    
                    	Domain\-format name
                    	**type**\: str
                    
                    	**length:** 1..32
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['regex','format']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('regex', (YLeaf(YType.str, 'regex'), ['str'])),
                            ('format', (YLeaf(YType.str, 'format'), ['str'])),
                        ])
                        self.regex = None
                        self.format = None
                        self._segment_path = lambda: "domain-name-regex" + "[regex='" + str(self.regex) + "']" + "[format='" + str(self.format) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, ['regex', 'format'], name, value)


                class Flow(Entity):
                    """
                    Match flow.
                    
                    .. attribute:: flow_tag
                    
                    	Configure the flow\-tag parameters
                    	**type**\: list of int
                    
                    	**range:** 1..63
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match-not"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('flow_tag', (YLeafList(YType.uint16, 'flow-tag'), ['int'])),
                        ])
                        self.flow_tag = []
                        self._segment_path = lambda: "flow"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, ['flow_tag'], name, value)


    class PolicyMaps(Entity):
        """
        Policy\-maps configuration.
        
        .. attribute:: policy_map
        
        	Policy\-map configuration
        	**type**\: list of  		 :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2018-03-02'

        def __init__(self):
            super(PolicyManager.PolicyMaps, self).__init__()

            self.yang_name = "policy-maps"
            self.yang_parent_name = "policy-manager"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("policy-map", ("policy_map", PolicyManager.PolicyMaps.PolicyMap))])
            self._leafs = OrderedDict()

            self.policy_map = YList(self)
            self._segment_path = lambda: "policy-maps"
            self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PolicyManager.PolicyMaps, [], name, value)


        class PolicyMap(Entity):
            """
            Policy\-map configuration.
            
            .. attribute:: type  (key)
            
            	Type of policy\-map
            	**type**\:  :py:class:`PolicyMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyMapType>`
            
            .. attribute:: name  (key)
            
            	Name of policy\-map
            	**type**\: str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: event
            
            	Policy event
            	**type**\: list of  		 :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event>`
            
            .. attribute:: policy_map_rule
            
            	Class\-map rule
            	**type**\: list of  		 :py:class:`PolicyMapRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule>`
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\: str
            
            

            """

            _prefix = 'infra-policymgr-cfg'
            _revision = '2018-03-02'

            def __init__(self):
                super(PolicyManager.PolicyMaps.PolicyMap, self).__init__()

                self.yang_name = "policy-map"
                self.yang_parent_name = "policy-maps"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['type','name']
                self._child_classes = OrderedDict([("event", ("event", PolicyManager.PolicyMaps.PolicyMap.Event)), ("policy-map-rule", ("policy_map_rule", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule))])
                self._leafs = OrderedDict([
                    ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PolicyMapType', '')])),
                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                    ('description', (YLeaf(YType.str, 'description'), ['str'])),
                ])
                self.type = None
                self.name = None
                self.description = None

                self.event = YList(self)
                self.policy_map_rule = YList(self)
                self._segment_path = lambda: "policy-map" + "[type='" + str(self.type) + "']" + "[name='" + str(self.name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/policy-maps/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap, ['type', 'name', 'description'], name, value)


            class Event(Entity):
                """
                Policy event.
                
                .. attribute:: event_type  (key)
                
                	Event type
                	**type**\:  :py:class:`EventType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.EventType>`
                
                .. attribute:: event_mode_match_all
                
                	Execute all the matched classes
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: event_mode_match_first
                
                	Execute only the first matched class
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: class_
                
                	Class\-map rule
                	**type**\: list of  		 :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2018-03-02'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.Event, self).__init__()

                    self.yang_name = "event"
                    self.yang_parent_name = "policy-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['event_type']
                    self._child_classes = OrderedDict([("class", ("class_", PolicyManager.PolicyMaps.PolicyMap.Event.Class))])
                    self._leafs = OrderedDict([
                        ('event_type', (YLeaf(YType.enumeration, 'event-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'EventType', '')])),
                        ('event_mode_match_all', (YLeaf(YType.empty, 'event-mode-match-all'), ['Empty'])),
                        ('event_mode_match_first', (YLeaf(YType.empty, 'event-mode-match-first'), ['Empty'])),
                    ])
                    self.event_type = None
                    self.event_mode_match_all = None
                    self.event_mode_match_first = None

                    self.class_ = YList(self)
                    self._segment_path = lambda: "event" + "[event-type='" + str(self.event_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event, ['event_type', 'event_mode_match_all', 'event_mode_match_first'], name, value)


                class Class(Entity):
                    """
                    Class\-map rule.
                    
                    .. attribute:: class_name  (key)
                    
                    	Name of class
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: class_type  (key)
                    
                    	Type of class
                    	**type**\:  :py:class:`PmapClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PmapClassMapType>`
                    
                    .. attribute:: class_execution_strategy
                    
                    	Class execution strategy
                    	**type**\:  :py:class:`ExecutionStrategy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.ExecutionStrategy>`
                    
                    .. attribute:: action_rule
                    
                    	Action rule
                    	**type**\: list of  		 :py:class:`ActionRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class, self).__init__()

                        self.yang_name = "class"
                        self.yang_parent_name = "event"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['class_name','class_type']
                        self._child_classes = OrderedDict([("action-rule", ("action_rule", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule))])
                        self._leafs = OrderedDict([
                            ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                            ('class_type', (YLeaf(YType.enumeration, 'class-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PmapClassMapType', '')])),
                            ('class_execution_strategy', (YLeaf(YType.enumeration, 'class-execution-strategy'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'ExecutionStrategy', '')])),
                        ])
                        self.class_name = None
                        self.class_type = None
                        self.class_execution_strategy = None

                        self.action_rule = YList(self)
                        self._segment_path = lambda: "class" + "[class-name='" + str(self.class_name) + "']" + "[class-type='" + str(self.class_type) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class, ['class_name', 'class_type', 'class_execution_strategy'], name, value)


                    class ActionRule(Entity):
                        """
                        Action rule.
                        
                        .. attribute:: action_sequence_number  (key)
                        
                        	Sequence number for this action
                        	**type**\: int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: activate_dynamic_template
                        
                        	Activate dynamic templates
                        	**type**\:  :py:class:`ActivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: authenticate
                        
                        	Authentication related configuration
                        	**type**\:  :py:class:`Authenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate>`
                        
                        .. attribute:: authorize
                        
                        	Authorize
                        	**type**\:  :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: deactivate_dynamic_template
                        
                        	Deactivate dynamic templates
                        	**type**\:  :py:class:`DeactivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: disconnect
                        
                        	Disconnect session
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: monitor
                        
                        	Monitor session
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set_timer
                        
                        	Set a timer to execute a rule on its  expiry
                        	**type**\:  :py:class:`SetTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer>`
                        
                        	**presence node**\: True
                        
                        .. attribute:: stop_timer
                        
                        	Disable timer before it expires
                        	**type**\:  :py:class:`StopTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule, self).__init__()

                            self.yang_name = "action-rule"
                            self.yang_parent_name = "class"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['action_sequence_number']
                            self._child_classes = OrderedDict([("activate-dynamic-template", ("activate_dynamic_template", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate)), ("authenticate", ("authenticate", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate)), ("authorize", ("authorize", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize)), ("deactivate-dynamic-template", ("deactivate_dynamic_template", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate)), ("set-timer", ("set_timer", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer)), ("stop-timer", ("stop_timer", PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer))])
                            self._leafs = OrderedDict([
                                ('action_sequence_number', (YLeaf(YType.uint16, 'action-sequence-number'), ['int'])),
                                ('disconnect', (YLeaf(YType.empty, 'disconnect'), ['Empty'])),
                                ('monitor', (YLeaf(YType.empty, 'monitor'), ['Empty'])),
                            ])
                            self.action_sequence_number = None
                            self.disconnect = None
                            self.monitor = None

                            self.activate_dynamic_template = None
                            self._children_name_map["activate_dynamic_template"] = "activate-dynamic-template"

                            self.authenticate = PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate()
                            self.authenticate.parent = self
                            self._children_name_map["authenticate"] = "authenticate"

                            self.authorize = None
                            self._children_name_map["authorize"] = "authorize"

                            self.deactivate_dynamic_template = None
                            self._children_name_map["deactivate_dynamic_template"] = "deactivate-dynamic-template"

                            self.set_timer = None
                            self._children_name_map["set_timer"] = "set-timer"

                            self.stop_timer = PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer()
                            self.stop_timer.parent = self
                            self._children_name_map["stop_timer"] = "stop-timer"
                            self._segment_path = lambda: "action-rule" + "[action-sequence-number='" + str(self.action_sequence_number) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule, ['action_sequence_number', 'disconnect', 'monitor'], name, value)


                        class ActivateDynamicTemplate(Entity):
                            """
                            Activate dynamic templates.
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\: str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate, self).__init__()

                                self.yang_name = "activate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('aaa_list', (YLeaf(YType.str, 'aaa-list'), ['str'])),
                                ])
                                self.name = None
                                self.aaa_list = None
                                self._segment_path = lambda: "activate-dynamic-template"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate, ['name', 'aaa_list'], name, value)


                        class Authenticate(Entity):
                            """
                            Authentication related configuration.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate, self).__init__()

                                self.yang_name = "authenticate"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('aaa_list', (YLeaf(YType.str, 'aaa-list'), ['str'])),
                                ])
                                self.aaa_list = None
                                self._segment_path = lambda: "authenticate"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate, ['aaa_list'], name, value)


                        class Authorize(Entity):
                            """
                            Authorize.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: format
                            
                            	Specify an Authorize format name
                            	**type**\: str
                            
                            .. attribute:: identifier
                            
                            	Specify an Authorize format name
                            	**type**\:  :py:class:`AuthorizeIdentifier <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.AuthorizeIdentifier>`
                            
                            .. attribute:: password
                            
                            	Specify a password to be used for AAA request
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize, self).__init__()

                                self.yang_name = "authorize"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('aaa_list', (YLeaf(YType.str, 'aaa-list'), ['str'])),
                                    ('format', (YLeaf(YType.str, 'format'), ['str'])),
                                    ('identifier', (YLeaf(YType.enumeration, 'identifier'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'AuthorizeIdentifier', '')])),
                                    ('password', (YLeaf(YType.str, 'password'), ['str'])),
                                ])
                                self.aaa_list = None
                                self.format = None
                                self.identifier = None
                                self.password = None
                                self._segment_path = lambda: "authorize"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize, ['aaa_list', 'format', 'identifier', 'password'], name, value)


                        class DeactivateDynamicTemplate(Entity):
                            """
                            Deactivate dynamic templates.
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\: str
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate, self).__init__()

                                self.yang_name = "deactivate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('name', (YLeaf(YType.str, 'name'), ['str'])),
                                    ('aaa_list', (YLeaf(YType.str, 'aaa-list'), ['str'])),
                                ])
                                self.name = None
                                self.aaa_list = None
                                self._segment_path = lambda: "deactivate-dynamic-template"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate, ['name', 'aaa_list'], name, value)


                        class SetTimer(Entity):
                            """
                            Set a timer to execute a rule on its 
                            expiry
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\: str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: timer_value
                            
                            	Timer value in minutes
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**mandatory**\: True
                            
                            	**units**\: minutes
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer, self).__init__()

                                self.yang_name = "set-timer"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self.is_presence_container = True
                                self._leafs = OrderedDict([
                                    ('timer_name', (YLeaf(YType.str, 'timer-name'), ['str'])),
                                    ('timer_value', (YLeaf(YType.uint32, 'timer-value'), ['int'])),
                                ])
                                self.timer_name = None
                                self.timer_value = None
                                self._segment_path = lambda: "set-timer"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer, ['timer_name', 'timer_value'], name, value)


                        class StopTimer(Entity):
                            """
                            Disable timer before it expires.
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer, self).__init__()

                                self.yang_name = "stop-timer"
                                self.yang_parent_name = "action-rule"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('timer_name', (YLeaf(YType.str, 'timer-name'), ['str'])),
                                ])
                                self.timer_name = None
                                self._segment_path = lambda: "stop-timer"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer, ['timer_name'], name, value)


            class PolicyMapRule(Entity):
                """
                Class\-map rule.
                
                .. attribute:: class_name  (key)
                
                	Name of class\-map
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                
                .. attribute:: class_type  (key)
                
                	Type of class\-map
                	**type**\:  :py:class:`PmapClassMapType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PmapClassMapType>`
                
                .. attribute:: shape
                
                	Policy action shape
                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape>`
                
                .. attribute:: min_bandwidth
                
                	Policy action minimum bandwidth queue
                	**type**\:  :py:class:`MinBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth>`
                
                .. attribute:: bandwidth_remaining
                
                	Policy action bandwidth remaining queue
                	**type**\:  :py:class:`BandwidthRemaining <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining>`
                
                .. attribute:: queue_limit
                
                	Policy action queue limit
                	**type**\:  :py:class:`QueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit>`
                
                .. attribute:: pfc
                
                	Policy action pfc
                	**type**\:  :py:class:`Pfc <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc>`
                
                .. attribute:: priority_level
                
                	Priority level
                	**type**\: int
                
                	**range:** 1..7
                
                .. attribute:: default_red
                
                	Default random early detection
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: ecn_red
                
                	ECN based random early detection
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: random_detect
                
                	Random early detection. All RED profiles in a class must be based on the same field
                	**type**\: list of  		 :py:class:`RandomDetect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect>`
                
                .. attribute:: set
                
                	Policy action packet marking
                	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set>`
                
                .. attribute:: police
                
                	Configures traffic policing action
                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police>`
                
                .. attribute:: service_policy
                
                	Configure a child service policy
                	**type**\:  :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy>`
                
                .. attribute:: cac_local
                
                	Policy action CAC
                	**type**\:  :py:class:`CacLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal>`
                
                .. attribute:: flow_params
                
                	Policy flow monitoring action
                	**type**\:  :py:class:`FlowParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams>`
                
                .. attribute:: metrics_ipcbr
                
                	Policy IP\-CBR metric action
                	**type**\:  :py:class:`MetricsIpcbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr>`
                
                .. attribute:: react
                
                	Policy action react
                	**type**\:  :py:class:`React <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React>`
                
                .. attribute:: http_redirect
                
                	Policy action http redirect. Redirect to this url
                	**type**\: str
                
                .. attribute:: pbr_transmit
                
                	Policy action PBR transmit
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: pbr_drop
                
                	Policy action PBR drop
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: decap_gre
                
                	Policy action DECAP GRE
                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                
                .. attribute:: pbr_redirect
                
                	Policy action redirect
                	**type**\:  :py:class:`PbrRedirect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect>`
                
                .. attribute:: pbr_forward
                
                	Policy action PBR forward
                	**type**\:  :py:class:`PbrForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward>`
                
                .. attribute:: service_fragment
                
                	Policy action service fragment.  Service fragment name
                	**type**\: str
                
                .. attribute:: fragment
                
                	Policy action fragment. Fragment name
                	**type**\: str
                
                .. attribute:: service_function_path
                
                	Policy action service function path
                	**type**\:  :py:class:`ServiceFunctionPath <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath>`
                
                	**presence node**\: True
                
                .. attribute:: http_enrichment
                
                	HTTP Enrichment action
                	**type**\:  :py:class:`HttpEnrichment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.HttpEnrichment>`
                
                

                """

                _prefix = 'infra-policymgr-cfg'
                _revision = '2018-03-02'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, self).__init__()

                    self.yang_name = "policy-map-rule"
                    self.yang_parent_name = "policy-map"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['class_name','class_type']
                    self._child_classes = OrderedDict([("shape", ("shape", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape)), ("min-bandwidth", ("min_bandwidth", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth)), ("bandwidth-remaining", ("bandwidth_remaining", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining)), ("queue-limit", ("queue_limit", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit)), ("pfc", ("pfc", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc)), ("random-detect", ("random_detect", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect)), ("set", ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set)), ("police", ("police", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police)), ("service-policy", ("service_policy", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy)), ("cac-local", ("cac_local", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal)), ("flow-params", ("flow_params", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams)), ("metrics-ipcbr", ("metrics_ipcbr", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr)), ("react", ("react", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React)), ("pbr-redirect", ("pbr_redirect", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect)), ("pbr-forward", ("pbr_forward", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward)), ("service-function-path", ("service_function_path", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath)), ("http-enrichment", ("http_enrichment", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.HttpEnrichment))])
                    self._leafs = OrderedDict([
                        ('class_name', (YLeaf(YType.str, 'class-name'), ['str'])),
                        ('class_type', (YLeaf(YType.enumeration, 'class-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg', 'PmapClassMapType', '')])),
                        ('priority_level', (YLeaf(YType.uint8, 'priority-level'), ['int'])),
                        ('default_red', (YLeaf(YType.empty, 'default-red'), ['Empty'])),
                        ('ecn_red', (YLeaf(YType.empty, 'ecn-red'), ['Empty'])),
                        ('http_redirect', (YLeaf(YType.str, 'http-redirect'), ['str'])),
                        ('pbr_transmit', (YLeaf(YType.empty, 'pbr-transmit'), ['Empty'])),
                        ('pbr_drop', (YLeaf(YType.empty, 'pbr-drop'), ['Empty'])),
                        ('decap_gre', (YLeaf(YType.empty, 'decap-gre'), ['Empty'])),
                        ('service_fragment', (YLeaf(YType.str, 'service-fragment'), ['str'])),
                        ('fragment', (YLeaf(YType.str, 'fragment'), ['str'])),
                    ])
                    self.class_name = None
                    self.class_type = None
                    self.priority_level = None
                    self.default_red = None
                    self.ecn_red = None
                    self.http_redirect = None
                    self.pbr_transmit = None
                    self.pbr_drop = None
                    self.decap_gre = None
                    self.service_fragment = None
                    self.fragment = None

                    self.shape = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape()
                    self.shape.parent = self
                    self._children_name_map["shape"] = "shape"

                    self.min_bandwidth = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth()
                    self.min_bandwidth.parent = self
                    self._children_name_map["min_bandwidth"] = "min-bandwidth"

                    self.bandwidth_remaining = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining()
                    self.bandwidth_remaining.parent = self
                    self._children_name_map["bandwidth_remaining"] = "bandwidth-remaining"

                    self.queue_limit = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit()
                    self.queue_limit.parent = self
                    self._children_name_map["queue_limit"] = "queue-limit"

                    self.pfc = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc()
                    self.pfc.parent = self
                    self._children_name_map["pfc"] = "pfc"

                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set()
                    self.set.parent = self
                    self._children_name_map["set"] = "set"

                    self.police = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police()
                    self.police.parent = self
                    self._children_name_map["police"] = "police"

                    self.service_policy = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy()
                    self.service_policy.parent = self
                    self._children_name_map["service_policy"] = "service-policy"

                    self.cac_local = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal()
                    self.cac_local.parent = self
                    self._children_name_map["cac_local"] = "cac-local"

                    self.flow_params = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams()
                    self.flow_params.parent = self
                    self._children_name_map["flow_params"] = "flow-params"

                    self.metrics_ipcbr = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr()
                    self.metrics_ipcbr.parent = self
                    self._children_name_map["metrics_ipcbr"] = "metrics-ipcbr"

                    self.react = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React()
                    self.react.parent = self
                    self._children_name_map["react"] = "react"

                    self.pbr_redirect = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect()
                    self.pbr_redirect.parent = self
                    self._children_name_map["pbr_redirect"] = "pbr-redirect"

                    self.pbr_forward = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward()
                    self.pbr_forward.parent = self
                    self._children_name_map["pbr_forward"] = "pbr-forward"

                    self.service_function_path = None
                    self._children_name_map["service_function_path"] = "service-function-path"

                    self.http_enrichment = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.HttpEnrichment()
                    self.http_enrichment.parent = self
                    self._children_name_map["http_enrichment"] = "http-enrichment"

                    self.random_detect = YList(self)
                    self._segment_path = lambda: "policy-map-rule" + "[class-name='" + str(self.class_name) + "']" + "[class-type='" + str(self.class_type) + "']"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, ['class_name', 'class_type', 'priority_level', 'default_red', 'ecn_red', 'http_redirect', 'pbr_transmit', 'pbr_drop', 'decap_gre', 'service_fragment', 'fragment'], name, value)


                class Shape(Entity):
                    """
                    Policy action shape.
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate>`
                    
                    .. attribute:: burst
                    
                    	Burst size configuration
                    	**type**\:  :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape, self).__init__()

                        self.yang_name = "shape"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rate", ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate)), ("burst", ("burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst))])
                        self._leafs = OrderedDict()

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"

                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst()
                        self.burst.parent = self
                        self._children_name_map["burst"] = "burst"
                        self._segment_path = lambda: "shape"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape, [], name, value)


                    class Rate(Entity):
                        """
                        Rate configuration.
                        
                        .. attribute:: value
                        
                        	Shape bandwidth value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unit
                        
                        	Shape bandwidth units
                        	**type**\: str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(percent)\|(per\-million)\|(per\-thousand)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "shape"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                            ])
                            self.value = None
                            self.unit = None
                            self._segment_path = lambda: "rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, ['value', 'unit'], name, value)


                    class Burst(Entity):
                        """
                        Burst size configuration.
                        
                        .. attribute:: value
                        
                        	Burst size value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: units
                        
                        	Burst size units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "shape"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "burst"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, ['value', 'units'], name, value)


                class MinBandwidth(Entity):
                    """
                    Policy action minimum bandwidth queue.
                    
                    .. attribute:: value
                    
                    	Minimum bandwidth value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit
                    
                    	Minimum bandwidth units
                    	**type**\: str
                    
                    	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(percent)\|(per\-million)\|(per\-thousand)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, self).__init__()

                        self.yang_name = "min-bandwidth"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                        ])
                        self.value = None
                        self.unit = None
                        self._segment_path = lambda: "min-bandwidth"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, ['value', 'unit'], name, value)


                class BandwidthRemaining(Entity):
                    """
                    Policy action bandwidth remaining queue.
                    
                    .. attribute:: value
                    
                    	Remaining bandwidth value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit
                    
                    	Remaining bandwidth units
                    	**type**\: str
                    
                    	**pattern:** (percent)\|(ratio)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, self).__init__()

                        self.yang_name = "bandwidth-remaining"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                        ])
                        self.value = None
                        self.unit = None
                        self._segment_path = lambda: "bandwidth-remaining"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, ['value', 'unit'], name, value)


                class QueueLimit(Entity):
                    """
                    Policy action queue limit.
                    
                    .. attribute:: value
                    
                    	Remaining bandwidth value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: unit
                    
                    	Remaining bandwidth units
                    	**type**\: str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)\|(percent)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, self).__init__()

                        self.yang_name = "queue-limit"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                            ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                        ])
                        self.value = None
                        self.unit = None
                        self._segment_path = lambda: "queue-limit"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, ['value', 'unit'], name, value)


                class Pfc(Entity):
                    """
                    Policy action pfc.
                    
                    .. attribute:: pfc_pause_set
                    
                    	Pfc Pause set value
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: pfc_buffer_size
                    
                    	
                    	**type**\:  :py:class:`PfcBufferSize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize>`
                    
                    .. attribute:: pfc_pause_threshold
                    
                    	
                    	**type**\:  :py:class:`PfcPauseThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold>`
                    
                    .. attribute:: pfc_resume_threshold
                    
                    	
                    	**type**\:  :py:class:`PfcResumeThreshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, self).__init__()

                        self.yang_name = "pfc"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("pfc-buffer-size", ("pfc_buffer_size", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize)), ("pfc-pause-threshold", ("pfc_pause_threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold)), ("pfc-resume-threshold", ("pfc_resume_threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold))])
                        self._leafs = OrderedDict([
                            ('pfc_pause_set', (YLeaf(YType.empty, 'pfc-pause-set'), ['Empty'])),
                        ])
                        self.pfc_pause_set = None

                        self.pfc_buffer_size = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize()
                        self.pfc_buffer_size.parent = self
                        self._children_name_map["pfc_buffer_size"] = "pfc-buffer-size"

                        self.pfc_pause_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold()
                        self.pfc_pause_threshold.parent = self
                        self._children_name_map["pfc_pause_threshold"] = "pfc-pause-threshold"

                        self.pfc_resume_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold()
                        self.pfc_resume_threshold.parent = self
                        self._children_name_map["pfc_resume_threshold"] = "pfc-resume-threshold"
                        self._segment_path = lambda: "pfc"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, ['pfc_pause_set'], name, value)


                    class PfcBufferSize(Entity):
                        """
                        
                        
                        .. attribute:: value
                        
                        	Pfc buffer size value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unit
                        
                        	Pfc buffer size units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, self).__init__()

                            self.yang_name = "pfc-buffer-size"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                            ])
                            self.value = None
                            self.unit = None
                            self._segment_path = lambda: "pfc-buffer-size"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, ['value', 'unit'], name, value)


                    class PfcPauseThreshold(Entity):
                        """
                        
                        
                        .. attribute:: value
                        
                        	Pfc pause threshold value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unit
                        
                        	Pfc pause threshold units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, self).__init__()

                            self.yang_name = "pfc-pause-threshold"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                            ])
                            self.value = None
                            self.unit = None
                            self._segment_path = lambda: "pfc-pause-threshold"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, ['value', 'unit'], name, value)


                    class PfcResumeThreshold(Entity):
                        """
                        
                        
                        .. attribute:: value
                        
                        	Pfc resume threshold value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: unit
                        
                        	Pfc resume threshold units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, self).__init__()

                            self.yang_name = "pfc-resume-threshold"
                            self.yang_parent_name = "pfc"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('unit', (YLeaf(YType.str, 'unit'), ['str'])),
                            ])
                            self.value = None
                            self.unit = None
                            self._segment_path = lambda: "pfc-resume-threshold"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, ['value', 'unit'], name, value)


                class RandomDetect(Entity):
                    """
                    Random early detection.
                    All RED profiles in a class must be based
                    on the same field.
                    
                    .. attribute:: threshold_min_value  (key)
                    
                    	Minimum RED threshold value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: threshold_min_units  (key)
                    
                    	Minimum RED threshold units
                    	**type**\: str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: threshold_max_value  (key)
                    
                    	Maximum RED threshold value
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: threshold_max_units  (key)
                    
                    	Maximum RED threshold units
                    	**type**\: str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: cos
                    
                    	WRED based on CoS
                    	**type**\: list of str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: discard_class
                    
                    	WRED based on discard class
                    	**type**\: list of int
                    
                    	**range:** 0..7
                    
                    .. attribute:: dscp
                    
                    	WRED based on DSCP
                    	**type**\: list of str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: mpls_exp
                    
                    	MPLS Experimental value based WRED
                    	**type**\: list of int
                    
                    	**range:** 0..7
                    
                    .. attribute:: precedence
                    
                    	WRED based on precedence
                    	**type**\: union of the below types:
                    
                    		**type**\: list of int
                    
                    			**range:** 0..7
                    
                    		**type**\: list of str
                    
                    			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    .. attribute:: dei
                    
                    	DEI based WRED
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: ecn
                    
                    	ECN based WRED
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, self).__init__()

                        self.yang_name = "random-detect"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['threshold_min_value','threshold_min_units','threshold_max_value','threshold_max_units']
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('threshold_min_value', (YLeaf(YType.uint32, 'threshold-min-value'), ['int'])),
                            ('threshold_min_units', (YLeaf(YType.str, 'threshold-min-units'), ['str'])),
                            ('threshold_max_value', (YLeaf(YType.uint32, 'threshold-max-value'), ['int'])),
                            ('threshold_max_units', (YLeaf(YType.str, 'threshold-max-units'), ['str'])),
                            ('cos', (YLeafList(YType.str, 'cos'), ['str'])),
                            ('discard_class', (YLeafList(YType.uint8, 'discard-class'), ['int'])),
                            ('dscp', (YLeafList(YType.str, 'dscp'), ['str'])),
                            ('mpls_exp', (YLeafList(YType.uint8, 'mpls-exp'), ['int'])),
                            ('precedence', (YLeafList(YType.str, 'precedence'), ['int','str'])),
                            ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                            ('ecn', (YLeaf(YType.empty, 'ecn'), ['Empty'])),
                        ])
                        self.threshold_min_value = None
                        self.threshold_min_units = None
                        self.threshold_max_value = None
                        self.threshold_max_units = None
                        self.cos = []
                        self.discard_class = []
                        self.dscp = []
                        self.mpls_exp = []
                        self.precedence = []
                        self.dei = None
                        self.ecn = None
                        self._segment_path = lambda: "random-detect" + "[threshold-min-value='" + str(self.threshold_min_value) + "']" + "[threshold-min-units='" + str(self.threshold_min_units) + "']" + "[threshold-max-value='" + str(self.threshold_max_value) + "']" + "[threshold-max-units='" + str(self.threshold_max_units) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, ['threshold_min_value', 'threshold_min_units', 'threshold_max_value', 'threshold_max_units', 'cos', 'discard_class', 'dscp', 'mpls_exp', 'precedence', 'dei', 'ecn'], name, value)


                class Set(Entity):
                    """
                    Policy action packet marking.
                    
                    .. attribute:: dscp
                    
                    	Marks a packet by setting the DSCP in the ToS byte
                    	**type**\: str
                    
                    	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                    
                    .. attribute:: qos_group
                    
                    	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                    	**type**\: int
                    
                    	**range:** 0..512
                    
                    .. attribute:: traffic_class
                    
                    	Sets the Traffic class identifiers on IPv4 or MPLS packets
                    	**type**\: int
                    
                    	**range:** 0..63
                    
                    .. attribute:: discard_class
                    
                    	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: forward_class
                    
                    	Sets the forward class
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: df
                    
                    	Set DF bit
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: cos
                    
                    	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: inner_cos
                    
                    	Set inner cos
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: precedence
                    
                    	Sets the precedence value in the IP header
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..7
                    
                    		**type**\: str
                    
                    			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    .. attribute:: precedence_tunnel
                    
                    	Sets the precedence tunnel value for ipsec
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 0..7
                    
                    		**type**\: str
                    
                    			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                    
                    .. attribute:: mpls_experimental_top_most
                    
                    	Sets the experimental value of the MPLS packet top\-most labels
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: mpls_experimental_imposition
                    
                    	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: srp_priority
                    
                    	Sets the spatial reuse protocol priority value of an  outgoing packet
                    	**type**\: int
                    
                    	**range:** 0..7
                    
                    .. attribute:: fr_de
                    
                    	Set FrameRelay DE bit
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: dei
                    
                    	Set DEI bit
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: dei_imposition
                    
                    	Set DEI imposition bit
                    	**type**\: int
                    
                    	**range:** 0..1
                    
                    .. attribute:: source_address
                    
                    	Source IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: destination_address
                    
                    	Destination IPv4 address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('dscp', (YLeaf(YType.str, 'dscp'), ['str'])),
                            ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                            ('traffic_class', (YLeaf(YType.uint8, 'traffic-class'), ['int'])),
                            ('discard_class', (YLeaf(YType.uint8, 'discard-class'), ['int'])),
                            ('forward_class', (YLeaf(YType.uint8, 'forward-class'), ['int'])),
                            ('df', (YLeaf(YType.uint8, 'df'), ['int'])),
                            ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                            ('inner_cos', (YLeaf(YType.uint8, 'inner-cos'), ['int'])),
                            ('precedence', (YLeaf(YType.str, 'precedence'), ['int','str'])),
                            ('precedence_tunnel', (YLeaf(YType.str, 'precedence-tunnel'), ['int','str'])),
                            ('mpls_experimental_top_most', (YLeaf(YType.uint8, 'mpls-experimental-top-most'), ['int'])),
                            ('mpls_experimental_imposition', (YLeaf(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                            ('srp_priority', (YLeaf(YType.uint8, 'srp-priority'), ['int'])),
                            ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                            ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                            ('dei_imposition', (YLeaf(YType.uint8, 'dei-imposition'), ['int'])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                        ])
                        self.dscp = None
                        self.qos_group = None
                        self.traffic_class = None
                        self.discard_class = None
                        self.forward_class = None
                        self.df = None
                        self.cos = None
                        self.inner_cos = None
                        self.precedence = None
                        self.precedence_tunnel = None
                        self.mpls_experimental_top_most = None
                        self.mpls_experimental_imposition = None
                        self.srp_priority = None
                        self.fr_de = None
                        self.dei = None
                        self.dei_imposition = None
                        self.source_address = None
                        self.destination_address = None
                        self._segment_path = lambda: "set"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, ['dscp', 'qos_group', 'traffic_class', 'discard_class', 'forward_class', 'df', 'cos', 'inner_cos', 'precedence', 'precedence_tunnel', 'mpls_experimental_top_most', 'mpls_experimental_imposition', 'srp_priority', 'fr_de', 'dei', 'dei_imposition', 'source_address', 'destination_address'], name, value)


                class Police(Entity):
                    """
                    Configures traffic policing action.
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate>`
                    
                    .. attribute:: peak_rate
                    
                    	Peak rate configuration
                    	**type**\:  :py:class:`PeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate>`
                    
                    .. attribute:: burst
                    
                    	Burst configuration
                    	**type**\:  :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst>`
                    
                    .. attribute:: peak_burst
                    
                    	Peak burst configuration
                    	**type**\:  :py:class:`PeakBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst>`
                    
                    .. attribute:: conform_action
                    
                    	Configures the action to take on packets that conform  to the rate limit
                    	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction>`
                    
                    .. attribute:: exceed_action
                    
                    	Configures the action to take on packets that exceed  the rate limit
                    	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction>`
                    
                    .. attribute:: violate_action
                    
                    	Configures the action to take on packets that violate the rate limit
                    	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rate", ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate)), ("peak-rate", ("peak_rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate)), ("burst", ("burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst)), ("peak-burst", ("peak_burst", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst)), ("conform-action", ("conform_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction)), ("exceed-action", ("exceed_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction)), ("violate-action", ("violate_action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction))])
                        self._leafs = OrderedDict()

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"

                        self.peak_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate()
                        self.peak_rate.parent = self
                        self._children_name_map["peak_rate"] = "peak-rate"

                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst()
                        self.burst.parent = self
                        self._children_name_map["burst"] = "burst"

                        self.peak_burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst()
                        self.peak_burst.parent = self
                        self._children_name_map["peak_burst"] = "peak-burst"

                        self.conform_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction()
                        self.conform_action.parent = self
                        self._children_name_map["conform_action"] = "conform-action"

                        self.exceed_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction()
                        self.exceed_action.parent = self
                        self._children_name_map["exceed_action"] = "exceed-action"

                        self.violate_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction()
                        self.violate_action.parent = self
                        self._children_name_map["violate_action"] = "violate-action"
                        self._segment_path = lambda: "police"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police, [], name, value)


                    class Rate(Entity):
                        """
                        Rate configuration.
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\: str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)\|(cellsps)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, ['value', 'units'], name, value)


                    class PeakRate(Entity):
                        """
                        Peak rate configuration.
                        
                        .. attribute:: value
                        
                        	Peak rate value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: units
                        
                        	Peak rate units
                        	**type**\: str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)\|(cellsps)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, self).__init__()

                            self.yang_name = "peak-rate"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "peak-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, ['value', 'units'], name, value)


                    class Burst(Entity):
                        """
                        Burst configuration.
                        
                        .. attribute:: value
                        
                        	Burst value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: units
                        
                        	Burst units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "burst"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, ['value', 'units'], name, value)


                    class PeakBurst(Entity):
                        """
                        Peak burst configuration.
                        
                        .. attribute:: value
                        
                        	Peak burst value
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: units
                        
                        	Peak burst units
                        	**type**\: str
                        
                        	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, self).__init__()

                            self.yang_name = "peak-burst"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "peak-burst"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, ['value', 'units'], name, value)


                    class ConformAction(Entity):
                        """
                        Configures the action to take on packets that conform 
                        to the rate limit.
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, self).__init__()

                            self.yang_name = "conform-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("set", ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set))])
                            self._leafs = OrderedDict([
                                ('transmit', (YLeaf(YType.empty, 'Transmit'), ['Empty'])),
                                ('drop', (YLeaf(YType.empty, 'drop'), ['Empty'])),
                            ])
                            self.transmit = None
                            self.drop = None

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._segment_path = lambda: "conform-action"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, ['transmit', 'drop'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\: str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\: int
                            
                            	**range:** 0..512
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "conform-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dscp', (YLeaf(YType.str, 'dscp'), ['str'])),
                                    ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                                    ('traffic_class', (YLeaf(YType.uint8, 'traffic-class'), ['int'])),
                                    ('discard_class', (YLeaf(YType.uint8, 'discard-class'), ['int'])),
                                    ('forward_class', (YLeaf(YType.uint8, 'forward-class'), ['int'])),
                                    ('df', (YLeaf(YType.uint8, 'df'), ['int'])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                    ('inner_cos', (YLeaf(YType.uint8, 'inner-cos'), ['int'])),
                                    ('precedence', (YLeaf(YType.str, 'precedence'), ['int','str'])),
                                    ('precedence_tunnel', (YLeaf(YType.str, 'precedence-tunnel'), ['int','str'])),
                                    ('mpls_experimental_top_most', (YLeaf(YType.uint8, 'mpls-experimental-top-most'), ['int'])),
                                    ('mpls_experimental_imposition', (YLeaf(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                                    ('srp_priority', (YLeaf(YType.uint8, 'srp-priority'), ['int'])),
                                    ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                                    ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                                    ('dei_imposition', (YLeaf(YType.uint8, 'dei-imposition'), ['int'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ])
                                self.dscp = None
                                self.qos_group = None
                                self.traffic_class = None
                                self.discard_class = None
                                self.forward_class = None
                                self.df = None
                                self.cos = None
                                self.inner_cos = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.mpls_experimental_top_most = None
                                self.mpls_experimental_imposition = None
                                self.srp_priority = None
                                self.fr_de = None
                                self.dei = None
                                self.dei_imposition = None
                                self.source_address = None
                                self.destination_address = None
                                self._segment_path = lambda: "set"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, ['dscp', 'qos_group', 'traffic_class', 'discard_class', 'forward_class', 'df', 'cos', 'inner_cos', 'precedence', 'precedence_tunnel', 'mpls_experimental_top_most', 'mpls_experimental_imposition', 'srp_priority', 'fr_de', 'dei', 'dei_imposition', 'source_address', 'destination_address'], name, value)


                    class ExceedAction(Entity):
                        """
                        Configures the action to take on packets that exceed 
                        the rate limit.
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, self).__init__()

                            self.yang_name = "exceed-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("set", ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set))])
                            self._leafs = OrderedDict([
                                ('transmit', (YLeaf(YType.empty, 'Transmit'), ['Empty'])),
                                ('drop', (YLeaf(YType.empty, 'drop'), ['Empty'])),
                            ])
                            self.transmit = None
                            self.drop = None

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._segment_path = lambda: "exceed-action"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, ['transmit', 'drop'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\: str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\: int
                            
                            	**range:** 0..512
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "exceed-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dscp', (YLeaf(YType.str, 'dscp'), ['str'])),
                                    ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                                    ('traffic_class', (YLeaf(YType.uint8, 'traffic-class'), ['int'])),
                                    ('discard_class', (YLeaf(YType.uint8, 'discard-class'), ['int'])),
                                    ('forward_class', (YLeaf(YType.uint8, 'forward-class'), ['int'])),
                                    ('df', (YLeaf(YType.uint8, 'df'), ['int'])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                    ('inner_cos', (YLeaf(YType.uint8, 'inner-cos'), ['int'])),
                                    ('precedence', (YLeaf(YType.str, 'precedence'), ['int','str'])),
                                    ('precedence_tunnel', (YLeaf(YType.str, 'precedence-tunnel'), ['int','str'])),
                                    ('mpls_experimental_top_most', (YLeaf(YType.uint8, 'mpls-experimental-top-most'), ['int'])),
                                    ('mpls_experimental_imposition', (YLeaf(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                                    ('srp_priority', (YLeaf(YType.uint8, 'srp-priority'), ['int'])),
                                    ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                                    ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                                    ('dei_imposition', (YLeaf(YType.uint8, 'dei-imposition'), ['int'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ])
                                self.dscp = None
                                self.qos_group = None
                                self.traffic_class = None
                                self.discard_class = None
                                self.forward_class = None
                                self.df = None
                                self.cos = None
                                self.inner_cos = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.mpls_experimental_top_most = None
                                self.mpls_experimental_imposition = None
                                self.srp_priority = None
                                self.fr_de = None
                                self.dei = None
                                self.dei_imposition = None
                                self.source_address = None
                                self.destination_address = None
                                self._segment_path = lambda: "set"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, ['dscp', 'qos_group', 'traffic_class', 'discard_class', 'forward_class', 'df', 'cos', 'inner_cos', 'precedence', 'precedence_tunnel', 'mpls_experimental_top_most', 'mpls_experimental_imposition', 'srp_priority', 'fr_de', 'dei', 'dei_imposition', 'source_address', 'destination_address'], name, value)


                    class ViolateAction(Entity):
                        """
                        Configures the action to take on packets that violate
                        the rate limit.
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, self).__init__()

                            self.yang_name = "violate-action"
                            self.yang_parent_name = "police"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("set", ("set", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set))])
                            self._leafs = OrderedDict([
                                ('transmit', (YLeaf(YType.empty, 'Transmit'), ['Empty'])),
                                ('drop', (YLeaf(YType.empty, 'drop'), ['Empty'])),
                            ])
                            self.transmit = None
                            self.drop = None

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._segment_path = lambda: "violate-action"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, ['transmit', 'drop'], name, value)


                        class Set(Entity):
                            """
                            Police action packet marking.
                            
                            .. attribute:: dscp
                            
                            	Marks a packet by setting the DSCP in the ToS byte
                            	**type**\: str
                            
                            	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                            
                            .. attribute:: qos_group
                            
                            	Sets the QoS group identifiers on IPv4 or MPLS packets. The set qos\-group is supported only on an ingress policy
                            	**type**\: int
                            
                            	**range:** 0..512
                            
                            .. attribute:: traffic_class
                            
                            	Sets the Traffic class identifiers on IPv4 or MPLS packets
                            	**type**\: int
                            
                            	**range:** 0..63
                            
                            .. attribute:: discard_class
                            
                            	Sets the discard class on IPv4 or MPLS packets. The discard\-class can be used only in service policies  that are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: forward_class
                            
                            	Sets the forward class
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: df
                            
                            	Set DF bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: inner_cos
                            
                            	Set inner cos
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: precedence
                            
                            	Sets the precedence value in the IP header
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: precedence_tunnel
                            
                            	Sets the precedence tunnel value for ipsec
                            	**type**\: union of the below types:
                            
                            		**type**\: int
                            
                            			**range:** 0..7
                            
                            		**type**\: str
                            
                            			**pattern:** (critical)\|(flash)\|(flash\-override)\|(immediate)\|(internet)\|(network)\|(priority)\|(routine)
                            
                            .. attribute:: mpls_experimental_top_most
                            
                            	Sets the experimental value of the MPLS packet top\-most labels
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: mpls_experimental_imposition
                            
                            	Sets the experimental value of the MPLS packet  imposition labels. Imposition can be used only in service policies that  are attached in the ingress policy
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\: int
                            
                            	**range:** 0..7
                            
                            .. attribute:: fr_de
                            
                            	Set FrameRelay DE bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei
                            
                            	Set DEI bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: dei_imposition
                            
                            	Set DEI imposition bit
                            	**type**\: int
                            
                            	**range:** 0..1
                            
                            .. attribute:: source_address
                            
                            	Source IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: destination_address
                            
                            	Destination IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "violate-action"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('dscp', (YLeaf(YType.str, 'dscp'), ['str'])),
                                    ('qos_group', (YLeaf(YType.uint16, 'qos-group'), ['int'])),
                                    ('traffic_class', (YLeaf(YType.uint8, 'traffic-class'), ['int'])),
                                    ('discard_class', (YLeaf(YType.uint8, 'discard-class'), ['int'])),
                                    ('forward_class', (YLeaf(YType.uint8, 'forward-class'), ['int'])),
                                    ('df', (YLeaf(YType.uint8, 'df'), ['int'])),
                                    ('cos', (YLeaf(YType.uint8, 'cos'), ['int'])),
                                    ('inner_cos', (YLeaf(YType.uint8, 'inner-cos'), ['int'])),
                                    ('precedence', (YLeaf(YType.str, 'precedence'), ['int','str'])),
                                    ('precedence_tunnel', (YLeaf(YType.str, 'precedence-tunnel'), ['int','str'])),
                                    ('mpls_experimental_top_most', (YLeaf(YType.uint8, 'mpls-experimental-top-most'), ['int'])),
                                    ('mpls_experimental_imposition', (YLeaf(YType.uint8, 'mpls-experimental-imposition'), ['int'])),
                                    ('srp_priority', (YLeaf(YType.uint8, 'srp-priority'), ['int'])),
                                    ('fr_de', (YLeaf(YType.uint8, 'fr-de'), ['int'])),
                                    ('dei', (YLeaf(YType.uint8, 'dei'), ['int'])),
                                    ('dei_imposition', (YLeaf(YType.uint8, 'dei-imposition'), ['int'])),
                                    ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                    ('destination_address', (YLeaf(YType.str, 'destination-address'), ['str'])),
                                ])
                                self.dscp = None
                                self.qos_group = None
                                self.traffic_class = None
                                self.discard_class = None
                                self.forward_class = None
                                self.df = None
                                self.cos = None
                                self.inner_cos = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.mpls_experimental_top_most = None
                                self.mpls_experimental_imposition = None
                                self.srp_priority = None
                                self.fr_de = None
                                self.dei = None
                                self.dei_imposition = None
                                self.source_address = None
                                self.destination_address = None
                                self._segment_path = lambda: "set"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, ['dscp', 'qos_group', 'traffic_class', 'discard_class', 'forward_class', 'df', 'cos', 'inner_cos', 'precedence', 'precedence_tunnel', 'mpls_experimental_top_most', 'mpls_experimental_imposition', 'srp_priority', 'fr_de', 'dei', 'dei_imposition', 'source_address', 'destination_address'], name, value)


                class ServicePolicy(Entity):
                    """
                    Configure a child service policy.
                    
                    .. attribute:: policy_name
                    
                    	Name of service\-policy
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: type
                    
                    	Type of service\-policy
                    	**type**\: str
                    
                    	**pattern:** (PBR)\|(QOS)\|(REDIRECT)\|(TRAFFIC)\|(pbr)\|(qos)\|(redirect)\|(traffic)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('policy_name', (YLeaf(YType.str, 'policy-name'), ['str'])),
                            ('type', (YLeaf(YType.str, 'type'), ['str'])),
                        ])
                        self.policy_name = None
                        self.type = None
                        self._segment_path = lambda: "service-policy"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, ['policy_name', 'type'], name, value)


                class CacLocal(Entity):
                    """
                    Policy action CAC.
                    
                    .. attribute:: rate
                    
                    	The rate allocated for all flows
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate>`
                    
                    .. attribute:: flow_rate
                    
                    	The rate allocated per flow
                    	**type**\:  :py:class:`FlowRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate>`
                    
                    .. attribute:: flow_idle_timeout
                    
                    	The interval after which a flow is removed,  if there is no activity. If timeout is 0 this flow does not expire
                    	**type**\: union of the below types:
                    
                    		**type**\: int
                    
                    			**range:** 10..2550
                    
                    		**type**\: str
                    
                    			**pattern:** (None)\|(none)
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, self).__init__()

                        self.yang_name = "cac-local"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rate", ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate)), ("flow-rate", ("flow_rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate))])
                        self._leafs = OrderedDict([
                            ('flow_idle_timeout', (YLeaf(YType.str, 'flow-idle-timeout'), ['int','str'])),
                        ])
                        self.flow_idle_timeout = None

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"

                        self.flow_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate()
                        self.flow_rate.parent = self
                        self._children_name_map["flow_rate"] = "flow-rate"
                        self._segment_path = lambda: "cac-local"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, ['flow_idle_timeout'], name, value)


                    class Rate(Entity):
                        """
                        The rate allocated for all flows.
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\: str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(cellsps)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "cac-local"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, ['value', 'units'], name, value)


                    class FlowRate(Entity):
                        """
                        The rate allocated per flow.
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\: int
                        
                        	**range:** 1..4294967295
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\: str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(cellsps)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, self).__init__()

                            self.yang_name = "flow-rate"
                            self.yang_parent_name = "cac-local"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('value', (YLeaf(YType.uint32, 'value'), ['int'])),
                                ('units', (YLeaf(YType.str, 'units'), ['str'])),
                            ])
                            self.value = None
                            self.units = None
                            self._segment_path = lambda: "flow-rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, ['value', 'units'], name, value)


                class FlowParams(Entity):
                    """
                    Policy flow monitoring action.
                    
                    .. attribute:: max_flow
                    
                    	Max simultaneous flows monitored per policy class
                    	**type**\: int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: interval_duration
                    
                    	Monitored interval duration
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    .. attribute:: history
                    
                    	Keep stats/metrics on box for so many intervals
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: timeout
                    
                    	Declare a flow dead if no packets received in so much time
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: seconds
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, self).__init__()

                        self.yang_name = "flow-params"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('max_flow', (YLeaf(YType.uint16, 'max-flow'), ['int'])),
                            ('interval_duration', (YLeaf(YType.uint32, 'interval-duration'), ['int'])),
                            ('history', (YLeaf(YType.uint32, 'history'), ['int'])),
                            ('timeout', (YLeaf(YType.uint32, 'timeout'), ['int'])),
                        ])
                        self.max_flow = None
                        self.interval_duration = None
                        self.history = None
                        self.timeout = None
                        self._segment_path = lambda: "flow-params"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, ['max_flow', 'interval_duration', 'history', 'timeout'], name, value)


                class MetricsIpcbr(Entity):
                    """
                    Policy IP\-CBR metric action.
                    
                    .. attribute:: rate
                    
                    	Nominal per\-flow data rate
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate>`
                    
                    .. attribute:: media_packet
                    
                    	Media\-packet structure
                    	**type**\:  :py:class:`MediaPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr, self).__init__()

                        self.yang_name = "metrics-ipcbr"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("rate", ("rate", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate)), ("media-packet", ("media_packet", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket))])
                        self._leafs = OrderedDict()

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"

                        self.media_packet = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket()
                        self.media_packet.parent = self
                        self._children_name_map["media_packet"] = "media-packet"
                        self._segment_path = lambda: "metrics-ipcbr"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr, [], name, value)


                    class Rate(Entity):
                        """
                        Nominal per\-flow data rate.
                        
                        .. attribute:: layer3
                        
                        	Nominal rate specified at the L3 (IP)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: bps
                        
                        .. attribute:: packet
                        
                        	Nominal IP layer packet rate (in pps)
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: pps
                        
                        .. attribute:: media
                        
                        	Nominal data rate of the media flow (ip payload)
                        	**type**\: int
                        
                        	**range:** 1..3000000000
                        
                        	**units**\: bps
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "metrics-ipcbr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('layer3', (YLeaf(YType.uint32, 'layer3'), ['int'])),
                                ('packet', (YLeaf(YType.uint32, 'packet'), ['int'])),
                                ('media', (YLeaf(YType.uint32, 'media'), ['int'])),
                            ])
                            self.layer3 = None
                            self.packet = None
                            self.media = None
                            self._segment_path = lambda: "rate"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, ['layer3', 'packet', 'media'], name, value)


                    class MediaPacket(Entity):
                        """
                        Media\-packet structure.
                        
                        .. attribute:: size
                        
                        	Nominal size of the media\-packet
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        	**units**\: bytes
                        
                        .. attribute:: count_in_layer3
                        
                        	Nominal number of media packets in an IP payload
                        	**type**\: int
                        
                        	**range:** 1..64
                        
                        	**units**\: packets
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, self).__init__()

                            self.yang_name = "media-packet"
                            self.yang_parent_name = "metrics-ipcbr"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('size', (YLeaf(YType.uint16, 'size'), ['int'])),
                                ('count_in_layer3', (YLeaf(YType.uint8, 'count-in-layer3'), ['int'])),
                            ])
                            self.size = None
                            self.count_in_layer3 = None
                            self._segment_path = lambda: "media-packet"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, ['size', 'count_in_layer3'], name, value)


                class React(Entity):
                    """
                    Policy action react.
                    
                    .. attribute:: descrition
                    
                    	String describing the react statement
                    	**type**\: str
                    
                    .. attribute:: action
                    
                    	Action on alert
                    	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action>`
                    
                    .. attribute:: alarm
                    
                    	Alaram settings
                    	**type**\:  :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm>`
                    
                    .. attribute:: threshold
                    
                    	Alarm threshold settings
                    	**type**\:  :py:class:`Threshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold>`
                    
                    .. attribute:: criterion_delay_factor
                    
                    	React criterion delay factor
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_media_stop
                    
                    	React criterion media stop
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_mrv
                    
                    	React criterion mrv
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_flow_count
                    
                    	React criterion flow count
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: criterion_packet_rate
                    
                    	React criterion packet rate
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, self).__init__()

                        self.yang_name = "react"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("action", ("action", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action)), ("alarm", ("alarm", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm)), ("threshold", ("threshold", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold))])
                        self._leafs = OrderedDict([
                            ('descrition', (YLeaf(YType.str, 'descrition'), ['str'])),
                            ('criterion_delay_factor', (YLeaf(YType.empty, 'criterion-delay-factor'), ['Empty'])),
                            ('criterion_media_stop', (YLeaf(YType.empty, 'criterion-media-stop'), ['Empty'])),
                            ('criterion_mrv', (YLeaf(YType.empty, 'criterion-mrv'), ['Empty'])),
                            ('criterion_flow_count', (YLeaf(YType.empty, 'criterion-flow-count'), ['Empty'])),
                            ('criterion_packet_rate', (YLeaf(YType.empty, 'criterion-packet-rate'), ['Empty'])),
                        ])
                        self.descrition = None
                        self.criterion_delay_factor = None
                        self.criterion_media_stop = None
                        self.criterion_mrv = None
                        self.criterion_flow_count = None
                        self.criterion_packet_rate = None

                        self.action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action()
                        self.action.parent = self
                        self._children_name_map["action"] = "action"

                        self.alarm = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm()
                        self.alarm.parent = self
                        self._children_name_map["alarm"] = "alarm"

                        self.threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold()
                        self.threshold.parent = self
                        self._children_name_map["threshold"] = "threshold"
                        self._segment_path = lambda: "react"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, ['descrition', 'criterion_delay_factor', 'criterion_media_stop', 'criterion_mrv', 'criterion_flow_count', 'criterion_packet_rate'], name, value)


                    class Action(Entity):
                        """
                        Action on alert.
                        
                        .. attribute:: syslog
                        
                        	Syslog
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        .. attribute:: snmp
                        
                        	SNMP
                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, self).__init__()

                            self.yang_name = "action"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('syslog', (YLeaf(YType.empty, 'syslog'), ['Empty'])),
                                ('snmp', (YLeaf(YType.empty, 'snmp'), ['Empty'])),
                            ])
                            self.syslog = None
                            self.snmp = None
                            self._segment_path = lambda: "action"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, ['syslog', 'snmp'], name, value)


                    class Alarm(Entity):
                        """
                        Alaram settings.
                        
                        .. attribute:: type
                        
                        	Alarm type
                        	**type**\:  :py:class:`Type <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type>`
                        
                        .. attribute:: severity
                        
                        	Severity of the alarm
                        	**type**\: str
                        
                        	**pattern:** (informational)\|(notification)\|(warning)\|(error)\|(critical)\|(alert)\|(emergency)
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, self).__init__()

                            self.yang_name = "alarm"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("type", ("type", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type))])
                            self._leafs = OrderedDict([
                                ('severity', (YLeaf(YType.str, 'severity'), ['str'])),
                            ])
                            self.severity = None

                            self.type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type()
                            self.type.parent = self
                            self._children_name_map["type"] = "type"
                            self._segment_path = lambda: "alarm"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, ['severity'], name, value)


                        class Type(Entity):
                            """
                            Alarm type.
                            
                            .. attribute:: discrete
                            
                            	Discrete alarm type
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: group_count
                            
                            	Number of flows to reach before  triggering alarm
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**units**\: number of flows
                            
                            .. attribute:: group_percent
                            
                            	Percent to reach before triggering alarm
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            	**units**\: percentage
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, self).__init__()

                                self.yang_name = "type"
                                self.yang_parent_name = "alarm"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('discrete', (YLeaf(YType.empty, 'discrete'), ['Empty'])),
                                    ('group_count', (YLeaf(YType.uint16, 'group-count'), ['int'])),
                                    ('group_percent', (YLeaf(YType.uint16, 'group-percent'), ['int'])),
                                ])
                                self.discrete = None
                                self.group_count = None
                                self.group_percent = None
                                self._segment_path = lambda: "type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, ['discrete', 'group_count', 'group_percent'], name, value)


                    class Threshold(Entity):
                        """
                        Alarm threshold settings.
                        
                        .. attribute:: trigger_value
                        
                        	Alarm trigger value settings
                        	**type**\:  :py:class:`TriggerValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue>`
                        
                        .. attribute:: trigger_type
                        
                        	Alarm trigger type settings
                        	**type**\:  :py:class:`TriggerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold, self).__init__()

                            self.yang_name = "threshold"
                            self.yang_parent_name = "react"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("trigger-value", ("trigger_value", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue)), ("trigger-type", ("trigger_type", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType))])
                            self._leafs = OrderedDict()

                            self.trigger_value = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue()
                            self.trigger_value.parent = self
                            self._children_name_map["trigger_value"] = "trigger-value"

                            self.trigger_type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType()
                            self.trigger_type.parent = self
                            self._children_name_map["trigger_type"] = "trigger-type"
                            self._segment_path = lambda: "threshold"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold, [], name, value)


                        class TriggerValue(Entity):
                            """
                            Alarm trigger value settings.
                            
                            .. attribute:: greater_than
                            
                            	Greater than
                            	**type**\: str
                            
                            .. attribute:: greater_than_equal
                            
                            	Greater than equal
                            	**type**\: str
                            
                            .. attribute:: less_than
                            
                            	Less than
                            	**type**\: str
                            
                            .. attribute:: less_than_equal
                            
                            	Less than equal
                            	**type**\: str
                            
                            .. attribute:: range
                            
                            	Range
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, self).__init__()

                                self.yang_name = "trigger-value"
                                self.yang_parent_name = "threshold"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('greater_than', (YLeaf(YType.str, 'greater-than'), ['str'])),
                                    ('greater_than_equal', (YLeaf(YType.str, 'greater-than-equal'), ['str'])),
                                    ('less_than', (YLeaf(YType.str, 'less-than'), ['str'])),
                                    ('less_than_equal', (YLeaf(YType.str, 'less-than-equal'), ['str'])),
                                    ('range', (YLeaf(YType.str, 'range'), ['str'])),
                                ])
                                self.greater_than = None
                                self.greater_than_equal = None
                                self.less_than = None
                                self.less_than_equal = None
                                self.range = None
                                self._segment_path = lambda: "trigger-value"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, ['greater_than', 'greater_than_equal', 'less_than', 'less_than_equal', 'range'], name, value)


                        class TriggerType(Entity):
                            """
                            Alarm trigger type settings.
                            
                            .. attribute:: immediate
                            
                            	Immediate trigger
                            	**type**\: :py:class:`Empty<ydk.types.Empty>`
                            
                            .. attribute:: average
                            
                            	Trigger averaged over N intervals
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, self).__init__()

                                self.yang_name = "trigger-type"
                                self.yang_parent_name = "threshold"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('immediate', (YLeaf(YType.empty, 'immediate'), ['Empty'])),
                                    ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                ])
                                self.immediate = None
                                self.average = None
                                self._segment_path = lambda: "trigger-type"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, ['immediate', 'average'], name, value)


                class PbrRedirect(Entity):
                    """
                    Policy action redirect
                    
                    .. attribute:: ipv4
                    
                    	Policy action redirect IPv4
                    	**type**\:  :py:class:`Ipv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4>`
                    
                    .. attribute:: ipv6
                    
                    	Policy action redirect IPv6
                    	**type**\:  :py:class:`Ipv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6>`
                    
                    .. attribute:: next_hop
                    
                    	Next hop address
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect, self).__init__()

                        self.yang_name = "pbr-redirect"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4", ("ipv4", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4)), ("ipv6", ("ipv6", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6)), ("next-hop", ("next_hop", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop))])
                        self._leafs = OrderedDict()

                        self.ipv4 = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4()
                        self.ipv4.parent = self
                        self._children_name_map["ipv4"] = "ipv4"

                        self.ipv6 = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6()
                        self.ipv6.parent = self
                        self._children_name_map["ipv6"] = "ipv6"

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._segment_path = lambda: "pbr-redirect"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect, [], name, value)


                    class Ipv4(Entity):
                        """
                        Policy action redirect IPv4
                        
                        .. attribute:: ipv4_next_hop
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf
                        
                        	IPv4 VRF
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4, self).__init__()

                            self.yang_name = "ipv4"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv4_next_hop', (YLeaf(YType.str, 'ipv4-next-hop'), ['str'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ])
                            self.ipv4_next_hop = None
                            self.vrf = None
                            self._segment_path = lambda: "ipv4"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv4, ['ipv4_next_hop', 'vrf'], name, value)


                    class Ipv6(Entity):
                        """
                        Policy action redirect IPv6
                        
                        .. attribute:: ipv6_next_hop
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf
                        
                        	IPv6 VRF
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6, self).__init__()

                            self.yang_name = "ipv6"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_next_hop', (YLeaf(YType.str, 'ipv6-next-hop'), ['str'])),
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                            ])
                            self.ipv6_next_hop = None
                            self.vrf = None
                            self._segment_path = lambda: "ipv6"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.Ipv6, ['ipv6_next_hop', 'vrf'], name, value)


                    class NextHop(Entity):
                        """
                        Next hop address.
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:  :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-redirect"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("route-target", ("route_target", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget))])
                            self._leafs = OrderedDict()

                            self.route_target = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget()
                            self.route_target.parent = self
                            self._children_name_map["route_target"] = "route-target"
                            self._segment_path = lambda: "next-hop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop, [], name, value)


                        class RouteTarget(Entity):
                            """
                            Route Target
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  :py:class:`Ipv4Address <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address>`
                            
                            .. attribute:: as_number
                            
                            	2\-byte/4\-byte AS number
                            	**type**\: int
                            
                            	**range:** 1..4294967295
                            
                            .. attribute:: index
                            
                            	ASN2\:index 2/4 byte (hex or decimal format)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2018-03-02'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "next-hop"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-address", ("ipv4_address", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address))])
                                self._leafs = OrderedDict([
                                    ('as_number', (YLeaf(YType.uint32, 'as-number'), ['int'])),
                                    ('index', (YLeaf(YType.uint32, 'index'), ['int'])),
                                ])
                                self.as_number = None
                                self.index = None

                                self.ipv4_address = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address()
                                self.ipv4_address.parent = self
                                self._children_name_map["ipv4_address"] = "ipv4-address"
                                self._segment_path = lambda: "route-target"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, ['as_number', 'index'], name, value)


                            class Ipv4Address(Entity):
                                """
                                IPv4 address.
                                
                                .. attribute:: address
                                
                                	IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: netmask
                                
                                	IPv4 netmask
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'infra-policymgr-cfg'
                                _revision = '2018-03-02'

                                def __init__(self):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, self).__init__()

                                    self.yang_name = "ipv4-address"
                                    self.yang_parent_name = "route-target"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('address', (YLeaf(YType.str, 'address'), ['str'])),
                                        ('netmask', (YLeaf(YType.str, 'netmask'), ['str'])),
                                    ])
                                    self.address = None
                                    self.netmask = None
                                    self._segment_path = lambda: "ipv4-address"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, ['address', 'netmask'], name, value)


                class PbrForward(Entity):
                    """
                    Policy action PBR forward.
                    
                    .. attribute:: default
                    
                    	Use system default routing table
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: next_hop
                    
                    	Use specific next\-hop. Here we present 5 different combination  for the pbf next\-hop.  1. vrf with v6 address  2. vrf with v4 address  3. vrf   4. v4 address  5. v6 address
                    	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, self).__init__()

                        self.yang_name = "pbr-forward"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("next-hop", ("next_hop", PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop))])
                        self._leafs = OrderedDict([
                            ('default', (YLeaf(YType.empty, 'default'), ['Empty'])),
                        ])
                        self.default = None

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._segment_path = lambda: "pbr-forward"
                        self._is_frozen = True

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
                        
                        .. attribute:: vrf
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2018-03-02'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-forward"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('vrf', (YLeaf(YType.str, 'vrf'), ['str'])),
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                            ])
                            self.vrf = None
                            self.ipv4_address = None
                            self.ipv6_address = None
                            self._segment_path = lambda: "next-hop"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, ['vrf', 'ipv4_address', 'ipv6_address'], name, value)


                class ServiceFunctionPath(Entity):
                    """
                    Policy action service function path.
                    
                    .. attribute:: path_id
                    
                    	Service function path id
                    	**type**\: int
                    
                    	**range:** 1..16777215
                    
                    	**mandatory**\: True
                    
                    .. attribute:: index
                    
                    	Service function path index
                    	**type**\: int
                    
                    	**range:** 1..255
                    
                    	**mandatory**\: True
                    
                    .. attribute:: metadata
                    
                    	Service function path metadata name
                    	**type**\: str
                    
                    

                    This class is a :ref:`presence class<presence-class>`

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, self).__init__()

                        self.yang_name = "service-function-path"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self.is_presence_container = True
                        self._leafs = OrderedDict([
                            ('path_id', (YLeaf(YType.uint32, 'path-id'), ['int'])),
                            ('index', (YLeaf(YType.uint8, 'index'), ['int'])),
                            ('metadata', (YLeaf(YType.str, 'metadata'), ['str'])),
                        ])
                        self.path_id = None
                        self.index = None
                        self.metadata = None
                        self._segment_path = lambda: "service-function-path"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, ['path_id', 'index', 'metadata'], name, value)


                class HttpEnrichment(Entity):
                    """
                    HTTP Enrichment action
                    
                    .. attribute:: subscribermac
                    
                    	Subscriber Mac
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: subscriberip
                    
                    	Subscriber IP
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: hostname
                    
                    	Hostname
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    .. attribute:: bngidentifierinterface
                    
                    	Bng Identifier Interface
                    	**type**\: :py:class:`Empty<ydk.types.Empty>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2018-03-02'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.HttpEnrichment, self).__init__()

                        self.yang_name = "http-enrichment"
                        self.yang_parent_name = "policy-map-rule"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('subscribermac', (YLeaf(YType.empty, 'subscribermac'), ['Empty'])),
                            ('subscriberip', (YLeaf(YType.empty, 'subscriberip'), ['Empty'])),
                            ('hostname', (YLeaf(YType.empty, 'hostname'), ['Empty'])),
                            ('bngidentifierinterface', (YLeaf(YType.empty, 'bngidentifierinterface'), ['Empty'])),
                        ])
                        self.subscribermac = None
                        self.subscriberip = None
                        self.hostname = None
                        self.bngidentifierinterface = None
                        self._segment_path = lambda: "http-enrichment"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.HttpEnrichment, ['subscribermac', 'subscriberip', 'hostname', 'bngidentifierinterface'], name, value)

    def clone_ptr(self):
        self._top_entity = PolicyManager()
        return self._top_entity

