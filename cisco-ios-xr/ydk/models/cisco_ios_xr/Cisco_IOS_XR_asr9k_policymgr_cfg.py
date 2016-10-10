""" Cisco_IOS_XR_asr9k_policymgr_cfg 

This module contains a collection of YANG definitions
for Cisco IOS\-XR ASR9k policy manager configuration.

Copyright (c) 2013, 2015\-2016 by Cisco Systems, Inc.
All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class AuthorizeIdentifierEnum(Enum):
    """
    AuthorizeIdentifierEnum

    Authorize identifier.

    .. data:: CIRCUIT_ID = 0

    	Authorize circuit ID.

    .. data:: REMOTE_ID = 1

    	Authorize remote ID.

    .. data:: SOURCE_ADDRESS_IPV4 = 2

    	Authorize source IPv4 address.

    .. data:: SOURCE_ADDRESS_IPV6 = 3

    	Authorize source IPv6 address.

    .. data:: SOURCE_ADDRESS_MAC = 4

    	Authorize source MAC address.

    .. data:: USERNAME = 5

    	Authorize username.

    """

    CIRCUIT_ID = 0

    REMOTE_ID = 1

    SOURCE_ADDRESS_IPV4 = 2

    SOURCE_ADDRESS_IPV6 = 3

    SOURCE_ADDRESS_MAC = 4

    USERNAME = 5


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['AuthorizeIdentifierEnum']


class ClassMapTypeEnum(Enum):
    """
    ClassMapTypeEnum

    Policy manager class\-map type.

    .. data:: QOS = 1

    	QoS Classmap.

    .. data:: TRAFFIC = 3

    	TRAFFIC Classmap.

    .. data:: CONTROL = 4

    	Control Subscriber Classmap.

    """

    QOS = 1

    TRAFFIC = 3

    CONTROL = 4


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['ClassMapTypeEnum']


class EventTypeEnum(Enum):
    """
    EventTypeEnum

    Event type.

    .. data:: ACCOUNT_LOGOFF = 0

    	Account logoff event.

    .. data:: ACCOUNT_LOGON = 1

    	Account logon event.

    .. data:: AUTHENTICATION_FAILURE = 2

    	Authentication failure event.

    .. data:: AUTHENTICATION_NO_RESPONSE = 3

    	Authentication no response event.

    .. data:: AUTHORIZATION_FAILURE = 4

    	Authorization failure event.

    .. data:: AUTHORIZATION_NO_RESPONSE = 5

    	Authorization no response event.

    .. data:: CREDIT_EXHAUSTED = 6

    	Credit exhaustion event.

    .. data:: EXCEPTION = 7

    	Exception event.

    .. data:: IDLE_TIMEOUT = 8

    	Idle timeout event.

    .. data:: QUOTA_DEPLETED = 9

    	Quota depletion event.

    .. data:: SERVICE_START = 10

    	Service start event.

    .. data:: SERVICE_STOP = 11

    	Service stop event.

    .. data:: SESSION_ACTIVATE = 12

    	Session activate event.

    .. data:: SESSION_START = 13

    	Session start event.

    .. data:: SESSION_STOP = 14

    	Session stop event.

    .. data:: TIMER_EXPIRY = 15

    	Timer expiry event.

    """

    ACCOUNT_LOGOFF = 0

    ACCOUNT_LOGON = 1

    AUTHENTICATION_FAILURE = 2

    AUTHENTICATION_NO_RESPONSE = 3

    AUTHORIZATION_FAILURE = 4

    AUTHORIZATION_NO_RESPONSE = 5

    CREDIT_EXHAUSTED = 6

    EXCEPTION = 7

    IDLE_TIMEOUT = 8

    QUOTA_DEPLETED = 9

    SERVICE_START = 10

    SERVICE_STOP = 11

    SESSION_ACTIVATE = 12

    SESSION_START = 13

    SESSION_STOP = 14

    TIMER_EXPIRY = 15


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['EventTypeEnum']


class ExecutionStrategyEnum(Enum):
    """
    ExecutionStrategyEnum

    Executuion strategy.

    .. data:: DO_ALL = 0

    	Do all actions.

    .. data:: DO_UNTIL_FAILURE = 1

    	Do all actions until failure.

    .. data:: DO_UNTIL_SUCCESS = 2

    	Do all actions until success.

    """

    DO_ALL = 0

    DO_UNTIL_FAILURE = 1

    DO_UNTIL_SUCCESS = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['ExecutionStrategyEnum']


class PmapClassMapTypeEnum(Enum):
    """
    PmapClassMapTypeEnum

    Policy manager class\-map type.

    .. data:: QOS = 1

    	QoS Classmap.

    .. data:: TRAFFIC = 2

    	TRAFFIC Classmap.

    .. data:: SUBSCRIBER_CONTROL = 3

    	Subscriber Control Classmap.

    """

    QOS = 1

    TRAFFIC = 2

    SUBSCRIBER_CONTROL = 3


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['PmapClassMapTypeEnum']


class PolicyMapTypeEnum(Enum):
    """
    PolicyMapTypeEnum

    Policy manager policy\-map type.

    .. data:: QOS = 1

    	QoS Policymap

    .. data:: PBR = 2

    	PBR Policymap

    .. data:: TRAFFIC = 3

    	TRAFFIC Policymap

    .. data:: SUBSCRIBER_CONTROL = 4

    	SUBSCRIBER-CONTROL Policymap

    .. data:: REDIRECT = 6

    	REDIRECT Policy map

    .. data:: FLOW_MONITOR = 7

    	FLOWMONITOR Policy map

    """

    QOS = 1

    PBR = 2

    TRAFFIC = 3

    SUBSCRIBER_CONTROL = 4

    REDIRECT = 6

    FLOW_MONITOR = 7


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['PolicyMapTypeEnum']



class PolicyManager(object):
    """
    Global Policy Manager configuration.
    
    .. attribute:: class_maps
    
    	Class\-maps configuration
    	**type**\:  :py:class:`ClassMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps>`
    
    .. attribute:: policy_maps
    
    	Policy\-maps configuration
    	**type**\:  :py:class:`PolicyMaps <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps>`
    
    

    """

    _prefix = 'asr9k-policymgr-cfg'
    _revision = '2015-05-18'

    def __init__(self):
        self.class_maps = PolicyManager.ClassMaps()
        self.class_maps.parent = self
        self.policy_maps = PolicyManager.PolicyMaps()
        self.policy_maps.parent = self


    class ClassMaps(object):
        """
        Class\-maps configuration.
        
        .. attribute:: class_map
        
        	Class\-map configuration
        	**type**\: list of  :py:class:`ClassMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap>`
        
        

        """

        _prefix = 'asr9k-policymgr-cfg'
        _revision = '2015-05-18'

        def __init__(self):
            self.parent = None
            self.class_map = YList()
            self.class_map.parent = self
            self.class_map.name = 'class_map'


        class ClassMap(object):
            """
            Class\-map configuration.
            
            .. attribute:: name  <key>
            
            	Name of class\-map
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: type  <key>
            
            	Type of class\-map
            	**type**\:  :py:class:`ClassMapTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.ClassMapTypeEnum>`
            
            .. attribute:: class_map_mode_match_all
            
            	Match any match criteria
            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: class_map_mode_match_any
            
            	Match all match criteria
            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\:  str
            
            .. attribute:: match
            
            	Match rules
            	**type**\:  :py:class:`Match <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match>`
            
            .. attribute:: match_not
            
            	Match not rules
            	**type**\:  :py:class:`MatchNot <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot>`
            
            

            """

            _prefix = 'asr9k-policymgr-cfg'
            _revision = '2015-05-18'

            def __init__(self):
                self.parent = None
                self.name = None
                self.type = None
                self.class_map_mode_match_all = None
                self.class_map_mode_match_any = None
                self.description = None
                self.match = PolicyManager.ClassMaps.ClassMap.Match()
                self.match.parent = self
                self.match_not = PolicyManager.ClassMaps.ClassMap.MatchNot()
                self.match_not.parent = self


            class Match(object):
                """
                Match rules.
                
                .. attribute:: atm_clp
                
                	Match ATM CLP bit
                	**type**\:  int
                
                	**range:** 0..1
                
                .. attribute:: atm_oam
                
                	Match ATM OAM
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\:  str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: cac_admit
                
                	Match CAC admitted
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: cac_unadmit
                
                	Match CAC unadmitted
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of  :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of  :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6>`
                
                .. attribute:: destination_mac
                
                	Match destination MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of  :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.DomainName>`
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\:  list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
                .. attribute:: flow
                
                	Match flow
                	**type**\:  :py:class:`Flow <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow>`
                
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
                
                	**range:** 1..64
                
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
                
                	**range:** 1..64
                
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
                
                	**range:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\:  str
                
                	**range:** 1..32
                
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
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of  :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of  :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6>`
                
                .. attribute:: source_mac
                
                	Match source MAC address
                	**type**\:  str
                
                	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flag
                	**type**\:  int
                
                	**range:** 1..4095
                
                .. attribute:: timer
                
                	Match timer
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                

                """

                _prefix = 'asr9k-policymgr-cfg'
                _revision = '2015-05-18'

                def __init__(self):
                    self.parent = None
                    self.atm_clp = None
                    self.atm_oam = None
                    self.authen_status = None
                    self.cac_admit = None
                    self.cac_unadmit = None
                    self.cos = YLeafList()
                    self.cos.parent = self
                    self.cos.name = 'cos'
                    self.destination_address_ipv4 = YList()
                    self.destination_address_ipv4.parent = self
                    self.destination_address_ipv4.name = 'destination_address_ipv4'
                    self.destination_address_ipv6 = YList()
                    self.destination_address_ipv6.parent = self
                    self.destination_address_ipv6.name = 'destination_address_ipv6'
                    self.destination_mac = None
                    self.destination_port = YLeafList()
                    self.destination_port.parent = self
                    self.destination_port.name = 'destination_port'
                    self.discard_class = YLeafList()
                    self.discard_class.parent = self
                    self.discard_class.name = 'discard_class'
                    self.domain_name = YList()
                    self.domain_name.parent = self
                    self.domain_name.name = 'domain_name'
                    self.dscp = YLeafList()
                    self.dscp.parent = self
                    self.dscp.name = 'dscp'
                    self.ethertype = YLeafList()
                    self.ethertype.parent = self
                    self.ethertype.name = 'ethertype'
                    self.flow = PolicyManager.ClassMaps.ClassMap.Match.Flow()
                    self.flow.parent = self
                    self.flow_tag = YLeafList()
                    self.flow_tag.parent = self
                    self.flow_tag.name = 'flow_tag'
                    self.fr_de = None
                    self.fragment_type = YLeafList()
                    self.fragment_type.parent = self
                    self.fragment_type.name = 'fragment_type'
                    self.frame_relay_dlci = YLeafList()
                    self.frame_relay_dlci.parent = self
                    self.frame_relay_dlci.name = 'frame_relay_dlci'
                    self.icmpv4_code = YLeafList()
                    self.icmpv4_code.parent = self
                    self.icmpv4_code.name = 'icmpv4_code'
                    self.icmpv4_type = YLeafList()
                    self.icmpv4_type.parent = self
                    self.icmpv4_type.name = 'icmpv4_type'
                    self.icmpv6_code = YLeafList()
                    self.icmpv6_code.parent = self
                    self.icmpv6_code.name = 'icmpv6_code'
                    self.icmpv6_type = YLeafList()
                    self.icmpv6_type.parent = self
                    self.icmpv6_type.name = 'icmpv6_type'
                    self.inner_cos = YLeafList()
                    self.inner_cos.parent = self
                    self.inner_cos.name = 'inner_cos'
                    self.inner_vlan = YLeafList()
                    self.inner_vlan.parent = self
                    self.inner_vlan.name = 'inner_vlan'
                    self.ipv4_acl = None
                    self.ipv4_dscp = YLeafList()
                    self.ipv4_dscp.parent = self
                    self.ipv4_dscp.name = 'ipv4_dscp'
                    self.ipv4_packet_length = YLeafList()
                    self.ipv4_packet_length.parent = self
                    self.ipv4_packet_length.name = 'ipv4_packet_length'
                    self.ipv4_precedence = YLeafList()
                    self.ipv4_precedence.parent = self
                    self.ipv4_precedence.name = 'ipv4_precedence'
                    self.ipv6_acl = None
                    self.ipv6_dscp = YLeafList()
                    self.ipv6_dscp.parent = self
                    self.ipv6_dscp.name = 'ipv6_dscp'
                    self.ipv6_packet_length = YLeafList()
                    self.ipv6_packet_length.parent = self
                    self.ipv6_packet_length.name = 'ipv6_packet_length'
                    self.ipv6_precedence = YLeafList()
                    self.ipv6_precedence.parent = self
                    self.ipv6_precedence.name = 'ipv6_precedence'
                    self.mpls_disposition_ipv4_access_list = None
                    self.mpls_disposition_ipv6_access_list = None
                    self.mpls_experimental_imposition = YLeafList()
                    self.mpls_experimental_imposition.parent = self
                    self.mpls_experimental_imposition.name = 'mpls_experimental_imposition'
                    self.mpls_experimental_topmost = YLeafList()
                    self.mpls_experimental_topmost.parent = self
                    self.mpls_experimental_topmost.name = 'mpls_experimental_topmost'
                    self.packet_length = YLeafList()
                    self.packet_length.parent = self
                    self.packet_length.name = 'packet_length'
                    self.precedence = YLeafList()
                    self.precedence.parent = self
                    self.precedence.name = 'precedence'
                    self.protocol = YLeafList()
                    self.protocol.parent = self
                    self.protocol.name = 'protocol'
                    self.qos_group = YLeafList()
                    self.qos_group.parent = self
                    self.qos_group.name = 'qos_group'
                    self.service_name = YLeafList()
                    self.service_name.parent = self
                    self.service_name.name = 'service_name'
                    self.service_name_regex = YLeafList()
                    self.service_name_regex.parent = self
                    self.service_name_regex.name = 'service_name_regex'
                    self.source_address_ipv4 = YList()
                    self.source_address_ipv4.parent = self
                    self.source_address_ipv4.name = 'source_address_ipv4'
                    self.source_address_ipv6 = YList()
                    self.source_address_ipv6.parent = self
                    self.source_address_ipv6.name = 'source_address_ipv6'
                    self.source_mac = None
                    self.source_port = YLeafList()
                    self.source_port.parent = self
                    self.source_port.name = 'source_port'
                    self.tcp_flag = None
                    self.timer = YLeafList()
                    self.timer.parent = self
                    self.timer.name = 'timer'
                    self.timer_regex = YLeafList()
                    self.timer_regex.parent = self
                    self.timer_regex.name = 'timer_regex'
                    self.user_name = YLeafList()
                    self.user_name.parent = self
                    self.user_name.name = 'user_name'
                    self.user_name_regex = YLeafList()
                    self.user_name_regex.parent = self
                    self.user_name_regex.name = 'user_name_regex'
                    self.vlan = YLeafList()
                    self.vlan.parent = self
                    self.vlan.name = 'vlan'


                class DestinationAddressIpv4(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.netmask = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.netmask is None:
                            raise YPYModelError('Key property netmask is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:destination-address-ipv4[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:netmask = ' + str(self.netmask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.netmask is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv4']['meta_info']


                class DestinationAddressIpv6(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:destination-address-ipv6[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.DestinationAddressIpv6']['meta_info']


                class SourceAddressIpv4(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.netmask = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.netmask is None:
                            raise YPYModelError('Key property netmask is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:source-address-ipv4[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:netmask = ' + str(self.netmask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.netmask is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv4']['meta_info']


                class SourceAddressIpv6(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:source-address-ipv6[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.SourceAddressIpv6']['meta_info']


                class DomainName(object):
                    """
                    Match domain name.
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**range:** 1..32
                    
                    .. attribute:: name  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**range:** 1..32
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.format = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.format is None:
                            raise YPYModelError('Key property format is None')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:domain-name[Cisco-IOS-XR-asr9k-policymgr-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.format is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.DomainName']['meta_info']


                class Flow(object):
                    """
                    Match flow.
                    
                    .. attribute:: flow_cache
                    
                    	Configure the flow\-cache parameters
                    	**type**\:  :py:class:`FlowCache <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache>`
                    
                    .. attribute:: flow_key
                    
                    	Configure the flow\-key parameters
                    	**type**\:  list of str
                    
                    	**pattern:** (SourceIP)\|(DestinationIP)\|(5Tuple)
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.flow_cache = PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache()
                        self.flow_cache.parent = self
                        self.flow_key = YLeafList()
                        self.flow_key.parent = self
                        self.flow_key.name = 'flow_key'


                    class FlowCache(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.idle_timeout = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:flow-cache'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.idle_timeout is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.Flow.FlowCache']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:flow'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.flow_cache is not None and self.flow_cache._has_data():
                            return True

                        if self.flow_key is not None:
                            for child in self.flow_key:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match.Flow']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:match'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.atm_clp is not None:
                        return True

                    if self.atm_oam is not None:
                        return True

                    if self.authen_status is not None:
                        return True

                    if self.cac_admit is not None:
                        return True

                    if self.cac_unadmit is not None:
                        return True

                    if self.cos is not None:
                        for child in self.cos:
                            if child is not None:
                                return True

                    if self.destination_address_ipv4 is not None:
                        for child_ref in self.destination_address_ipv4:
                            if child_ref._has_data():
                                return True

                    if self.destination_address_ipv6 is not None:
                        for child_ref in self.destination_address_ipv6:
                            if child_ref._has_data():
                                return True

                    if self.destination_mac is not None:
                        return True

                    if self.destination_port is not None:
                        for child in self.destination_port:
                            if child is not None:
                                return True

                    if self.discard_class is not None:
                        for child in self.discard_class:
                            if child is not None:
                                return True

                    if self.domain_name is not None:
                        for child_ref in self.domain_name:
                            if child_ref._has_data():
                                return True

                    if self.dscp is not None:
                        for child in self.dscp:
                            if child is not None:
                                return True

                    if self.ethertype is not None:
                        for child in self.ethertype:
                            if child is not None:
                                return True

                    if self.flow is not None and self.flow._has_data():
                        return True

                    if self.flow_tag is not None:
                        for child in self.flow_tag:
                            if child is not None:
                                return True

                    if self.fr_de is not None:
                        return True

                    if self.fragment_type is not None:
                        for child in self.fragment_type:
                            if child is not None:
                                return True

                    if self.frame_relay_dlci is not None:
                        for child in self.frame_relay_dlci:
                            if child is not None:
                                return True

                    if self.icmpv4_code is not None:
                        for child in self.icmpv4_code:
                            if child is not None:
                                return True

                    if self.icmpv4_type is not None:
                        for child in self.icmpv4_type:
                            if child is not None:
                                return True

                    if self.icmpv6_code is not None:
                        for child in self.icmpv6_code:
                            if child is not None:
                                return True

                    if self.icmpv6_type is not None:
                        for child in self.icmpv6_type:
                            if child is not None:
                                return True

                    if self.inner_cos is not None:
                        for child in self.inner_cos:
                            if child is not None:
                                return True

                    if self.inner_vlan is not None:
                        for child in self.inner_vlan:
                            if child is not None:
                                return True

                    if self.ipv4_acl is not None:
                        return True

                    if self.ipv4_dscp is not None:
                        for child in self.ipv4_dscp:
                            if child is not None:
                                return True

                    if self.ipv4_packet_length is not None:
                        for child in self.ipv4_packet_length:
                            if child is not None:
                                return True

                    if self.ipv4_precedence is not None:
                        for child in self.ipv4_precedence:
                            if child is not None:
                                return True

                    if self.ipv6_acl is not None:
                        return True

                    if self.ipv6_dscp is not None:
                        for child in self.ipv6_dscp:
                            if child is not None:
                                return True

                    if self.ipv6_packet_length is not None:
                        for child in self.ipv6_packet_length:
                            if child is not None:
                                return True

                    if self.ipv6_precedence is not None:
                        for child in self.ipv6_precedence:
                            if child is not None:
                                return True

                    if self.mpls_disposition_ipv4_access_list is not None:
                        return True

                    if self.mpls_disposition_ipv6_access_list is not None:
                        return True

                    if self.mpls_experimental_imposition is not None:
                        for child in self.mpls_experimental_imposition:
                            if child is not None:
                                return True

                    if self.mpls_experimental_topmost is not None:
                        for child in self.mpls_experimental_topmost:
                            if child is not None:
                                return True

                    if self.packet_length is not None:
                        for child in self.packet_length:
                            if child is not None:
                                return True

                    if self.precedence is not None:
                        for child in self.precedence:
                            if child is not None:
                                return True

                    if self.protocol is not None:
                        for child in self.protocol:
                            if child is not None:
                                return True

                    if self.qos_group is not None:
                        for child in self.qos_group:
                            if child is not None:
                                return True

                    if self.service_name is not None:
                        for child in self.service_name:
                            if child is not None:
                                return True

                    if self.service_name_regex is not None:
                        for child in self.service_name_regex:
                            if child is not None:
                                return True

                    if self.source_address_ipv4 is not None:
                        for child_ref in self.source_address_ipv4:
                            if child_ref._has_data():
                                return True

                    if self.source_address_ipv6 is not None:
                        for child_ref in self.source_address_ipv6:
                            if child_ref._has_data():
                                return True

                    if self.source_mac is not None:
                        return True

                    if self.source_port is not None:
                        for child in self.source_port:
                            if child is not None:
                                return True

                    if self.tcp_flag is not None:
                        return True

                    if self.timer is not None:
                        for child in self.timer:
                            if child is not None:
                                return True

                    if self.timer_regex is not None:
                        for child in self.timer_regex:
                            if child is not None:
                                return True

                    if self.user_name is not None:
                        for child in self.user_name:
                            if child is not None:
                                return True

                    if self.user_name_regex is not None:
                        for child in self.user_name_regex:
                            if child is not None:
                                return True

                    if self.vlan is not None:
                        for child in self.vlan:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                    return meta._meta_table['PolicyManager.ClassMaps.ClassMap.Match']['meta_info']


            class MatchNot(object):
                """
                Match not rules.
                
                .. attribute:: authen_status
                
                	Match authentication status
                	**type**\:  str
                
                	**pattern:** (authenticated)\|(unauthenticated)
                
                .. attribute:: cos
                
                	Match CoS
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: destination_address_ipv4
                
                	Match destination IPv4 address
                	**type**\: list of  :py:class:`DestinationAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4>`
                
                .. attribute:: destination_address_ipv6
                
                	Match destination IPv6 address
                	**type**\: list of  :py:class:`DestinationAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6>`
                
                .. attribute:: destination_port
                
                	Match destination port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: discard_class
                
                	Match discard class
                	**type**\:  list of int
                
                	**range:** 0..7
                
                .. attribute:: domain_name
                
                	Match domain name
                	**type**\: list of  :py:class:`DomainName <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName>`
                
                .. attribute:: dscp
                
                	Match DSCP
                	**type**\:  list of str
                
                	**pattern:** ([0\-9]\|[1\-5][0\-9]\|6[0\-3])\|(([0\-9]\|[1\-5][0\-9]\|6[0\-3])\-([0\-9]\|[1\-5][0\-9]\|6[0\-3]))\|(af11)\|(af12)\|(af13)\|(af21)\|(af22)\|(af23)\|(af31)\|(af32)\|(af33)\|(af41)\|(af42)\|(af43)\|(ef)\|(default)\|(cs1)\|(cs2)\|(cs3)\|(cs4)\|(cs5)\|(cs6)\|(cs7)
                
                .. attribute:: ethertype
                
                	Match Ethertype
                	**type**\:  list of str
                
                	**pattern:** ((153[6\-9]\|15[4\-9][0\-9]\|1[6\-9][0\-9][0\-9]\|[2\-9][0\-9][0\-9][0\-9])\|([1\-5][0\-9][0\-9][0\-9][0\-9]\|6[0\-4][0\-9][0\-9][0\-9])\|(65[0\-4][0\-9][0\-9]\|655[0\-2][0\-9]\|6553[0\-5]))\|((arp)\|(ipv4)\|(ipv6))
                
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
                
                	**range:** 1..64
                
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
                
                	**range:** 1..64
                
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
                
                	**range:** 1..32
                
                .. attribute:: mpls_disposition_ipv6_access_list
                
                	Match MPLS Label Disposition IPv6 access list
                	**type**\:  str
                
                	**range:** 1..32
                
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
                
                .. attribute:: service_name
                
                	Match servicve name
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: service_name_regex
                
                	Match servicve name regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: source_address_ipv4
                
                	Match source IPv4 address
                	**type**\: list of  :py:class:`SourceAddressIpv4 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4>`
                
                .. attribute:: source_address_ipv6
                
                	Match source IPv6 address
                	**type**\: list of  :py:class:`SourceAddressIpv6 <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6>`
                
                .. attribute:: source_port
                
                	Match source port.  Should be value 0..65535 or range
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                .. attribute:: tcp_flag
                
                	Match TCP flag
                	**type**\:  int
                
                	**range:** 1..4095
                
                .. attribute:: timer
                
                	Match timer
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: timer_regex
                
                	Match timer regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: user_name
                
                	Match user name
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: user_name_regex
                
                	Match user name regular expression
                	**type**\:  list of str
                
                	**range:** 1..32
                
                .. attribute:: vlan
                
                	Match VLAN ID
                	**type**\:  list of str
                
                	**pattern:** (\\d+)\|(\\d+\\\-\\d+)
                
                

                """

                _prefix = 'asr9k-policymgr-cfg'
                _revision = '2015-05-18'

                def __init__(self):
                    self.parent = None
                    self.authen_status = None
                    self.cos = YLeafList()
                    self.cos.parent = self
                    self.cos.name = 'cos'
                    self.destination_address_ipv4 = YList()
                    self.destination_address_ipv4.parent = self
                    self.destination_address_ipv4.name = 'destination_address_ipv4'
                    self.destination_address_ipv6 = YList()
                    self.destination_address_ipv6.parent = self
                    self.destination_address_ipv6.name = 'destination_address_ipv6'
                    self.destination_port = YLeafList()
                    self.destination_port.parent = self
                    self.destination_port.name = 'destination_port'
                    self.discard_class = YLeafList()
                    self.discard_class.parent = self
                    self.discard_class.name = 'discard_class'
                    self.domain_name = YList()
                    self.domain_name.parent = self
                    self.domain_name.name = 'domain_name'
                    self.dscp = YLeafList()
                    self.dscp.parent = self
                    self.dscp.name = 'dscp'
                    self.ethertype = YLeafList()
                    self.ethertype.parent = self
                    self.ethertype.name = 'ethertype'
                    self.flow_tag = YLeafList()
                    self.flow_tag.parent = self
                    self.flow_tag.name = 'flow_tag'
                    self.fr_de = None
                    self.fragment_type = YLeafList()
                    self.fragment_type.parent = self
                    self.fragment_type.name = 'fragment_type'
                    self.frame_relay_dlci = YLeafList()
                    self.frame_relay_dlci.parent = self
                    self.frame_relay_dlci.name = 'frame_relay_dlci'
                    self.icmpv4_code = YLeafList()
                    self.icmpv4_code.parent = self
                    self.icmpv4_code.name = 'icmpv4_code'
                    self.icmpv4_type = YLeafList()
                    self.icmpv4_type.parent = self
                    self.icmpv4_type.name = 'icmpv4_type'
                    self.icmpv6_code = YLeafList()
                    self.icmpv6_code.parent = self
                    self.icmpv6_code.name = 'icmpv6_code'
                    self.icmpv6_type = YLeafList()
                    self.icmpv6_type.parent = self
                    self.icmpv6_type.name = 'icmpv6_type'
                    self.inner_cos = YLeafList()
                    self.inner_cos.parent = self
                    self.inner_cos.name = 'inner_cos'
                    self.inner_vlan = YLeafList()
                    self.inner_vlan.parent = self
                    self.inner_vlan.name = 'inner_vlan'
                    self.ipv4_acl = None
                    self.ipv4_dscp = YLeafList()
                    self.ipv4_dscp.parent = self
                    self.ipv4_dscp.name = 'ipv4_dscp'
                    self.ipv4_packet_length = YLeafList()
                    self.ipv4_packet_length.parent = self
                    self.ipv4_packet_length.name = 'ipv4_packet_length'
                    self.ipv4_precedence = YLeafList()
                    self.ipv4_precedence.parent = self
                    self.ipv4_precedence.name = 'ipv4_precedence'
                    self.ipv6_acl = None
                    self.ipv6_dscp = YLeafList()
                    self.ipv6_dscp.parent = self
                    self.ipv6_dscp.name = 'ipv6_dscp'
                    self.ipv6_packet_length = YLeafList()
                    self.ipv6_packet_length.parent = self
                    self.ipv6_packet_length.name = 'ipv6_packet_length'
                    self.ipv6_precedence = YLeafList()
                    self.ipv6_precedence.parent = self
                    self.ipv6_precedence.name = 'ipv6_precedence'
                    self.mpls_disposition_ipv4_access_list = None
                    self.mpls_disposition_ipv6_access_list = None
                    self.mpls_experimental_imposition = YLeafList()
                    self.mpls_experimental_imposition.parent = self
                    self.mpls_experimental_imposition.name = 'mpls_experimental_imposition'
                    self.mpls_experimental_topmost = YLeafList()
                    self.mpls_experimental_topmost.parent = self
                    self.mpls_experimental_topmost.name = 'mpls_experimental_topmost'
                    self.packet_length = YLeafList()
                    self.packet_length.parent = self
                    self.packet_length.name = 'packet_length'
                    self.precedence = YLeafList()
                    self.precedence.parent = self
                    self.precedence.name = 'precedence'
                    self.protocol = YLeafList()
                    self.protocol.parent = self
                    self.protocol.name = 'protocol'
                    self.qos_group = YLeafList()
                    self.qos_group.parent = self
                    self.qos_group.name = 'qos_group'
                    self.service_name = YLeafList()
                    self.service_name.parent = self
                    self.service_name.name = 'service_name'
                    self.service_name_regex = YLeafList()
                    self.service_name_regex.parent = self
                    self.service_name_regex.name = 'service_name_regex'
                    self.source_address_ipv4 = YList()
                    self.source_address_ipv4.parent = self
                    self.source_address_ipv4.name = 'source_address_ipv4'
                    self.source_address_ipv6 = YList()
                    self.source_address_ipv6.parent = self
                    self.source_address_ipv6.name = 'source_address_ipv6'
                    self.source_port = YLeafList()
                    self.source_port.parent = self
                    self.source_port.name = 'source_port'
                    self.tcp_flag = None
                    self.timer = YLeafList()
                    self.timer.parent = self
                    self.timer.name = 'timer'
                    self.timer_regex = YLeafList()
                    self.timer_regex.parent = self
                    self.timer_regex.name = 'timer_regex'
                    self.user_name = YLeafList()
                    self.user_name.parent = self
                    self.user_name.name = 'user_name'
                    self.user_name_regex = YLeafList()
                    self.user_name_regex.parent = self
                    self.user_name_regex.name = 'user_name_regex'
                    self.vlan = YLeafList()
                    self.vlan.parent = self
                    self.vlan.name = 'vlan'


                class DestinationAddressIpv4(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.netmask = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.netmask is None:
                            raise YPYModelError('Key property netmask is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:destination-address-ipv4[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:netmask = ' + str(self.netmask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.netmask is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv4']['meta_info']


                class DestinationAddressIpv6(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:destination-address-ipv6[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DestinationAddressIpv6']['meta_info']


                class SourceAddressIpv4(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.netmask = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.netmask is None:
                            raise YPYModelError('Key property netmask is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:source-address-ipv4[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:netmask = ' + str(self.netmask) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.netmask is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv4']['meta_info']


                class SourceAddressIpv6(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.address = None
                        self.prefix_length = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.address is None:
                            raise YPYModelError('Key property address is None')
                        if self.prefix_length is None:
                            raise YPYModelError('Key property prefix_length is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:source-address-ipv6[Cisco-IOS-XR-asr9k-policymgr-cfg:address = ' + str(self.address) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:prefix-length = ' + str(self.prefix_length) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.address is not None:
                            return True

                        if self.prefix_length is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.SourceAddressIpv6']['meta_info']


                class DomainName(object):
                    """
                    Match domain name.
                    
                    .. attribute:: format  <key>
                    
                    	Domain\-format name
                    	**type**\:  str
                    
                    	**range:** 1..32
                    
                    .. attribute:: name  <key>
                    
                    	Domain name or regular expression
                    	**type**\:  str
                    
                    	**range:** 1..32
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.format = None
                        self.name = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.format is None:
                            raise YPYModelError('Key property format is None')
                        if self.name is None:
                            raise YPYModelError('Key property name is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:domain-name[Cisco-IOS-XR-asr9k-policymgr-cfg:format = ' + str(self.format) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:name = ' + str(self.name) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.format is not None:
                            return True

                        if self.name is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot.DomainName']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:match-not'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.authen_status is not None:
                        return True

                    if self.cos is not None:
                        for child in self.cos:
                            if child is not None:
                                return True

                    if self.destination_address_ipv4 is not None:
                        for child_ref in self.destination_address_ipv4:
                            if child_ref._has_data():
                                return True

                    if self.destination_address_ipv6 is not None:
                        for child_ref in self.destination_address_ipv6:
                            if child_ref._has_data():
                                return True

                    if self.destination_port is not None:
                        for child in self.destination_port:
                            if child is not None:
                                return True

                    if self.discard_class is not None:
                        for child in self.discard_class:
                            if child is not None:
                                return True

                    if self.domain_name is not None:
                        for child_ref in self.domain_name:
                            if child_ref._has_data():
                                return True

                    if self.dscp is not None:
                        for child in self.dscp:
                            if child is not None:
                                return True

                    if self.ethertype is not None:
                        for child in self.ethertype:
                            if child is not None:
                                return True

                    if self.flow_tag is not None:
                        for child in self.flow_tag:
                            if child is not None:
                                return True

                    if self.fr_de is not None:
                        return True

                    if self.fragment_type is not None:
                        for child in self.fragment_type:
                            if child is not None:
                                return True

                    if self.frame_relay_dlci is not None:
                        for child in self.frame_relay_dlci:
                            if child is not None:
                                return True

                    if self.icmpv4_code is not None:
                        for child in self.icmpv4_code:
                            if child is not None:
                                return True

                    if self.icmpv4_type is not None:
                        for child in self.icmpv4_type:
                            if child is not None:
                                return True

                    if self.icmpv6_code is not None:
                        for child in self.icmpv6_code:
                            if child is not None:
                                return True

                    if self.icmpv6_type is not None:
                        for child in self.icmpv6_type:
                            if child is not None:
                                return True

                    if self.inner_cos is not None:
                        for child in self.inner_cos:
                            if child is not None:
                                return True

                    if self.inner_vlan is not None:
                        for child in self.inner_vlan:
                            if child is not None:
                                return True

                    if self.ipv4_acl is not None:
                        return True

                    if self.ipv4_dscp is not None:
                        for child in self.ipv4_dscp:
                            if child is not None:
                                return True

                    if self.ipv4_packet_length is not None:
                        for child in self.ipv4_packet_length:
                            if child is not None:
                                return True

                    if self.ipv4_precedence is not None:
                        for child in self.ipv4_precedence:
                            if child is not None:
                                return True

                    if self.ipv6_acl is not None:
                        return True

                    if self.ipv6_dscp is not None:
                        for child in self.ipv6_dscp:
                            if child is not None:
                                return True

                    if self.ipv6_packet_length is not None:
                        for child in self.ipv6_packet_length:
                            if child is not None:
                                return True

                    if self.ipv6_precedence is not None:
                        for child in self.ipv6_precedence:
                            if child is not None:
                                return True

                    if self.mpls_disposition_ipv4_access_list is not None:
                        return True

                    if self.mpls_disposition_ipv6_access_list is not None:
                        return True

                    if self.mpls_experimental_imposition is not None:
                        for child in self.mpls_experimental_imposition:
                            if child is not None:
                                return True

                    if self.mpls_experimental_topmost is not None:
                        for child in self.mpls_experimental_topmost:
                            if child is not None:
                                return True

                    if self.packet_length is not None:
                        for child in self.packet_length:
                            if child is not None:
                                return True

                    if self.precedence is not None:
                        for child in self.precedence:
                            if child is not None:
                                return True

                    if self.protocol is not None:
                        for child in self.protocol:
                            if child is not None:
                                return True

                    if self.qos_group is not None:
                        for child in self.qos_group:
                            if child is not None:
                                return True

                    if self.service_name is not None:
                        for child in self.service_name:
                            if child is not None:
                                return True

                    if self.service_name_regex is not None:
                        for child in self.service_name_regex:
                            if child is not None:
                                return True

                    if self.source_address_ipv4 is not None:
                        for child_ref in self.source_address_ipv4:
                            if child_ref._has_data():
                                return True

                    if self.source_address_ipv6 is not None:
                        for child_ref in self.source_address_ipv6:
                            if child_ref._has_data():
                                return True

                    if self.source_port is not None:
                        for child in self.source_port:
                            if child is not None:
                                return True

                    if self.tcp_flag is not None:
                        return True

                    if self.timer is not None:
                        for child in self.timer:
                            if child is not None:
                                return True

                    if self.timer_regex is not None:
                        for child in self.timer_regex:
                            if child is not None:
                                return True

                    if self.user_name is not None:
                        for child in self.user_name:
                            if child is not None:
                                return True

                    if self.user_name_regex is not None:
                        for child in self.user_name_regex:
                            if child is not None:
                                return True

                    if self.vlan is not None:
                        for child in self.vlan:
                            if child is not None:
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                    return meta._meta_table['PolicyManager.ClassMaps.ClassMap.MatchNot']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-manager/Cisco-IOS-XR-asr9k-policymgr-cfg:class-maps/Cisco-IOS-XR-asr9k-policymgr-cfg:class-map[Cisco-IOS-XR-asr9k-policymgr-cfg:name = ' + str(self.name) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.type is not None:
                    return True

                if self.class_map_mode_match_all is not None:
                    return True

                if self.class_map_mode_match_any is not None:
                    return True

                if self.description is not None:
                    return True

                if self.match is not None and self.match._has_data():
                    return True

                if self.match_not is not None and self.match_not._has_data():
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                return meta._meta_table['PolicyManager.ClassMaps.ClassMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-manager/Cisco-IOS-XR-asr9k-policymgr-cfg:class-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.class_map is not None:
                for child_ref in self.class_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
            return meta._meta_table['PolicyManager.ClassMaps']['meta_info']


    class PolicyMaps(object):
        """
        Policy\-maps configuration.
        
        .. attribute:: policy_map
        
        	Policy\-map configuration
        	**type**\: list of  :py:class:`PolicyMap <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap>`
        
        

        """

        _prefix = 'asr9k-policymgr-cfg'
        _revision = '2015-05-18'

        def __init__(self):
            self.parent = None
            self.policy_map = YList()
            self.policy_map.parent = self
            self.policy_map.name = 'policy_map'


        class PolicyMap(object):
            """
            Policy\-map configuration.
            
            .. attribute:: name  <key>
            
            	Name of policy\-map
            	**type**\:  str
            
            	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
            
            .. attribute:: type  <key>
            
            	Type of policy\-map
            	**type**\:  :py:class:`PolicyMapTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyMapTypeEnum>`
            
            .. attribute:: description
            
            	Description for this policy\-map
            	**type**\:  str
            
            .. attribute:: event
            
            	Policy event
            	**type**\: list of  :py:class:`Event <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event>`
            
            .. attribute:: policy_map_rule
            
            	Class\-map rule
            	**type**\: list of  :py:class:`PolicyMapRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule>`
            
            

            """

            _prefix = 'asr9k-policymgr-cfg'
            _revision = '2015-05-18'

            def __init__(self):
                self.parent = None
                self.name = None
                self.type = None
                self.description = None
                self.event = YList()
                self.event.parent = self
                self.event.name = 'event'
                self.policy_map_rule = YList()
                self.policy_map_rule.parent = self
                self.policy_map_rule.name = 'policy_map_rule'


            class Event(object):
                """
                Policy event.
                
                .. attribute:: event_type  <key>
                
                	Event type
                	**type**\:  :py:class:`EventTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.EventTypeEnum>`
                
                .. attribute:: class_
                
                	Class\-map rule
                	**type**\: list of  :py:class:`Class <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class>`
                
                .. attribute:: event_mode_match_all
                
                	Execute all the matched classes
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: event_mode_match_first
                
                	Execute only the first matched class
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                

                """

                _prefix = 'asr9k-policymgr-cfg'
                _revision = '2015-05-18'

                def __init__(self):
                    self.parent = None
                    self.event_type = None
                    self.class_ = YList()
                    self.class_.parent = self
                    self.class_.name = 'class_'
                    self.event_mode_match_all = None
                    self.event_mode_match_first = None


                class Class(object):
                    """
                    Class\-map rule.
                    
                    .. attribute:: class_name  <key>
                    
                    	Name of class
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: class_type  <key>
                    
                    	Type of class
                    	**type**\:  :py:class:`PmapClassMapTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PmapClassMapTypeEnum>`
                    
                    .. attribute:: action_rule
                    
                    	Action rule
                    	**type**\: list of  :py:class:`ActionRule <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule>`
                    
                    .. attribute:: class_execution_strategy
                    
                    	Class execution strategy
                    	**type**\:  :py:class:`ExecutionStrategyEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.ExecutionStrategyEnum>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.class_name = None
                        self.class_type = None
                        self.action_rule = YList()
                        self.action_rule.parent = self
                        self.action_rule.name = 'action_rule'
                        self.class_execution_strategy = None


                    class ActionRule(object):
                        """
                        Action rule.
                        
                        .. attribute:: action_sequence_number  <key>
                        
                        	Sequence number for this action
                        	**type**\:  int
                        
                        	**range:** 1..65535
                        
                        .. attribute:: activate_dynamic_template
                        
                        	Activate dynamic templates
                        	**type**\:  :py:class:`ActivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate>`
                        
                        .. attribute:: authenticate
                        
                        	Authentication related configuration
                        	**type**\:  :py:class:`Authenticate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate>`
                        
                        .. attribute:: authorize
                        
                        	Authorize
                        	**type**\:  :py:class:`Authorize <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize>`
                        
                        .. attribute:: deactivate_dynamic_template
                        
                        	Deactivate dynamic templates
                        	**type**\:  :py:class:`DeactivateDynamicTemplate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate>`
                        
                        .. attribute:: disconnect
                        
                        	Disconnect session
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: monitor
                        
                        	Monitor session
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: set_timer
                        
                        	Set a timer to execute a rule on its  expiry
                        	**type**\:  :py:class:`SetTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer>`
                        
                        .. attribute:: stop_timer
                        
                        	Disable timer before it expires
                        	**type**\:  :py:class:`StopTimer <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.action_sequence_number = None
                            self.activate_dynamic_template = None
                            self.authenticate = PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate()
                            self.authenticate.parent = self
                            self.authorize = None
                            self.deactivate_dynamic_template = None
                            self.disconnect = None
                            self.monitor = None
                            self.set_timer = None
                            self.stop_timer = PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer()
                            self.stop_timer.parent = self


                        class ActivateDynamicTemplate(object):
                            """
                            Activate dynamic templates.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.aaa_list = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:activate-dynamic-template'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self._is_presence:
                                    return True
                                if self.aaa_list is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.ActivateDynamicTemplate']['meta_info']


                        class Authenticate(object):
                            """
                            Authentication related configuration.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.aaa_list = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:authenticate'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.aaa_list is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authenticate']['meta_info']


                        class Authorize(object):
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
                            	**type**\:  :py:class:`AuthorizeIdentifierEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.AuthorizeIdentifierEnum>`
                            
                            .. attribute:: password
                            
                            	Specify a password to be used for AAA request
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.aaa_list = None
                                self.format = None
                                self.identifier = None
                                self.password = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:authorize'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self._is_presence:
                                    return True
                                if self.aaa_list is not None:
                                    return True

                                if self.format is not None:
                                    return True

                                if self.identifier is not None:
                                    return True

                                if self.password is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.Authorize']['meta_info']


                        class DeactivateDynamicTemplate(object):
                            """
                            Deactivate dynamic templates.
                            
                            .. attribute:: aaa_list
                            
                            	Name of the AAA method list
                            	**type**\:  str
                            
                            .. attribute:: name
                            
                            	Dynamic template name
                            	**type**\:  str
                            
                            	**mandatory**\: True
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.aaa_list = None
                                self.name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:deactivate-dynamic-template'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self._is_presence:
                                    return True
                                if self.aaa_list is not None:
                                    return True

                                if self.name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.DeactivateDynamicTemplate']['meta_info']


                        class SetTimer(object):
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
                            
                            .. attribute:: _is_presence
                            
                            	Is present if this instance represents presence container else not
                            	**type**\: bool
                            
                            

                            This class is a :ref:`presence class<presence-class>`

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self._is_presence = True
                                self.timer_name = None
                                self.timer_value = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set-timer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self._is_presence:
                                    return True
                                if self.timer_name is not None:
                                    return True

                                if self.timer_value is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.SetTimer']['meta_info']


                        class StopTimer(object):
                            """
                            Disable timer before it expires.
                            
                            .. attribute:: timer_name
                            
                            	Name of the timer
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.timer_name = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:stop-timer'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.timer_name is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule.StopTimer']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')
                            if self.action_sequence_number is None:
                                raise YPYModelError('Key property action_sequence_number is None')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:action-rule[Cisco-IOS-XR-asr9k-policymgr-cfg:action-sequence-number = ' + str(self.action_sequence_number) + ']'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.action_sequence_number is not None:
                                return True

                            if self.activate_dynamic_template is not None and self.activate_dynamic_template._has_data():
                                return True

                            if self.authenticate is not None and self.authenticate._has_data():
                                return True

                            if self.authorize is not None and self.authorize._has_data():
                                return True

                            if self.deactivate_dynamic_template is not None and self.deactivate_dynamic_template._has_data():
                                return True

                            if self.disconnect is not None:
                                return True

                            if self.monitor is not None:
                                return True

                            if self.set_timer is not None and self.set_timer._has_data():
                                return True

                            if self.stop_timer is not None and self.stop_timer._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class.ActionRule']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.class_name is None:
                            raise YPYModelError('Key property class_name is None')
                        if self.class_type is None:
                            raise YPYModelError('Key property class_type is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:class[Cisco-IOS-XR-asr9k-policymgr-cfg:class-name = ' + str(self.class_name) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:class-type = ' + str(self.class_type) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.class_name is not None:
                            return True

                        if self.class_type is not None:
                            return True

                        if self.action_rule is not None:
                            for child_ref in self.action_rule:
                                if child_ref._has_data():
                                    return True

                        if self.class_execution_strategy is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event.Class']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.event_type is None:
                        raise YPYModelError('Key property event_type is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:event[Cisco-IOS-XR-asr9k-policymgr-cfg:event-type = ' + str(self.event_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.event_type is not None:
                        return True

                    if self.class_ is not None:
                        for child_ref in self.class_:
                            if child_ref._has_data():
                                return True

                    if self.event_mode_match_all is not None:
                        return True

                    if self.event_mode_match_first is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                    return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.Event']['meta_info']


            class PolicyMapRule(object):
                """
                Class\-map rule.
                
                .. attribute:: class_name  <key>
                
                	Name of class\-map
                	**type**\:  str
                
                	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                
                .. attribute:: class_type  <key>
                
                	Type of class\-map
                	**type**\:  :py:class:`PmapClassMapTypeEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PmapClassMapTypeEnum>`
                
                .. attribute:: bandwidth_remaining
                
                	Policy action bandwidth remaining queue
                	**type**\:  :py:class:`BandwidthRemaining <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining>`
                
                .. attribute:: cac_local
                
                	Policy action CAC
                	**type**\:  :py:class:`CacLocal <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal>`
                
                .. attribute:: default_red
                
                	Default random early detection
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: ecn_red
                
                	ECN based random early detection
                	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                
                .. attribute:: flow_params
                
                	Policy flow monitoring action
                	**type**\:  :py:class:`FlowParams <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams>`
                
                .. attribute:: fragment
                
                	Policy action fragment. Fragment name
                	**type**\:  str
                
                .. attribute:: metrics_ipcbr
                
                	Policy IP\-CBR metric action
                	**type**\:  :py:class:`MetricsIpcbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr>`
                
                .. attribute:: min_bandwidth
                
                	Policy action minimum bandwidth queue
                	**type**\:  :py:class:`MinBandwidth <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth>`
                
                .. attribute:: pbr
                
                	Policy action PBR
                	**type**\:  :py:class:`Pbr <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr>`
                
                .. attribute:: police
                
                	Configures traffic policing action
                	**type**\:  :py:class:`Police <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police>`
                
                .. attribute:: priority_level
                
                	Priority level
                	**type**\:  int
                
                	**range:** 1..7
                
                .. attribute:: queue_limit
                
                	Policy action queue limit
                	**type**\:  :py:class:`QueueLimit <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit>`
                
                .. attribute:: random_detect
                
                	Random early detection. All RED profiles in a class must be based on the same field
                	**type**\: list of  :py:class:`RandomDetect <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect>`
                
                .. attribute:: react
                
                	Policy action react
                	**type**\:  :py:class:`React <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React>`
                
                .. attribute:: service_fragment
                
                	Policy action service fragment.  Service fragment name
                	**type**\:  str
                
                .. attribute:: service_policy
                
                	Configure a child service policy
                	**type**\:  :py:class:`ServicePolicy <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy>`
                
                .. attribute:: set
                
                	Policy action packet marking
                	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set>`
                
                .. attribute:: shape
                
                	Policy action shape
                	**type**\:  :py:class:`Shape <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape>`
                
                

                """

                _prefix = 'asr9k-policymgr-cfg'
                _revision = '2015-05-18'

                def __init__(self):
                    self.parent = None
                    self.class_name = None
                    self.class_type = None
                    self.bandwidth_remaining = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining()
                    self.bandwidth_remaining.parent = self
                    self.cac_local = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal()
                    self.cac_local.parent = self
                    self.default_red = None
                    self.ecn_red = None
                    self.flow_params = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams()
                    self.flow_params.parent = self
                    self.fragment = None
                    self.metrics_ipcbr = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr()
                    self.metrics_ipcbr.parent = self
                    self.min_bandwidth = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth()
                    self.min_bandwidth.parent = self
                    self.pbr = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr()
                    self.pbr.parent = self
                    self.police = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police()
                    self.police.parent = self
                    self.priority_level = None
                    self.queue_limit = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit()
                    self.queue_limit.parent = self
                    self.random_detect = YList()
                    self.random_detect.parent = self
                    self.random_detect.name = 'random_detect'
                    self.react = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React()
                    self.react.parent = self
                    self.service_fragment = None
                    self.service_policy = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy()
                    self.service_policy.parent = self
                    self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set()
                    self.set.parent = self
                    self.shape = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape()
                    self.shape.parent = self


                class Shape(object):
                    """
                    Policy action shape.
                    
                    .. attribute:: burst
                    
                    	Burst size configuration
                    	**type**\:  :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst>`
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst()
                        self.burst.parent = self
                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate()
                        self.rate.parent = self


                    class Rate(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.unit = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.unit is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Rate']['meta_info']


                    class Burst(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:burst'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape.Burst']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:shape'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.burst is not None and self.burst._has_data():
                            return True

                        if self.rate is not None and self.rate._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Shape']['meta_info']


                class MinBandwidth(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.unit = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:min-bandwidth'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.unit is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MinBandwidth']['meta_info']


                class BandwidthRemaining(object):
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.unit = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:bandwidth-remaining'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.unit is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.BandwidthRemaining']['meta_info']


                class QueueLimit(object):
                    """
                    Policy action queue limit.
                    
                    .. attribute:: unit
                    
                    	Remaining bandwidth units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: value
                    
                    	Remaining bandwidth value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.unit = None
                        self.value = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:queue-limit'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.unit is not None:
                            return True

                        if self.value is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.QueueLimit']['meta_info']


                class RandomDetect(object):
                    """
                    Random early detection.
                    All RED profiles in a class must be based
                    on the same field.
                    
                    .. attribute:: threshold_max_units  <key>
                    
                    	Maximum RED threshold units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: threshold_max_value  <key>
                    
                    	Maximum RED threshold value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: threshold_min_units  <key>
                    
                    	Minimum RED threshold units
                    	**type**\:  str
                    
                    	**pattern:** (bytes)\|(kbytes)\|(mbytes)\|(gbytes)\|(us)\|(ms)\|(packets)\|(cells)
                    
                    .. attribute:: threshold_min_value  <key>
                    
                    	Minimum RED threshold value
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
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

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.threshold_max_units = None
                        self.threshold_max_value = None
                        self.threshold_min_units = None
                        self.threshold_min_value = None
                        self.cos = YLeafList()
                        self.cos.parent = self
                        self.cos.name = 'cos'
                        self.dei = None
                        self.discard_class = YLeafList()
                        self.discard_class.parent = self
                        self.discard_class.name = 'discard_class'
                        self.dscp = YLeafList()
                        self.dscp.parent = self
                        self.dscp.name = 'dscp'
                        self.mpls_exp = YLeafList()
                        self.mpls_exp.parent = self
                        self.mpls_exp.name = 'mpls_exp'
                        self.precedence = YLeafList()
                        self.precedence.parent = self
                        self.precedence.name = 'precedence'

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.threshold_max_units is None:
                            raise YPYModelError('Key property threshold_max_units is None')
                        if self.threshold_max_value is None:
                            raise YPYModelError('Key property threshold_max_value is None')
                        if self.threshold_min_units is None:
                            raise YPYModelError('Key property threshold_min_units is None')
                        if self.threshold_min_value is None:
                            raise YPYModelError('Key property threshold_min_value is None')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:random-detect[Cisco-IOS-XR-asr9k-policymgr-cfg:threshold-max-units = ' + str(self.threshold_max_units) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:threshold-max-value = ' + str(self.threshold_max_value) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:threshold-min-units = ' + str(self.threshold_min_units) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:threshold-min-value = ' + str(self.threshold_min_value) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.threshold_max_units is not None:
                            return True

                        if self.threshold_max_value is not None:
                            return True

                        if self.threshold_min_units is not None:
                            return True

                        if self.threshold_min_value is not None:
                            return True

                        if self.cos is not None:
                            for child in self.cos:
                                if child is not None:
                                    return True

                        if self.dei is not None:
                            return True

                        if self.discard_class is not None:
                            for child in self.discard_class:
                                if child is not None:
                                    return True

                        if self.dscp is not None:
                            for child in self.dscp:
                                if child is not None:
                                    return True

                        if self.mpls_exp is not None:
                            for child in self.mpls_exp:
                                if child is not None:
                                    return True

                        if self.precedence is not None:
                            for child in self.precedence:
                                if child is not None:
                                    return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.RandomDetect']['meta_info']


                class Set(object):
                    """
                    Policy action packet marking.
                    
                    .. attribute:: cos
                    
                    	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
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
                    
                    .. attribute:: srp_priority
                    
                    	Sets the spatial reuse protocol priority value of an  outgoing packet
                    	**type**\:  int
                    
                    	**range:** 0..7
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.cos = None
                        self.df = None
                        self.discard_class = None
                        self.dscp = None
                        self.forward_class = None
                        self.fr_de = None
                        self.inner_cos = None
                        self.mpls_experimental_imposition = None
                        self.mpls_experimental_top_most = None
                        self.precedence = None
                        self.precedence_tunnel = None
                        self.qos_group = None
                        self.srp_priority = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.cos is not None:
                            return True

                        if self.df is not None:
                            return True

                        if self.discard_class is not None:
                            return True

                        if self.dscp is not None:
                            return True

                        if self.forward_class is not None:
                            return True

                        if self.fr_de is not None:
                            return True

                        if self.inner_cos is not None:
                            return True

                        if self.mpls_experimental_imposition is not None:
                            return True

                        if self.mpls_experimental_top_most is not None:
                            return True

                        if self.precedence is not None:
                            return True

                        if self.precedence_tunnel is not None:
                            return True

                        if self.qos_group is not None:
                            return True

                        if self.srp_priority is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Set']['meta_info']


                class Police(object):
                    """
                    Configures traffic policing action.
                    
                    .. attribute:: burst
                    
                    	Burst configuration
                    	**type**\:  :py:class:`Burst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst>`
                    
                    .. attribute:: conform_action
                    
                    	Configures the action to take on packets that conform  to the rate limit
                    	**type**\:  :py:class:`ConformAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction>`
                    
                    .. attribute:: exceed_action
                    
                    	Configures the action to take on packets that exceed  the rate limit
                    	**type**\:  :py:class:`ExceedAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction>`
                    
                    .. attribute:: peak_burst
                    
                    	Peak burst configuration
                    	**type**\:  :py:class:`PeakBurst <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst>`
                    
                    .. attribute:: peak_rate
                    
                    	Peak rate configuration
                    	**type**\:  :py:class:`PeakRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate>`
                    
                    .. attribute:: rate
                    
                    	Rate configuration
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate>`
                    
                    .. attribute:: violate_action
                    
                    	Configures the action to take on packets that violate the rate limit
                    	**type**\:  :py:class:`ViolateAction <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst()
                        self.burst.parent = self
                        self.conform_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction()
                        self.conform_action.parent = self
                        self.exceed_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction()
                        self.exceed_action.parent = self
                        self.peak_burst = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst()
                        self.peak_burst.parent = self
                        self.peak_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate()
                        self.peak_rate.parent = self
                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate()
                        self.rate.parent = self
                        self.violate_action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction()
                        self.violate_action.parent = self


                    class Rate(object):
                        """
                        Rate configuration.
                        
                        .. attribute:: units
                        
                        	Rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)
                        
                        .. attribute:: value
                        
                        	Rate value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Rate']['meta_info']


                    class PeakRate(object):
                        """
                        Peak rate configuration.
                        
                        .. attribute:: units
                        
                        	Peak rate units
                        	**type**\:  str
                        
                        	**pattern:** (bps)\|(kbps)\|(mbps)\|(gbps)\|(pps)\|(percent)
                        
                        .. attribute:: value
                        
                        	Peak rate value
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:peak-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakRate']['meta_info']


                    class Burst(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:burst'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.Burst']['meta_info']


                    class PeakBurst(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:peak-burst'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.PeakBurst']['meta_info']


                    class ConformAction(object):
                        """
                        Configures the action to take on packets that conform 
                        to the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.drop = None
                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set()
                            self.set.parent = self
                            self.transmit = None


                        class Set(object):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
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
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.cos = None
                                self.df = None
                                self.discard_class = None
                                self.dscp = None
                                self.forward_class = None
                                self.fr_de = None
                                self.inner_cos = None
                                self.mpls_experimental_imposition = None
                                self.mpls_experimental_top_most = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.qos_group = None
                                self.srp_priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.cos is not None:
                                    return True

                                if self.df is not None:
                                    return True

                                if self.discard_class is not None:
                                    return True

                                if self.dscp is not None:
                                    return True

                                if self.forward_class is not None:
                                    return True

                                if self.fr_de is not None:
                                    return True

                                if self.inner_cos is not None:
                                    return True

                                if self.mpls_experimental_imposition is not None:
                                    return True

                                if self.mpls_experimental_top_most is not None:
                                    return True

                                if self.precedence is not None:
                                    return True

                                if self.precedence_tunnel is not None:
                                    return True

                                if self.qos_group is not None:
                                    return True

                                if self.srp_priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction.Set']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:conform-action'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.drop is not None:
                                return True

                            if self.set is not None and self.set._has_data():
                                return True

                            if self.transmit is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ConformAction']['meta_info']


                    class ExceedAction(object):
                        """
                        Configures the action to take on packets that exceed 
                        the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.drop = None
                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set()
                            self.set.parent = self
                            self.transmit = None


                        class Set(object):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
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
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.cos = None
                                self.df = None
                                self.discard_class = None
                                self.dscp = None
                                self.forward_class = None
                                self.fr_de = None
                                self.inner_cos = None
                                self.mpls_experimental_imposition = None
                                self.mpls_experimental_top_most = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.qos_group = None
                                self.srp_priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.cos is not None:
                                    return True

                                if self.df is not None:
                                    return True

                                if self.discard_class is not None:
                                    return True

                                if self.dscp is not None:
                                    return True

                                if self.forward_class is not None:
                                    return True

                                if self.fr_de is not None:
                                    return True

                                if self.inner_cos is not None:
                                    return True

                                if self.mpls_experimental_imposition is not None:
                                    return True

                                if self.mpls_experimental_top_most is not None:
                                    return True

                                if self.precedence is not None:
                                    return True

                                if self.precedence_tunnel is not None:
                                    return True

                                if self.qos_group is not None:
                                    return True

                                if self.srp_priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction.Set']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:exceed-action'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.drop is not None:
                                return True

                            if self.set is not None and self.set._has_data():
                                return True

                            if self.transmit is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ExceedAction']['meta_info']


                    class ViolateAction(object):
                        """
                        Configures the action to take on packets that violate
                        the rate limit.
                        
                        .. attribute:: drop
                        
                        	Police action drop
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: set
                        
                        	Police action packet marking
                        	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set>`
                        
                        .. attribute:: transmit
                        
                        	Police action transmit
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.drop = None
                            self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set()
                            self.set.parent = self
                            self.transmit = None


                        class Set(object):
                            """
                            Police action packet marking.
                            
                            .. attribute:: cos
                            
                            	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
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
                            
                            .. attribute:: srp_priority
                            
                            	Sets the spatial reuse protocol priority value of an  outgoing packet
                            	**type**\:  int
                            
                            	**range:** 0..7
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.cos = None
                                self.df = None
                                self.discard_class = None
                                self.dscp = None
                                self.forward_class = None
                                self.fr_de = None
                                self.inner_cos = None
                                self.mpls_experimental_imposition = None
                                self.mpls_experimental_top_most = None
                                self.precedence = None
                                self.precedence_tunnel = None
                                self.qos_group = None
                                self.srp_priority = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.cos is not None:
                                    return True

                                if self.df is not None:
                                    return True

                                if self.discard_class is not None:
                                    return True

                                if self.dscp is not None:
                                    return True

                                if self.forward_class is not None:
                                    return True

                                if self.fr_de is not None:
                                    return True

                                if self.inner_cos is not None:
                                    return True

                                if self.mpls_experimental_imposition is not None:
                                    return True

                                if self.mpls_experimental_top_most is not None:
                                    return True

                                if self.precedence is not None:
                                    return True

                                if self.precedence_tunnel is not None:
                                    return True

                                if self.qos_group is not None:
                                    return True

                                if self.srp_priority is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction.Set']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:violate-action'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.drop is not None:
                                return True

                            if self.set is not None and self.set._has_data():
                                return True

                            if self.transmit is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police.ViolateAction']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:police'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.burst is not None and self.burst._has_data():
                            return True

                        if self.conform_action is not None and self.conform_action._has_data():
                            return True

                        if self.exceed_action is not None and self.exceed_action._has_data():
                            return True

                        if self.peak_burst is not None and self.peak_burst._has_data():
                            return True

                        if self.peak_rate is not None and self.peak_rate._has_data():
                            return True

                        if self.rate is not None and self.rate._has_data():
                            return True

                        if self.violate_action is not None and self.violate_action._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Police']['meta_info']


                class ServicePolicy(object):
                    """
                    Configure a child service policy.
                    
                    .. attribute:: policy_name
                    
                    	Name of service\-policy
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9][a\-zA\-Z0\-9\\.\_@$%+#\:=<>\\\-]{0,62}
                    
                    .. attribute:: type
                    
                    	Type of service\-policy
                    	**type**\:  str
                    
                    	**pattern:** (PBR)\|(QOS)\|(REDIRECT)\|(TRAFFIC)
                    \|(pbr)\|(qos)\|(redirect)\|(traffic)
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.policy_name = None
                        self.type = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:service-policy'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.policy_name is not None:
                            return True

                        if self.type is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.ServicePolicy']['meta_info']


                class CacLocal(object):
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
                    	**type**\:  :py:class:`FlowRate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate>`
                    
                    .. attribute:: rate
                    
                    	The rate allocated for all flows
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.flow_idle_timeout = None
                        self.flow_rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate()
                        self.flow_rate.parent = self
                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate()
                        self.rate.parent = self


                    class Rate(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.Rate']['meta_info']


                    class FlowRate(object):
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

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.units = None
                            self.value = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:flow-rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.units is not None:
                                return True

                            if self.value is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal.FlowRate']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:cac-local'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.flow_idle_timeout is not None:
                            return True

                        if self.flow_rate is not None and self.flow_rate._has_data():
                            return True

                        if self.rate is not None and self.rate._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.CacLocal']['meta_info']


                class FlowParams(object):
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
                    
                    .. attribute:: max_flow
                    
                    	Max simultaneous flows monitored per policy class
                    	**type**\:  int
                    
                    	**range:** 0..4096
                    
                    .. attribute:: timeout
                    
                    	Declare a flow dead if no packets received in so much time
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.history = None
                        self.interval_duration = None
                        self.max_flow = None
                        self.timeout = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:flow-params'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.history is not None:
                            return True

                        if self.interval_duration is not None:
                            return True

                        if self.max_flow is not None:
                            return True

                        if self.timeout is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.FlowParams']['meta_info']


                class MetricsIpcbr(object):
                    """
                    Policy IP\-CBR metric action.
                    
                    .. attribute:: media_packet
                    
                    	Media\-packet structure
                    	**type**\:  :py:class:`MediaPacket <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket>`
                    
                    .. attribute:: rate
                    
                    	Nominal per\-flow data rate
                    	**type**\:  :py:class:`Rate <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.media_packet = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket()
                        self.media_packet.parent = self
                        self.rate = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate()
                        self.rate.parent = self


                    class Rate(object):
                        """
                        Nominal per\-flow data rate.
                        
                        .. attribute:: layer3
                        
                        	Nominal rate specified at the L3 (IP)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: media
                        
                        	Nominal data rate of the media flow (ip payload)
                        	**type**\:  int
                        
                        	**range:** 1..3000000000
                        
                        .. attribute:: packet
                        
                        	Nominal IP layer packet rate (in pps)
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.layer3 = None
                            self.media = None
                            self.packet = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:rate'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.layer3 is not None:
                                return True

                            if self.media is not None:
                                return True

                            if self.packet is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.Rate']['meta_info']


                    class MediaPacket(object):
                        """
                        Media\-packet structure.
                        
                        .. attribute:: count_in_layer3
                        
                        	Nominal number of media packets in an IP payload
                        	**type**\:  int
                        
                        	**range:** 1..64
                        
                        .. attribute:: size
                        
                        	Nominal size of the media\-packet
                        	**type**\:  int
                        
                        	**range:** 0..65535
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.count_in_layer3 = None
                            self.size = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:media-packet'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.count_in_layer3 is not None:
                                return True

                            if self.size is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr.MediaPacket']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:metrics-ipcbr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.media_packet is not None and self.media_packet._has_data():
                            return True

                        if self.rate is not None and self.rate._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.MetricsIpcbr']['meta_info']


                class React(object):
                    """
                    Policy action react.
                    
                    .. attribute:: action
                    
                    	Action on alert
                    	**type**\:  :py:class:`Action <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action>`
                    
                    .. attribute:: alarm
                    
                    	Alaram settings
                    	**type**\:  :py:class:`Alarm <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm>`
                    
                    .. attribute:: criterion_delay_factor
                    
                    	React criterion delay factor
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: criterion_flow_count
                    
                    	React criterion flow count
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: criterion_media_stop
                    
                    	React criterion media stop
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: criterion_mrv
                    
                    	React criterion mrv
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: criterion_packet_rate
                    
                    	React criterion packet rate
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: descrition
                    
                    	String describing the react statement
                    	**type**\:  str
                    
                    .. attribute:: treshold
                    
                    	Alarm threshold settings
                    	**type**\:  :py:class:`Treshold <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.action = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action()
                        self.action.parent = self
                        self.alarm = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm()
                        self.alarm.parent = self
                        self.criterion_delay_factor = None
                        self.criterion_flow_count = None
                        self.criterion_media_stop = None
                        self.criterion_mrv = None
                        self.criterion_packet_rate = None
                        self.descrition = None
                        self.treshold = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold()
                        self.treshold.parent = self


                    class Action(object):
                        """
                        Action on alert.
                        
                        .. attribute:: snmp
                        
                        	SNMP
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: syslog
                        
                        	Syslog
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.snmp = None
                            self.syslog = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:action'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.snmp is not None:
                                return True

                            if self.syslog is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Action']['meta_info']


                    class Alarm(object):
                        """
                        Alaram settings.
                        
                        .. attribute:: severity
                        
                        	Severity of the alarm
                        	**type**\:  str
                        
                        	**pattern:** (informational)\|(notification)\|(warning)\|(error)\|(critical)\|(alert)\|(emergency)
                        
                        .. attribute:: type
                        
                        	Alarm type
                        	**type**\:  :py:class:`Type <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.severity = None
                            self.type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type()
                            self.type.parent = self


                        class Type(object):
                            """
                            Alarm type.
                            
                            .. attribute:: discrete
                            
                            	Discrete alarm type
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            .. attribute:: group_count
                            
                            	Number of flows to reach before  triggering alarm
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: group_percent
                            
                            	Percent to reach before triggering alarm
                            	**type**\:  int
                            
                            	**range:** 0..65535
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.discrete = None
                                self.group_count = None
                                self.group_percent = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.discrete is not None:
                                    return True

                                if self.group_count is not None:
                                    return True

                                if self.group_percent is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm.Type']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:alarm'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.severity is not None:
                                return True

                            if self.type is not None and self.type._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Alarm']['meta_info']


                    class Treshold(object):
                        """
                        Alarm threshold settings.
                        
                        .. attribute:: trigger_type
                        
                        	Alarm trigger type settings
                        	**type**\:  :py:class:`TriggerType <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerType>`
                        
                        .. attribute:: trigger_value
                        
                        	Alarm trigger value settings
                        	**type**\:  :py:class:`TriggerValue <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerValue>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.trigger_type = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerType()
                            self.trigger_type.parent = self
                            self.trigger_value = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerValue()
                            self.trigger_value.parent = self


                        class TriggerValue(object):
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

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.greater_than = None
                                self.greater_than_equal = None
                                self.less_than = None
                                self.less_than_equal = None
                                self.range = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:trigger-value'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.greater_than is not None:
                                    return True

                                if self.greater_than_equal is not None:
                                    return True

                                if self.less_than is not None:
                                    return True

                                if self.less_than_equal is not None:
                                    return True

                                if self.range is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerValue']['meta_info']


                        class TriggerType(object):
                            """
                            Alarm trigger type settings.
                            
                            .. attribute:: average
                            
                            	Trigger averaged over N intervals
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: immediate
                            
                            	Immediate trigger
                            	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                            
                            

                            """

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.average = None
                                self.immediate = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:trigger-type'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.average is not None:
                                    return True

                                if self.immediate is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold.TriggerType']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:treshold'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.trigger_type is not None and self.trigger_type._has_data():
                                return True

                            if self.trigger_value is not None and self.trigger_value._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React.Treshold']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:react'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.action is not None and self.action._has_data():
                            return True

                        if self.alarm is not None and self.alarm._has_data():
                            return True

                        if self.criterion_delay_factor is not None:
                            return True

                        if self.criterion_flow_count is not None:
                            return True

                        if self.criterion_media_stop is not None:
                            return True

                        if self.criterion_mrv is not None:
                            return True

                        if self.criterion_packet_rate is not None:
                            return True

                        if self.descrition is not None:
                            return True

                        if self.treshold is not None and self.treshold._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.React']['meta_info']


                class Pbr(object):
                    """
                    Policy action PBR.
                    
                    .. attribute:: http_redirect
                    
                    	Policy action http redirect. Redirect to this url
                    	**type**\:  str
                    
                    .. attribute:: pbr_drop
                    
                    	Policy action PBR drop
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: pbr_forward
                    
                    	Policy action PBR forward
                    	**type**\:  :py:class:`PbrForward <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward>`
                    
                    .. attribute:: pbr_transmit
                    
                    	Policy action PBR transmit
                    	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                    
                    .. attribute:: set
                    
                    	PBR action packet marking
                    	**type**\:  :py:class:`Set <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.Set>`
                    
                    

                    """

                    _prefix = 'asr9k-policymgr-cfg'
                    _revision = '2015-05-18'

                    def __init__(self):
                        self.parent = None
                        self.http_redirect = None
                        self.pbr_drop = None
                        self.pbr_forward = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward()
                        self.pbr_forward.parent = self
                        self.pbr_transmit = None
                        self.set = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.Set()
                        self.set.parent = self


                    class PbrForward(object):
                        """
                        Policy action PBR forward.
                        
                        .. attribute:: default
                        
                        	Use system default routing table
                        	**type**\:  :py:class:`Empty <ydk.types.Empty>`
                        
                        .. attribute:: next_hop
                        
                        	Use specific next\-hop. Here we present 5 different combination  for the pbf next\-hop.  1. vrf with v6 address  2. vrf with v4 address  3. vrf   4. v4 address  5. v6 address
                        	**type**\:  :py:class:`NextHop <ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_policymgr_cfg.PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward.NextHop>`
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.default = None
                            self.next_hop = PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward.NextHop()
                            self.next_hop.parent = self


                        class NextHop(object):
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

                            _prefix = 'asr9k-policymgr-cfg'
                            _revision = '2015-05-18'

                            def __init__(self):
                                self.parent = None
                                self.ipv4_address = None
                                self.ipv6_address = None
                                self.vrf = None

                            @property
                            def _common_path(self):
                                if self.parent is None:
                                    raise YPYModelError('parent is not set . Cannot derive path.')

                                return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:next-hop'

                            def is_config(self):
                                ''' Returns True if this instance represents config data else returns False '''
                                return True

                            def _has_data(self):
                                if not self.is_config():
                                    return False
                                if self.ipv4_address is not None:
                                    return True

                                if self.ipv6_address is not None:
                                    return True

                                if self.vrf is not None:
                                    return True

                                return False

                            @staticmethod
                            def _meta_info():
                                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward.NextHop']['meta_info']

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:pbr-forward'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.default is not None:
                                return True

                            if self.next_hop is not None and self.next_hop._has_data():
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.PbrForward']['meta_info']


                    class Set(object):
                        """
                        PBR action packet marking.
                        
                        .. attribute:: cos
                        
                        	Sets the specific IEEE 802.1Q Layer 2 CoS value of an outgoing packet. This command should be used by a router if a user wants to mark a packet that is being sent to a switch.  Switches can leverage Layer 2 header information,  including a CoS value marking. Packets entering an  interface cannot be set with a CoS value
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
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
                        
                        .. attribute:: srp_priority
                        
                        	Sets the spatial reuse protocol priority value of an  outgoing packet
                        	**type**\:  int
                        
                        	**range:** 0..7
                        
                        

                        """

                        _prefix = 'asr9k-policymgr-cfg'
                        _revision = '2015-05-18'

                        def __init__(self):
                            self.parent = None
                            self.cos = None
                            self.df = None
                            self.discard_class = None
                            self.dscp = None
                            self.forward_class = None
                            self.fr_de = None
                            self.inner_cos = None
                            self.mpls_experimental_imposition = None
                            self.mpls_experimental_top_most = None
                            self.precedence = None
                            self.precedence_tunnel = None
                            self.qos_group = None
                            self.srp_priority = None

                        @property
                        def _common_path(self):
                            if self.parent is None:
                                raise YPYModelError('parent is not set . Cannot derive path.')

                            return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:set'

                        def is_config(self):
                            ''' Returns True if this instance represents config data else returns False '''
                            return True

                        def _has_data(self):
                            if not self.is_config():
                                return False
                            if self.cos is not None:
                                return True

                            if self.df is not None:
                                return True

                            if self.discard_class is not None:
                                return True

                            if self.dscp is not None:
                                return True

                            if self.forward_class is not None:
                                return True

                            if self.fr_de is not None:
                                return True

                            if self.inner_cos is not None:
                                return True

                            if self.mpls_experimental_imposition is not None:
                                return True

                            if self.mpls_experimental_top_most is not None:
                                return True

                            if self.precedence is not None:
                                return True

                            if self.precedence_tunnel is not None:
                                return True

                            if self.qos_group is not None:
                                return True

                            if self.srp_priority is not None:
                                return True

                            return False

                        @staticmethod
                        def _meta_info():
                            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                            return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr.Set']['meta_info']

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:pbr'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return True

                    def _has_data(self):
                        if not self.is_config():
                            return False
                        if self.http_redirect is not None:
                            return True

                        if self.pbr_drop is not None:
                            return True

                        if self.pbr_forward is not None and self.pbr_forward._has_data():
                            return True

                        if self.pbr_transmit is not None:
                            return True

                        if self.set is not None and self.set._has_data():
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                        return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule.Pbr']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')
                    if self.class_name is None:
                        raise YPYModelError('Key property class_name is None')
                    if self.class_type is None:
                        raise YPYModelError('Key property class_type is None')

                    return self.parent._common_path +'/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-map-rule[Cisco-IOS-XR-asr9k-policymgr-cfg:class-name = ' + str(self.class_name) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:class-type = ' + str(self.class_type) + ']'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return True

                def _has_data(self):
                    if not self.is_config():
                        return False
                    if self.class_name is not None:
                        return True

                    if self.class_type is not None:
                        return True

                    if self.bandwidth_remaining is not None and self.bandwidth_remaining._has_data():
                        return True

                    if self.cac_local is not None and self.cac_local._has_data():
                        return True

                    if self.default_red is not None:
                        return True

                    if self.ecn_red is not None:
                        return True

                    if self.flow_params is not None and self.flow_params._has_data():
                        return True

                    if self.fragment is not None:
                        return True

                    if self.metrics_ipcbr is not None and self.metrics_ipcbr._has_data():
                        return True

                    if self.min_bandwidth is not None and self.min_bandwidth._has_data():
                        return True

                    if self.pbr is not None and self.pbr._has_data():
                        return True

                    if self.police is not None and self.police._has_data():
                        return True

                    if self.priority_level is not None:
                        return True

                    if self.queue_limit is not None and self.queue_limit._has_data():
                        return True

                    if self.random_detect is not None:
                        for child_ref in self.random_detect:
                            if child_ref._has_data():
                                return True

                    if self.react is not None and self.react._has_data():
                        return True

                    if self.service_fragment is not None:
                        return True

                    if self.service_policy is not None and self.service_policy._has_data():
                        return True

                    if self.set is not None and self.set._has_data():
                        return True

                    if self.shape is not None and self.shape._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                    return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap.PolicyMapRule']['meta_info']

            @property
            def _common_path(self):
                if self.name is None:
                    raise YPYModelError('Key property name is None')
                if self.type is None:
                    raise YPYModelError('Key property type is None')

                return '/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-manager/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-maps/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-map[Cisco-IOS-XR-asr9k-policymgr-cfg:name = ' + str(self.name) + '][Cisco-IOS-XR-asr9k-policymgr-cfg:type = ' + str(self.type) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return True

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.name is not None:
                    return True

                if self.type is not None:
                    return True

                if self.description is not None:
                    return True

                if self.event is not None:
                    for child_ref in self.event:
                        if child_ref._has_data():
                            return True

                if self.policy_map_rule is not None:
                    for child_ref in self.policy_map_rule:
                        if child_ref._has_data():
                            return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
                return meta._meta_table['PolicyManager.PolicyMaps.PolicyMap']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-manager/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-maps'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return True

        def _has_data(self):
            if not self.is_config():
                return False
            if self.policy_map is not None:
                for child_ref in self.policy_map:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
            return meta._meta_table['PolicyManager.PolicyMaps']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XR-asr9k-policymgr-cfg:policy-manager'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return True

    def _has_data(self):
        if not self.is_config():
            return False
        if self.class_maps is not None and self.class_maps._has_data():
            return True

        if self.policy_maps is not None and self.policy_maps._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xr._meta import _Cisco_IOS_XR_asr9k_policymgr_cfg as meta
        return meta._meta_table['PolicyManager']['meta_info']


