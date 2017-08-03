""" Cisco_IOS_XR_infra_policymgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ASR9k policy manager configuration.
 
Copyright (c) 2013, 2015\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    _revision = '2017-03-03'

    def __init__(self):
        super(PolicyManager, self).__init__()
        self._top_entity = None

        self.yang_name = "policy-manager"
        self.yang_parent_name = "Cisco-IOS-XR-infra-policymgr-cfg"

        self.class_maps = PolicyManager.ClassMaps()
        self.class_maps.parent = self
        self._children_name_map["class_maps"] = "class-maps"
        self._children_yang_names.add("class-maps")

        self.policy_maps = PolicyManager.PolicyMaps()
        self.policy_maps.parent = self
        self._children_name_map["policy_maps"] = "policy-maps"
        self._children_yang_names.add("policy-maps")


    class ClassMaps(Entity):
        """
        Class\-maps configuration.
        
        .. attribute:: class_map
        
        	Class\-map configuration
        	**type**\: list of    :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.ClassMaps.ClassMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2017-03-03'

        def __init__(self):
            super(PolicyManager.ClassMaps, self).__init__()

            self.yang_name = "class-maps"
            self.yang_parent_name = "policy-manager"

            self.class_map = YList(self)

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
                        super(PolicyManager.ClassMaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PolicyManager.ClassMaps, self).__setattr__(name, value)


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
            _revision = '2017-03-03'

            def __init__(self):
                super(PolicyManager.ClassMaps.ClassMap, self).__init__()

                self.yang_name = "class-map"
                self.yang_parent_name = "class-maps"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "name",
                                "class_map_mode_match_all",
                                "class_map_mode_match_any",
                                "description") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PolicyManager.ClassMaps.ClassMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PolicyManager.ClassMaps.ClassMap, self).__setattr__(name, value)


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
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
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
                _revision = '2017-03-03'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.Match, self).__init__()

                    self.yang_name = "match"
                    self.yang_parent_name = "class-map"

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

                    self.dhcp_client_id = YLeafList(YType.str, "dhcp-client-id")

                    self.dhcp_client_id_regex = YLeafList(YType.str, "dhcp-client-id-regex")

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
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("atm_clp",
                                    "atm_oam",
                                    "authen_status",
                                    "cac_admit",
                                    "cac_unadmit",
                                    "circuit_id",
                                    "circuit_id_regex",
                                    "cos",
                                    "dei",
                                    "dei_inner",
                                    "destination_mac",
                                    "destination_port",
                                    "dhcp_client_id",
                                    "dhcp_client_id_regex",
                                    "discard_class",
                                    "dscp",
                                    "ethernet_services_acl",
                                    "ethertype",
                                    "flow_tag",
                                    "fr_de",
                                    "fragment_type",
                                    "frame_relay_dlci",
                                    "icmpv4_code",
                                    "icmpv4_type",
                                    "icmpv6_code",
                                    "icmpv6_type",
                                    "inner_cos",
                                    "inner_vlan",
                                    "ipv4_acl",
                                    "ipv4_dscp",
                                    "ipv4_packet_length",
                                    "ipv4_precedence",
                                    "ipv6_acl",
                                    "ipv6_dscp",
                                    "ipv6_packet_length",
                                    "ipv6_precedence",
                                    "mpls_disposition_ipv4_access_list",
                                    "mpls_disposition_ipv6_access_list",
                                    "mpls_experimental_imposition",
                                    "mpls_experimental_topmost",
                                    "packet_length",
                                    "precedence",
                                    "protocol",
                                    "qos_group",
                                    "remote_id",
                                    "remote_id_regex",
                                    "service_name",
                                    "service_name_regex",
                                    "source_mac",
                                    "source_port",
                                    "tcp_flag",
                                    "timer",
                                    "timer_regex",
                                    "traffic_class",
                                    "user_name",
                                    "user_name_regex",
                                    "vlan",
                                    "vpls_broadcast",
                                    "vpls_control",
                                    "vpls_known",
                                    "vpls_multicast",
                                    "vpls_unknown") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PolicyManager.ClassMaps.ClassMap.Match, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PolicyManager.ClassMaps.ClassMap.Match, self).__setattr__(name, value)


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match"

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "netmask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.netmask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "netmask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match"

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "netmask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.netmask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "netmask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match"

                        self.name = YLeaf(YType.str, "name")

                        self.format = YLeaf(YType.str, "format")

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
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.DomainName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.DomainName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "domain-name" + "[name='" + self.name.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
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
                        if(name == "name" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match"

                        self.regex = YLeaf(YType.str, "regex")

                        self.format = YLeaf(YType.str, "format")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("regex",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.regex.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.regex.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "domain-name-regex" + "[regex='" + self.regex.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.regex.is_set or self.regex.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.regex.get_name_leafdata())
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
                        if(name == "regex" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "regex"):
                            self.regex = value
                            self.regex.value_namespace = name_space
                            self.regex.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.Match.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match"

                        self.flow_key = YLeafList(YType.str, "flow-key")

                        self.flow_cache = PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache()
                        self.flow_cache.parent = self
                        self._children_name_map["flow_cache"] = "flow-cache"
                        self._children_yang_names.add("flow-cache")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("flow_key") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.Match.Flow, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.Match.Flow, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, self).__init__()

                            self.yang_name = "flow-cache"
                            self.yang_parent_name = "flow"

                            self.idle_timeout = YLeaf(YType.str, "idle-timeout")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("idle_timeout") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache, self).__setattr__(name, value)

                        def has_data(self):
                            return self.idle_timeout.is_set

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.idle_timeout.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow-cache" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.idle_timeout.is_set or self.idle_timeout.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.idle_timeout.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "idle-timeout"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "idle-timeout"):
                                self.idle_timeout = value
                                self.idle_timeout.value_namespace = name_space
                                self.idle_timeout.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for leaf in self.flow_key.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (self.flow_cache is not None and self.flow_cache.has_data())

                    def has_operation(self):
                        for leaf in self.flow_key.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.flow_key.yfilter != YFilter.not_set or
                            (self.flow_cache is not None and self.flow_cache.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flow" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.flow_key.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "flow-cache"):
                            if (self.flow_cache is None):
                                self.flow_cache = PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache()
                                self.flow_cache.parent = self
                                self._children_name_map["flow_cache"] = "flow-cache"
                            return self.flow_cache

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow-cache" or name == "flow-key"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "flow-key"):
                            self.flow_key.append(value)

                def has_data(self):
                    for c in self.destination_address_ipv4:
                        if (c.has_data()):
                            return True
                    for c in self.destination_address_ipv6:
                        if (c.has_data()):
                            return True
                    for c in self.domain_name:
                        if (c.has_data()):
                            return True
                    for c in self.domain_name_regex:
                        if (c.has_data()):
                            return True
                    for c in self.source_address_ipv4:
                        if (c.has_data()):
                            return True
                    for c in self.source_address_ipv6:
                        if (c.has_data()):
                            return True
                    for leaf in self.circuit_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.circuit_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.cos.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.destination_mac.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.destination_port.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dhcp_client_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dhcp_client_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.discard_class.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ethertype.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.flow_tag.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.fragment_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.frame_relay_dlci.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv4_code.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv4_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv6_code.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv6_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.inner_cos.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.inner_vlan.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.mpls_experimental_imposition.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.mpls_experimental_topmost.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.protocol.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.qos_group.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.remote_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.remote_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.service_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.service_name_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.source_mac.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.source_port.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.timer.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.timer_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.traffic_class.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.user_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.user_name_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.vlan.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.atm_clp.is_set or
                        self.atm_oam.is_set or
                        self.authen_status.is_set or
                        self.cac_admit.is_set or
                        self.cac_unadmit.is_set or
                        self.dei.is_set or
                        self.dei_inner.is_set or
                        self.ethernet_services_acl.is_set or
                        self.fr_de.is_set or
                        self.ipv4_acl.is_set or
                        self.ipv6_acl.is_set or
                        self.mpls_disposition_ipv4_access_list.is_set or
                        self.mpls_disposition_ipv6_access_list.is_set or
                        self.tcp_flag.is_set or
                        self.vpls_broadcast.is_set or
                        self.vpls_control.is_set or
                        self.vpls_known.is_set or
                        self.vpls_multicast.is_set or
                        self.vpls_unknown.is_set or
                        (self.flow is not None and self.flow.has_data()))

                def has_operation(self):
                    for c in self.destination_address_ipv4:
                        if (c.has_operation()):
                            return True
                    for c in self.destination_address_ipv6:
                        if (c.has_operation()):
                            return True
                    for c in self.domain_name:
                        if (c.has_operation()):
                            return True
                    for c in self.domain_name_regex:
                        if (c.has_operation()):
                            return True
                    for c in self.source_address_ipv4:
                        if (c.has_operation()):
                            return True
                    for c in self.source_address_ipv6:
                        if (c.has_operation()):
                            return True
                    for leaf in self.circuit_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.circuit_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.cos.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.destination_mac.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.destination_port.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dhcp_client_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dhcp_client_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.discard_class.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ethertype.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.flow_tag.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.fragment_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.frame_relay_dlci.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv4_code.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv4_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv6_code.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv6_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.inner_cos.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.inner_vlan.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.mpls_experimental_imposition.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.mpls_experimental_topmost.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.protocol.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.qos_group.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.remote_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.remote_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.service_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.service_name_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.source_mac.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.source_port.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.timer.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.timer_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.traffic_class.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.user_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.user_name_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.vlan.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.atm_clp.yfilter != YFilter.not_set or
                        self.atm_oam.yfilter != YFilter.not_set or
                        self.authen_status.yfilter != YFilter.not_set or
                        self.cac_admit.yfilter != YFilter.not_set or
                        self.cac_unadmit.yfilter != YFilter.not_set or
                        self.circuit_id.yfilter != YFilter.not_set or
                        self.circuit_id_regex.yfilter != YFilter.not_set or
                        self.cos.yfilter != YFilter.not_set or
                        self.dei.yfilter != YFilter.not_set or
                        self.dei_inner.yfilter != YFilter.not_set or
                        self.destination_mac.yfilter != YFilter.not_set or
                        self.destination_port.yfilter != YFilter.not_set or
                        self.dhcp_client_id.yfilter != YFilter.not_set or
                        self.dhcp_client_id_regex.yfilter != YFilter.not_set or
                        self.discard_class.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.ethernet_services_acl.yfilter != YFilter.not_set or
                        self.ethertype.yfilter != YFilter.not_set or
                        self.flow_tag.yfilter != YFilter.not_set or
                        self.fr_de.yfilter != YFilter.not_set or
                        self.fragment_type.yfilter != YFilter.not_set or
                        self.frame_relay_dlci.yfilter != YFilter.not_set or
                        self.icmpv4_code.yfilter != YFilter.not_set or
                        self.icmpv4_type.yfilter != YFilter.not_set or
                        self.icmpv6_code.yfilter != YFilter.not_set or
                        self.icmpv6_type.yfilter != YFilter.not_set or
                        self.inner_cos.yfilter != YFilter.not_set or
                        self.inner_vlan.yfilter != YFilter.not_set or
                        self.ipv4_acl.yfilter != YFilter.not_set or
                        self.ipv4_dscp.yfilter != YFilter.not_set or
                        self.ipv4_packet_length.yfilter != YFilter.not_set or
                        self.ipv4_precedence.yfilter != YFilter.not_set or
                        self.ipv6_acl.yfilter != YFilter.not_set or
                        self.ipv6_dscp.yfilter != YFilter.not_set or
                        self.ipv6_packet_length.yfilter != YFilter.not_set or
                        self.ipv6_precedence.yfilter != YFilter.not_set or
                        self.mpls_disposition_ipv4_access_list.yfilter != YFilter.not_set or
                        self.mpls_disposition_ipv6_access_list.yfilter != YFilter.not_set or
                        self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                        self.mpls_experimental_topmost.yfilter != YFilter.not_set or
                        self.packet_length.yfilter != YFilter.not_set or
                        self.precedence.yfilter != YFilter.not_set or
                        self.protocol.yfilter != YFilter.not_set or
                        self.qos_group.yfilter != YFilter.not_set or
                        self.remote_id.yfilter != YFilter.not_set or
                        self.remote_id_regex.yfilter != YFilter.not_set or
                        self.service_name.yfilter != YFilter.not_set or
                        self.service_name_regex.yfilter != YFilter.not_set or
                        self.source_mac.yfilter != YFilter.not_set or
                        self.source_port.yfilter != YFilter.not_set or
                        self.tcp_flag.yfilter != YFilter.not_set or
                        self.timer.yfilter != YFilter.not_set or
                        self.timer_regex.yfilter != YFilter.not_set or
                        self.traffic_class.yfilter != YFilter.not_set or
                        self.user_name.yfilter != YFilter.not_set or
                        self.user_name_regex.yfilter != YFilter.not_set or
                        self.vlan.yfilter != YFilter.not_set or
                        self.vpls_broadcast.yfilter != YFilter.not_set or
                        self.vpls_control.yfilter != YFilter.not_set or
                        self.vpls_known.yfilter != YFilter.not_set or
                        self.vpls_multicast.yfilter != YFilter.not_set or
                        self.vpls_unknown.yfilter != YFilter.not_set or
                        (self.flow is not None and self.flow.has_operation()))

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
                    if (self.atm_clp.is_set or self.atm_clp.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.atm_clp.get_name_leafdata())
                    if (self.atm_oam.is_set or self.atm_oam.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.atm_oam.get_name_leafdata())
                    if (self.authen_status.is_set or self.authen_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_status.get_name_leafdata())
                    if (self.cac_admit.is_set or self.cac_admit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cac_admit.get_name_leafdata())
                    if (self.cac_unadmit.is_set or self.cac_unadmit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.cac_unadmit.get_name_leafdata())
                    if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei.get_name_leafdata())
                    if (self.dei_inner.is_set or self.dei_inner.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei_inner.get_name_leafdata())
                    if (self.ethernet_services_acl.is_set or self.ethernet_services_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ethernet_services_acl.get_name_leafdata())
                    if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fr_de.get_name_leafdata())
                    if (self.ipv4_acl.is_set or self.ipv4_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_acl.get_name_leafdata())
                    if (self.ipv6_acl.is_set or self.ipv6_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_acl.get_name_leafdata())
                    if (self.mpls_disposition_ipv4_access_list.is_set or self.mpls_disposition_ipv4_access_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_disposition_ipv4_access_list.get_name_leafdata())
                    if (self.mpls_disposition_ipv6_access_list.is_set or self.mpls_disposition_ipv6_access_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_disposition_ipv6_access_list.get_name_leafdata())
                    if (self.tcp_flag.is_set or self.tcp_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tcp_flag.get_name_leafdata())
                    if (self.vpls_broadcast.is_set or self.vpls_broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_broadcast.get_name_leafdata())
                    if (self.vpls_control.is_set or self.vpls_control.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_control.get_name_leafdata())
                    if (self.vpls_known.is_set or self.vpls_known.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_known.get_name_leafdata())
                    if (self.vpls_multicast.is_set or self.vpls_multicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_multicast.get_name_leafdata())
                    if (self.vpls_unknown.is_set or self.vpls_unknown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_unknown.get_name_leafdata())

                    leaf_name_data.extend(self.circuit_id.get_name_leafdata())

                    leaf_name_data.extend(self.circuit_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.cos.get_name_leafdata())

                    leaf_name_data.extend(self.destination_mac.get_name_leafdata())

                    leaf_name_data.extend(self.destination_port.get_name_leafdata())

                    leaf_name_data.extend(self.dhcp_client_id.get_name_leafdata())

                    leaf_name_data.extend(self.dhcp_client_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.discard_class.get_name_leafdata())

                    leaf_name_data.extend(self.dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ethertype.get_name_leafdata())

                    leaf_name_data.extend(self.flow_tag.get_name_leafdata())

                    leaf_name_data.extend(self.fragment_type.get_name_leafdata())

                    leaf_name_data.extend(self.frame_relay_dlci.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv4_code.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv4_type.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv6_code.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv6_type.get_name_leafdata())

                    leaf_name_data.extend(self.inner_cos.get_name_leafdata())

                    leaf_name_data.extend(self.inner_vlan.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_precedence.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_precedence.get_name_leafdata())

                    leaf_name_data.extend(self.mpls_experimental_imposition.get_name_leafdata())

                    leaf_name_data.extend(self.mpls_experimental_topmost.get_name_leafdata())

                    leaf_name_data.extend(self.packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.precedence.get_name_leafdata())

                    leaf_name_data.extend(self.protocol.get_name_leafdata())

                    leaf_name_data.extend(self.qos_group.get_name_leafdata())

                    leaf_name_data.extend(self.remote_id.get_name_leafdata())

                    leaf_name_data.extend(self.remote_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.service_name.get_name_leafdata())

                    leaf_name_data.extend(self.service_name_regex.get_name_leafdata())

                    leaf_name_data.extend(self.source_mac.get_name_leafdata())

                    leaf_name_data.extend(self.source_port.get_name_leafdata())

                    leaf_name_data.extend(self.timer.get_name_leafdata())

                    leaf_name_data.extend(self.timer_regex.get_name_leafdata())

                    leaf_name_data.extend(self.traffic_class.get_name_leafdata())

                    leaf_name_data.extend(self.user_name.get_name_leafdata())

                    leaf_name_data.extend(self.user_name_regex.get_name_leafdata())

                    leaf_name_data.extend(self.vlan.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "destination-address-ipv4"):
                        for c in self.destination_address_ipv4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_address_ipv4.append(c)
                        return c

                    if (child_yang_name == "destination-address-ipv6"):
                        for c in self.destination_address_ipv6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_address_ipv6.append(c)
                        return c

                    if (child_yang_name == "domain-name"):
                        for c in self.domain_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.DomainName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.domain_name.append(c)
                        return c

                    if (child_yang_name == "domain-name-regex"):
                        for c in self.domain_name_regex:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.DomainNameRegex()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.domain_name_regex.append(c)
                        return c

                    if (child_yang_name == "flow"):
                        if (self.flow is None):
                            self.flow = PolicyManager.ClassMaps.ClassMap.Match.Flow()
                            self.flow.parent = self
                            self._children_name_map["flow"] = "flow"
                        return self.flow

                    if (child_yang_name == "source-address-ipv4"):
                        for c in self.source_address_ipv4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.source_address_ipv4.append(c)
                        return c

                    if (child_yang_name == "source-address-ipv6"):
                        for c in self.source_address_ipv6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.source_address_ipv6.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-address-ipv4" or name == "destination-address-ipv6" or name == "domain-name" or name == "domain-name-regex" or name == "flow" or name == "source-address-ipv4" or name == "source-address-ipv6" or name == "atm-clp" or name == "atm-oam" or name == "authen-status" or name == "cac-admit" or name == "cac-unadmit" or name == "circuit-id" or name == "circuit-id-regex" or name == "cos" or name == "dei" or name == "dei-inner" or name == "destination-mac" or name == "destination-port" or name == "dhcp-client-id" or name == "dhcp-client-id-regex" or name == "discard-class" or name == "dscp" or name == "ethernet-services-acl" or name == "ethertype" or name == "flow-tag" or name == "fr-de" or name == "fragment-type" or name == "frame-relay-dlci" or name == "icmpv4-code" or name == "icmpv4-type" or name == "icmpv6-code" or name == "icmpv6-type" or name == "inner-cos" or name == "inner-vlan" or name == "ipv4-acl" or name == "ipv4-dscp" or name == "ipv4-packet-length" or name == "ipv4-precedence" or name == "ipv6-acl" or name == "ipv6-dscp" or name == "ipv6-packet-length" or name == "ipv6-precedence" or name == "mpls-disposition-ipv4-access-list" or name == "mpls-disposition-ipv6-access-list" or name == "mpls-experimental-imposition" or name == "mpls-experimental-topmost" or name == "packet-length" or name == "precedence" or name == "protocol" or name == "qos-group" or name == "remote-id" or name == "remote-id-regex" or name == "service-name" or name == "service-name-regex" or name == "source-mac" or name == "source-port" or name == "tcp-flag" or name == "timer" or name == "timer-regex" or name == "traffic-class" or name == "user-name" or name == "user-name-regex" or name == "vlan" or name == "vpls-broadcast" or name == "vpls-control" or name == "vpls-known" or name == "vpls-multicast" or name == "vpls-unknown"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "atm-clp"):
                        self.atm_clp = value
                        self.atm_clp.value_namespace = name_space
                        self.atm_clp.value_namespace_prefix = name_space_prefix
                    if(value_path == "atm-oam"):
                        self.atm_oam = value
                        self.atm_oam.value_namespace = name_space
                        self.atm_oam.value_namespace_prefix = name_space_prefix
                    if(value_path == "authen-status"):
                        self.authen_status = value
                        self.authen_status.value_namespace = name_space
                        self.authen_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "cac-admit"):
                        self.cac_admit = value
                        self.cac_admit.value_namespace = name_space
                        self.cac_admit.value_namespace_prefix = name_space_prefix
                    if(value_path == "cac-unadmit"):
                        self.cac_unadmit = value
                        self.cac_unadmit.value_namespace = name_space
                        self.cac_unadmit.value_namespace_prefix = name_space_prefix
                    if(value_path == "circuit-id"):
                        self.circuit_id.append(value)
                    if(value_path == "circuit-id-regex"):
                        self.circuit_id_regex.append(value)
                    if(value_path == "cos"):
                        self.cos.append(value)
                    if(value_path == "dei"):
                        self.dei = value
                        self.dei.value_namespace = name_space
                        self.dei.value_namespace_prefix = name_space_prefix
                    if(value_path == "dei-inner"):
                        self.dei_inner = value
                        self.dei_inner.value_namespace = name_space
                        self.dei_inner.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-mac"):
                        self.destination_mac.append(value)
                    if(value_path == "destination-port"):
                        self.destination_port.append(value)
                    if(value_path == "dhcp-client-id"):
                        self.dhcp_client_id.append(value)
                    if(value_path == "dhcp-client-id-regex"):
                        self.dhcp_client_id_regex.append(value)
                    if(value_path == "discard-class"):
                        self.discard_class.append(value)
                    if(value_path == "dscp"):
                        self.dscp.append(value)
                    if(value_path == "ethernet-services-acl"):
                        self.ethernet_services_acl = value
                        self.ethernet_services_acl.value_namespace = name_space
                        self.ethernet_services_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ethertype"):
                        self.ethertype.append(value)
                    if(value_path == "flow-tag"):
                        self.flow_tag.append(value)
                    if(value_path == "fr-de"):
                        self.fr_de = value
                        self.fr_de.value_namespace = name_space
                        self.fr_de.value_namespace_prefix = name_space_prefix
                    if(value_path == "fragment-type"):
                        self.fragment_type.append(value)
                    if(value_path == "frame-relay-dlci"):
                        self.frame_relay_dlci.append(value)
                    if(value_path == "icmpv4-code"):
                        self.icmpv4_code.append(value)
                    if(value_path == "icmpv4-type"):
                        self.icmpv4_type.append(value)
                    if(value_path == "icmpv6-code"):
                        self.icmpv6_code.append(value)
                    if(value_path == "icmpv6-type"):
                        self.icmpv6_type.append(value)
                    if(value_path == "inner-cos"):
                        self.inner_cos.append(value)
                    if(value_path == "inner-vlan"):
                        self.inner_vlan.append(value)
                    if(value_path == "ipv4-acl"):
                        self.ipv4_acl = value
                        self.ipv4_acl.value_namespace = name_space
                        self.ipv4_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-dscp"):
                        self.ipv4_dscp.append(value)
                    if(value_path == "ipv4-packet-length"):
                        self.ipv4_packet_length.append(value)
                    if(value_path == "ipv4-precedence"):
                        self.ipv4_precedence.append(value)
                    if(value_path == "ipv6-acl"):
                        self.ipv6_acl = value
                        self.ipv6_acl.value_namespace = name_space
                        self.ipv6_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-dscp"):
                        self.ipv6_dscp.append(value)
                    if(value_path == "ipv6-packet-length"):
                        self.ipv6_packet_length.append(value)
                    if(value_path == "ipv6-precedence"):
                        self.ipv6_precedence.append(value)
                    if(value_path == "mpls-disposition-ipv4-access-list"):
                        self.mpls_disposition_ipv4_access_list = value
                        self.mpls_disposition_ipv4_access_list.value_namespace = name_space
                        self.mpls_disposition_ipv4_access_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-disposition-ipv6-access-list"):
                        self.mpls_disposition_ipv6_access_list = value
                        self.mpls_disposition_ipv6_access_list.value_namespace = name_space
                        self.mpls_disposition_ipv6_access_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-experimental-imposition"):
                        self.mpls_experimental_imposition.append(value)
                    if(value_path == "mpls-experimental-topmost"):
                        self.mpls_experimental_topmost.append(value)
                    if(value_path == "packet-length"):
                        self.packet_length.append(value)
                    if(value_path == "precedence"):
                        self.precedence.append(value)
                    if(value_path == "protocol"):
                        self.protocol.append(value)
                    if(value_path == "qos-group"):
                        self.qos_group.append(value)
                    if(value_path == "remote-id"):
                        self.remote_id.append(value)
                    if(value_path == "remote-id-regex"):
                        self.remote_id_regex.append(value)
                    if(value_path == "service-name"):
                        self.service_name.append(value)
                    if(value_path == "service-name-regex"):
                        self.service_name_regex.append(value)
                    if(value_path == "source-mac"):
                        self.source_mac.append(value)
                    if(value_path == "source-port"):
                        self.source_port.append(value)
                    if(value_path == "tcp-flag"):
                        self.tcp_flag = value
                        self.tcp_flag.value_namespace = name_space
                        self.tcp_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "timer"):
                        self.timer.append(value)
                    if(value_path == "timer-regex"):
                        self.timer_regex.append(value)
                    if(value_path == "traffic-class"):
                        self.traffic_class.append(value)
                    if(value_path == "user-name"):
                        self.user_name.append(value)
                    if(value_path == "user-name-regex"):
                        self.user_name_regex.append(value)
                    if(value_path == "vlan"):
                        self.vlan.append(value)
                    if(value_path == "vpls-broadcast"):
                        self.vpls_broadcast = value
                        self.vpls_broadcast.value_namespace = name_space
                        self.vpls_broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-control"):
                        self.vpls_control = value
                        self.vpls_control.value_namespace = name_space
                        self.vpls_control.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-known"):
                        self.vpls_known = value
                        self.vpls_known.value_namespace = name_space
                        self.vpls_known.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-multicast"):
                        self.vpls_multicast = value
                        self.vpls_multicast.value_namespace = name_space
                        self.vpls_multicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-unknown"):
                        self.vpls_unknown = value
                        self.vpls_unknown.value_namespace = name_space
                        self.vpls_unknown.value_namespace_prefix = name_space_prefix


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
                	**type**\:  list of str
                
                	**length:** 1..32
                
                .. attribute:: dhcp_client_id_regex
                
                	Match dhcp client id regex
                	**type**\:  list of str
                
                	**length:** 1..32
                
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
                _revision = '2017-03-03'

                def __init__(self):
                    super(PolicyManager.ClassMaps.ClassMap.MatchNot, self).__init__()

                    self.yang_name = "match-not"
                    self.yang_parent_name = "class-map"

                    self.authen_status = YLeaf(YType.str, "authen-status")

                    self.circuit_id = YLeafList(YType.str, "circuit-id")

                    self.circuit_id_regex = YLeafList(YType.str, "circuit-id-regex")

                    self.cos = YLeafList(YType.uint8, "cos")

                    self.dei = YLeaf(YType.uint8, "dei")

                    self.dei_inner = YLeaf(YType.uint8, "dei-inner")

                    self.destination_mac = YLeafList(YType.str, "destination-mac")

                    self.destination_port = YLeafList(YType.str, "destination-port")

                    self.dhcp_client_id = YLeafList(YType.str, "dhcp-client-id")

                    self.dhcp_client_id_regex = YLeafList(YType.str, "dhcp-client-id-regex")

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
                    self.domain_name = YList(self)
                    self.domain_name_regex = YList(self)
                    self.source_address_ipv4 = YList(self)
                    self.source_address_ipv6 = YList(self)

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("authen_status",
                                    "circuit_id",
                                    "circuit_id_regex",
                                    "cos",
                                    "dei",
                                    "dei_inner",
                                    "destination_mac",
                                    "destination_port",
                                    "dhcp_client_id",
                                    "dhcp_client_id_regex",
                                    "discard_class",
                                    "dscp",
                                    "ethernet_services_acl",
                                    "ethertype",
                                    "flow_tag",
                                    "fr_de",
                                    "fragment_type",
                                    "frame_relay_dlci",
                                    "icmpv4_code",
                                    "icmpv4_type",
                                    "icmpv6_code",
                                    "icmpv6_type",
                                    "inner_cos",
                                    "inner_vlan",
                                    "ipv4_acl",
                                    "ipv4_dscp",
                                    "ipv4_packet_length",
                                    "ipv4_precedence",
                                    "ipv6_acl",
                                    "ipv6_dscp",
                                    "ipv6_packet_length",
                                    "ipv6_precedence",
                                    "mpls_disposition_ipv4_access_list",
                                    "mpls_disposition_ipv6_access_list",
                                    "mpls_experimental_imposition",
                                    "mpls_experimental_topmost",
                                    "packet_length",
                                    "precedence",
                                    "protocol",
                                    "qos_group",
                                    "remote_id",
                                    "remote_id_regex",
                                    "service_name",
                                    "service_name_regex",
                                    "source_mac",
                                    "source_port",
                                    "tcp_flag",
                                    "timer",
                                    "timer_regex",
                                    "traffic_class",
                                    "user_name",
                                    "user_name_regex",
                                    "vlan",
                                    "vpls_broadcast",
                                    "vpls_control",
                                    "vpls_known",
                                    "vpls_multicast",
                                    "vpls_unknown") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PolicyManager.ClassMaps.ClassMap.MatchNot, self).__setattr__(name, value)


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, self).__init__()

                        self.yang_name = "destination-address-ipv4"
                        self.yang_parent_name = "match-not"

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "netmask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.netmask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "netmask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, self).__init__()

                        self.yang_name = "destination-address-ipv6"
                        self.yang_parent_name = "match-not"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, self).__init__()

                        self.yang_name = "source-address-ipv4"
                        self.yang_parent_name = "match-not"

                        self.address = YLeaf(YType.str, "address")

                        self.netmask = YLeaf(YType.str, "netmask")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "netmask") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.netmask.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.netmask.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-address-ipv4" + "[address='" + self.address.get() + "']" + "[netmask='" + self.netmask.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.netmask.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "netmask"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "netmask"):
                            self.netmask = value
                            self.netmask.value_namespace = name_space
                            self.netmask.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, self).__init__()

                        self.yang_name = "source-address-ipv6"
                        self.yang_parent_name = "match-not"

                        self.address = YLeaf(YType.str, "address")

                        self.prefix_length = YLeaf(YType.uint8, "prefix-length")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("address",
                                        "prefix_length") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.address.is_set or
                            self.prefix_length.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.address.yfilter != YFilter.not_set or
                            self.prefix_length.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "source-address-ipv6" + "[address='" + self.address.get() + "']" + "[prefix-length='" + self.prefix_length.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.address.get_name_leafdata())
                        if (self.prefix_length.is_set or self.prefix_length.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefix_length.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "address" or name == "prefix-length"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "address"):
                            self.address = value
                            self.address.value_namespace = name_space
                            self.address.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefix-length"):
                            self.prefix_length = value
                            self.prefix_length.value_namespace = name_space
                            self.prefix_length.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, self).__init__()

                        self.yang_name = "domain-name"
                        self.yang_parent_name = "match-not"

                        self.name = YLeaf(YType.str, "name")

                        self.format = YLeaf(YType.str, "format")

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
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.name.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "domain-name" + "[name='" + self.name.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
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
                        if(name == "name" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, self).__init__()

                        self.yang_name = "domain-name-regex"
                        self.yang_parent_name = "match-not"

                        self.regex = YLeaf(YType.str, "regex")

                        self.format = YLeaf(YType.str, "format")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("regex",
                                        "format") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.regex.is_set or
                            self.format.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.regex.yfilter != YFilter.not_set or
                            self.format.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "domain-name-regex" + "[regex='" + self.regex.get() + "']" + "[format='" + self.format.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.regex.is_set or self.regex.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.regex.get_name_leafdata())
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
                        if(name == "regex" or name == "format"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "regex"):
                            self.regex = value
                            self.regex.value_namespace = name_space
                            self.regex.value_namespace_prefix = name_space_prefix
                        if(value_path == "format"):
                            self.format = value
                            self.format.value_namespace = name_space
                            self.format.value_namespace_prefix = name_space_prefix


                class Flow(Entity):
                    """
                    Match flow.
                    
                    .. attribute:: flow_tag
                    
                    	Configure the flow\-tag parameters
                    	**type**\:  list of int
                    
                    	**range:** 1..63
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, self).__init__()

                        self.yang_name = "flow"
                        self.yang_parent_name = "match-not"

                        self.flow_tag = YLeafList(YType.uint16, "flow-tag")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("flow_tag") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.ClassMaps.ClassMap.MatchNot.Flow, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.flow_tag.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return False

                    def has_operation(self):
                        for leaf in self.flow_tag.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.flow_tag.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flow" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()

                        leaf_name_data.extend(self.flow_tag.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow-tag"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "flow-tag"):
                            self.flow_tag.append(value)

                def has_data(self):
                    for c in self.destination_address_ipv4:
                        if (c.has_data()):
                            return True
                    for c in self.destination_address_ipv6:
                        if (c.has_data()):
                            return True
                    for c in self.domain_name:
                        if (c.has_data()):
                            return True
                    for c in self.domain_name_regex:
                        if (c.has_data()):
                            return True
                    for c in self.source_address_ipv4:
                        if (c.has_data()):
                            return True
                    for c in self.source_address_ipv6:
                        if (c.has_data()):
                            return True
                    for leaf in self.circuit_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.circuit_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.cos.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.destination_mac.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.destination_port.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dhcp_client_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dhcp_client_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.discard_class.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ethertype.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.flow_tag.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.fragment_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.frame_relay_dlci.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv4_code.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv4_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv6_code.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.icmpv6_type.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.inner_cos.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.inner_vlan.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv4_precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_dscp.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.ipv6_precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.mpls_experimental_imposition.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.mpls_experimental_topmost.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.packet_length.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.precedence.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.protocol.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.qos_group.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.remote_id.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.remote_id_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.service_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.service_name_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.source_mac.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.source_port.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.timer.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.timer_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.traffic_class.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.user_name.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.user_name_regex.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    for leaf in self.vlan.getYLeafs():
                        if (leaf.yfilter != YFilter.not_set):
                            return True
                    return (
                        self.authen_status.is_set or
                        self.dei.is_set or
                        self.dei_inner.is_set or
                        self.ethernet_services_acl.is_set or
                        self.fr_de.is_set or
                        self.ipv4_acl.is_set or
                        self.ipv6_acl.is_set or
                        self.mpls_disposition_ipv4_access_list.is_set or
                        self.mpls_disposition_ipv6_access_list.is_set or
                        self.tcp_flag.is_set or
                        self.vpls_broadcast.is_set or
                        self.vpls_control.is_set or
                        self.vpls_known.is_set or
                        self.vpls_multicast.is_set or
                        self.vpls_unknown.is_set or
                        (self.flow is not None and self.flow.has_data()))

                def has_operation(self):
                    for c in self.destination_address_ipv4:
                        if (c.has_operation()):
                            return True
                    for c in self.destination_address_ipv6:
                        if (c.has_operation()):
                            return True
                    for c in self.domain_name:
                        if (c.has_operation()):
                            return True
                    for c in self.domain_name_regex:
                        if (c.has_operation()):
                            return True
                    for c in self.source_address_ipv4:
                        if (c.has_operation()):
                            return True
                    for c in self.source_address_ipv6:
                        if (c.has_operation()):
                            return True
                    for leaf in self.circuit_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.circuit_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.cos.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.destination_mac.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.destination_port.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dhcp_client_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dhcp_client_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.discard_class.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ethertype.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.flow_tag.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.fragment_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.frame_relay_dlci.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv4_code.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv4_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv6_code.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.icmpv6_type.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.inner_cos.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.inner_vlan.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv4_precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_dscp.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.ipv6_precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.mpls_experimental_imposition.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.mpls_experimental_topmost.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.packet_length.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.precedence.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.protocol.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.qos_group.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.remote_id.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.remote_id_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.service_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.service_name_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.source_mac.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.source_port.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.timer.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.timer_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.traffic_class.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.user_name.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.user_name_regex.getYLeafs():
                        if (leaf.is_set):
                            return True
                    for leaf in self.vlan.getYLeafs():
                        if (leaf.is_set):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.authen_status.yfilter != YFilter.not_set or
                        self.circuit_id.yfilter != YFilter.not_set or
                        self.circuit_id_regex.yfilter != YFilter.not_set or
                        self.cos.yfilter != YFilter.not_set or
                        self.dei.yfilter != YFilter.not_set or
                        self.dei_inner.yfilter != YFilter.not_set or
                        self.destination_mac.yfilter != YFilter.not_set or
                        self.destination_port.yfilter != YFilter.not_set or
                        self.dhcp_client_id.yfilter != YFilter.not_set or
                        self.dhcp_client_id_regex.yfilter != YFilter.not_set or
                        self.discard_class.yfilter != YFilter.not_set or
                        self.dscp.yfilter != YFilter.not_set or
                        self.ethernet_services_acl.yfilter != YFilter.not_set or
                        self.ethertype.yfilter != YFilter.not_set or
                        self.flow_tag.yfilter != YFilter.not_set or
                        self.fr_de.yfilter != YFilter.not_set or
                        self.fragment_type.yfilter != YFilter.not_set or
                        self.frame_relay_dlci.yfilter != YFilter.not_set or
                        self.icmpv4_code.yfilter != YFilter.not_set or
                        self.icmpv4_type.yfilter != YFilter.not_set or
                        self.icmpv6_code.yfilter != YFilter.not_set or
                        self.icmpv6_type.yfilter != YFilter.not_set or
                        self.inner_cos.yfilter != YFilter.not_set or
                        self.inner_vlan.yfilter != YFilter.not_set or
                        self.ipv4_acl.yfilter != YFilter.not_set or
                        self.ipv4_dscp.yfilter != YFilter.not_set or
                        self.ipv4_packet_length.yfilter != YFilter.not_set or
                        self.ipv4_precedence.yfilter != YFilter.not_set or
                        self.ipv6_acl.yfilter != YFilter.not_set or
                        self.ipv6_dscp.yfilter != YFilter.not_set or
                        self.ipv6_packet_length.yfilter != YFilter.not_set or
                        self.ipv6_precedence.yfilter != YFilter.not_set or
                        self.mpls_disposition_ipv4_access_list.yfilter != YFilter.not_set or
                        self.mpls_disposition_ipv6_access_list.yfilter != YFilter.not_set or
                        self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                        self.mpls_experimental_topmost.yfilter != YFilter.not_set or
                        self.packet_length.yfilter != YFilter.not_set or
                        self.precedence.yfilter != YFilter.not_set or
                        self.protocol.yfilter != YFilter.not_set or
                        self.qos_group.yfilter != YFilter.not_set or
                        self.remote_id.yfilter != YFilter.not_set or
                        self.remote_id_regex.yfilter != YFilter.not_set or
                        self.service_name.yfilter != YFilter.not_set or
                        self.service_name_regex.yfilter != YFilter.not_set or
                        self.source_mac.yfilter != YFilter.not_set or
                        self.source_port.yfilter != YFilter.not_set or
                        self.tcp_flag.yfilter != YFilter.not_set or
                        self.timer.yfilter != YFilter.not_set or
                        self.timer_regex.yfilter != YFilter.not_set or
                        self.traffic_class.yfilter != YFilter.not_set or
                        self.user_name.yfilter != YFilter.not_set or
                        self.user_name_regex.yfilter != YFilter.not_set or
                        self.vlan.yfilter != YFilter.not_set or
                        self.vpls_broadcast.yfilter != YFilter.not_set or
                        self.vpls_control.yfilter != YFilter.not_set or
                        self.vpls_known.yfilter != YFilter.not_set or
                        self.vpls_multicast.yfilter != YFilter.not_set or
                        self.vpls_unknown.yfilter != YFilter.not_set or
                        (self.flow is not None and self.flow.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "match-not" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.authen_status.is_set or self.authen_status.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.authen_status.get_name_leafdata())
                    if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei.get_name_leafdata())
                    if (self.dei_inner.is_set or self.dei_inner.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.dei_inner.get_name_leafdata())
                    if (self.ethernet_services_acl.is_set or self.ethernet_services_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ethernet_services_acl.get_name_leafdata())
                    if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fr_de.get_name_leafdata())
                    if (self.ipv4_acl.is_set or self.ipv4_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv4_acl.get_name_leafdata())
                    if (self.ipv6_acl.is_set or self.ipv6_acl.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ipv6_acl.get_name_leafdata())
                    if (self.mpls_disposition_ipv4_access_list.is_set or self.mpls_disposition_ipv4_access_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_disposition_ipv4_access_list.get_name_leafdata())
                    if (self.mpls_disposition_ipv6_access_list.is_set or self.mpls_disposition_ipv6_access_list.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mpls_disposition_ipv6_access_list.get_name_leafdata())
                    if (self.tcp_flag.is_set or self.tcp_flag.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tcp_flag.get_name_leafdata())
                    if (self.vpls_broadcast.is_set or self.vpls_broadcast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_broadcast.get_name_leafdata())
                    if (self.vpls_control.is_set or self.vpls_control.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_control.get_name_leafdata())
                    if (self.vpls_known.is_set or self.vpls_known.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_known.get_name_leafdata())
                    if (self.vpls_multicast.is_set or self.vpls_multicast.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_multicast.get_name_leafdata())
                    if (self.vpls_unknown.is_set or self.vpls_unknown.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.vpls_unknown.get_name_leafdata())

                    leaf_name_data.extend(self.circuit_id.get_name_leafdata())

                    leaf_name_data.extend(self.circuit_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.cos.get_name_leafdata())

                    leaf_name_data.extend(self.destination_mac.get_name_leafdata())

                    leaf_name_data.extend(self.destination_port.get_name_leafdata())

                    leaf_name_data.extend(self.dhcp_client_id.get_name_leafdata())

                    leaf_name_data.extend(self.dhcp_client_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.discard_class.get_name_leafdata())

                    leaf_name_data.extend(self.dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ethertype.get_name_leafdata())

                    leaf_name_data.extend(self.flow_tag.get_name_leafdata())

                    leaf_name_data.extend(self.fragment_type.get_name_leafdata())

                    leaf_name_data.extend(self.frame_relay_dlci.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv4_code.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv4_type.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv6_code.get_name_leafdata())

                    leaf_name_data.extend(self.icmpv6_type.get_name_leafdata())

                    leaf_name_data.extend(self.inner_cos.get_name_leafdata())

                    leaf_name_data.extend(self.inner_vlan.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.ipv4_precedence.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_dscp.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.ipv6_precedence.get_name_leafdata())

                    leaf_name_data.extend(self.mpls_experimental_imposition.get_name_leafdata())

                    leaf_name_data.extend(self.mpls_experimental_topmost.get_name_leafdata())

                    leaf_name_data.extend(self.packet_length.get_name_leafdata())

                    leaf_name_data.extend(self.precedence.get_name_leafdata())

                    leaf_name_data.extend(self.protocol.get_name_leafdata())

                    leaf_name_data.extend(self.qos_group.get_name_leafdata())

                    leaf_name_data.extend(self.remote_id.get_name_leafdata())

                    leaf_name_data.extend(self.remote_id_regex.get_name_leafdata())

                    leaf_name_data.extend(self.service_name.get_name_leafdata())

                    leaf_name_data.extend(self.service_name_regex.get_name_leafdata())

                    leaf_name_data.extend(self.source_mac.get_name_leafdata())

                    leaf_name_data.extend(self.source_port.get_name_leafdata())

                    leaf_name_data.extend(self.timer.get_name_leafdata())

                    leaf_name_data.extend(self.timer_regex.get_name_leafdata())

                    leaf_name_data.extend(self.traffic_class.get_name_leafdata())

                    leaf_name_data.extend(self.user_name.get_name_leafdata())

                    leaf_name_data.extend(self.user_name_regex.get_name_leafdata())

                    leaf_name_data.extend(self.vlan.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "destination-address-ipv4"):
                        for c in self.destination_address_ipv4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_address_ipv4.append(c)
                        return c

                    if (child_yang_name == "destination-address-ipv6"):
                        for c in self.destination_address_ipv6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.destination_address_ipv6.append(c)
                        return c

                    if (child_yang_name == "domain-name"):
                        for c in self.domain_name:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.domain_name.append(c)
                        return c

                    if (child_yang_name == "domain-name-regex"):
                        for c in self.domain_name_regex:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.DomainNameRegex()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.domain_name_regex.append(c)
                        return c

                    if (child_yang_name == "flow"):
                        if (self.flow is None):
                            self.flow = PolicyManager.ClassMaps.ClassMap.MatchNot.Flow()
                            self.flow.parent = self
                            self._children_name_map["flow"] = "flow"
                        return self.flow

                    if (child_yang_name == "source-address-ipv4"):
                        for c in self.source_address_ipv4:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.source_address_ipv4.append(c)
                        return c

                    if (child_yang_name == "source-address-ipv6"):
                        for c in self.source_address_ipv6:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.source_address_ipv6.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-address-ipv4" or name == "destination-address-ipv6" or name == "domain-name" or name == "domain-name-regex" or name == "flow" or name == "source-address-ipv4" or name == "source-address-ipv6" or name == "authen-status" or name == "circuit-id" or name == "circuit-id-regex" or name == "cos" or name == "dei" or name == "dei-inner" or name == "destination-mac" or name == "destination-port" or name == "dhcp-client-id" or name == "dhcp-client-id-regex" or name == "discard-class" or name == "dscp" or name == "ethernet-services-acl" or name == "ethertype" or name == "flow-tag" or name == "fr-de" or name == "fragment-type" or name == "frame-relay-dlci" or name == "icmpv4-code" or name == "icmpv4-type" or name == "icmpv6-code" or name == "icmpv6-type" or name == "inner-cos" or name == "inner-vlan" or name == "ipv4-acl" or name == "ipv4-dscp" or name == "ipv4-packet-length" or name == "ipv4-precedence" or name == "ipv6-acl" or name == "ipv6-dscp" or name == "ipv6-packet-length" or name == "ipv6-precedence" or name == "mpls-disposition-ipv4-access-list" or name == "mpls-disposition-ipv6-access-list" or name == "mpls-experimental-imposition" or name == "mpls-experimental-topmost" or name == "packet-length" or name == "precedence" or name == "protocol" or name == "qos-group" or name == "remote-id" or name == "remote-id-regex" or name == "service-name" or name == "service-name-regex" or name == "source-mac" or name == "source-port" or name == "tcp-flag" or name == "timer" or name == "timer-regex" or name == "traffic-class" or name == "user-name" or name == "user-name-regex" or name == "vlan" or name == "vpls-broadcast" or name == "vpls-control" or name == "vpls-known" or name == "vpls-multicast" or name == "vpls-unknown"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "authen-status"):
                        self.authen_status = value
                        self.authen_status.value_namespace = name_space
                        self.authen_status.value_namespace_prefix = name_space_prefix
                    if(value_path == "circuit-id"):
                        self.circuit_id.append(value)
                    if(value_path == "circuit-id-regex"):
                        self.circuit_id_regex.append(value)
                    if(value_path == "cos"):
                        self.cos.append(value)
                    if(value_path == "dei"):
                        self.dei = value
                        self.dei.value_namespace = name_space
                        self.dei.value_namespace_prefix = name_space_prefix
                    if(value_path == "dei-inner"):
                        self.dei_inner = value
                        self.dei_inner.value_namespace = name_space
                        self.dei_inner.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-mac"):
                        self.destination_mac.append(value)
                    if(value_path == "destination-port"):
                        self.destination_port.append(value)
                    if(value_path == "dhcp-client-id"):
                        self.dhcp_client_id.append(value)
                    if(value_path == "dhcp-client-id-regex"):
                        self.dhcp_client_id_regex.append(value)
                    if(value_path == "discard-class"):
                        self.discard_class.append(value)
                    if(value_path == "dscp"):
                        self.dscp.append(value)
                    if(value_path == "ethernet-services-acl"):
                        self.ethernet_services_acl = value
                        self.ethernet_services_acl.value_namespace = name_space
                        self.ethernet_services_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ethertype"):
                        self.ethertype.append(value)
                    if(value_path == "flow-tag"):
                        self.flow_tag.append(value)
                    if(value_path == "fr-de"):
                        self.fr_de = value
                        self.fr_de.value_namespace = name_space
                        self.fr_de.value_namespace_prefix = name_space_prefix
                    if(value_path == "fragment-type"):
                        self.fragment_type.append(value)
                    if(value_path == "frame-relay-dlci"):
                        self.frame_relay_dlci.append(value)
                    if(value_path == "icmpv4-code"):
                        self.icmpv4_code.append(value)
                    if(value_path == "icmpv4-type"):
                        self.icmpv4_type.append(value)
                    if(value_path == "icmpv6-code"):
                        self.icmpv6_code.append(value)
                    if(value_path == "icmpv6-type"):
                        self.icmpv6_type.append(value)
                    if(value_path == "inner-cos"):
                        self.inner_cos.append(value)
                    if(value_path == "inner-vlan"):
                        self.inner_vlan.append(value)
                    if(value_path == "ipv4-acl"):
                        self.ipv4_acl = value
                        self.ipv4_acl.value_namespace = name_space
                        self.ipv4_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv4-dscp"):
                        self.ipv4_dscp.append(value)
                    if(value_path == "ipv4-packet-length"):
                        self.ipv4_packet_length.append(value)
                    if(value_path == "ipv4-precedence"):
                        self.ipv4_precedence.append(value)
                    if(value_path == "ipv6-acl"):
                        self.ipv6_acl = value
                        self.ipv6_acl.value_namespace = name_space
                        self.ipv6_acl.value_namespace_prefix = name_space_prefix
                    if(value_path == "ipv6-dscp"):
                        self.ipv6_dscp.append(value)
                    if(value_path == "ipv6-packet-length"):
                        self.ipv6_packet_length.append(value)
                    if(value_path == "ipv6-precedence"):
                        self.ipv6_precedence.append(value)
                    if(value_path == "mpls-disposition-ipv4-access-list"):
                        self.mpls_disposition_ipv4_access_list = value
                        self.mpls_disposition_ipv4_access_list.value_namespace = name_space
                        self.mpls_disposition_ipv4_access_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-disposition-ipv6-access-list"):
                        self.mpls_disposition_ipv6_access_list = value
                        self.mpls_disposition_ipv6_access_list.value_namespace = name_space
                        self.mpls_disposition_ipv6_access_list.value_namespace_prefix = name_space_prefix
                    if(value_path == "mpls-experimental-imposition"):
                        self.mpls_experimental_imposition.append(value)
                    if(value_path == "mpls-experimental-topmost"):
                        self.mpls_experimental_topmost.append(value)
                    if(value_path == "packet-length"):
                        self.packet_length.append(value)
                    if(value_path == "precedence"):
                        self.precedence.append(value)
                    if(value_path == "protocol"):
                        self.protocol.append(value)
                    if(value_path == "qos-group"):
                        self.qos_group.append(value)
                    if(value_path == "remote-id"):
                        self.remote_id.append(value)
                    if(value_path == "remote-id-regex"):
                        self.remote_id_regex.append(value)
                    if(value_path == "service-name"):
                        self.service_name.append(value)
                    if(value_path == "service-name-regex"):
                        self.service_name_regex.append(value)
                    if(value_path == "source-mac"):
                        self.source_mac.append(value)
                    if(value_path == "source-port"):
                        self.source_port.append(value)
                    if(value_path == "tcp-flag"):
                        self.tcp_flag = value
                        self.tcp_flag.value_namespace = name_space
                        self.tcp_flag.value_namespace_prefix = name_space_prefix
                    if(value_path == "timer"):
                        self.timer.append(value)
                    if(value_path == "timer-regex"):
                        self.timer_regex.append(value)
                    if(value_path == "traffic-class"):
                        self.traffic_class.append(value)
                    if(value_path == "user-name"):
                        self.user_name.append(value)
                    if(value_path == "user-name-regex"):
                        self.user_name_regex.append(value)
                    if(value_path == "vlan"):
                        self.vlan.append(value)
                    if(value_path == "vpls-broadcast"):
                        self.vpls_broadcast = value
                        self.vpls_broadcast.value_namespace = name_space
                        self.vpls_broadcast.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-control"):
                        self.vpls_control = value
                        self.vpls_control.value_namespace = name_space
                        self.vpls_control.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-known"):
                        self.vpls_known = value
                        self.vpls_known.value_namespace = name_space
                        self.vpls_known.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-multicast"):
                        self.vpls_multicast = value
                        self.vpls_multicast.value_namespace = name_space
                        self.vpls_multicast.value_namespace_prefix = name_space_prefix
                    if(value_path == "vpls-unknown"):
                        self.vpls_unknown = value
                        self.vpls_unknown.value_namespace = name_space
                        self.vpls_unknown.value_namespace_prefix = name_space_prefix

            def has_data(self):
                return (
                    self.type.is_set or
                    self.name.is_set or
                    self.class_map_mode_match_all.is_set or
                    self.class_map_mode_match_any.is_set or
                    self.description.is_set or
                    (self.match is not None and self.match.has_data()) or
                    (self.match_not is not None and self.match_not.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.class_map_mode_match_all.yfilter != YFilter.not_set or
                    self.class_map_mode_match_any.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    (self.match is not None and self.match.has_operation()) or
                    (self.match_not is not None and self.match_not.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "class-map" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/class-maps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.class_map_mode_match_all.is_set or self.class_map_mode_match_all.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.class_map_mode_match_all.get_name_leafdata())
                if (self.class_map_mode_match_any.is_set or self.class_map_mode_match_any.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.class_map_mode_match_any.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "match"):
                    if (self.match is None):
                        self.match = PolicyManager.ClassMaps.ClassMap.Match()
                        self.match.parent = self
                        self._children_name_map["match"] = "match"
                    return self.match

                if (child_yang_name == "match-not"):
                    if (self.match_not is None):
                        self.match_not = PolicyManager.ClassMaps.ClassMap.MatchNot()
                        self.match_not.parent = self
                        self._children_name_map["match_not"] = "match-not"
                    return self.match_not

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "match" or name == "match-not" or name == "type" or name == "name" or name == "class-map-mode-match-all" or name == "class-map-mode-match-any" or name == "description"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "class-map-mode-match-all"):
                    self.class_map_mode_match_all = value
                    self.class_map_mode_match_all.value_namespace = name_space
                    self.class_map_mode_match_all.value_namespace_prefix = name_space_prefix
                if(value_path == "class-map-mode-match-any"):
                    self.class_map_mode_match_any = value
                    self.class_map_mode_match_any.value_namespace = name_space
                    self.class_map_mode_match_any.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.class_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.class_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "class-maps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "class-map"):
                for c in self.class_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PolicyManager.ClassMaps.ClassMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.class_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "class-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class PolicyMaps(Entity):
        """
        Policy\-maps configuration.
        
        .. attribute:: policy_map
        
        	Policy\-map configuration
        	**type**\: list of    :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap>`
        
        

        """

        _prefix = 'infra-policymgr-cfg'
        _revision = '2017-03-03'

        def __init__(self):
            super(PolicyManager.PolicyMaps, self).__init__()

            self.yang_name = "policy-maps"
            self.yang_parent_name = "policy-manager"

            self.policy_map = YList(self)

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
                        super(PolicyManager.PolicyMaps, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(PolicyManager.PolicyMaps, self).__setattr__(name, value)


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
            _revision = '2017-03-03'

            def __init__(self):
                super(PolicyManager.PolicyMaps.PolicyMap, self).__init__()

                self.yang_name = "policy-map"
                self.yang_parent_name = "policy-maps"

                self.type = YLeaf(YType.enumeration, "type")

                self.name = YLeaf(YType.str, "name")

                self.description = YLeaf(YType.str, "description")

                self.event = YList(self)
                self.policy_map_rule = YList(self)

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("type",
                                "name",
                                "description") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(PolicyManager.PolicyMaps.PolicyMap, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(PolicyManager.PolicyMaps.PolicyMap, self).__setattr__(name, value)


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
                _revision = '2017-03-03'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.Event, self).__init__()

                    self.yang_name = "event"
                    self.yang_parent_name = "policy-map"

                    self.event_type = YLeaf(YType.enumeration, "event-type")

                    self.event_mode_match_all = YLeaf(YType.empty, "event-mode-match-all")

                    self.event_mode_match_first = YLeaf(YType.empty, "event-mode-match-first")

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
                        if name in ("event_type",
                                    "event_mode_match_all",
                                    "event_mode_match_first") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PolicyManager.PolicyMaps.PolicyMap.Event, self).__setattr__(name, value)


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_, self).__init__()

                        self.yang_name = "class"
                        self.yang_parent_name = "event"

                        self.class_name = YLeaf(YType.str, "class-name")

                        self.class_type = YLeaf(YType.enumeration, "class-type")

                        self.class_execution_strategy = YLeaf(YType.enumeration, "class-execution-strategy")

                        self.action_rule = YList(self)

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
                                        "class_type",
                                        "class_execution_strategy") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule, self).__init__()

                            self.yang_name = "action-rule"
                            self.yang_parent_name = "class"

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

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("action_sequence_number",
                                            "disconnect",
                                            "monitor") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule, self).__setattr__(name, value)


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate, self).__init__()

                                self.yang_name = "activate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

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
                                    if name in ("aaa_list",
                                                "name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.aaa_list.is_set or
                                    self.name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aaa_list.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "activate-dynamic-template" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aaa_list.is_set or self.aaa_list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aaa_list.get_name_leafdata())
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
                                if(name == "aaa-list" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aaa-list"):
                                    self.aaa_list = value
                                    self.aaa_list.value_namespace = name_space
                                    self.aaa_list.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix


                        class Authenticate(Entity):
                            """
                            Authentication related configuration.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate, self).__init__()

                                self.yang_name = "authenticate"
                                self.yang_parent_name = "action-rule"

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("aaa_list") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate, self).__setattr__(name, value)

                            def has_data(self):
                                return self.aaa_list.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aaa_list.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "authenticate" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aaa_list.is_set or self.aaa_list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aaa_list.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "aaa-list"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aaa-list"):
                                    self.aaa_list = value
                                    self.aaa_list.value_namespace = name_space
                                    self.aaa_list.value_namespace_prefix = name_space_prefix


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize, self).__init__()

                                self.yang_name = "authorize"
                                self.yang_parent_name = "action-rule"
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

                                self.format = YLeaf(YType.str, "format")

                                self.identifier = YLeaf(YType.enumeration, "identifier")

                                self.password = YLeaf(YType.str, "password")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("aaa_list",
                                                "format",
                                                "identifier",
                                                "password") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.aaa_list.is_set or
                                    self.format.is_set or
                                    self.identifier.is_set or
                                    self.password.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aaa_list.yfilter != YFilter.not_set or
                                    self.format.yfilter != YFilter.not_set or
                                    self.identifier.yfilter != YFilter.not_set or
                                    self.password.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "authorize" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aaa_list.is_set or self.aaa_list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aaa_list.get_name_leafdata())
                                if (self.format.is_set or self.format.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.format.get_name_leafdata())
                                if (self.identifier.is_set or self.identifier.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.identifier.get_name_leafdata())
                                if (self.password.is_set or self.password.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.password.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "aaa-list" or name == "format" or name == "identifier" or name == "password"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aaa-list"):
                                    self.aaa_list = value
                                    self.aaa_list.value_namespace = name_space
                                    self.aaa_list.value_namespace_prefix = name_space_prefix
                                if(value_path == "format"):
                                    self.format = value
                                    self.format.value_namespace = name_space
                                    self.format.value_namespace_prefix = name_space_prefix
                                if(value_path == "identifier"):
                                    self.identifier = value
                                    self.identifier.value_namespace = name_space
                                    self.identifier.value_namespace_prefix = name_space_prefix
                                if(value_path == "password"):
                                    self.password = value
                                    self.password.value_namespace = name_space
                                    self.password.value_namespace_prefix = name_space_prefix


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate, self).__init__()

                                self.yang_name = "deactivate-dynamic-template"
                                self.yang_parent_name = "action-rule"
                                self.is_presence_container = True

                                self.aaa_list = YLeaf(YType.str, "aaa-list")

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
                                    if name in ("aaa_list",
                                                "name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.aaa_list.is_set or
                                    self.name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.aaa_list.yfilter != YFilter.not_set or
                                    self.name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "deactivate-dynamic-template" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.aaa_list.is_set or self.aaa_list.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.aaa_list.get_name_leafdata())
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
                                if(name == "aaa-list" or name == "name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "aaa-list"):
                                    self.aaa_list = value
                                    self.aaa_list.value_namespace = name_space
                                    self.aaa_list.value_namespace_prefix = name_space_prefix
                                if(value_path == "name"):
                                    self.name = value
                                    self.name.value_namespace = name_space
                                    self.name.value_namespace_prefix = name_space_prefix


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer, self).__init__()

                                self.yang_name = "set-timer"
                                self.yang_parent_name = "action-rule"
                                self.is_presence_container = True

                                self.timer_name = YLeaf(YType.str, "timer-name")

                                self.timer_value = YLeaf(YType.uint32, "timer-value")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("timer_name",
                                                "timer_value") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.timer_name.is_set or
                                    self.timer_value.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.timer_name.yfilter != YFilter.not_set or
                                    self.timer_value.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "set-timer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.timer_name.is_set or self.timer_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timer_name.get_name_leafdata())
                                if (self.timer_value.is_set or self.timer_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timer_value.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "timer-name" or name == "timer-value"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "timer-name"):
                                    self.timer_name = value
                                    self.timer_name.value_namespace = name_space
                                    self.timer_name.value_namespace_prefix = name_space_prefix
                                if(value_path == "timer-value"):
                                    self.timer_value = value
                                    self.timer_value.value_namespace = name_space
                                    self.timer_value.value_namespace_prefix = name_space_prefix


                        class StopTimer(Entity):
                            """
                            Disable timer before it expires.
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'infra-policymgr-cfg'
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer, self).__init__()

                                self.yang_name = "stop-timer"
                                self.yang_parent_name = "action-rule"

                                self.timer_name = YLeaf(YType.str, "timer-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("timer_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer, self).__setattr__(name, value)

                            def has_data(self):
                                return self.timer_name.is_set

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.timer_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "stop-timer" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.timer_name.is_set or self.timer_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.timer_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "timer-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "timer-name"):
                                    self.timer_name = value
                                    self.timer_name.value_namespace = name_space
                                    self.timer_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.action_sequence_number.is_set or
                                self.disconnect.is_set or
                                self.monitor.is_set or
                                (self.authenticate is not None and self.authenticate.has_data()) or
                                (self.stop_timer is not None and self.stop_timer.has_data()) or
                                (self.activate_dynamic_template is not None) or
                                (self.authorize is not None) or
                                (self.deactivate_dynamic_template is not None) or
                                (self.set_timer is not None))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.action_sequence_number.yfilter != YFilter.not_set or
                                self.disconnect.yfilter != YFilter.not_set or
                                self.monitor.yfilter != YFilter.not_set or
                                (self.activate_dynamic_template is not None and self.activate_dynamic_template.has_operation()) or
                                (self.authenticate is not None and self.authenticate.has_operation()) or
                                (self.authorize is not None and self.authorize.has_operation()) or
                                (self.deactivate_dynamic_template is not None and self.deactivate_dynamic_template.has_operation()) or
                                (self.set_timer is not None and self.set_timer.has_operation()) or
                                (self.stop_timer is not None and self.stop_timer.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "action-rule" + "[action-sequence-number='" + self.action_sequence_number.get() + "']" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.action_sequence_number.is_set or self.action_sequence_number.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.action_sequence_number.get_name_leafdata())
                            if (self.disconnect.is_set or self.disconnect.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.disconnect.get_name_leafdata())
                            if (self.monitor.is_set or self.monitor.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.monitor.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "activate-dynamic-template"):
                                if (self.activate_dynamic_template is None):
                                    self.activate_dynamic_template = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.ActivateDynamicTemplate()
                                    self.activate_dynamic_template.parent = self
                                    self._children_name_map["activate_dynamic_template"] = "activate-dynamic-template"
                                return self.activate_dynamic_template

                            if (child_yang_name == "authenticate"):
                                if (self.authenticate is None):
                                    self.authenticate = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authenticate()
                                    self.authenticate.parent = self
                                    self._children_name_map["authenticate"] = "authenticate"
                                return self.authenticate

                            if (child_yang_name == "authorize"):
                                if (self.authorize is None):
                                    self.authorize = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.Authorize()
                                    self.authorize.parent = self
                                    self._children_name_map["authorize"] = "authorize"
                                return self.authorize

                            if (child_yang_name == "deactivate-dynamic-template"):
                                if (self.deactivate_dynamic_template is None):
                                    self.deactivate_dynamic_template = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.DeactivateDynamicTemplate()
                                    self.deactivate_dynamic_template.parent = self
                                    self._children_name_map["deactivate_dynamic_template"] = "deactivate-dynamic-template"
                                return self.deactivate_dynamic_template

                            if (child_yang_name == "set-timer"):
                                if (self.set_timer is None):
                                    self.set_timer = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.SetTimer()
                                    self.set_timer.parent = self
                                    self._children_name_map["set_timer"] = "set-timer"
                                return self.set_timer

                            if (child_yang_name == "stop-timer"):
                                if (self.stop_timer is None):
                                    self.stop_timer = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule.StopTimer()
                                    self.stop_timer.parent = self
                                    self._children_name_map["stop_timer"] = "stop-timer"
                                return self.stop_timer

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "activate-dynamic-template" or name == "authenticate" or name == "authorize" or name == "deactivate-dynamic-template" or name == "set-timer" or name == "stop-timer" or name == "action-sequence-number" or name == "disconnect" or name == "monitor"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "action-sequence-number"):
                                self.action_sequence_number = value
                                self.action_sequence_number.value_namespace = name_space
                                self.action_sequence_number.value_namespace_prefix = name_space_prefix
                            if(value_path == "disconnect"):
                                self.disconnect = value
                                self.disconnect.value_namespace = name_space
                                self.disconnect.value_namespace_prefix = name_space_prefix
                            if(value_path == "monitor"):
                                self.monitor = value
                                self.monitor.value_namespace = name_space
                                self.monitor.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.action_rule:
                            if (c.has_data()):
                                return True
                        return (
                            self.class_name.is_set or
                            self.class_type.is_set or
                            self.class_execution_strategy.is_set)

                    def has_operation(self):
                        for c in self.action_rule:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.class_name.yfilter != YFilter.not_set or
                            self.class_type.yfilter != YFilter.not_set or
                            self.class_execution_strategy.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "class" + "[class-name='" + self.class_name.get() + "']" + "[class-type='" + self.class_type.get() + "']" + path_buffer

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
                        if (self.class_type.is_set or self.class_type.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.class_type.get_name_leafdata())
                        if (self.class_execution_strategy.is_set or self.class_execution_strategy.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.class_execution_strategy.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "action-rule"):
                            for c in self.action_rule:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = PolicyManager.PolicyMaps.PolicyMap.Event.Class_.ActionRule()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.action_rule.append(c)
                            return c

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "action-rule" or name == "class-name" or name == "class-type" or name == "class-execution-strategy"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "class-name"):
                            self.class_name = value
                            self.class_name.value_namespace = name_space
                            self.class_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "class-type"):
                            self.class_type = value
                            self.class_type.value_namespace = name_space
                            self.class_type.value_namespace_prefix = name_space_prefix
                        if(value_path == "class-execution-strategy"):
                            self.class_execution_strategy = value
                            self.class_execution_strategy.value_namespace = name_space
                            self.class_execution_strategy.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.class_:
                        if (c.has_data()):
                            return True
                    return (
                        self.event_type.is_set or
                        self.event_mode_match_all.is_set or
                        self.event_mode_match_first.is_set)

                def has_operation(self):
                    for c in self.class_:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.event_type.yfilter != YFilter.not_set or
                        self.event_mode_match_all.yfilter != YFilter.not_set or
                        self.event_mode_match_first.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "event" + "[event-type='" + self.event_type.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.event_type.is_set or self.event_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.event_type.get_name_leafdata())
                    if (self.event_mode_match_all.is_set or self.event_mode_match_all.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.event_mode_match_all.get_name_leafdata())
                    if (self.event_mode_match_first.is_set or self.event_mode_match_first.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.event_mode_match_first.get_name_leafdata())

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
                        c = PolicyManager.PolicyMaps.PolicyMap.Event.Class_()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.class_.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "class" or name == "event-type" or name == "event-mode-match-all" or name == "event-mode-match-first"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "event-type"):
                        self.event_type = value
                        self.event_type.value_namespace = name_space
                        self.event_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "event-mode-match-all"):
                        self.event_mode_match_all = value
                        self.event_mode_match_all.value_namespace = name_space
                        self.event_mode_match_all.value_namespace_prefix = name_space_prefix
                    if(value_path == "event-mode-match-first"):
                        self.event_mode_match_first = value
                        self.event_mode_match_first.value_namespace = name_space
                        self.event_mode_match_first.value_namespace_prefix = name_space_prefix


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
                _revision = '2017-03-03'

                def __init__(self):
                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, self).__init__()

                    self.yang_name = "policy-map-rule"
                    self.yang_parent_name = "policy-map"

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

                    self.service_function_path = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath()
                    self.service_function_path.parent = self
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
                                    "class_type",
                                    "decap_gre",
                                    "default_red",
                                    "ecn_red",
                                    "fragment",
                                    "http_redirect",
                                    "pbr_drop",
                                    "pbr_transmit",
                                    "priority_level",
                                    "service_fragment") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule, self).__setattr__(name, value)


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape, self).__init__()

                        self.yang_name = "shape"
                        self.yang_parent_name = "policy-map-rule"

                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst()
                        self.burst.parent = self
                        self._children_name_map["burst"] = "burst"
                        self._children_yang_names.add("burst")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "shape"

                            self.unit = YLeaf(YType.str, "unit")

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
                                if name in ("unit",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.unit.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.unit.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "unit" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "unit"):
                                self.unit = value
                                self.unit.value_namespace = name_space
                                self.unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "shape"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "burst" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.burst is not None and self.burst.has_data()) or
                            (self.rate is not None and self.rate.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.burst is not None and self.burst.has_operation()) or
                            (self.rate is not None and self.rate.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "shape" + path_buffer

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

                        if (child_yang_name == "burst"):
                            if (self.burst is None):
                                self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst()
                                self.burst.parent = self
                                self._children_name_map["burst"] = "burst"
                            return self.burst

                        if (child_yang_name == "rate"):
                            if (self.rate is None):
                                self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate()
                                self.rate.parent = self
                                self._children_name_map["rate"] = "rate"
                            return self.rate

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "burst" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, self).__init__()

                        self.yang_name = "min-bandwidth"
                        self.yang_parent_name = "policy-map-rule"

                        self.unit = YLeaf(YType.str, "unit")

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
                            if name in ("unit",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.unit.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.unit.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "min-bandwidth" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
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
                        if(name == "unit" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "unit"):
                            self.unit = value
                            self.unit.value_namespace = name_space
                            self.unit.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, self).__init__()

                        self.yang_name = "bandwidth-remaining"
                        self.yang_parent_name = "policy-map-rule"

                        self.unit = YLeaf(YType.str, "unit")

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
                            if name in ("unit",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.unit.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.unit.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bandwidth-remaining" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
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
                        if(name == "unit" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "unit"):
                            self.unit = value
                            self.unit.value_namespace = name_space
                            self.unit.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, self).__init__()

                        self.yang_name = "queue-limit"
                        self.yang_parent_name = "policy-map-rule"

                        self.unit = YLeaf(YType.str, "unit")

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
                            if name in ("unit",
                                        "value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.unit.is_set or
                            self.value.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.unit.yfilter != YFilter.not_set or
                            self.value.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "queue-limit" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
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
                        if(name == "unit" or name == "value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "unit"):
                            self.unit = value
                            self.unit.value_namespace = name_space
                            self.unit.value_namespace_prefix = name_space_prefix
                        if(value_path == "value"):
                            self.value = value
                            self.value.value_namespace = name_space
                            self.value.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, self).__init__()

                        self.yang_name = "pfc"
                        self.yang_parent_name = "policy-map-rule"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("pfc_pause_set") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, self).__init__()

                            self.yang_name = "pfc-buffer-size"
                            self.yang_parent_name = "pfc"

                            self.unit = YLeaf(YType.str, "unit")

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
                                if name in ("unit",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.unit.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.unit.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pfc-buffer-size" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "unit" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "unit"):
                                self.unit = value
                                self.unit.value_namespace = name_space
                                self.unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, self).__init__()

                            self.yang_name = "pfc-pause-threshold"
                            self.yang_parent_name = "pfc"

                            self.unit = YLeaf(YType.str, "unit")

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
                                if name in ("unit",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.unit.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.unit.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pfc-pause-threshold" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "unit" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "unit"):
                                self.unit = value
                                self.unit.value_namespace = name_space
                                self.unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, self).__init__()

                            self.yang_name = "pfc-resume-threshold"
                            self.yang_parent_name = "pfc"

                            self.unit = YLeaf(YType.str, "unit")

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
                                if name in ("unit",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.unit.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.unit.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pfc-resume-threshold" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
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
                            if(name == "unit" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "unit"):
                                self.unit = value
                                self.unit.value_namespace = name_space
                                self.unit.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.pfc_pause_set.is_set or
                            (self.pfc_buffer_size is not None and self.pfc_buffer_size.has_data()) or
                            (self.pfc_pause_threshold is not None and self.pfc_pause_threshold.has_data()) or
                            (self.pfc_resume_threshold is not None and self.pfc_resume_threshold.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.pfc_pause_set.yfilter != YFilter.not_set or
                            (self.pfc_buffer_size is not None and self.pfc_buffer_size.has_operation()) or
                            (self.pfc_pause_threshold is not None and self.pfc_pause_threshold.has_operation()) or
                            (self.pfc_resume_threshold is not None and self.pfc_resume_threshold.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pfc" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.pfc_pause_set.is_set or self.pfc_pause_set.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pfc_pause_set.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "pfc-buffer-size"):
                            if (self.pfc_buffer_size is None):
                                self.pfc_buffer_size = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcBufferSize()
                                self.pfc_buffer_size.parent = self
                                self._children_name_map["pfc_buffer_size"] = "pfc-buffer-size"
                            return self.pfc_buffer_size

                        if (child_yang_name == "pfc-pause-threshold"):
                            if (self.pfc_pause_threshold is None):
                                self.pfc_pause_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcPauseThreshold()
                                self.pfc_pause_threshold.parent = self
                                self._children_name_map["pfc_pause_threshold"] = "pfc-pause-threshold"
                            return self.pfc_pause_threshold

                        if (child_yang_name == "pfc-resume-threshold"):
                            if (self.pfc_resume_threshold is None):
                                self.pfc_resume_threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc.PfcResumeThreshold()
                                self.pfc_resume_threshold.parent = self
                                self._children_name_map["pfc_resume_threshold"] = "pfc-resume-threshold"
                            return self.pfc_resume_threshold

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "pfc-buffer-size" or name == "pfc-pause-threshold" or name == "pfc-resume-threshold" or name == "pfc-pause-set"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "pfc-pause-set"):
                            self.pfc_pause_set = value
                            self.pfc_pause_set.value_namespace = name_space
                            self.pfc_pause_set.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, self).__init__()

                        self.yang_name = "random-detect"
                        self.yang_parent_name = "policy-map-rule"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("threshold_min_value",
                                        "threshold_min_units",
                                        "threshold_max_value",
                                        "threshold_max_units",
                                        "cos",
                                        "dei",
                                        "discard_class",
                                        "dscp",
                                        "ecn",
                                        "mpls_exp",
                                        "precedence") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect, self).__setattr__(name, value)

                    def has_data(self):
                        for leaf in self.cos.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.discard_class.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.dscp.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.mpls_exp.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        for leaf in self.precedence.getYLeafs():
                            if (leaf.yfilter != YFilter.not_set):
                                return True
                        return (
                            self.threshold_min_value.is_set or
                            self.threshold_min_units.is_set or
                            self.threshold_max_value.is_set or
                            self.threshold_max_units.is_set or
                            self.dei.is_set or
                            self.ecn.is_set)

                    def has_operation(self):
                        for leaf in self.cos.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.discard_class.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.dscp.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.mpls_exp.getYLeafs():
                            if (leaf.is_set):
                                return True
                        for leaf in self.precedence.getYLeafs():
                            if (leaf.is_set):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.threshold_min_value.yfilter != YFilter.not_set or
                            self.threshold_min_units.yfilter != YFilter.not_set or
                            self.threshold_max_value.yfilter != YFilter.not_set or
                            self.threshold_max_units.yfilter != YFilter.not_set or
                            self.cos.yfilter != YFilter.not_set or
                            self.dei.yfilter != YFilter.not_set or
                            self.discard_class.yfilter != YFilter.not_set or
                            self.dscp.yfilter != YFilter.not_set or
                            self.ecn.yfilter != YFilter.not_set or
                            self.mpls_exp.yfilter != YFilter.not_set or
                            self.precedence.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "random-detect" + "[threshold-min-value='" + self.threshold_min_value.get() + "']" + "[threshold-min-units='" + self.threshold_min_units.get() + "']" + "[threshold-max-value='" + self.threshold_max_value.get() + "']" + "[threshold-max-units='" + self.threshold_max_units.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.threshold_min_value.is_set or self.threshold_min_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_min_value.get_name_leafdata())
                        if (self.threshold_min_units.is_set or self.threshold_min_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_min_units.get_name_leafdata())
                        if (self.threshold_max_value.is_set or self.threshold_max_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_max_value.get_name_leafdata())
                        if (self.threshold_max_units.is_set or self.threshold_max_units.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.threshold_max_units.get_name_leafdata())
                        if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dei.get_name_leafdata())
                        if (self.ecn.is_set or self.ecn.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.ecn.get_name_leafdata())

                        leaf_name_data.extend(self.cos.get_name_leafdata())

                        leaf_name_data.extend(self.discard_class.get_name_leafdata())

                        leaf_name_data.extend(self.dscp.get_name_leafdata())

                        leaf_name_data.extend(self.mpls_exp.get_name_leafdata())

                        leaf_name_data.extend(self.precedence.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "threshold-min-value" or name == "threshold-min-units" or name == "threshold-max-value" or name == "threshold-max-units" or name == "cos" or name == "dei" or name == "discard-class" or name == "dscp" or name == "ecn" or name == "mpls-exp" or name == "precedence"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "threshold-min-value"):
                            self.threshold_min_value = value
                            self.threshold_min_value.value_namespace = name_space
                            self.threshold_min_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold-min-units"):
                            self.threshold_min_units = value
                            self.threshold_min_units.value_namespace = name_space
                            self.threshold_min_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold-max-value"):
                            self.threshold_max_value = value
                            self.threshold_max_value.value_namespace = name_space
                            self.threshold_max_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "threshold-max-units"):
                            self.threshold_max_units = value
                            self.threshold_max_units.value_namespace = name_space
                            self.threshold_max_units.value_namespace_prefix = name_space_prefix
                        if(value_path == "cos"):
                            self.cos.append(value)
                        if(value_path == "dei"):
                            self.dei = value
                            self.dei.value_namespace = name_space
                            self.dei.value_namespace_prefix = name_space_prefix
                        if(value_path == "discard-class"):
                            self.discard_class.append(value)
                        if(value_path == "dscp"):
                            self.dscp.append(value)
                        if(value_path == "ecn"):
                            self.ecn = value
                            self.ecn.value_namespace = name_space
                            self.ecn.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-exp"):
                            self.mpls_exp.append(value)
                        if(value_path == "precedence"):
                            self.precedence.append(value)


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
                    
                    	Sets the discard class
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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, self).__init__()

                        self.yang_name = "set"
                        self.yang_parent_name = "policy-map-rule"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("cos",
                                        "dei",
                                        "dei_imposition",
                                        "destination_address",
                                        "df",
                                        "discard_class",
                                        "dscp",
                                        "forward_class",
                                        "fr_de",
                                        "inner_cos",
                                        "mpls_experimental_imposition",
                                        "mpls_experimental_top_most",
                                        "precedence",
                                        "precedence_tunnel",
                                        "qos_group",
                                        "source_address",
                                        "srp_priority",
                                        "traffic_class") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.cos.is_set or
                            self.dei.is_set or
                            self.dei_imposition.is_set or
                            self.destination_address.is_set or
                            self.df.is_set or
                            self.discard_class.is_set or
                            self.dscp.is_set or
                            self.forward_class.is_set or
                            self.fr_de.is_set or
                            self.inner_cos.is_set or
                            self.mpls_experimental_imposition.is_set or
                            self.mpls_experimental_top_most.is_set or
                            self.precedence.is_set or
                            self.precedence_tunnel.is_set or
                            self.qos_group.is_set or
                            self.source_address.is_set or
                            self.srp_priority.is_set or
                            self.traffic_class.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.cos.yfilter != YFilter.not_set or
                            self.dei.yfilter != YFilter.not_set or
                            self.dei_imposition.yfilter != YFilter.not_set or
                            self.destination_address.yfilter != YFilter.not_set or
                            self.df.yfilter != YFilter.not_set or
                            self.discard_class.yfilter != YFilter.not_set or
                            self.dscp.yfilter != YFilter.not_set or
                            self.forward_class.yfilter != YFilter.not_set or
                            self.fr_de.yfilter != YFilter.not_set or
                            self.inner_cos.yfilter != YFilter.not_set or
                            self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                            self.mpls_experimental_top_most.yfilter != YFilter.not_set or
                            self.precedence.yfilter != YFilter.not_set or
                            self.precedence_tunnel.yfilter != YFilter.not_set or
                            self.qos_group.yfilter != YFilter.not_set or
                            self.source_address.yfilter != YFilter.not_set or
                            self.srp_priority.yfilter != YFilter.not_set or
                            self.traffic_class.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "set" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.cos.get_name_leafdata())
                        if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dei.get_name_leafdata())
                        if (self.dei_imposition.is_set or self.dei_imposition.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dei_imposition.get_name_leafdata())
                        if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_address.get_name_leafdata())
                        if (self.df.is_set or self.df.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.df.get_name_leafdata())
                        if (self.discard_class.is_set or self.discard_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.discard_class.get_name_leafdata())
                        if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dscp.get_name_leafdata())
                        if (self.forward_class.is_set or self.forward_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.forward_class.get_name_leafdata())
                        if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.fr_de.get_name_leafdata())
                        if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.inner_cos.get_name_leafdata())
                        if (self.mpls_experimental_imposition.is_set or self.mpls_experimental_imposition.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_experimental_imposition.get_name_leafdata())
                        if (self.mpls_experimental_top_most.is_set or self.mpls_experimental_top_most.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.mpls_experimental_top_most.get_name_leafdata())
                        if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.precedence.get_name_leafdata())
                        if (self.precedence_tunnel.is_set or self.precedence_tunnel.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.precedence_tunnel.get_name_leafdata())
                        if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.qos_group.get_name_leafdata())
                        if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_address.get_name_leafdata())
                        if (self.srp_priority.is_set or self.srp_priority.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.srp_priority.get_name_leafdata())
                        if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_class.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "cos" or name == "dei" or name == "dei-imposition" or name == "destination-address" or name == "df" or name == "discard-class" or name == "dscp" or name == "forward-class" or name == "fr-de" or name == "inner-cos" or name == "mpls-experimental-imposition" or name == "mpls-experimental-top-most" or name == "precedence" or name == "precedence-tunnel" or name == "qos-group" or name == "source-address" or name == "srp-priority" or name == "traffic-class"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "cos"):
                            self.cos = value
                            self.cos.value_namespace = name_space
                            self.cos.value_namespace_prefix = name_space_prefix
                        if(value_path == "dei"):
                            self.dei = value
                            self.dei.value_namespace = name_space
                            self.dei.value_namespace_prefix = name_space_prefix
                        if(value_path == "dei-imposition"):
                            self.dei_imposition = value
                            self.dei_imposition.value_namespace = name_space
                            self.dei_imposition.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-address"):
                            self.destination_address = value
                            self.destination_address.value_namespace = name_space
                            self.destination_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "df"):
                            self.df = value
                            self.df.value_namespace = name_space
                            self.df.value_namespace_prefix = name_space_prefix
                        if(value_path == "discard-class"):
                            self.discard_class = value
                            self.discard_class.value_namespace = name_space
                            self.discard_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "dscp"):
                            self.dscp = value
                            self.dscp.value_namespace = name_space
                            self.dscp.value_namespace_prefix = name_space_prefix
                        if(value_path == "forward-class"):
                            self.forward_class = value
                            self.forward_class.value_namespace = name_space
                            self.forward_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "fr-de"):
                            self.fr_de = value
                            self.fr_de.value_namespace = name_space
                            self.fr_de.value_namespace_prefix = name_space_prefix
                        if(value_path == "inner-cos"):
                            self.inner_cos = value
                            self.inner_cos.value_namespace = name_space
                            self.inner_cos.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-experimental-imposition"):
                            self.mpls_experimental_imposition = value
                            self.mpls_experimental_imposition.value_namespace = name_space
                            self.mpls_experimental_imposition.value_namespace_prefix = name_space_prefix
                        if(value_path == "mpls-experimental-top-most"):
                            self.mpls_experimental_top_most = value
                            self.mpls_experimental_top_most.value_namespace = name_space
                            self.mpls_experimental_top_most.value_namespace_prefix = name_space_prefix
                        if(value_path == "precedence"):
                            self.precedence = value
                            self.precedence.value_namespace = name_space
                            self.precedence.value_namespace_prefix = name_space_prefix
                        if(value_path == "precedence-tunnel"):
                            self.precedence_tunnel = value
                            self.precedence_tunnel.value_namespace = name_space
                            self.precedence_tunnel.value_namespace_prefix = name_space_prefix
                        if(value_path == "qos-group"):
                            self.qos_group = value
                            self.qos_group.value_namespace = name_space
                            self.qos_group.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-address"):
                            self.source_address = value
                            self.source_address.value_namespace = name_space
                            self.source_address.value_namespace_prefix = name_space_prefix
                        if(value_path == "srp-priority"):
                            self.srp_priority = value
                            self.srp_priority.value_namespace = name_space
                            self.srp_priority.value_namespace_prefix = name_space_prefix
                        if(value_path == "traffic-class"):
                            self.traffic_class = value
                            self.traffic_class.value_namespace = name_space
                            self.traffic_class.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police, self).__init__()

                        self.yang_name = "police"
                        self.yang_parent_name = "policy-map-rule"

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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "police"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, self).__init__()

                            self.yang_name = "peak-rate"
                            self.yang_parent_name = "police"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peak-rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, self).__init__()

                            self.yang_name = "burst"
                            self.yang_parent_name = "police"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "burst" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, self).__init__()

                            self.yang_name = "peak-burst"
                            self.yang_parent_name = "police"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "peak-burst" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, self).__init__()

                            self.yang_name = "conform-action"
                            self.yang_parent_name = "police"

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("drop",
                                            "transmit") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction, self).__setattr__(name, value)


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
                            
                            	Sets the discard class
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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "conform-action"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cos",
                                                "dei",
                                                "dei_imposition",
                                                "destination_address",
                                                "df",
                                                "discard_class",
                                                "dscp",
                                                "forward_class",
                                                "fr_de",
                                                "inner_cos",
                                                "mpls_experimental_imposition",
                                                "mpls_experimental_top_most",
                                                "precedence",
                                                "precedence_tunnel",
                                                "qos_group",
                                                "source_address",
                                                "srp_priority",
                                                "traffic_class") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cos.is_set or
                                    self.dei.is_set or
                                    self.dei_imposition.is_set or
                                    self.destination_address.is_set or
                                    self.df.is_set or
                                    self.discard_class.is_set or
                                    self.dscp.is_set or
                                    self.forward_class.is_set or
                                    self.fr_de.is_set or
                                    self.inner_cos.is_set or
                                    self.mpls_experimental_imposition.is_set or
                                    self.mpls_experimental_top_most.is_set or
                                    self.precedence.is_set or
                                    self.precedence_tunnel.is_set or
                                    self.qos_group.is_set or
                                    self.source_address.is_set or
                                    self.srp_priority.is_set or
                                    self.traffic_class.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.dei.yfilter != YFilter.not_set or
                                    self.dei_imposition.yfilter != YFilter.not_set or
                                    self.destination_address.yfilter != YFilter.not_set or
                                    self.df.yfilter != YFilter.not_set or
                                    self.discard_class.yfilter != YFilter.not_set or
                                    self.dscp.yfilter != YFilter.not_set or
                                    self.forward_class.yfilter != YFilter.not_set or
                                    self.fr_de.yfilter != YFilter.not_set or
                                    self.inner_cos.yfilter != YFilter.not_set or
                                    self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                                    self.mpls_experimental_top_most.yfilter != YFilter.not_set or
                                    self.precedence.yfilter != YFilter.not_set or
                                    self.precedence_tunnel.yfilter != YFilter.not_set or
                                    self.qos_group.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.srp_priority.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "set" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei.get_name_leafdata())
                                if (self.dei_imposition.is_set or self.dei_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei_imposition.get_name_leafdata())
                                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                                if (self.df.is_set or self.df.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.df.get_name_leafdata())
                                if (self.discard_class.is_set or self.discard_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.discard_class.get_name_leafdata())
                                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dscp.get_name_leafdata())
                                if (self.forward_class.is_set or self.forward_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.forward_class.get_name_leafdata())
                                if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fr_de.get_name_leafdata())
                                if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_cos.get_name_leafdata())
                                if (self.mpls_experimental_imposition.is_set or self.mpls_experimental_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_imposition.get_name_leafdata())
                                if (self.mpls_experimental_top_most.is_set or self.mpls_experimental_top_most.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_top_most.get_name_leafdata())
                                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence.get_name_leafdata())
                                if (self.precedence_tunnel.is_set or self.precedence_tunnel.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence_tunnel.get_name_leafdata())
                                if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.qos_group.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.srp_priority.is_set or self.srp_priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.srp_priority.get_name_leafdata())
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cos" or name == "dei" or name == "dei-imposition" or name == "destination-address" or name == "df" or name == "discard-class" or name == "dscp" or name == "forward-class" or name == "fr-de" or name == "inner-cos" or name == "mpls-experimental-imposition" or name == "mpls-experimental-top-most" or name == "precedence" or name == "precedence-tunnel" or name == "qos-group" or name == "source-address" or name == "srp-priority" or name == "traffic-class"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei"):
                                    self.dei = value
                                    self.dei.value_namespace = name_space
                                    self.dei.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei-imposition"):
                                    self.dei_imposition = value
                                    self.dei_imposition.value_namespace = name_space
                                    self.dei_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "destination-address"):
                                    self.destination_address = value
                                    self.destination_address.value_namespace = name_space
                                    self.destination_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "df"):
                                    self.df = value
                                    self.df.value_namespace = name_space
                                    self.df.value_namespace_prefix = name_space_prefix
                                if(value_path == "discard-class"):
                                    self.discard_class = value
                                    self.discard_class.value_namespace = name_space
                                    self.discard_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "dscp"):
                                    self.dscp = value
                                    self.dscp.value_namespace = name_space
                                    self.dscp.value_namespace_prefix = name_space_prefix
                                if(value_path == "forward-class"):
                                    self.forward_class = value
                                    self.forward_class.value_namespace = name_space
                                    self.forward_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "fr-de"):
                                    self.fr_de = value
                                    self.fr_de.value_namespace = name_space
                                    self.fr_de.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-cos"):
                                    self.inner_cos = value
                                    self.inner_cos.value_namespace = name_space
                                    self.inner_cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-imposition"):
                                    self.mpls_experimental_imposition = value
                                    self.mpls_experimental_imposition.value_namespace = name_space
                                    self.mpls_experimental_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-top-most"):
                                    self.mpls_experimental_top_most = value
                                    self.mpls_experimental_top_most.value_namespace = name_space
                                    self.mpls_experimental_top_most.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence"):
                                    self.precedence = value
                                    self.precedence.value_namespace = name_space
                                    self.precedence.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence-tunnel"):
                                    self.precedence_tunnel = value
                                    self.precedence_tunnel.value_namespace = name_space
                                    self.precedence_tunnel.value_namespace_prefix = name_space_prefix
                                if(value_path == "qos-group"):
                                    self.qos_group = value
                                    self.qos_group.value_namespace = name_space
                                    self.qos_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "srp-priority"):
                                    self.srp_priority = value
                                    self.srp_priority.value_namespace = name_space
                                    self.srp_priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.drop.is_set or
                                self.transmit.is_set or
                                (self.set is not None and self.set.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.drop.yfilter != YFilter.not_set or
                                self.transmit.yfilter != YFilter.not_set or
                                (self.set is not None and self.set.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "conform-action" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.drop.is_set or self.drop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drop.get_name_leafdata())
                            if (self.transmit.is_set or self.transmit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "set"):
                                if (self.set is None):
                                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set()
                                    self.set.parent = self
                                    self._children_name_map["set"] = "set"
                                return self.set

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set" or name == "drop" or name == "Transmit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "drop"):
                                self.drop = value
                                self.drop.value_namespace = name_space
                                self.drop.value_namespace_prefix = name_space_prefix
                            if(value_path == "Transmit"):
                                self.transmit = value
                                self.transmit.value_namespace = name_space
                                self.transmit.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, self).__init__()

                            self.yang_name = "exceed-action"
                            self.yang_parent_name = "police"

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("drop",
                                            "transmit") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction, self).__setattr__(name, value)


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
                            
                            	Sets the discard class
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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "exceed-action"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cos",
                                                "dei",
                                                "dei_imposition",
                                                "destination_address",
                                                "df",
                                                "discard_class",
                                                "dscp",
                                                "forward_class",
                                                "fr_de",
                                                "inner_cos",
                                                "mpls_experimental_imposition",
                                                "mpls_experimental_top_most",
                                                "precedence",
                                                "precedence_tunnel",
                                                "qos_group",
                                                "source_address",
                                                "srp_priority",
                                                "traffic_class") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cos.is_set or
                                    self.dei.is_set or
                                    self.dei_imposition.is_set or
                                    self.destination_address.is_set or
                                    self.df.is_set or
                                    self.discard_class.is_set or
                                    self.dscp.is_set or
                                    self.forward_class.is_set or
                                    self.fr_de.is_set or
                                    self.inner_cos.is_set or
                                    self.mpls_experimental_imposition.is_set or
                                    self.mpls_experimental_top_most.is_set or
                                    self.precedence.is_set or
                                    self.precedence_tunnel.is_set or
                                    self.qos_group.is_set or
                                    self.source_address.is_set or
                                    self.srp_priority.is_set or
                                    self.traffic_class.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.dei.yfilter != YFilter.not_set or
                                    self.dei_imposition.yfilter != YFilter.not_set or
                                    self.destination_address.yfilter != YFilter.not_set or
                                    self.df.yfilter != YFilter.not_set or
                                    self.discard_class.yfilter != YFilter.not_set or
                                    self.dscp.yfilter != YFilter.not_set or
                                    self.forward_class.yfilter != YFilter.not_set or
                                    self.fr_de.yfilter != YFilter.not_set or
                                    self.inner_cos.yfilter != YFilter.not_set or
                                    self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                                    self.mpls_experimental_top_most.yfilter != YFilter.not_set or
                                    self.precedence.yfilter != YFilter.not_set or
                                    self.precedence_tunnel.yfilter != YFilter.not_set or
                                    self.qos_group.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.srp_priority.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "set" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei.get_name_leafdata())
                                if (self.dei_imposition.is_set or self.dei_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei_imposition.get_name_leafdata())
                                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                                if (self.df.is_set or self.df.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.df.get_name_leafdata())
                                if (self.discard_class.is_set or self.discard_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.discard_class.get_name_leafdata())
                                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dscp.get_name_leafdata())
                                if (self.forward_class.is_set or self.forward_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.forward_class.get_name_leafdata())
                                if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fr_de.get_name_leafdata())
                                if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_cos.get_name_leafdata())
                                if (self.mpls_experimental_imposition.is_set or self.mpls_experimental_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_imposition.get_name_leafdata())
                                if (self.mpls_experimental_top_most.is_set or self.mpls_experimental_top_most.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_top_most.get_name_leafdata())
                                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence.get_name_leafdata())
                                if (self.precedence_tunnel.is_set or self.precedence_tunnel.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence_tunnel.get_name_leafdata())
                                if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.qos_group.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.srp_priority.is_set or self.srp_priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.srp_priority.get_name_leafdata())
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cos" or name == "dei" or name == "dei-imposition" or name == "destination-address" or name == "df" or name == "discard-class" or name == "dscp" or name == "forward-class" or name == "fr-de" or name == "inner-cos" or name == "mpls-experimental-imposition" or name == "mpls-experimental-top-most" or name == "precedence" or name == "precedence-tunnel" or name == "qos-group" or name == "source-address" or name == "srp-priority" or name == "traffic-class"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei"):
                                    self.dei = value
                                    self.dei.value_namespace = name_space
                                    self.dei.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei-imposition"):
                                    self.dei_imposition = value
                                    self.dei_imposition.value_namespace = name_space
                                    self.dei_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "destination-address"):
                                    self.destination_address = value
                                    self.destination_address.value_namespace = name_space
                                    self.destination_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "df"):
                                    self.df = value
                                    self.df.value_namespace = name_space
                                    self.df.value_namespace_prefix = name_space_prefix
                                if(value_path == "discard-class"):
                                    self.discard_class = value
                                    self.discard_class.value_namespace = name_space
                                    self.discard_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "dscp"):
                                    self.dscp = value
                                    self.dscp.value_namespace = name_space
                                    self.dscp.value_namespace_prefix = name_space_prefix
                                if(value_path == "forward-class"):
                                    self.forward_class = value
                                    self.forward_class.value_namespace = name_space
                                    self.forward_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "fr-de"):
                                    self.fr_de = value
                                    self.fr_de.value_namespace = name_space
                                    self.fr_de.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-cos"):
                                    self.inner_cos = value
                                    self.inner_cos.value_namespace = name_space
                                    self.inner_cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-imposition"):
                                    self.mpls_experimental_imposition = value
                                    self.mpls_experimental_imposition.value_namespace = name_space
                                    self.mpls_experimental_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-top-most"):
                                    self.mpls_experimental_top_most = value
                                    self.mpls_experimental_top_most.value_namespace = name_space
                                    self.mpls_experimental_top_most.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence"):
                                    self.precedence = value
                                    self.precedence.value_namespace = name_space
                                    self.precedence.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence-tunnel"):
                                    self.precedence_tunnel = value
                                    self.precedence_tunnel.value_namespace = name_space
                                    self.precedence_tunnel.value_namespace_prefix = name_space_prefix
                                if(value_path == "qos-group"):
                                    self.qos_group = value
                                    self.qos_group.value_namespace = name_space
                                    self.qos_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "srp-priority"):
                                    self.srp_priority = value
                                    self.srp_priority.value_namespace = name_space
                                    self.srp_priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.drop.is_set or
                                self.transmit.is_set or
                                (self.set is not None and self.set.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.drop.yfilter != YFilter.not_set or
                                self.transmit.yfilter != YFilter.not_set or
                                (self.set is not None and self.set.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "exceed-action" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.drop.is_set or self.drop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drop.get_name_leafdata())
                            if (self.transmit.is_set or self.transmit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "set"):
                                if (self.set is None):
                                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set()
                                    self.set.parent = self
                                    self._children_name_map["set"] = "set"
                                return self.set

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set" or name == "drop" or name == "Transmit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "drop"):
                                self.drop = value
                                self.drop.value_namespace = name_space
                                self.drop.value_namespace_prefix = name_space_prefix
                            if(value_path == "Transmit"):
                                self.transmit = value
                                self.transmit.value_namespace = name_space
                                self.transmit.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, self).__init__()

                            self.yang_name = "violate-action"
                            self.yang_parent_name = "police"

                            self.drop = YLeaf(YType.empty, "drop")

                            self.transmit = YLeaf(YType.empty, "Transmit")

                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                            self._children_yang_names.add("set")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("drop",
                                            "transmit") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction, self).__setattr__(name, value)


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
                            
                            	Sets the discard class
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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, self).__init__()

                                self.yang_name = "set"
                                self.yang_parent_name = "violate-action"

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

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("cos",
                                                "dei",
                                                "dei_imposition",
                                                "destination_address",
                                                "df",
                                                "discard_class",
                                                "dscp",
                                                "forward_class",
                                                "fr_de",
                                                "inner_cos",
                                                "mpls_experimental_imposition",
                                                "mpls_experimental_top_most",
                                                "precedence",
                                                "precedence_tunnel",
                                                "qos_group",
                                                "source_address",
                                                "srp_priority",
                                                "traffic_class") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.cos.is_set or
                                    self.dei.is_set or
                                    self.dei_imposition.is_set or
                                    self.destination_address.is_set or
                                    self.df.is_set or
                                    self.discard_class.is_set or
                                    self.dscp.is_set or
                                    self.forward_class.is_set or
                                    self.fr_de.is_set or
                                    self.inner_cos.is_set or
                                    self.mpls_experimental_imposition.is_set or
                                    self.mpls_experimental_top_most.is_set or
                                    self.precedence.is_set or
                                    self.precedence_tunnel.is_set or
                                    self.qos_group.is_set or
                                    self.source_address.is_set or
                                    self.srp_priority.is_set or
                                    self.traffic_class.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.cos.yfilter != YFilter.not_set or
                                    self.dei.yfilter != YFilter.not_set or
                                    self.dei_imposition.yfilter != YFilter.not_set or
                                    self.destination_address.yfilter != YFilter.not_set or
                                    self.df.yfilter != YFilter.not_set or
                                    self.discard_class.yfilter != YFilter.not_set or
                                    self.dscp.yfilter != YFilter.not_set or
                                    self.forward_class.yfilter != YFilter.not_set or
                                    self.fr_de.yfilter != YFilter.not_set or
                                    self.inner_cos.yfilter != YFilter.not_set or
                                    self.mpls_experimental_imposition.yfilter != YFilter.not_set or
                                    self.mpls_experimental_top_most.yfilter != YFilter.not_set or
                                    self.precedence.yfilter != YFilter.not_set or
                                    self.precedence_tunnel.yfilter != YFilter.not_set or
                                    self.qos_group.yfilter != YFilter.not_set or
                                    self.source_address.yfilter != YFilter.not_set or
                                    self.srp_priority.yfilter != YFilter.not_set or
                                    self.traffic_class.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "set" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.cos.is_set or self.cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.cos.get_name_leafdata())
                                if (self.dei.is_set or self.dei.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei.get_name_leafdata())
                                if (self.dei_imposition.is_set or self.dei_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dei_imposition.get_name_leafdata())
                                if (self.destination_address.is_set or self.destination_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_address.get_name_leafdata())
                                if (self.df.is_set or self.df.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.df.get_name_leafdata())
                                if (self.discard_class.is_set or self.discard_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.discard_class.get_name_leafdata())
                                if (self.dscp.is_set or self.dscp.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.dscp.get_name_leafdata())
                                if (self.forward_class.is_set or self.forward_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.forward_class.get_name_leafdata())
                                if (self.fr_de.is_set or self.fr_de.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.fr_de.get_name_leafdata())
                                if (self.inner_cos.is_set or self.inner_cos.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.inner_cos.get_name_leafdata())
                                if (self.mpls_experimental_imposition.is_set or self.mpls_experimental_imposition.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_imposition.get_name_leafdata())
                                if (self.mpls_experimental_top_most.is_set or self.mpls_experimental_top_most.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mpls_experimental_top_most.get_name_leafdata())
                                if (self.precedence.is_set or self.precedence.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence.get_name_leafdata())
                                if (self.precedence_tunnel.is_set or self.precedence_tunnel.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.precedence_tunnel.get_name_leafdata())
                                if (self.qos_group.is_set or self.qos_group.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.qos_group.get_name_leafdata())
                                if (self.source_address.is_set or self.source_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.source_address.get_name_leafdata())
                                if (self.srp_priority.is_set or self.srp_priority.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.srp_priority.get_name_leafdata())
                                if (self.traffic_class.is_set or self.traffic_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_class.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "cos" or name == "dei" or name == "dei-imposition" or name == "destination-address" or name == "df" or name == "discard-class" or name == "dscp" or name == "forward-class" or name == "fr-de" or name == "inner-cos" or name == "mpls-experimental-imposition" or name == "mpls-experimental-top-most" or name == "precedence" or name == "precedence-tunnel" or name == "qos-group" or name == "source-address" or name == "srp-priority" or name == "traffic-class"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "cos"):
                                    self.cos = value
                                    self.cos.value_namespace = name_space
                                    self.cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei"):
                                    self.dei = value
                                    self.dei.value_namespace = name_space
                                    self.dei.value_namespace_prefix = name_space_prefix
                                if(value_path == "dei-imposition"):
                                    self.dei_imposition = value
                                    self.dei_imposition.value_namespace = name_space
                                    self.dei_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "destination-address"):
                                    self.destination_address = value
                                    self.destination_address.value_namespace = name_space
                                    self.destination_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "df"):
                                    self.df = value
                                    self.df.value_namespace = name_space
                                    self.df.value_namespace_prefix = name_space_prefix
                                if(value_path == "discard-class"):
                                    self.discard_class = value
                                    self.discard_class.value_namespace = name_space
                                    self.discard_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "dscp"):
                                    self.dscp = value
                                    self.dscp.value_namespace = name_space
                                    self.dscp.value_namespace_prefix = name_space_prefix
                                if(value_path == "forward-class"):
                                    self.forward_class = value
                                    self.forward_class.value_namespace = name_space
                                    self.forward_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "fr-de"):
                                    self.fr_de = value
                                    self.fr_de.value_namespace = name_space
                                    self.fr_de.value_namespace_prefix = name_space_prefix
                                if(value_path == "inner-cos"):
                                    self.inner_cos = value
                                    self.inner_cos.value_namespace = name_space
                                    self.inner_cos.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-imposition"):
                                    self.mpls_experimental_imposition = value
                                    self.mpls_experimental_imposition.value_namespace = name_space
                                    self.mpls_experimental_imposition.value_namespace_prefix = name_space_prefix
                                if(value_path == "mpls-experimental-top-most"):
                                    self.mpls_experimental_top_most = value
                                    self.mpls_experimental_top_most.value_namespace = name_space
                                    self.mpls_experimental_top_most.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence"):
                                    self.precedence = value
                                    self.precedence.value_namespace = name_space
                                    self.precedence.value_namespace_prefix = name_space_prefix
                                if(value_path == "precedence-tunnel"):
                                    self.precedence_tunnel = value
                                    self.precedence_tunnel.value_namespace = name_space
                                    self.precedence_tunnel.value_namespace_prefix = name_space_prefix
                                if(value_path == "qos-group"):
                                    self.qos_group = value
                                    self.qos_group.value_namespace = name_space
                                    self.qos_group.value_namespace_prefix = name_space_prefix
                                if(value_path == "source-address"):
                                    self.source_address = value
                                    self.source_address.value_namespace = name_space
                                    self.source_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "srp-priority"):
                                    self.srp_priority = value
                                    self.srp_priority.value_namespace = name_space
                                    self.srp_priority.value_namespace_prefix = name_space_prefix
                                if(value_path == "traffic-class"):
                                    self.traffic_class = value
                                    self.traffic_class.value_namespace = name_space
                                    self.traffic_class.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.drop.is_set or
                                self.transmit.is_set or
                                (self.set is not None and self.set.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.drop.yfilter != YFilter.not_set or
                                self.transmit.yfilter != YFilter.not_set or
                                (self.set is not None and self.set.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "violate-action" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.drop.is_set or self.drop.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.drop.get_name_leafdata())
                            if (self.transmit.is_set or self.transmit.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.transmit.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "set"):
                                if (self.set is None):
                                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set()
                                    self.set.parent = self
                                    self._children_name_map["set"] = "set"
                                return self.set

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "set" or name == "drop" or name == "Transmit"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "drop"):
                                self.drop = value
                                self.drop.value_namespace = name_space
                                self.drop.value_namespace_prefix = name_space_prefix
                            if(value_path == "Transmit"):
                                self.transmit = value
                                self.transmit.value_namespace = name_space
                                self.transmit.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.burst is not None and self.burst.has_data()) or
                            (self.conform_action is not None and self.conform_action.has_data()) or
                            (self.exceed_action is not None and self.exceed_action.has_data()) or
                            (self.peak_burst is not None and self.peak_burst.has_data()) or
                            (self.peak_rate is not None and self.peak_rate.has_data()) or
                            (self.rate is not None and self.rate.has_data()) or
                            (self.violate_action is not None and self.violate_action.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.burst is not None and self.burst.has_operation()) or
                            (self.conform_action is not None and self.conform_action.has_operation()) or
                            (self.exceed_action is not None and self.exceed_action.has_operation()) or
                            (self.peak_burst is not None and self.peak_burst.has_operation()) or
                            (self.peak_rate is not None and self.peak_rate.has_operation()) or
                            (self.rate is not None and self.rate.has_operation()) or
                            (self.violate_action is not None and self.violate_action.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "police" + path_buffer

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

                        if (child_yang_name == "burst"):
                            if (self.burst is None):
                                self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst()
                                self.burst.parent = self
                                self._children_name_map["burst"] = "burst"
                            return self.burst

                        if (child_yang_name == "conform-action"):
                            if (self.conform_action is None):
                                self.conform_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction()
                                self.conform_action.parent = self
                                self._children_name_map["conform_action"] = "conform-action"
                            return self.conform_action

                        if (child_yang_name == "exceed-action"):
                            if (self.exceed_action is None):
                                self.exceed_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction()
                                self.exceed_action.parent = self
                                self._children_name_map["exceed_action"] = "exceed-action"
                            return self.exceed_action

                        if (child_yang_name == "peak-burst"):
                            if (self.peak_burst is None):
                                self.peak_burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst()
                                self.peak_burst.parent = self
                                self._children_name_map["peak_burst"] = "peak-burst"
                            return self.peak_burst

                        if (child_yang_name == "peak-rate"):
                            if (self.peak_rate is None):
                                self.peak_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate()
                                self.peak_rate.parent = self
                                self._children_name_map["peak_rate"] = "peak-rate"
                            return self.peak_rate

                        if (child_yang_name == "rate"):
                            if (self.rate is None):
                                self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate()
                                self.rate.parent = self
                                self._children_name_map["rate"] = "rate"
                            return self.rate

                        if (child_yang_name == "violate-action"):
                            if (self.violate_action is None):
                                self.violate_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction()
                                self.violate_action.parent = self
                                self._children_name_map["violate_action"] = "violate-action"
                            return self.violate_action

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "burst" or name == "conform-action" or name == "exceed-action" or name == "peak-burst" or name == "peak-rate" or name == "rate" or name == "violate-action"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, self).__init__()

                        self.yang_name = "service-policy"
                        self.yang_parent_name = "policy-map-rule"

                        self.policy_name = YLeaf(YType.str, "policy-name")

                        self.type = YLeaf(YType.str, "type")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("policy_name",
                                        "type") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.policy_name.is_set or
                            self.type.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.policy_name.yfilter != YFilter.not_set or
                            self.type.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-policy" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.policy_name.is_set or self.policy_name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.policy_name.get_name_leafdata())
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
                        if(name == "policy-name" or name == "type"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "policy-name"):
                            self.policy_name = value
                            self.policy_name.value_namespace = name_space
                            self.policy_name.value_namespace_prefix = name_space_prefix
                        if(value_path == "type"):
                            self.type = value
                            self.type.value_namespace = name_space
                            self.type.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, self).__init__()

                        self.yang_name = "cac-local"
                        self.yang_parent_name = "policy-map-rule"

                        self.flow_idle_timeout = YLeaf(YType.str, "flow-idle-timeout")

                        self.flow_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate()
                        self.flow_rate.parent = self
                        self._children_name_map["flow_rate"] = "flow-rate"
                        self._children_yang_names.add("flow-rate")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("flow_idle_timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "cac-local"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, self).__init__()

                            self.yang_name = "flow-rate"
                            self.yang_parent_name = "cac-local"

                            self.units = YLeaf(YType.str, "units")

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
                                if name in ("units",
                                            "value") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.units.is_set or
                                self.value.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.units.yfilter != YFilter.not_set or
                                self.value.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "flow-rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.units.is_set or self.units.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.units.get_name_leafdata())
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
                            if(name == "units" or name == "value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "units"):
                                self.units = value
                                self.units.value_namespace = name_space
                                self.units.value_namespace_prefix = name_space_prefix
                            if(value_path == "value"):
                                self.value = value
                                self.value.value_namespace = name_space
                                self.value.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.flow_idle_timeout.is_set or
                            (self.flow_rate is not None and self.flow_rate.has_data()) or
                            (self.rate is not None and self.rate.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.flow_idle_timeout.yfilter != YFilter.not_set or
                            (self.flow_rate is not None and self.flow_rate.has_operation()) or
                            (self.rate is not None and self.rate.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "cac-local" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.flow_idle_timeout.is_set or self.flow_idle_timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.flow_idle_timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "flow-rate"):
                            if (self.flow_rate is None):
                                self.flow_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate()
                                self.flow_rate.parent = self
                                self._children_name_map["flow_rate"] = "flow-rate"
                            return self.flow_rate

                        if (child_yang_name == "rate"):
                            if (self.rate is None):
                                self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate()
                                self.rate.parent = self
                                self._children_name_map["rate"] = "rate"
                            return self.rate

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "flow-rate" or name == "rate" or name == "flow-idle-timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "flow-idle-timeout"):
                            self.flow_idle_timeout = value
                            self.flow_idle_timeout.value_namespace = name_space
                            self.flow_idle_timeout.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, self).__init__()

                        self.yang_name = "flow-params"
                        self.yang_parent_name = "policy-map-rule"

                        self.history = YLeaf(YType.uint32, "history")

                        self.interval_duration = YLeaf(YType.uint32, "interval-duration")

                        self.max_flow = YLeaf(YType.uint16, "max-flow")

                        self.timeout = YLeaf(YType.uint32, "timeout")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("history",
                                        "interval_duration",
                                        "max_flow",
                                        "timeout") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.history.is_set or
                            self.interval_duration.is_set or
                            self.max_flow.is_set or
                            self.timeout.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.history.yfilter != YFilter.not_set or
                            self.interval_duration.yfilter != YFilter.not_set or
                            self.max_flow.yfilter != YFilter.not_set or
                            self.timeout.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "flow-params" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.history.is_set or self.history.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.history.get_name_leafdata())
                        if (self.interval_duration.is_set or self.interval_duration.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interval_duration.get_name_leafdata())
                        if (self.max_flow.is_set or self.max_flow.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.max_flow.get_name_leafdata())
                        if (self.timeout.is_set or self.timeout.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.timeout.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "history" or name == "interval-duration" or name == "max-flow" or name == "timeout"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "history"):
                            self.history = value
                            self.history.value_namespace = name_space
                            self.history.value_namespace_prefix = name_space_prefix
                        if(value_path == "interval-duration"):
                            self.interval_duration = value
                            self.interval_duration.value_namespace = name_space
                            self.interval_duration.value_namespace_prefix = name_space_prefix
                        if(value_path == "max-flow"):
                            self.max_flow = value
                            self.max_flow.value_namespace = name_space
                            self.max_flow.value_namespace_prefix = name_space_prefix
                        if(value_path == "timeout"):
                            self.timeout = value
                            self.timeout.value_namespace = name_space
                            self.timeout.value_namespace_prefix = name_space_prefix


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr, self).__init__()

                        self.yang_name = "metrics-ipcbr"
                        self.yang_parent_name = "policy-map-rule"

                        self.media_packet = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket()
                        self.media_packet.parent = self
                        self._children_name_map["media_packet"] = "media-packet"
                        self._children_yang_names.add("media-packet")

                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate()
                        self.rate.parent = self
                        self._children_name_map["rate"] = "rate"
                        self._children_yang_names.add("rate")


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, self).__init__()

                            self.yang_name = "rate"
                            self.yang_parent_name = "metrics-ipcbr"

                            self.layer3 = YLeaf(YType.uint32, "layer3")

                            self.media = YLeaf(YType.uint32, "media")

                            self.packet = YLeaf(YType.uint32, "packet")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("layer3",
                                            "media",
                                            "packet") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.layer3.is_set or
                                self.media.is_set or
                                self.packet.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.layer3.yfilter != YFilter.not_set or
                                self.media.yfilter != YFilter.not_set or
                                self.packet.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "rate" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.layer3.is_set or self.layer3.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.layer3.get_name_leafdata())
                            if (self.media.is_set or self.media.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.media.get_name_leafdata())
                            if (self.packet.is_set or self.packet.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.packet.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "layer3" or name == "media" or name == "packet"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "layer3"):
                                self.layer3 = value
                                self.layer3.value_namespace = name_space
                                self.layer3.value_namespace_prefix = name_space_prefix
                            if(value_path == "media"):
                                self.media = value
                                self.media.value_namespace = name_space
                                self.media.value_namespace_prefix = name_space_prefix
                            if(value_path == "packet"):
                                self.packet = value
                                self.packet.value_namespace = name_space
                                self.packet.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, self).__init__()

                            self.yang_name = "media-packet"
                            self.yang_parent_name = "metrics-ipcbr"

                            self.count_in_layer3 = YLeaf(YType.uint8, "count-in-layer3")

                            self.size = YLeaf(YType.uint16, "size")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("count_in_layer3",
                                            "size") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.count_in_layer3.is_set or
                                self.size.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.count_in_layer3.yfilter != YFilter.not_set or
                                self.size.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "media-packet" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.count_in_layer3.is_set or self.count_in_layer3.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.count_in_layer3.get_name_leafdata())
                            if (self.size.is_set or self.size.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.size.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "count-in-layer3" or name == "size"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "count-in-layer3"):
                                self.count_in_layer3 = value
                                self.count_in_layer3.value_namespace = name_space
                                self.count_in_layer3.value_namespace_prefix = name_space_prefix
                            if(value_path == "size"):
                                self.size = value
                                self.size.value_namespace = name_space
                                self.size.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            (self.media_packet is not None and self.media_packet.has_data()) or
                            (self.rate is not None and self.rate.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.media_packet is not None and self.media_packet.has_operation()) or
                            (self.rate is not None and self.rate.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "metrics-ipcbr" + path_buffer

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

                        if (child_yang_name == "media-packet"):
                            if (self.media_packet is None):
                                self.media_packet = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket()
                                self.media_packet.parent = self
                                self._children_name_map["media_packet"] = "media-packet"
                            return self.media_packet

                        if (child_yang_name == "rate"):
                            if (self.rate is None):
                                self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate()
                                self.rate.parent = self
                                self._children_name_map["rate"] = "rate"
                            return self.rate

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "media-packet" or name == "rate"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, self).__init__()

                        self.yang_name = "react"
                        self.yang_parent_name = "policy-map-rule"

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

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("criterion_delay_factor",
                                        "criterion_flow_count",
                                        "criterion_media_stop",
                                        "criterion_mrv",
                                        "criterion_packet_rate",
                                        "descrition") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, self).__init__()

                            self.yang_name = "action"
                            self.yang_parent_name = "react"

                            self.snmp = YLeaf(YType.empty, "snmp")

                            self.syslog = YLeaf(YType.empty, "syslog")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("snmp",
                                            "syslog") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.snmp.is_set or
                                self.syslog.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.snmp.yfilter != YFilter.not_set or
                                self.syslog.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "action" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.snmp.is_set or self.snmp.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.snmp.get_name_leafdata())
                            if (self.syslog.is_set or self.syslog.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.syslog.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "snmp" or name == "syslog"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "snmp"):
                                self.snmp = value
                                self.snmp.value_namespace = name_space
                                self.snmp.value_namespace_prefix = name_space_prefix
                            if(value_path == "syslog"):
                                self.syslog = value
                                self.syslog.value_namespace = name_space
                                self.syslog.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, self).__init__()

                            self.yang_name = "alarm"
                            self.yang_parent_name = "react"

                            self.severity = YLeaf(YType.str, "severity")

                            self.type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type()
                            self.type.parent = self
                            self._children_name_map["type"] = "type"
                            self._children_yang_names.add("type")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("severity") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm, self).__setattr__(name, value)


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, self).__init__()

                                self.yang_name = "type"
                                self.yang_parent_name = "alarm"

                                self.discrete = YLeaf(YType.empty, "discrete")

                                self.group_count = YLeaf(YType.uint16, "group-count")

                                self.group_percent = YLeaf(YType.uint16, "group-percent")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("discrete",
                                                "group_count",
                                                "group_percent") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.discrete.is_set or
                                    self.group_count.is_set or
                                    self.group_percent.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.discrete.yfilter != YFilter.not_set or
                                    self.group_count.yfilter != YFilter.not_set or
                                    self.group_percent.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.discrete.is_set or self.discrete.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.discrete.get_name_leafdata())
                                if (self.group_count.is_set or self.group_count.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_count.get_name_leafdata())
                                if (self.group_percent.is_set or self.group_percent.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.group_percent.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "discrete" or name == "group-count" or name == "group-percent"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "discrete"):
                                    self.discrete = value
                                    self.discrete.value_namespace = name_space
                                    self.discrete.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-count"):
                                    self.group_count = value
                                    self.group_count.value_namespace = name_space
                                    self.group_count.value_namespace_prefix = name_space_prefix
                                if(value_path == "group-percent"):
                                    self.group_percent = value
                                    self.group_percent.value_namespace = name_space
                                    self.group_percent.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.severity.is_set or
                                (self.type is not None and self.type.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.severity.yfilter != YFilter.not_set or
                                (self.type is not None and self.type.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "alarm" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.severity.is_set or self.severity.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.severity.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "type"):
                                if (self.type is None):
                                    self.type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type()
                                    self.type.parent = self
                                    self._children_name_map["type"] = "type"
                                return self.type

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "type" or name == "severity"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "severity"):
                                self.severity = value
                                self.severity.value_namespace = name_space
                                self.severity.value_namespace_prefix = name_space_prefix


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold, self).__init__()

                            self.yang_name = "threshold"
                            self.yang_parent_name = "react"

                            self.trigger_type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType()
                            self.trigger_type.parent = self
                            self._children_name_map["trigger_type"] = "trigger-type"
                            self._children_yang_names.add("trigger-type")

                            self.trigger_value = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue()
                            self.trigger_value.parent = self
                            self._children_name_map["trigger_value"] = "trigger-value"
                            self._children_yang_names.add("trigger-value")


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, self).__init__()

                                self.yang_name = "trigger-value"
                                self.yang_parent_name = "threshold"

                                self.greater_than = YLeaf(YType.str, "greater-than")

                                self.greater_than_equal = YLeaf(YType.str, "greater-than-equal")

                                self.less_than = YLeaf(YType.str, "less-than")

                                self.less_than_equal = YLeaf(YType.str, "less-than-equal")

                                self.range = YLeaf(YType.str, "range")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("greater_than",
                                                "greater_than_equal",
                                                "less_than",
                                                "less_than_equal",
                                                "range") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.greater_than.is_set or
                                    self.greater_than_equal.is_set or
                                    self.less_than.is_set or
                                    self.less_than_equal.is_set or
                                    self.range.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.greater_than.yfilter != YFilter.not_set or
                                    self.greater_than_equal.yfilter != YFilter.not_set or
                                    self.less_than.yfilter != YFilter.not_set or
                                    self.less_than_equal.yfilter != YFilter.not_set or
                                    self.range.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "trigger-value" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.greater_than.is_set or self.greater_than.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.greater_than.get_name_leafdata())
                                if (self.greater_than_equal.is_set or self.greater_than_equal.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.greater_than_equal.get_name_leafdata())
                                if (self.less_than.is_set or self.less_than.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.less_than.get_name_leafdata())
                                if (self.less_than_equal.is_set or self.less_than_equal.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.less_than_equal.get_name_leafdata())
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
                                if(name == "greater-than" or name == "greater-than-equal" or name == "less-than" or name == "less-than-equal" or name == "range"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "greater-than"):
                                    self.greater_than = value
                                    self.greater_than.value_namespace = name_space
                                    self.greater_than.value_namespace_prefix = name_space_prefix
                                if(value_path == "greater-than-equal"):
                                    self.greater_than_equal = value
                                    self.greater_than_equal.value_namespace = name_space
                                    self.greater_than_equal.value_namespace_prefix = name_space_prefix
                                if(value_path == "less-than"):
                                    self.less_than = value
                                    self.less_than.value_namespace = name_space
                                    self.less_than.value_namespace_prefix = name_space_prefix
                                if(value_path == "less-than-equal"):
                                    self.less_than_equal = value
                                    self.less_than_equal.value_namespace = name_space
                                    self.less_than_equal.value_namespace_prefix = name_space_prefix
                                if(value_path == "range"):
                                    self.range = value
                                    self.range.value_namespace = name_space
                                    self.range.value_namespace_prefix = name_space_prefix


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, self).__init__()

                                self.yang_name = "trigger-type"
                                self.yang_parent_name = "threshold"

                                self.average = YLeaf(YType.uint32, "average")

                                self.immediate = YLeaf(YType.empty, "immediate")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("average",
                                                "immediate") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.average.is_set or
                                    self.immediate.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.average.yfilter != YFilter.not_set or
                                    self.immediate.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "trigger-type" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.average.is_set or self.average.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.average.get_name_leafdata())
                                if (self.immediate.is_set or self.immediate.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.immediate.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "average" or name == "immediate"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "average"):
                                    self.average = value
                                    self.average.value_namespace = name_space
                                    self.average.value_namespace_prefix = name_space_prefix
                                if(value_path == "immediate"):
                                    self.immediate = value
                                    self.immediate.value_namespace = name_space
                                    self.immediate.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                (self.trigger_type is not None and self.trigger_type.has_data()) or
                                (self.trigger_value is not None and self.trigger_value.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.trigger_type is not None and self.trigger_type.has_operation()) or
                                (self.trigger_value is not None and self.trigger_value.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "threshold" + path_buffer

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

                            if (child_yang_name == "trigger-type"):
                                if (self.trigger_type is None):
                                    self.trigger_type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerType()
                                    self.trigger_type.parent = self
                                    self._children_name_map["trigger_type"] = "trigger-type"
                                return self.trigger_type

                            if (child_yang_name == "trigger-value"):
                                if (self.trigger_value is None):
                                    self.trigger_value = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold.TriggerValue()
                                    self.trigger_value.parent = self
                                    self._children_name_map["trigger_value"] = "trigger-value"
                                return self.trigger_value

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "trigger-type" or name == "trigger-value"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.criterion_delay_factor.is_set or
                            self.criterion_flow_count.is_set or
                            self.criterion_media_stop.is_set or
                            self.criterion_mrv.is_set or
                            self.criterion_packet_rate.is_set or
                            self.descrition.is_set or
                            (self.action is not None and self.action.has_data()) or
                            (self.alarm is not None and self.alarm.has_data()) or
                            (self.threshold is not None and self.threshold.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.criterion_delay_factor.yfilter != YFilter.not_set or
                            self.criterion_flow_count.yfilter != YFilter.not_set or
                            self.criterion_media_stop.yfilter != YFilter.not_set or
                            self.criterion_mrv.yfilter != YFilter.not_set or
                            self.criterion_packet_rate.yfilter != YFilter.not_set or
                            self.descrition.yfilter != YFilter.not_set or
                            (self.action is not None and self.action.has_operation()) or
                            (self.alarm is not None and self.alarm.has_operation()) or
                            (self.threshold is not None and self.threshold.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "react" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.criterion_delay_factor.is_set or self.criterion_delay_factor.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.criterion_delay_factor.get_name_leafdata())
                        if (self.criterion_flow_count.is_set or self.criterion_flow_count.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.criterion_flow_count.get_name_leafdata())
                        if (self.criterion_media_stop.is_set or self.criterion_media_stop.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.criterion_media_stop.get_name_leafdata())
                        if (self.criterion_mrv.is_set or self.criterion_mrv.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.criterion_mrv.get_name_leafdata())
                        if (self.criterion_packet_rate.is_set or self.criterion_packet_rate.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.criterion_packet_rate.get_name_leafdata())
                        if (self.descrition.is_set or self.descrition.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.descrition.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "action"):
                            if (self.action is None):
                                self.action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action()
                                self.action.parent = self
                                self._children_name_map["action"] = "action"
                            return self.action

                        if (child_yang_name == "alarm"):
                            if (self.alarm is None):
                                self.alarm = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm()
                                self.alarm.parent = self
                                self._children_name_map["alarm"] = "alarm"
                            return self.alarm

                        if (child_yang_name == "threshold"):
                            if (self.threshold is None):
                                self.threshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Threshold()
                                self.threshold.parent = self
                                self._children_name_map["threshold"] = "threshold"
                            return self.threshold

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "action" or name == "alarm" or name == "threshold" or name == "criterion-delay-factor" or name == "criterion-flow-count" or name == "criterion-media-stop" or name == "criterion-mrv" or name == "criterion-packet-rate" or name == "descrition"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "criterion-delay-factor"):
                            self.criterion_delay_factor = value
                            self.criterion_delay_factor.value_namespace = name_space
                            self.criterion_delay_factor.value_namespace_prefix = name_space_prefix
                        if(value_path == "criterion-flow-count"):
                            self.criterion_flow_count = value
                            self.criterion_flow_count.value_namespace = name_space
                            self.criterion_flow_count.value_namespace_prefix = name_space_prefix
                        if(value_path == "criterion-media-stop"):
                            self.criterion_media_stop = value
                            self.criterion_media_stop.value_namespace = name_space
                            self.criterion_media_stop.value_namespace_prefix = name_space_prefix
                        if(value_path == "criterion-mrv"):
                            self.criterion_mrv = value
                            self.criterion_mrv.value_namespace = name_space
                            self.criterion_mrv.value_namespace_prefix = name_space_prefix
                        if(value_path == "criterion-packet-rate"):
                            self.criterion_packet_rate = value
                            self.criterion_packet_rate.value_namespace = name_space
                            self.criterion_packet_rate.value_namespace_prefix = name_space_prefix
                        if(value_path == "descrition"):
                            self.descrition = value
                            self.descrition.value_namespace = name_space
                            self.descrition.value_namespace_prefix = name_space_prefix


                class PbrRedirect(Entity):
                    """
                    Policy action redirect
                    
                    .. attribute:: next_hop
                    
                    	Next hop address
                    	**type**\:   :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop>`
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect, self).__init__()

                        self.yang_name = "pbr-redirect"
                        self.yang_parent_name = "policy-map-rule"

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")


                    class NextHop(Entity):
                        """
                        Next hop address.
                        
                        .. attribute:: route_target
                        
                        	Route Target
                        	**type**\:   :py:class:`RouteTarget <ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget>`
                        
                        

                        """

                        _prefix = 'infra-policymgr-cfg'
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-redirect"

                            self.route_target = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget()
                            self.route_target.parent = self
                            self._children_name_map["route_target"] = "route-target"
                            self._children_yang_names.add("route-target")


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
                            _revision = '2017-03-03'

                            def __init__(self):
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, self).__init__()

                                self.yang_name = "route-target"
                                self.yang_parent_name = "next-hop"

                                self.as_number = YLeaf(YType.uint32, "as-number")

                                self.index = YLeaf(YType.uint32, "index")

                                self.ipv4_address = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address()
                                self.ipv4_address.parent = self
                                self._children_name_map["ipv4_address"] = "ipv4-address"
                                self._children_yang_names.add("ipv4-address")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("as_number",
                                                "index") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget, self).__setattr__(name, value)


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
                                _revision = '2017-03-03'

                                def __init__(self):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, self).__init__()

                                    self.yang_name = "ipv4-address"
                                    self.yang_parent_name = "route-target"

                                    self.address = YLeaf(YType.str, "address")

                                    self.netmask = YLeaf(YType.str, "netmask")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("address",
                                                    "netmask") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.address.is_set or
                                        self.netmask.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.address.yfilter != YFilter.not_set or
                                        self.netmask.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv4-address" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.address.is_set or self.address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.address.get_name_leafdata())
                                    if (self.netmask.is_set or self.netmask.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.netmask.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "address" or name == "netmask"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "address"):
                                        self.address = value
                                        self.address.value_namespace = name_space
                                        self.address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "netmask"):
                                        self.netmask = value
                                        self.netmask.value_namespace = name_space
                                        self.netmask.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.as_number.is_set or
                                    self.index.is_set or
                                    (self.ipv4_address is not None and self.ipv4_address.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.as_number.yfilter != YFilter.not_set or
                                    self.index.yfilter != YFilter.not_set or
                                    (self.ipv4_address is not None and self.ipv4_address.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "route-target" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.as_number.is_set or self.as_number.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.as_number.get_name_leafdata())
                                if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.index.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipv4-address"):
                                    if (self.ipv4_address is None):
                                        self.ipv4_address = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget.Ipv4Address()
                                        self.ipv4_address.parent = self
                                        self._children_name_map["ipv4_address"] = "ipv4-address"
                                    return self.ipv4_address

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-address" or name == "as-number" or name == "index"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "as-number"):
                                    self.as_number = value
                                    self.as_number.value_namespace = name_space
                                    self.as_number.value_namespace_prefix = name_space_prefix
                                if(value_path == "index"):
                                    self.index = value
                                    self.index.value_namespace = name_space
                                    self.index.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (self.route_target is not None and self.route_target.has_data())

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                (self.route_target is not None and self.route_target.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + path_buffer

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

                            if (child_yang_name == "route-target"):
                                if (self.route_target is None):
                                    self.route_target = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop.RouteTarget()
                                    self.route_target.parent = self
                                    self._children_name_map["route_target"] = "route-target"
                                return self.route_target

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "route-target"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (self.next_hop is not None and self.next_hop.has_data())

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            (self.next_hop is not None and self.next_hop.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pbr-redirect" + path_buffer

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

                        if (child_yang_name == "next-hop"):
                            if (self.next_hop is None):
                                self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                            return self.next_hop

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        pass


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
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, self).__init__()

                        self.yang_name = "pbr-forward"
                        self.yang_parent_name = "policy-map-rule"

                        self.default = YLeaf(YType.empty, "default")

                        self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop()
                        self.next_hop.parent = self
                        self._children_name_map["next_hop"] = "next-hop"
                        self._children_yang_names.add("next-hop")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("default") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward, self).__setattr__(name, value)


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
                        _revision = '2017-03-03'

                        def __init__(self):
                            super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, self).__init__()

                            self.yang_name = "next-hop"
                            self.yang_parent_name = "pbr-forward"

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf = YLeaf(YType.str, "vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv4_address",
                                            "ipv6_address",
                                            "vrf") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ipv4_address.is_set or
                                self.ipv6_address.is_set or
                                self.vrf.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set or
                                self.vrf.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                            if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-address" or name == "ipv6-address" or name == "vrf"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf"):
                                self.vrf = value
                                self.vrf.value_namespace = name_space
                                self.vrf.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.default.is_set or
                            (self.next_hop is not None and self.next_hop.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.default.yfilter != YFilter.not_set or
                            (self.next_hop is not None and self.next_hop.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "pbr-forward" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.default.is_set or self.default.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.default.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "next-hop"):
                            if (self.next_hop is None):
                                self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward.NextHop()
                                self.next_hop.parent = self
                                self._children_name_map["next_hop"] = "next-hop"
                            return self.next_hop

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "next-hop" or name == "default"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "default"):
                            self.default = value
                            self.default.value_namespace = name_space
                            self.default.value_namespace_prefix = name_space_prefix


                class ServiceFunctionPath(Entity):
                    """
                    Policy action service function path.
                    
                    .. attribute:: index
                    
                    	Service function path index
                    	**type**\:  int
                    
                    	**range:** 1..255
                    
                    .. attribute:: metadata
                    
                    	Service function path metadata name
                    	**type**\:  str
                    
                    .. attribute:: path_id
                    
                    	Service function path id
                    	**type**\:  int
                    
                    	**range:** 1..16777215
                    
                    

                    """

                    _prefix = 'infra-policymgr-cfg'
                    _revision = '2017-03-03'

                    def __init__(self):
                        super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, self).__init__()

                        self.yang_name = "service-function-path"
                        self.yang_parent_name = "policy-map-rule"

                        self.index = YLeaf(YType.uint8, "index")

                        self.metadata = YLeaf(YType.str, "metadata")

                        self.path_id = YLeaf(YType.uint32, "path-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("index",
                                        "metadata",
                                        "path_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.index.is_set or
                            self.metadata.is_set or
                            self.path_id.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.index.yfilter != YFilter.not_set or
                            self.metadata.yfilter != YFilter.not_set or
                            self.path_id.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "service-function-path" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.index.is_set or self.index.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.index.get_name_leafdata())
                        if (self.metadata.is_set or self.metadata.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.metadata.get_name_leafdata())
                        if (self.path_id.is_set or self.path_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.path_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "index" or name == "metadata" or name == "path-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "index"):
                            self.index = value
                            self.index.value_namespace = name_space
                            self.index.value_namespace_prefix = name_space_prefix
                        if(value_path == "metadata"):
                            self.metadata = value
                            self.metadata.value_namespace = name_space
                            self.metadata.value_namespace_prefix = name_space_prefix
                        if(value_path == "path-id"):
                            self.path_id = value
                            self.path_id.value_namespace = name_space
                            self.path_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.random_detect:
                        if (c.has_data()):
                            return True
                    return (
                        self.class_name.is_set or
                        self.class_type.is_set or
                        self.decap_gre.is_set or
                        self.default_red.is_set or
                        self.ecn_red.is_set or
                        self.fragment.is_set or
                        self.http_redirect.is_set or
                        self.pbr_drop.is_set or
                        self.pbr_transmit.is_set or
                        self.priority_level.is_set or
                        self.service_fragment.is_set or
                        (self.bandwidth_remaining is not None and self.bandwidth_remaining.has_data()) or
                        (self.cac_local is not None and self.cac_local.has_data()) or
                        (self.flow_params is not None and self.flow_params.has_data()) or
                        (self.metrics_ipcbr is not None and self.metrics_ipcbr.has_data()) or
                        (self.min_bandwidth is not None and self.min_bandwidth.has_data()) or
                        (self.pbr_forward is not None and self.pbr_forward.has_data()) or
                        (self.pbr_redirect is not None and self.pbr_redirect.has_data()) or
                        (self.pfc is not None and self.pfc.has_data()) or
                        (self.police is not None and self.police.has_data()) or
                        (self.queue_limit is not None and self.queue_limit.has_data()) or
                        (self.react is not None and self.react.has_data()) or
                        (self.service_function_path is not None and self.service_function_path.has_data()) or
                        (self.service_policy is not None and self.service_policy.has_data()) or
                        (self.set is not None and self.set.has_data()) or
                        (self.shape is not None and self.shape.has_data()))

                def has_operation(self):
                    for c in self.random_detect:
                        if (c.has_operation()):
                            return True
                    return (
                        self.yfilter != YFilter.not_set or
                        self.class_name.yfilter != YFilter.not_set or
                        self.class_type.yfilter != YFilter.not_set or
                        self.decap_gre.yfilter != YFilter.not_set or
                        self.default_red.yfilter != YFilter.not_set or
                        self.ecn_red.yfilter != YFilter.not_set or
                        self.fragment.yfilter != YFilter.not_set or
                        self.http_redirect.yfilter != YFilter.not_set or
                        self.pbr_drop.yfilter != YFilter.not_set or
                        self.pbr_transmit.yfilter != YFilter.not_set or
                        self.priority_level.yfilter != YFilter.not_set or
                        self.service_fragment.yfilter != YFilter.not_set or
                        (self.bandwidth_remaining is not None and self.bandwidth_remaining.has_operation()) or
                        (self.cac_local is not None and self.cac_local.has_operation()) or
                        (self.flow_params is not None and self.flow_params.has_operation()) or
                        (self.metrics_ipcbr is not None and self.metrics_ipcbr.has_operation()) or
                        (self.min_bandwidth is not None and self.min_bandwidth.has_operation()) or
                        (self.pbr_forward is not None and self.pbr_forward.has_operation()) or
                        (self.pbr_redirect is not None and self.pbr_redirect.has_operation()) or
                        (self.pfc is not None and self.pfc.has_operation()) or
                        (self.police is not None and self.police.has_operation()) or
                        (self.queue_limit is not None and self.queue_limit.has_operation()) or
                        (self.react is not None and self.react.has_operation()) or
                        (self.service_function_path is not None and self.service_function_path.has_operation()) or
                        (self.service_policy is not None and self.service_policy.has_operation()) or
                        (self.set is not None and self.set.has_operation()) or
                        (self.shape is not None and self.shape.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "policy-map-rule" + "[class-name='" + self.class_name.get() + "']" + "[class-type='" + self.class_type.get() + "']" + path_buffer

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
                    if (self.class_type.is_set or self.class_type.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.class_type.get_name_leafdata())
                    if (self.decap_gre.is_set or self.decap_gre.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.decap_gre.get_name_leafdata())
                    if (self.default_red.is_set or self.default_red.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.default_red.get_name_leafdata())
                    if (self.ecn_red.is_set or self.ecn_red.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.ecn_red.get_name_leafdata())
                    if (self.fragment.is_set or self.fragment.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.fragment.get_name_leafdata())
                    if (self.http_redirect.is_set or self.http_redirect.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.http_redirect.get_name_leafdata())
                    if (self.pbr_drop.is_set or self.pbr_drop.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pbr_drop.get_name_leafdata())
                    if (self.pbr_transmit.is_set or self.pbr_transmit.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.pbr_transmit.get_name_leafdata())
                    if (self.priority_level.is_set or self.priority_level.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.priority_level.get_name_leafdata())
                    if (self.service_fragment.is_set or self.service_fragment.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.service_fragment.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "bandwidth-remaining"):
                        if (self.bandwidth_remaining is None):
                            self.bandwidth_remaining = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining()
                            self.bandwidth_remaining.parent = self
                            self._children_name_map["bandwidth_remaining"] = "bandwidth-remaining"
                        return self.bandwidth_remaining

                    if (child_yang_name == "cac-local"):
                        if (self.cac_local is None):
                            self.cac_local = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal()
                            self.cac_local.parent = self
                            self._children_name_map["cac_local"] = "cac-local"
                        return self.cac_local

                    if (child_yang_name == "flow-params"):
                        if (self.flow_params is None):
                            self.flow_params = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams()
                            self.flow_params.parent = self
                            self._children_name_map["flow_params"] = "flow-params"
                        return self.flow_params

                    if (child_yang_name == "metrics-ipcbr"):
                        if (self.metrics_ipcbr is None):
                            self.metrics_ipcbr = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr()
                            self.metrics_ipcbr.parent = self
                            self._children_name_map["metrics_ipcbr"] = "metrics-ipcbr"
                        return self.metrics_ipcbr

                    if (child_yang_name == "min-bandwidth"):
                        if (self.min_bandwidth is None):
                            self.min_bandwidth = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth()
                            self.min_bandwidth.parent = self
                            self._children_name_map["min_bandwidth"] = "min-bandwidth"
                        return self.min_bandwidth

                    if (child_yang_name == "pbr-forward"):
                        if (self.pbr_forward is None):
                            self.pbr_forward = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrForward()
                            self.pbr_forward.parent = self
                            self._children_name_map["pbr_forward"] = "pbr-forward"
                        return self.pbr_forward

                    if (child_yang_name == "pbr-redirect"):
                        if (self.pbr_redirect is None):
                            self.pbr_redirect = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.PbrRedirect()
                            self.pbr_redirect.parent = self
                            self._children_name_map["pbr_redirect"] = "pbr-redirect"
                        return self.pbr_redirect

                    if (child_yang_name == "pfc"):
                        if (self.pfc is None):
                            self.pfc = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pfc()
                            self.pfc.parent = self
                            self._children_name_map["pfc"] = "pfc"
                        return self.pfc

                    if (child_yang_name == "police"):
                        if (self.police is None):
                            self.police = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police()
                            self.police.parent = self
                            self._children_name_map["police"] = "police"
                        return self.police

                    if (child_yang_name == "queue-limit"):
                        if (self.queue_limit is None):
                            self.queue_limit = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit()
                            self.queue_limit.parent = self
                            self._children_name_map["queue_limit"] = "queue-limit"
                        return self.queue_limit

                    if (child_yang_name == "random-detect"):
                        for c in self.random_detect:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.random_detect.append(c)
                        return c

                    if (child_yang_name == "react"):
                        if (self.react is None):
                            self.react = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React()
                            self.react.parent = self
                            self._children_name_map["react"] = "react"
                        return self.react

                    if (child_yang_name == "service-function-path"):
                        if (self.service_function_path is None):
                            self.service_function_path = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServiceFunctionPath()
                            self.service_function_path.parent = self
                            self._children_name_map["service_function_path"] = "service-function-path"
                        return self.service_function_path

                    if (child_yang_name == "service-policy"):
                        if (self.service_policy is None):
                            self.service_policy = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy()
                            self.service_policy.parent = self
                            self._children_name_map["service_policy"] = "service-policy"
                        return self.service_policy

                    if (child_yang_name == "set"):
                        if (self.set is None):
                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set()
                            self.set.parent = self
                            self._children_name_map["set"] = "set"
                        return self.set

                    if (child_yang_name == "shape"):
                        if (self.shape is None):
                            self.shape = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape()
                            self.shape.parent = self
                            self._children_name_map["shape"] = "shape"
                        return self.shape

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bandwidth-remaining" or name == "cac-local" or name == "flow-params" or name == "metrics-ipcbr" or name == "min-bandwidth" or name == "pbr-forward" or name == "pbr-redirect" or name == "pfc" or name == "police" or name == "queue-limit" or name == "random-detect" or name == "react" or name == "service-function-path" or name == "service-policy" or name == "set" or name == "shape" or name == "class-name" or name == "class-type" or name == "decap-gre" or name == "default-red" or name == "ecn-red" or name == "fragment" or name == "http-redirect" or name == "pbr-drop" or name == "pbr-transmit" or name == "priority-level" or name == "service-fragment"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "class-name"):
                        self.class_name = value
                        self.class_name.value_namespace = name_space
                        self.class_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "class-type"):
                        self.class_type = value
                        self.class_type.value_namespace = name_space
                        self.class_type.value_namespace_prefix = name_space_prefix
                    if(value_path == "decap-gre"):
                        self.decap_gre = value
                        self.decap_gre.value_namespace = name_space
                        self.decap_gre.value_namespace_prefix = name_space_prefix
                    if(value_path == "default-red"):
                        self.default_red = value
                        self.default_red.value_namespace = name_space
                        self.default_red.value_namespace_prefix = name_space_prefix
                    if(value_path == "ecn-red"):
                        self.ecn_red = value
                        self.ecn_red.value_namespace = name_space
                        self.ecn_red.value_namespace_prefix = name_space_prefix
                    if(value_path == "fragment"):
                        self.fragment = value
                        self.fragment.value_namespace = name_space
                        self.fragment.value_namespace_prefix = name_space_prefix
                    if(value_path == "http-redirect"):
                        self.http_redirect = value
                        self.http_redirect.value_namespace = name_space
                        self.http_redirect.value_namespace_prefix = name_space_prefix
                    if(value_path == "pbr-drop"):
                        self.pbr_drop = value
                        self.pbr_drop.value_namespace = name_space
                        self.pbr_drop.value_namespace_prefix = name_space_prefix
                    if(value_path == "pbr-transmit"):
                        self.pbr_transmit = value
                        self.pbr_transmit.value_namespace = name_space
                        self.pbr_transmit.value_namespace_prefix = name_space_prefix
                    if(value_path == "priority-level"):
                        self.priority_level = value
                        self.priority_level.value_namespace = name_space
                        self.priority_level.value_namespace_prefix = name_space_prefix
                    if(value_path == "service-fragment"):
                        self.service_fragment = value
                        self.service_fragment.value_namespace = name_space
                        self.service_fragment.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.event:
                    if (c.has_data()):
                        return True
                for c in self.policy_map_rule:
                    if (c.has_data()):
                        return True
                return (
                    self.type.is_set or
                    self.name.is_set or
                    self.description.is_set)

            def has_operation(self):
                for c in self.event:
                    if (c.has_operation()):
                        return True
                for c in self.policy_map_rule:
                    if (c.has_operation()):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.type.yfilter != YFilter.not_set or
                    self.name.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "policy-map" + "[type='" + self.type.get() + "']" + "[name='" + self.name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/policy-maps/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.type.is_set or self.type.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.type.get_name_leafdata())
                if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.name.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "event"):
                    for c in self.event:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = PolicyManager.PolicyMaps.PolicyMap.Event()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.event.append(c)
                    return c

                if (child_yang_name == "policy-map-rule"):
                    for c in self.policy_map_rule:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.policy_map_rule.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "event" or name == "policy-map-rule" or name == "type" or name == "name" or name == "description"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "type"):
                    self.type = value
                    self.type.value_namespace = name_space
                    self.type.value_namespace_prefix = name_space_prefix
                if(value_path == "name"):
                    self.name = value
                    self.name.value_namespace = name_space
                    self.name.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.policy_map:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.policy_map:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "policy-maps" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "policy-map"):
                for c in self.policy_map:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = PolicyManager.PolicyMaps.PolicyMap()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.policy_map.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "policy-map"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.class_maps is not None and self.class_maps.has_data()) or
            (self.policy_maps is not None and self.policy_maps.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.class_maps is not None and self.class_maps.has_operation()) or
            (self.policy_maps is not None and self.policy_maps.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-infra-policymgr-cfg:policy-manager" + path_buffer

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

        if (child_yang_name == "class-maps"):
            if (self.class_maps is None):
                self.class_maps = PolicyManager.ClassMaps()
                self.class_maps.parent = self
                self._children_name_map["class_maps"] = "class-maps"
            return self.class_maps

        if (child_yang_name == "policy-maps"):
            if (self.policy_maps is None):
                self.policy_maps = PolicyManager.PolicyMaps()
                self.policy_maps.parent = self
                self._children_name_map["policy_maps"] = "policy-maps"
            return self.policy_maps

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "class-maps" or name == "policy-maps"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = PolicyManager()
        return self._top_entity

