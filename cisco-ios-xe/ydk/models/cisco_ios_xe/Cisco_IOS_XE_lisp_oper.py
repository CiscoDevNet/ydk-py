""" Cisco_IOS_XE_lisp_oper 

This module contains a collection of YANG definitions for
LISP operational data.
Copyright (c) 2017\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class LispAddressFamilyType(Enum):
    """
    LispAddressFamilyType (Enum Class)

    Address\-family of a LISP address or prefix

    .. data:: ipv4_afi = 0

    	IANA IPv4 address family

    .. data:: ipv6_afi = 1

    	IANA IPv6 address family

    .. data:: mac_afi = 2

    	IANA MAC address family

    """

    ipv4_afi = Enum.YLeaf(0, "ipv4-afi")

    ipv6_afi = Enum.YLeaf(1, "ipv6-afi")

    mac_afi = Enum.YLeaf(2, "mac-afi")


class LispIaftypeType(Enum):
    """
    LispIaftypeType (Enum Class)

    Type of service for an Address\-Family within a single

    LISP instance

    .. data:: iaf_ipv4 = 0

    	IPv4 instance service

    .. data:: iaf_ipv6 = 1

    	IPv6 instance service

    .. data:: iaf_mac = 2

    	MAC (L2) instance service

    .. data:: iaf_ar = 3

    	Address Resolution (L3 address-to-MAC) instance

    	service

    .. data:: iaf_rar = 4

    	Reverse Address Resolution (MAC-to-L3 address)

    	instance service

    """

    iaf_ipv4 = Enum.YLeaf(0, "iaf-ipv4")

    iaf_ipv6 = Enum.YLeaf(1, "iaf-ipv6")

    iaf_mac = Enum.YLeaf(2, "iaf-mac")

    iaf_ar = Enum.YLeaf(3, "iaf-ar")

    iaf_rar = Enum.YLeaf(4, "iaf-rar")


class LispMapReplyActionType(Enum):
    """
    LispMapReplyActionType (Enum Class)

    Defines the LISP map\-cache ACT type as described

    in the section 6.1.4 of RFC 6830. Valid only

    for negative map\-cache entries

    .. data:: no_action = 0

    	Mapping is kept alive and no encapsulation occurs

    .. data:: natively_forward = 1

    	Matching packets are forwarded without

    	LISP encapsulation

    .. data:: send_map_request = 2

    	Matching packets trigger sending Map-Requests

    .. data:: drop = 3

    	Matching packets are dropped

    """

    no_action = Enum.YLeaf(0, "no-action")

    natively_forward = Enum.YLeaf(1, "natively-forward")

    send_map_request = Enum.YLeaf(2, "send-map-request")

    drop = Enum.YLeaf(3, "drop")


class LispRlocStateType(Enum):
    """
    LispRlocStateType (Enum Class)

    Reachability state of a RLOC

    .. data:: lisp_rloc_state_down = 0

    	Locator is down or unreachable

    .. data:: lisp_rloc_state_up = 1

    	Locator is up and reachable

    """

    lisp_rloc_state_down = Enum.YLeaf(0, "lisp-rloc-state-down")

    lisp_rloc_state_up = Enum.YLeaf(1, "lisp-rloc-state-up")


class LispSessionStateType(Enum):
    """
    LispSessionStateType (Enum Class)

    State of a TCP session

    .. data:: lisp_session_state_incomplete = 0

    	Session parameters are incomplete

    .. data:: lisp_session_state_listening = 1

    	Session represents the passively listening socket

    .. data:: lisp_session_state_down = 2

    	Session is down

    .. data:: lisp_session_state_up = 3

    	Session is up

    """

    lisp_session_state_incomplete = Enum.YLeaf(0, "lisp-session-state-incomplete")

    lisp_session_state_listening = Enum.YLeaf(1, "lisp-session-state-listening")

    lisp_session_state_down = Enum.YLeaf(2, "lisp-session-state-down")

    lisp_session_state_up = Enum.YLeaf(3, "lisp-session-state-up")



class LispState(Entity):
    """
    Operational state of the LISP subsystem
    
    .. attribute:: lisp_routers
    
    	List of LISP routers
    	**type**\: list of  		 :py:class:`LispRouters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters>`
    
    

    """

    _prefix = 'lisp-ios-xe-oper'
    _revision = '2017-10-25'

    def __init__(self):
        super(LispState, self).__init__()
        self._top_entity = None

        self.yang_name = "lisp-state"
        self.yang_parent_name = "Cisco-IOS-XE-lisp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([])
        self._child_list_classes = OrderedDict([("lisp-routers", ("lisp_routers", LispState.LispRouters))])
        self._leafs = OrderedDict()

        self.lisp_routers = YList(self)
        self._segment_path = lambda: "Cisco-IOS-XE-lisp-oper:lisp-state"

    def __setattr__(self, name, value):
        self._perform_setattr(LispState, [], name, value)


    class LispRouters(Entity):
        """
        List of LISP routers
        
        .. attribute:: top_id  (key)
        
        	ID number of the LISP router
        	**type**\: int
        
        	**range:** 0..4294967295
        
        .. attribute:: site_id
        
        	Site\-ID common to all devices attached to the same site
        	**type**\: int
        
        	**range:** 0..18446744073709551615
        
        .. attribute:: xtr_id
        
        	xTR\-ID of the device
        	**type**\: list of int
        
        	**range:** 0..255
        
        .. attribute:: instances
        
        	List of LISP instances
        	**type**\: list of  		 :py:class:`Instances <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances>`
        
        .. attribute:: sessions
        
        	List of Reliable Registration sessions
        	**type**\: list of  		 :py:class:`Sessions <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Sessions>`
        
        .. attribute:: local_rlocs
        
        	This list represents the set of routing locators configured on this device
        	**type**\: list of  		 :py:class:`LocalRlocs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.LocalRlocs>`
        
        

        """

        _prefix = 'lisp-ios-xe-oper'
        _revision = '2017-10-25'

        def __init__(self):
            super(LispState.LispRouters, self).__init__()

            self.yang_name = "lisp-routers"
            self.yang_parent_name = "lisp-state"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = ['top_id']
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("instances", ("instances", LispState.LispRouters.Instances)), ("sessions", ("sessions", LispState.LispRouters.Sessions)), ("local-rlocs", ("local_rlocs", LispState.LispRouters.LocalRlocs))])
            self._leafs = OrderedDict([
                ('top_id', YLeaf(YType.uint32, 'top-id')),
                ('site_id', YLeaf(YType.uint64, 'site-id')),
                ('xtr_id', YLeafList(YType.uint8, 'xtr-id')),
            ])
            self.top_id = None
            self.site_id = None
            self.xtr_id = []

            self.instances = YList(self)
            self.sessions = YList(self)
            self.local_rlocs = YList(self)
            self._segment_path = lambda: "lisp-routers" + "[top-id='" + str(self.top_id) + "']"
            self._absolute_path = lambda: "Cisco-IOS-XE-lisp-oper:lisp-state/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(LispState.LispRouters, ['top_id', 'site_id', 'xtr_id'], name, value)


        class Instances(Entity):
            """
            List of LISP instances
            
            .. attribute:: iid  (key)
            
            	LISP Instance ID
            	**type**\: int
            
            	**range:** 0..16777215
            
            .. attribute:: af
            
            	List of Address\-Families enabled in this LISP instance
            	**type**\: list of  		 :py:class:`Af <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af>`
            
            .. attribute:: vrf_name
            
            	Name of VRF that is mapped to the given LISP Instance ID
            	**type**\: str
            
            .. attribute:: is_rloc_probing
            
            	Status of RLOC Probing
            	**type**\: bool
            
            .. attribute:: ms_eid_membership
            
            	MS registration EID membership list (list of locators known to the MS as allowed to send traffic in the instance)
            	**type**\: list of  		 :py:class:`MsEidMembership <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.MsEidMembership>`
            
            .. attribute:: etr_eid_membership
            
            	ETR EID membership list (list of locators known to the ETR as allowed to send traffic in the instance)
            	**type**\: list of  		 :py:class:`EtrEidMembership <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.EtrEidMembership>`
            
            

            """

            _prefix = 'lisp-ios-xe-oper'
            _revision = '2017-10-25'

            def __init__(self):
                super(LispState.LispRouters.Instances, self).__init__()

                self.yang_name = "instances"
                self.yang_parent_name = "lisp-routers"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['iid']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([("af", ("af", LispState.LispRouters.Instances.Af)), ("ms-eid-membership", ("ms_eid_membership", LispState.LispRouters.Instances.MsEidMembership)), ("etr-eid-membership", ("etr_eid_membership", LispState.LispRouters.Instances.EtrEidMembership))])
                self._leafs = OrderedDict([
                    ('iid', YLeaf(YType.uint32, 'iid')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('is_rloc_probing', YLeaf(YType.boolean, 'is-rloc-probing')),
                ])
                self.iid = None
                self.vrf_name = None
                self.is_rloc_probing = None

                self.af = YList(self)
                self.ms_eid_membership = YList(self)
                self.etr_eid_membership = YList(self)
                self._segment_path = lambda: "instances" + "[iid='" + str(self.iid) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(LispState.LispRouters.Instances, ['iid', 'vrf_name', 'is_rloc_probing'], name, value)


            class Af(Entity):
                """
                List of Address\-Families enabled in this LISP instance
                
                .. attribute:: iaftype  (key)
                
                	Instance\-specific service type
                	**type**\:  :py:class:`LispIaftypeType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispIaftypeType>`
                
                .. attribute:: role
                
                	LISP device role for this service
                	**type**\:  :py:class:`Role <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.Role>`
                
                .. attribute:: map_cache
                
                	Map\-cache for this service instance
                	**type**\: list of  		 :py:class:`MapCache <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache>`
                
                .. attribute:: l2_domain_id
                
                	ID of Vlan or Bridge\-Domain that is mapped to the given L2 LISP Instance ID
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: map_cache_size
                
                	Current size of EID\-to\-RLOC map\-cache on this device
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: map_cache_limit
                
                	Maximum permissible number of entries in EID\-to\-RLOC map\-cache on this device
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: etr_map_cache_ttl
                
                	TTL of the EID\-to\-RLOC map record provided by the local device in mapping records
                	**type**\: int
                
                	**range:** 0..4294967295
                
                	**units**\: minutes
                
                .. attribute:: registration_more_specific
                
                	Number of EID prefix registrations that were accepted as a result of the 'accept\-more\-specific' configuration
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: registration_more_specific_warning_threshold
                
                	The warning threshold for the 'accept\-more\-specific' registration count on the Map\-Server
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: registration_more_specific_limit
                
                	Maximum number of registrations on the Map\-Server which could be accepted due to configuration of 'accept\-more\-specific'
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: map_cache_threshold
                
                	The map\-cache utilization warning threshold on the xTR
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: map_requests_in
                
                	Total number of map requests received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_requests_out
                
                	Total number of map requests sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: encapsulated_map_requests_in
                
                	Total number of encapsulated Map\-Requests received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: encapsulated_map_requests_out
                
                	Total number of encapsulated Map\-Requests sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rloc_probe_map_requests_in
                
                	Total number of RLOC probe Map\-Requests received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rloc_probe_map_requests_out
                
                	Total number of RLOC probe Map\-Requests sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_requests_expired_on_queue
                
                	Total number of Map\-Requests for any EID\-Prefix of the given address family and Instance ID which were not sent out by this device because they timed out while on the transmit queue
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_requests_no_reply
                
                	Total number of Map\-Requests attempted by this device for any EID\-Prefix of the given address family and Instance ID without reciving a Map\-Reply
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_requests_from_disallowed_locators
                
                	Total number of Map\-Request messages for any EID\-Prefix of the given address family and Instance ID dropped by this device due to configuration 'map\-resolver allowed\-locator'
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: smr_map_requests_in
                
                	Total number of SMR Map\-Requests received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: smr_map_requests_out
                
                	Total number of SMR Map\-Requests sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ddt_itr_map_requests_dropped
                
                	Total number of ITR's Map\-Request messages for any EID\-Prefix of the given address family and Instance ID dropped by the DDT Map\-Resolver
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ddt_itr_map_requests_nonce_collision
                
                	Total number of ITR's Map\-Request messages for any EID\-Prefix of the given address family and Instance ID dropped by the DDT Map\-Resolver due to nonce conflict
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ddt_itr_map_requests_bad_xtr_nonce
                
                	Total number of ITR's Map\-Request messages for any EID\-Prefix of the given address family and Instance ID dropped by the DDT Map\-Resolver due bad nonce
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: mr_map_requests_forwarded
                
                	Total number of Map\-Requests for any EID\-Prefix of the given address family and Instance ID forwarded by this device to Map\-Resolver on ALT
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ms_map_requests_forwarded
                
                	Total number of Map\-Requests for any EID\-Prefix of the given address family and Instance ID forwarded by this device to ETR
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: to_alt_map_requests_out
                
                	Total number of Map\-Requests for any EID\-Prefix of the given address family and Instance ID forwarded by this device to ALT
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_reply_records_in
                
                	Total number of Map\-Reply records received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_reply_records_out
                
                	Total number of Map\-Reply records sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: authoritative_records_in
                
                	Total number of authoritative Map\-Reply records received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: authoritative_records_out
                
                	Total number of authoritative Map\-Reply records sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: non_authoritative_records_in
                
                	Total number of non authoritative Map\-Reply records received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: non_authoritative_records_out
                
                	Total number of non authoritative Map\-Reply records sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: negative_records_in
                
                	Total number of negative Map\-Reply records received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: negative_records_out
                
                	Total number of negative Map\-Reply records sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rloc_probe_records_in
                
                	Total number of RLOC probe Map\-Replies for any EID\-Prefix of the given address family and Instance ID received by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rloc_probe_records_out
                
                	Total number of RLOC probe Map\-Replies for any EID\-Prefix of the given address family and Instance ID sent by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: ms_proxy_reply_records_out
                
                	Total number of MS proxy Map\-Replies for any EID\-Prefix of the given address family and Instance ID sent by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_subscribe_in
                
                	Total number of WLC Subscribe messages received by this device for the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_subscribe_out
                
                	Total number of WLC Subscribe messages sent by this device for the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_subscribe_in_failure
                
                	Total number of received WLC Subscribe messages for the given address family and Instance ID with incorrect formatting
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_subscribe_out_failure
                
                	Total number of WLC Subscribe messages for the given address family and Instance ID which were not sent due to internal errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_unsubscribe_in
                
                	Total number of WLC Unsubscribe messages received by this device for the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_unsubscribe_out
                
                	Total number of WLC Unsubscribe messages sent by this device for the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_unsubscribe_in_failure
                
                	Total number of received WLC Unsubscribe messages for the given address family and Instance ID with incorrect formatting
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_unsubscribe_out_failure
                
                	Total number of WLC Unsubscribe messages for the given address family and Instance ID which were not sent due to internal errors
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_register_records_in
                
                	Total number of Map\-Register records for any EID\-Prefix of the given address family and Instance ID received by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_register_records_out
                
                	Total number of Map\-Registers records sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_registers_ms_disabled
                
                	Total number of Map\-Register messages dropped due to Map\-Server functionality not enabled for the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_registers_auth_failed
                
                	Total number of Map\-Register messages for any EID\-Prefix of the given address family and Instance ID dropped due to authentication failure
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_registers_from_disallowed_locators
                
                	Total number of Map\-Register messages received from disallowed locators
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_in
                
                	Total number of WLC Map\-Register messages received by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_out
                
                	Total number of WLC Map\-Register messages sent by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_in_ap
                
                	Total number of WLC Map\-Register messages received by this device for AP join in the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_out_ap
                
                	Total number of WLC Map\-Register messages sent by this device for AP join in the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_in_client
                
                	Total number of WLC Map\-Register messages received by this device for wireless client join in the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_out_client
                
                	Total number of WLC Map\-Register messages sent by this device for wireless client join in the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_in_failure
                
                	Total number of WLC Map\-Register messages received in the given address family and Instance ID and discarded due to parsing error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_register_records_out_failure
                
                	Total number of WLC Map\-Register messages for any EID\-Prefix of the given address family and Instance ID which were not sent because of internal error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_notify_records_in
                
                	Total number of Map\-Notify records for any EID\-Prefix of the given address family and Instance ID received by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_notify_records_out
                
                	Total number of Map\-Notify records for any EID\-Prefix of the given address family and Instance ID sent by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: map_notify_auth_failed
                
                	Total number of Map\-Notify messages for any EID\-Prefix of the given address family and Instance ID dropped due to authentication failure
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_in
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID received by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_out
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID sent by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_in_ap
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID received by this device for AP join
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_out_ap
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID sent by this device for AP join
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_in_client
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID received by this device for wireless client join
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_out_client
                
                	Total number of WLC Map\-Notify records for any EID\-Prefix of the given address family and Instance ID sent by this device for wireless client join
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_in_failure
                
                	Total number of WLC Map\-Notify messages received in the given address family and Instance ID and discarded due to parsing error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: wlc_map_notify_records_out_failure
                
                	Total number of WLC Map\-Notify messages for any EID\-Prefix of the given address family and Instance ID which were not sent because of internal error
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: mapping_record_ttl_alerts
                
                	Total number of mapping records received by this device for any EID\-Prefix of the given address family and Instance ID with TTL exceeding 7 days
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_eid_entries_created
                
                	Total number of remote EID map\-cache entries created by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_eid_entries_deleted
                
                	Total number of remote EID map\-cache entries deleted by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: remote_eid_nsf_replay_entries_created
                
                	Total number of remote EID map\-cache entries for any EID\-Prefix of the given address family and Instance ID recreated by this device after NSF switchover
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forwarding_data_signals_processed
                
                	Total number of forwarding plane data signals processed by this device for any EID\-Prefix of the given address family and Instance ID
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forwarding_data_signals_dropped
                
                	Total number of forwarding plane data signals for any EID\-Prefix of the given address family and Instance ID dropped by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forwarding_reachability_reports_processed
                
                	Total number of forwarding plane reachability reports for any EID\-Prefix of the given address family and Instance ID processed by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: forwarding_reachability_reports_dropped
                
                	Total number of forwarding plane reachability reports for any EID\-Prefix of the given address family and Instance ID dropped by this device
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: is_etr_accept_mapping
                
                	Indicates whether the ETR accepts piggybacked mapping records received in a Map\-Request
                	**type**\: bool
                
                .. attribute:: is_etr_accept_mapping_verify
                
                	Indicates if ETR will try to verify accepted piggybacked mapping records received in a Map\-Request
                	**type**\: bool
                
                .. attribute:: local_dbase
                
                	ETR's database of local EID prefixes
                	**type**\: list of  		 :py:class:`LocalDbase <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.LocalDbase>`
                
                .. attribute:: ms_registrations
                
                	Map\-Server database of registered EID Prefixes
                	**type**\: list of  		 :py:class:`MsRegistrations <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MsRegistrations>`
                
                .. attribute:: map_servers
                
                	List of Map\-Servers to which the ETR should register
                	**type**\: list of  		 :py:class:`MapServers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapServers>`
                
                .. attribute:: map_resolvers
                
                	List of Map\-Resolvers where [P]ITR should send its Map\-Requests
                	**type**\: list of  		 :py:class:`MapResolvers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapResolvers>`
                
                .. attribute:: proxy_etrs
                
                	List of all Proxy ETRs that this device is configured to use
                	**type**\: list of  		 :py:class:`ProxyEtrs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.ProxyEtrs>`
                
                

                """

                _prefix = 'lisp-ios-xe-oper'
                _revision = '2017-10-25'

                def __init__(self):
                    super(LispState.LispRouters.Instances.Af, self).__init__()

                    self.yang_name = "af"
                    self.yang_parent_name = "instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['iaftype']
                    self._child_container_classes = OrderedDict([("role", ("role", LispState.LispRouters.Instances.Af.Role))])
                    self._child_list_classes = OrderedDict([("map-cache", ("map_cache", LispState.LispRouters.Instances.Af.MapCache)), ("local-dbase", ("local_dbase", LispState.LispRouters.Instances.Af.LocalDbase)), ("ms-registrations", ("ms_registrations", LispState.LispRouters.Instances.Af.MsRegistrations)), ("map-servers", ("map_servers", LispState.LispRouters.Instances.Af.MapServers)), ("map-resolvers", ("map_resolvers", LispState.LispRouters.Instances.Af.MapResolvers)), ("proxy-etrs", ("proxy_etrs", LispState.LispRouters.Instances.Af.ProxyEtrs))])
                    self._leafs = OrderedDict([
                        ('iaftype', YLeaf(YType.enumeration, 'iaftype')),
                        ('l2_domain_id', YLeaf(YType.uint32, 'l2-domain-id')),
                        ('map_cache_size', YLeaf(YType.uint32, 'map-cache-size')),
                        ('map_cache_limit', YLeaf(YType.uint32, 'map-cache-limit')),
                        ('etr_map_cache_ttl', YLeaf(YType.uint32, 'etr-map-cache-ttl')),
                        ('registration_more_specific', YLeaf(YType.uint32, 'registration-more-specific')),
                        ('registration_more_specific_warning_threshold', YLeaf(YType.uint32, 'registration-more-specific-warning-threshold')),
                        ('registration_more_specific_limit', YLeaf(YType.uint32, 'registration-more-specific-limit')),
                        ('map_cache_threshold', YLeaf(YType.uint32, 'map-cache-threshold')),
                        ('map_requests_in', YLeaf(YType.uint64, 'map-requests-in')),
                        ('map_requests_out', YLeaf(YType.uint64, 'map-requests-out')),
                        ('encapsulated_map_requests_in', YLeaf(YType.uint64, 'encapsulated-map-requests-in')),
                        ('encapsulated_map_requests_out', YLeaf(YType.uint64, 'encapsulated-map-requests-out')),
                        ('rloc_probe_map_requests_in', YLeaf(YType.uint64, 'rloc-probe-map-requests-in')),
                        ('rloc_probe_map_requests_out', YLeaf(YType.uint64, 'rloc-probe-map-requests-out')),
                        ('map_requests_expired_on_queue', YLeaf(YType.uint64, 'map-requests-expired-on-queue')),
                        ('map_requests_no_reply', YLeaf(YType.uint64, 'map-requests-no-reply')),
                        ('map_requests_from_disallowed_locators', YLeaf(YType.uint64, 'map-requests-from-disallowed-locators')),
                        ('smr_map_requests_in', YLeaf(YType.uint64, 'smr-map-requests-in')),
                        ('smr_map_requests_out', YLeaf(YType.uint64, 'smr-map-requests-out')),
                        ('ddt_itr_map_requests_dropped', YLeaf(YType.uint64, 'ddt-itr-map-requests-dropped')),
                        ('ddt_itr_map_requests_nonce_collision', YLeaf(YType.uint64, 'ddt-itr-map-requests-nonce-collision')),
                        ('ddt_itr_map_requests_bad_xtr_nonce', YLeaf(YType.uint64, 'ddt-itr-map-requests-bad-xtr-nonce')),
                        ('mr_map_requests_forwarded', YLeaf(YType.uint64, 'mr-map-requests-forwarded')),
                        ('ms_map_requests_forwarded', YLeaf(YType.uint64, 'ms-map-requests-forwarded')),
                        ('to_alt_map_requests_out', YLeaf(YType.uint64, 'to-alt-map-requests-out')),
                        ('map_reply_records_in', YLeaf(YType.uint64, 'map-reply-records-in')),
                        ('map_reply_records_out', YLeaf(YType.uint64, 'map-reply-records-out')),
                        ('authoritative_records_in', YLeaf(YType.uint64, 'authoritative-records-in')),
                        ('authoritative_records_out', YLeaf(YType.uint64, 'authoritative-records-out')),
                        ('non_authoritative_records_in', YLeaf(YType.uint64, 'non-authoritative-records-in')),
                        ('non_authoritative_records_out', YLeaf(YType.uint64, 'non-authoritative-records-out')),
                        ('negative_records_in', YLeaf(YType.uint64, 'negative-records-in')),
                        ('negative_records_out', YLeaf(YType.uint64, 'negative-records-out')),
                        ('rloc_probe_records_in', YLeaf(YType.uint64, 'rloc-probe-records-in')),
                        ('rloc_probe_records_out', YLeaf(YType.uint64, 'rloc-probe-records-out')),
                        ('ms_proxy_reply_records_out', YLeaf(YType.uint64, 'ms-proxy-reply-records-out')),
                        ('wlc_subscribe_in', YLeaf(YType.uint64, 'wlc-subscribe-in')),
                        ('wlc_subscribe_out', YLeaf(YType.uint64, 'wlc-subscribe-out')),
                        ('wlc_subscribe_in_failure', YLeaf(YType.uint64, 'wlc-subscribe-in-failure')),
                        ('wlc_subscribe_out_failure', YLeaf(YType.uint64, 'wlc-subscribe-out-failure')),
                        ('wlc_unsubscribe_in', YLeaf(YType.uint64, 'wlc-unsubscribe-in')),
                        ('wlc_unsubscribe_out', YLeaf(YType.uint64, 'wlc-unsubscribe-out')),
                        ('wlc_unsubscribe_in_failure', YLeaf(YType.uint64, 'wlc-unsubscribe-in-failure')),
                        ('wlc_unsubscribe_out_failure', YLeaf(YType.uint64, 'wlc-unsubscribe-out-failure')),
                        ('map_register_records_in', YLeaf(YType.uint64, 'map-register-records-in')),
                        ('map_register_records_out', YLeaf(YType.uint64, 'map-register-records-out')),
                        ('map_registers_ms_disabled', YLeaf(YType.uint64, 'map-registers-ms-disabled')),
                        ('map_registers_auth_failed', YLeaf(YType.uint64, 'map-registers-auth-failed')),
                        ('map_registers_from_disallowed_locators', YLeaf(YType.uint64, 'map-registers-from-disallowed-locators')),
                        ('wlc_map_register_records_in', YLeaf(YType.uint64, 'wlc-map-register-records-in')),
                        ('wlc_map_register_records_out', YLeaf(YType.uint64, 'wlc-map-register-records-out')),
                        ('wlc_map_register_records_in_ap', YLeaf(YType.uint64, 'wlc-map-register-records-in-ap')),
                        ('wlc_map_register_records_out_ap', YLeaf(YType.uint64, 'wlc-map-register-records-out-ap')),
                        ('wlc_map_register_records_in_client', YLeaf(YType.uint64, 'wlc-map-register-records-in-client')),
                        ('wlc_map_register_records_out_client', YLeaf(YType.uint64, 'wlc-map-register-records-out-client')),
                        ('wlc_map_register_records_in_failure', YLeaf(YType.uint64, 'wlc-map-register-records-in-failure')),
                        ('wlc_map_register_records_out_failure', YLeaf(YType.uint64, 'wlc-map-register-records-out-failure')),
                        ('map_notify_records_in', YLeaf(YType.uint64, 'map-notify-records-in')),
                        ('map_notify_records_out', YLeaf(YType.uint64, 'map-notify-records-out')),
                        ('map_notify_auth_failed', YLeaf(YType.uint64, 'map-notify-auth-failed')),
                        ('wlc_map_notify_records_in', YLeaf(YType.uint64, 'wlc-map-notify-records-in')),
                        ('wlc_map_notify_records_out', YLeaf(YType.uint64, 'wlc-map-notify-records-out')),
                        ('wlc_map_notify_records_in_ap', YLeaf(YType.uint64, 'wlc-map-notify-records-in-ap')),
                        ('wlc_map_notify_records_out_ap', YLeaf(YType.uint64, 'wlc-map-notify-records-out-ap')),
                        ('wlc_map_notify_records_in_client', YLeaf(YType.uint64, 'wlc-map-notify-records-in-client')),
                        ('wlc_map_notify_records_out_client', YLeaf(YType.uint64, 'wlc-map-notify-records-out-client')),
                        ('wlc_map_notify_records_in_failure', YLeaf(YType.uint64, 'wlc-map-notify-records-in-failure')),
                        ('wlc_map_notify_records_out_failure', YLeaf(YType.uint64, 'wlc-map-notify-records-out-failure')),
                        ('mapping_record_ttl_alerts', YLeaf(YType.uint64, 'mapping-record-ttl-alerts')),
                        ('remote_eid_entries_created', YLeaf(YType.uint64, 'remote-eid-entries-created')),
                        ('remote_eid_entries_deleted', YLeaf(YType.uint64, 'remote-eid-entries-deleted')),
                        ('remote_eid_nsf_replay_entries_created', YLeaf(YType.uint64, 'remote-eid-nsf-replay-entries-created')),
                        ('forwarding_data_signals_processed', YLeaf(YType.uint64, 'forwarding-data-signals-processed')),
                        ('forwarding_data_signals_dropped', YLeaf(YType.uint64, 'forwarding-data-signals-dropped')),
                        ('forwarding_reachability_reports_processed', YLeaf(YType.uint64, 'forwarding-reachability-reports-processed')),
                        ('forwarding_reachability_reports_dropped', YLeaf(YType.uint64, 'forwarding-reachability-reports-dropped')),
                        ('is_etr_accept_mapping', YLeaf(YType.boolean, 'is-etr-accept-mapping')),
                        ('is_etr_accept_mapping_verify', YLeaf(YType.boolean, 'is-etr-accept-mapping-verify')),
                    ])
                    self.iaftype = None
                    self.l2_domain_id = None
                    self.map_cache_size = None
                    self.map_cache_limit = None
                    self.etr_map_cache_ttl = None
                    self.registration_more_specific = None
                    self.registration_more_specific_warning_threshold = None
                    self.registration_more_specific_limit = None
                    self.map_cache_threshold = None
                    self.map_requests_in = None
                    self.map_requests_out = None
                    self.encapsulated_map_requests_in = None
                    self.encapsulated_map_requests_out = None
                    self.rloc_probe_map_requests_in = None
                    self.rloc_probe_map_requests_out = None
                    self.map_requests_expired_on_queue = None
                    self.map_requests_no_reply = None
                    self.map_requests_from_disallowed_locators = None
                    self.smr_map_requests_in = None
                    self.smr_map_requests_out = None
                    self.ddt_itr_map_requests_dropped = None
                    self.ddt_itr_map_requests_nonce_collision = None
                    self.ddt_itr_map_requests_bad_xtr_nonce = None
                    self.mr_map_requests_forwarded = None
                    self.ms_map_requests_forwarded = None
                    self.to_alt_map_requests_out = None
                    self.map_reply_records_in = None
                    self.map_reply_records_out = None
                    self.authoritative_records_in = None
                    self.authoritative_records_out = None
                    self.non_authoritative_records_in = None
                    self.non_authoritative_records_out = None
                    self.negative_records_in = None
                    self.negative_records_out = None
                    self.rloc_probe_records_in = None
                    self.rloc_probe_records_out = None
                    self.ms_proxy_reply_records_out = None
                    self.wlc_subscribe_in = None
                    self.wlc_subscribe_out = None
                    self.wlc_subscribe_in_failure = None
                    self.wlc_subscribe_out_failure = None
                    self.wlc_unsubscribe_in = None
                    self.wlc_unsubscribe_out = None
                    self.wlc_unsubscribe_in_failure = None
                    self.wlc_unsubscribe_out_failure = None
                    self.map_register_records_in = None
                    self.map_register_records_out = None
                    self.map_registers_ms_disabled = None
                    self.map_registers_auth_failed = None
                    self.map_registers_from_disallowed_locators = None
                    self.wlc_map_register_records_in = None
                    self.wlc_map_register_records_out = None
                    self.wlc_map_register_records_in_ap = None
                    self.wlc_map_register_records_out_ap = None
                    self.wlc_map_register_records_in_client = None
                    self.wlc_map_register_records_out_client = None
                    self.wlc_map_register_records_in_failure = None
                    self.wlc_map_register_records_out_failure = None
                    self.map_notify_records_in = None
                    self.map_notify_records_out = None
                    self.map_notify_auth_failed = None
                    self.wlc_map_notify_records_in = None
                    self.wlc_map_notify_records_out = None
                    self.wlc_map_notify_records_in_ap = None
                    self.wlc_map_notify_records_out_ap = None
                    self.wlc_map_notify_records_in_client = None
                    self.wlc_map_notify_records_out_client = None
                    self.wlc_map_notify_records_in_failure = None
                    self.wlc_map_notify_records_out_failure = None
                    self.mapping_record_ttl_alerts = None
                    self.remote_eid_entries_created = None
                    self.remote_eid_entries_deleted = None
                    self.remote_eid_nsf_replay_entries_created = None
                    self.forwarding_data_signals_processed = None
                    self.forwarding_data_signals_dropped = None
                    self.forwarding_reachability_reports_processed = None
                    self.forwarding_reachability_reports_dropped = None
                    self.is_etr_accept_mapping = None
                    self.is_etr_accept_mapping_verify = None

                    self.role = LispState.LispRouters.Instances.Af.Role()
                    self.role.parent = self
                    self._children_name_map["role"] = "role"
                    self._children_yang_names.add("role")

                    self.map_cache = YList(self)
                    self.local_dbase = YList(self)
                    self.ms_registrations = YList(self)
                    self.map_servers = YList(self)
                    self.map_resolvers = YList(self)
                    self.proxy_etrs = YList(self)
                    self._segment_path = lambda: "af" + "[iaftype='" + str(self.iaftype) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(LispState.LispRouters.Instances.Af, ['iaftype', 'l2_domain_id', 'map_cache_size', 'map_cache_limit', 'etr_map_cache_ttl', 'registration_more_specific', 'registration_more_specific_warning_threshold', 'registration_more_specific_limit', 'map_cache_threshold', 'map_requests_in', 'map_requests_out', 'encapsulated_map_requests_in', 'encapsulated_map_requests_out', 'rloc_probe_map_requests_in', 'rloc_probe_map_requests_out', 'map_requests_expired_on_queue', 'map_requests_no_reply', 'map_requests_from_disallowed_locators', 'smr_map_requests_in', 'smr_map_requests_out', 'ddt_itr_map_requests_dropped', 'ddt_itr_map_requests_nonce_collision', 'ddt_itr_map_requests_bad_xtr_nonce', 'mr_map_requests_forwarded', 'ms_map_requests_forwarded', 'to_alt_map_requests_out', 'map_reply_records_in', 'map_reply_records_out', 'authoritative_records_in', 'authoritative_records_out', 'non_authoritative_records_in', 'non_authoritative_records_out', 'negative_records_in', 'negative_records_out', 'rloc_probe_records_in', 'rloc_probe_records_out', 'ms_proxy_reply_records_out', 'wlc_subscribe_in', 'wlc_subscribe_out', 'wlc_subscribe_in_failure', 'wlc_subscribe_out_failure', 'wlc_unsubscribe_in', 'wlc_unsubscribe_out', 'wlc_unsubscribe_in_failure', 'wlc_unsubscribe_out_failure', 'map_register_records_in', 'map_register_records_out', 'map_registers_ms_disabled', 'map_registers_auth_failed', 'map_registers_from_disallowed_locators', 'wlc_map_register_records_in', 'wlc_map_register_records_out', 'wlc_map_register_records_in_ap', 'wlc_map_register_records_out_ap', 'wlc_map_register_records_in_client', 'wlc_map_register_records_out_client', 'wlc_map_register_records_in_failure', 'wlc_map_register_records_out_failure', 'map_notify_records_in', 'map_notify_records_out', 'map_notify_auth_failed', 'wlc_map_notify_records_in', 'wlc_map_notify_records_out', 'wlc_map_notify_records_in_ap', 'wlc_map_notify_records_out_ap', 'wlc_map_notify_records_in_client', 'wlc_map_notify_records_out_client', 'wlc_map_notify_records_in_failure', 'wlc_map_notify_records_out_failure', 'mapping_record_ttl_alerts', 'remote_eid_entries_created', 'remote_eid_entries_deleted', 'remote_eid_nsf_replay_entries_created', 'forwarding_data_signals_processed', 'forwarding_data_signals_dropped', 'forwarding_reachability_reports_processed', 'forwarding_reachability_reports_dropped', 'is_etr_accept_mapping', 'is_etr_accept_mapping_verify'], name, value)


                class Role(Entity):
                    """
                    LISP device role for this service
                    
                    .. attribute:: is_ms
                    
                    	LISP Map\-Server
                    	**type**\: bool
                    
                    .. attribute:: is_mr
                    
                    	LISP Map\-Resolver
                    	**type**\: bool
                    
                    .. attribute:: is_itr
                    
                    	LISP ITR
                    	**type**\: bool
                    
                    .. attribute:: is_etr
                    
                    	LISP ETR
                    	**type**\: bool
                    
                    .. attribute:: is_pitr
                    
                    	LISP Proxy\-ITR
                    	**type**\: bool
                    
                    .. attribute:: is_petr
                    
                    	LISP Proxy\-ETR
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.Role, self).__init__()

                        self.yang_name = "role"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('is_ms', YLeaf(YType.boolean, 'is-ms')),
                            ('is_mr', YLeaf(YType.boolean, 'is-mr')),
                            ('is_itr', YLeaf(YType.boolean, 'is-itr')),
                            ('is_etr', YLeaf(YType.boolean, 'is-etr')),
                            ('is_pitr', YLeaf(YType.boolean, 'is-pitr')),
                            ('is_petr', YLeaf(YType.boolean, 'is-petr')),
                        ])
                        self.is_ms = None
                        self.is_mr = None
                        self.is_itr = None
                        self.is_etr = None
                        self.is_pitr = None
                        self.is_petr = None
                        self._segment_path = lambda: "role"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.Role, ['is_ms', 'is_mr', 'is_itr', 'is_etr', 'is_pitr', 'is_petr'], name, value)


                class MapCache(Entity):
                    """
                    Map\-cache for this service instance
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the prefix
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: prefix  (key)
                    
                    	LISP prefix. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: up_time
                    
                    	Time that this entry was created
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_modified_time
                    
                    	Last time that the RLOC information or the entry state were modified
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_update_time
                    
                    	Last time a mapping record for this entry was received, not valid if the entry is static
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: ttl
                    
                    	Mapping validity period
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: milliseconds
                    
                    .. attribute:: is_authoritative
                    
                    	Indication if the mapping came from an authoritative source
                    	**type**\: bool
                    
                    .. attribute:: is_static
                    
                    	Indication if the mapping is static (i.e. configured)
                    	**type**\: bool
                    
                    .. attribute:: is_negative
                    
                    	Indication if the mapping is negative (i.e. provides no locators for LISP encapsulation)
                    	**type**\: bool
                    
                    .. attribute:: nmr_action
                    
                    	Forwarding action in case of negative entry
                    	**type**\:  :py:class:`LispMapReplyActionType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispMapReplyActionType>`
                    
                    .. attribute:: expiry_time
                    
                    	Time when this entry will expire if not refreshed; for entries which do not have an expiration time this time will be less than the entry creation time
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: encapsulated_packets
                    
                    	Number of packets of the transit traffic which were encapsulated because they matched this map\-cache entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: encapsulated_octets
                    
                    	Number of bytes of the transit traffic which were encapsulated because they matched this map\-cache entry
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: is_active
                    
                    	Indication if the mapping is active, that is there was transit traffic matching this map\-cache entry seen in approximately the last minute
                    	**type**\: bool
                    
                    .. attribute:: map_cache_rloc
                    
                    	List of locators for positive mapping
                    	**type**\: list of  		 :py:class:`MapCacheRloc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.MapCache, self).__init__()

                        self.yang_name = "map-cache"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','prefix']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("map-cache-rloc", ("map_cache_rloc", LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc))])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('prefix', YLeaf(YType.str, 'prefix')),
                            ('up_time', YLeaf(YType.str, 'up-time')),
                            ('last_modified_time', YLeaf(YType.str, 'last-modified-time')),
                            ('last_update_time', YLeaf(YType.str, 'last-update-time')),
                            ('ttl', YLeaf(YType.uint32, 'ttl')),
                            ('is_authoritative', YLeaf(YType.boolean, 'is-authoritative')),
                            ('is_static', YLeaf(YType.boolean, 'is-static')),
                            ('is_negative', YLeaf(YType.boolean, 'is-negative')),
                            ('nmr_action', YLeaf(YType.enumeration, 'nmr-action')),
                            ('expiry_time', YLeaf(YType.str, 'expiry-time')),
                            ('encapsulated_packets', YLeaf(YType.uint64, 'encapsulated-packets')),
                            ('encapsulated_octets', YLeaf(YType.uint64, 'encapsulated-octets')),
                            ('is_active', YLeaf(YType.boolean, 'is-active')),
                        ])
                        self.afi = None
                        self.prefix = None
                        self.up_time = None
                        self.last_modified_time = None
                        self.last_update_time = None
                        self.ttl = None
                        self.is_authoritative = None
                        self.is_static = None
                        self.is_negative = None
                        self.nmr_action = None
                        self.expiry_time = None
                        self.encapsulated_packets = None
                        self.encapsulated_octets = None
                        self.is_active = None

                        self.map_cache_rloc = YList(self)
                        self._segment_path = lambda: "map-cache" + "[afi='" + str(self.afi) + "']" + "[prefix='" + str(self.prefix) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache, ['afi', 'prefix', 'up_time', 'last_modified_time', 'last_update_time', 'ttl', 'is_authoritative', 'is_static', 'is_negative', 'nmr_action', 'expiry_time', 'encapsulated_packets', 'encapsulated_octets', 'is_active'], name, value)


                    class MapCacheRloc(Entity):
                        """
                        List of locators for positive mapping
                        
                        .. attribute:: afi  (key)
                        
                        	LISP Address\-Family of the address
                        	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                        
                        .. attribute:: address  (key)
                        
                        	LISP address. Format is defined by the AF
                        	**type**\: str
                        
                        .. attribute:: state
                        
                        	Up/down state of the locator
                        	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                        
                        .. attribute:: creation_time
                        
                        	Time when this RLOC entry was created
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: last_state_change_time
                        
                        	Time when up/down state of the RLOC for this map\-cache entry last changed
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: rloc_probe_rtt
                        
                        	Round\-trip time of RLOC probe and corresponding reply
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: milliseconds
                        
                        .. attribute:: params
                        
                        	Properties of the locator
                        	**type**\:  :py:class:`Params <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc.Params>`
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-10-25'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc, self).__init__()

                            self.yang_name = "map-cache-rloc"
                            self.yang_parent_name = "map-cache"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['afi','address']
                            self._child_container_classes = OrderedDict([("params", ("params", LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc.Params))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', YLeaf(YType.enumeration, 'afi')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('state', YLeaf(YType.enumeration, 'state')),
                                ('creation_time', YLeaf(YType.str, 'creation-time')),
                                ('last_state_change_time', YLeaf(YType.str, 'last-state-change-time')),
                                ('rloc_probe_rtt', YLeaf(YType.uint32, 'rloc-probe-rtt')),
                            ])
                            self.afi = None
                            self.address = None
                            self.state = None
                            self.creation_time = None
                            self.last_state_change_time = None
                            self.rloc_probe_rtt = None

                            self.params = LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc.Params()
                            self.params.parent = self
                            self._children_name_map["params"] = "params"
                            self._children_yang_names.add("params")
                            self._segment_path = lambda: "map-cache-rloc" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc, ['afi', 'address', 'state', 'creation_time', 'last_state_change_time', 'rloc_probe_rtt'], name, value)


                        class Params(Entity):
                            """
                            Properties of the locator
                            
                            .. attribute:: priority
                            
                            	Locator priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: weight
                            
                            	Locator weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_priority
                            
                            	Locator's multicast priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_weight
                            
                            	Locator's multicast weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'lisp-ios-xe-oper'
                            _revision = '2017-10-25'

                            def __init__(self):
                                super(LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc.Params, self).__init__()

                                self.yang_name = "params"
                                self.yang_parent_name = "map-cache-rloc"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('priority', YLeaf(YType.uint8, 'priority')),
                                    ('weight', YLeaf(YType.uint8, 'weight')),
                                    ('mcast_priority', YLeaf(YType.uint8, 'mcast-priority')),
                                    ('mcast_weight', YLeaf(YType.uint8, 'mcast-weight')),
                                ])
                                self.priority = None
                                self.weight = None
                                self.mcast_priority = None
                                self.mcast_weight = None
                                self._segment_path = lambda: "params"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LispState.LispRouters.Instances.Af.MapCache.MapCacheRloc.Params, ['priority', 'weight', 'mcast_priority', 'mcast_weight'], name, value)


                class LocalDbase(Entity):
                    """
                    ETR's database of local EID prefixes
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the prefix
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: prefix  (key)
                    
                    	LISP prefix. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: lsb
                    
                    	The Locator Status Bits for this EID\-Prefix
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: is_reachable
                    
                    	If the prefix is currently reachable from this device via EID interfaces
                    	**type**\: bool
                    
                    .. attribute:: local_dbase_rloc
                    
                    	List of locators
                    	**type**\: list of  		 :py:class:`LocalDbaseRloc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.LocalDbase, self).__init__()

                        self.yang_name = "local-dbase"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','prefix']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([("local-dbase-rloc", ("local_dbase_rloc", LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc))])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('prefix', YLeaf(YType.str, 'prefix')),
                            ('lsb', YLeaf(YType.uint32, 'lsb')),
                            ('is_reachable', YLeaf(YType.boolean, 'is-reachable')),
                        ])
                        self.afi = None
                        self.prefix = None
                        self.lsb = None
                        self.is_reachable = None

                        self.local_dbase_rloc = YList(self)
                        self._segment_path = lambda: "local-dbase" + "[afi='" + str(self.afi) + "']" + "[prefix='" + str(self.prefix) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.LocalDbase, ['afi', 'prefix', 'lsb', 'is_reachable'], name, value)


                    class LocalDbaseRloc(Entity):
                        """
                        List of locators
                        
                        .. attribute:: afi  (key)
                        
                        	LISP Address\-Family of the address
                        	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                        
                        .. attribute:: address  (key)
                        
                        	LISP address. Format is defined by the AF
                        	**type**\: str
                        
                        .. attribute:: params
                        
                        	Properties of the locator
                        	**type**\:  :py:class:`Params <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc.Params>`
                        
                        .. attribute:: state
                        
                        	Up/down state of the locator
                        	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                        
                        .. attribute:: is_local
                        
                        	Indicates if RLOC local to the device or to another xTR in the site; TRUE means RLOC is local to the device
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-10-25'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc, self).__init__()

                            self.yang_name = "local-dbase-rloc"
                            self.yang_parent_name = "local-dbase"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['afi','address']
                            self._child_container_classes = OrderedDict([("params", ("params", LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc.Params))])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', YLeaf(YType.enumeration, 'afi')),
                                ('address', YLeaf(YType.str, 'address')),
                                ('state', YLeaf(YType.enumeration, 'state')),
                                ('is_local', YLeaf(YType.boolean, 'is-local')),
                            ])
                            self.afi = None
                            self.address = None
                            self.state = None
                            self.is_local = None

                            self.params = LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc.Params()
                            self.params.parent = self
                            self._children_name_map["params"] = "params"
                            self._children_yang_names.add("params")
                            self._segment_path = lambda: "local-dbase-rloc" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc, ['afi', 'address', 'state', 'is_local'], name, value)


                        class Params(Entity):
                            """
                            Properties of the locator
                            
                            .. attribute:: priority
                            
                            	Locator priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: weight
                            
                            	Locator weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_priority
                            
                            	Locator's multicast priority
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            .. attribute:: mcast_weight
                            
                            	Locator's multicast weight
                            	**type**\: int
                            
                            	**range:** 0..255
                            
                            

                            """

                            _prefix = 'lisp-ios-xe-oper'
                            _revision = '2017-10-25'

                            def __init__(self):
                                super(LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc.Params, self).__init__()

                                self.yang_name = "params"
                                self.yang_parent_name = "local-dbase-rloc"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('priority', YLeaf(YType.uint8, 'priority')),
                                    ('weight', YLeaf(YType.uint8, 'weight')),
                                    ('mcast_priority', YLeaf(YType.uint8, 'mcast-priority')),
                                    ('mcast_weight', YLeaf(YType.uint8, 'mcast-weight')),
                                ])
                                self.priority = None
                                self.weight = None
                                self.mcast_priority = None
                                self.mcast_weight = None
                                self._segment_path = lambda: "params"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LispState.LispRouters.Instances.Af.LocalDbase.LocalDbaseRloc.Params, ['priority', 'weight', 'mcast_priority', 'mcast_weight'], name, value)


                class MsRegistrations(Entity):
                    """
                    Map\-Server database of registered EID Prefixes
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the prefix
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: prefix  (key)
                    
                    	LISP prefix. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: last_registration_source
                    
                    	Source address of the last valid registration received for this EID prefix
                    	**type**\:  :py:class:`LastRegistrationSource <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MsRegistrations.LastRegistrationSource>`
                    
                    .. attribute:: last_registration_source_port
                    
                    	Source port of the last valid registration received for this EID prefix
                    	**type**\: int
                    
                    	**range:** 0..65535
                    
                    .. attribute:: creation_time
                    
                    	Time when a valid registration was first received for this EID prefix
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: last_registration_time
                    
                    	Time when most recent valid registration was received for this EID prefix
                    	**type**\: str
                    
                    	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                    
                    .. attribute:: site_name
                    
                    	Name of site matching this registration
                    	**type**\: str
                    
                    .. attribute:: site_description
                    
                    	Description given for the site matching this registration
                    	**type**\: str
                    
                    .. attribute:: is_registered
                    
                    	Indicates the registration status of the given EID\-Prefix. If this object is true, then it means the EID\-Prefix is registered
                    	**type**\: bool
                    
                    .. attribute:: authentication_error
                    
                    	Count of registrations received for the EID prefix with authentication error
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: rloc_mismatch_error
                    
                    	Count of received registrations for the prefix that had at least one RLOC that was not in the allowed list of RLOCs
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: etr_registrations
                    
                    	List of registrations for this EID prefix received from different ETRs
                    	**type**\: list of  		 :py:class:`EtrRegistrations <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.MsRegistrations, self).__init__()

                        self.yang_name = "ms-registrations"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','prefix']
                        self._child_container_classes = OrderedDict([("last-registration-source", ("last_registration_source", LispState.LispRouters.Instances.Af.MsRegistrations.LastRegistrationSource))])
                        self._child_list_classes = OrderedDict([("etr-registrations", ("etr_registrations", LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations))])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('prefix', YLeaf(YType.str, 'prefix')),
                            ('last_registration_source_port', YLeaf(YType.uint16, 'last-registration-source-port')),
                            ('creation_time', YLeaf(YType.str, 'creation-time')),
                            ('last_registration_time', YLeaf(YType.str, 'last-registration-time')),
                            ('site_name', YLeaf(YType.str, 'site-name')),
                            ('site_description', YLeaf(YType.str, 'site-description')),
                            ('is_registered', YLeaf(YType.boolean, 'is-registered')),
                            ('authentication_error', YLeaf(YType.uint64, 'authentication-error')),
                            ('rloc_mismatch_error', YLeaf(YType.uint64, 'rloc-mismatch-error')),
                        ])
                        self.afi = None
                        self.prefix = None
                        self.last_registration_source_port = None
                        self.creation_time = None
                        self.last_registration_time = None
                        self.site_name = None
                        self.site_description = None
                        self.is_registered = None
                        self.authentication_error = None
                        self.rloc_mismatch_error = None

                        self.last_registration_source = LispState.LispRouters.Instances.Af.MsRegistrations.LastRegistrationSource()
                        self.last_registration_source.parent = self
                        self._children_name_map["last_registration_source"] = "last-registration-source"
                        self._children_yang_names.add("last-registration-source")

                        self.etr_registrations = YList(self)
                        self._segment_path = lambda: "ms-registrations" + "[afi='" + str(self.afi) + "']" + "[prefix='" + str(self.prefix) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.MsRegistrations, ['afi', 'prefix', 'last_registration_source_port', 'creation_time', 'last_registration_time', 'site_name', 'site_description', 'is_registered', 'authentication_error', 'rloc_mismatch_error'], name, value)


                    class LastRegistrationSource(Entity):
                        """
                        Source address of the last valid registration received
                        for this EID prefix
                        
                        .. attribute:: afi
                        
                        	LISP Address\-Family of the address
                        	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                        
                        .. attribute:: address
                        
                        	LISP address. Format is defined by the AF
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-10-25'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.MsRegistrations.LastRegistrationSource, self).__init__()

                            self.yang_name = "last-registration-source"
                            self.yang_parent_name = "ms-registrations"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('afi', YLeaf(YType.enumeration, 'afi')),
                                ('address', YLeaf(YType.str, 'address')),
                            ])
                            self.afi = None
                            self.address = None
                            self._segment_path = lambda: "last-registration-source"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.MsRegistrations.LastRegistrationSource, ['afi', 'address'], name, value)


                    class EtrRegistrations(Entity):
                        """
                        List of registrations for this EID prefix received
                        from different ETRs
                        
                        .. attribute:: source_address  (key)
                        
                        	RLOC address of the registration source
                        	**type**\: union of the below types:
                        
                        		**type**\: str
                        
                        			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        		**type**\: str
                        
                        			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_port  (key)
                        
                        	Port of the registration source
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: last_registration_time
                        
                        	Time when valid registration from the source was last received
                        	**type**\: str
                        
                        	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                        
                        .. attribute:: ttl
                        
                        	Registration validity period
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: minutes
                        
                        .. attribute:: proxy_reply
                        
                        	Indicates if the registering ETR requested proxy\-replying on Map\-Requests by the Map\-Server
                        	**type**\: bool
                        
                        .. attribute:: wants_map_notify
                        
                        	Indicates if the registering ETR wants to be informed about matching registrations with Map\-Notifies
                        	**type**\: bool
                        
                        .. attribute:: ms_registration_rloc
                        
                        	List of locators
                        	**type**\: list of  		 :py:class:`MsRegistrationRloc <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc>`
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-10-25'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations, self).__init__()

                            self.yang_name = "etr-registrations"
                            self.yang_parent_name = "ms-registrations"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['source_address','source_port']
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("ms-registration-rloc", ("ms_registration_rloc", LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc))])
                            self._leafs = OrderedDict([
                                ('source_address', YLeaf(YType.str, 'source-address')),
                                ('source_port', YLeaf(YType.uint16, 'source-port')),
                                ('last_registration_time', YLeaf(YType.str, 'last-registration-time')),
                                ('ttl', YLeaf(YType.uint32, 'ttl')),
                                ('proxy_reply', YLeaf(YType.boolean, 'proxy-reply')),
                                ('wants_map_notify', YLeaf(YType.boolean, 'wants-map-notify')),
                            ])
                            self.source_address = None
                            self.source_port = None
                            self.last_registration_time = None
                            self.ttl = None
                            self.proxy_reply = None
                            self.wants_map_notify = None

                            self.ms_registration_rloc = YList(self)
                            self._segment_path = lambda: "etr-registrations" + "[source-address='" + str(self.source_address) + "']" + "[source-port='" + str(self.source_port) + "']"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations, ['source_address', 'source_port', 'last_registration_time', 'ttl', 'proxy_reply', 'wants_map_notify'], name, value)


                        class MsRegistrationRloc(Entity):
                            """
                            List of locators
                            
                            .. attribute:: afi  (key)
                            
                            	LISP Address\-Family of the address
                            	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                            
                            .. attribute:: address  (key)
                            
                            	LISP address. Format is defined by the AF
                            	**type**\: str
                            
                            .. attribute:: params
                            
                            	Properties of the locator
                            	**type**\:  :py:class:`Params <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc.Params>`
                            
                            .. attribute:: state
                            
                            	Up/down state of the locator
                            	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                            
                            .. attribute:: is_local
                            
                            	Indicates if RLOC is local to device which sent registration or to another xTR in the site; TRUE means RLOC is local to the registering device
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'lisp-ios-xe-oper'
                            _revision = '2017-10-25'

                            def __init__(self):
                                super(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc, self).__init__()

                                self.yang_name = "ms-registration-rloc"
                                self.yang_parent_name = "etr-registrations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['afi','address']
                                self._child_container_classes = OrderedDict([("params", ("params", LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc.Params))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('afi', YLeaf(YType.enumeration, 'afi')),
                                    ('address', YLeaf(YType.str, 'address')),
                                    ('state', YLeaf(YType.enumeration, 'state')),
                                    ('is_local', YLeaf(YType.boolean, 'is-local')),
                                ])
                                self.afi = None
                                self.address = None
                                self.state = None
                                self.is_local = None

                                self.params = LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc.Params()
                                self.params.parent = self
                                self._children_name_map["params"] = "params"
                                self._children_yang_names.add("params")
                                self._segment_path = lambda: "ms-registration-rloc" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc, ['afi', 'address', 'state', 'is_local'], name, value)


                            class Params(Entity):
                                """
                                Properties of the locator
                                
                                .. attribute:: priority
                                
                                	Locator priority
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: weight
                                
                                	Locator weight
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: mcast_priority
                                
                                	Locator's multicast priority
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: mcast_weight
                                
                                	Locator's multicast weight
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                

                                """

                                _prefix = 'lisp-ios-xe-oper'
                                _revision = '2017-10-25'

                                def __init__(self):
                                    super(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc.Params, self).__init__()

                                    self.yang_name = "params"
                                    self.yang_parent_name = "ms-registration-rloc"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('priority', YLeaf(YType.uint8, 'priority')),
                                        ('weight', YLeaf(YType.uint8, 'weight')),
                                        ('mcast_priority', YLeaf(YType.uint8, 'mcast-priority')),
                                        ('mcast_weight', YLeaf(YType.uint8, 'mcast-weight')),
                                    ])
                                    self.priority = None
                                    self.weight = None
                                    self.mcast_priority = None
                                    self.mcast_weight = None
                                    self._segment_path = lambda: "params"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(LispState.LispRouters.Instances.Af.MsRegistrations.EtrRegistrations.MsRegistrationRloc.Params, ['priority', 'weight', 'mcast_priority', 'mcast_weight'], name, value)


                class MapServers(Entity):
                    """
                    List of Map\-Servers to which the ETR should register
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the address
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: address  (key)
                    
                    	LISP address. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	Up/down state of the locator
                    	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.MapServers, self).__init__()

                        self.yang_name = "map-servers"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','address']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('address', YLeaf(YType.str, 'address')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.afi = None
                        self.address = None
                        self.state = None
                        self._segment_path = lambda: "map-servers" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.MapServers, ['afi', 'address', 'state'], name, value)


                class MapResolvers(Entity):
                    """
                    List of Map\-Resolvers where [P]ITR should send its
                    Map\-Requests
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the address
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: address  (key)
                    
                    	LISP address. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	Up/down state of the locator
                    	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.MapResolvers, self).__init__()

                        self.yang_name = "map-resolvers"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','address']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('address', YLeaf(YType.str, 'address')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.afi = None
                        self.address = None
                        self.state = None
                        self._segment_path = lambda: "map-resolvers" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.MapResolvers, ['afi', 'address', 'state'], name, value)


                class ProxyEtrs(Entity):
                    """
                    List of all Proxy ETRs that this device is configured
                    to use
                    
                    .. attribute:: afi  (key)
                    
                    	LISP Address\-Family of the address
                    	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
                    
                    .. attribute:: address  (key)
                    
                    	LISP address. Format is defined by the AF
                    	**type**\: str
                    
                    .. attribute:: params
                    
                    	Properties of the locator
                    	**type**\:  :py:class:`Params <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispState.LispRouters.Instances.Af.ProxyEtrs.Params>`
                    
                    .. attribute:: state
                    
                    	Up/down state of the locator
                    	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
                    
                    

                    """

                    _prefix = 'lisp-ios-xe-oper'
                    _revision = '2017-10-25'

                    def __init__(self):
                        super(LispState.LispRouters.Instances.Af.ProxyEtrs, self).__init__()

                        self.yang_name = "proxy-etrs"
                        self.yang_parent_name = "af"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi','address']
                        self._child_container_classes = OrderedDict([("params", ("params", LispState.LispRouters.Instances.Af.ProxyEtrs.Params))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi', YLeaf(YType.enumeration, 'afi')),
                            ('address', YLeaf(YType.str, 'address')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                        ])
                        self.afi = None
                        self.address = None
                        self.state = None

                        self.params = LispState.LispRouters.Instances.Af.ProxyEtrs.Params()
                        self.params.parent = self
                        self._children_name_map["params"] = "params"
                        self._children_yang_names.add("params")
                        self._segment_path = lambda: "proxy-etrs" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(LispState.LispRouters.Instances.Af.ProxyEtrs, ['afi', 'address', 'state'], name, value)


                    class Params(Entity):
                        """
                        Properties of the locator
                        
                        .. attribute:: priority
                        
                        	Locator priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: weight
                        
                        	Locator weight
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: mcast_priority
                        
                        	Locator's multicast priority
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        .. attribute:: mcast_weight
                        
                        	Locator's multicast weight
                        	**type**\: int
                        
                        	**range:** 0..255
                        
                        

                        """

                        _prefix = 'lisp-ios-xe-oper'
                        _revision = '2017-10-25'

                        def __init__(self):
                            super(LispState.LispRouters.Instances.Af.ProxyEtrs.Params, self).__init__()

                            self.yang_name = "params"
                            self.yang_parent_name = "proxy-etrs"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('priority', YLeaf(YType.uint8, 'priority')),
                                ('weight', YLeaf(YType.uint8, 'weight')),
                                ('mcast_priority', YLeaf(YType.uint8, 'mcast-priority')),
                                ('mcast_weight', YLeaf(YType.uint8, 'mcast-weight')),
                            ])
                            self.priority = None
                            self.weight = None
                            self.mcast_priority = None
                            self.mcast_weight = None
                            self._segment_path = lambda: "params"

                        def __setattr__(self, name, value):
                            self._perform_setattr(LispState.LispRouters.Instances.Af.ProxyEtrs.Params, ['priority', 'weight', 'mcast_priority', 'mcast_weight'], name, value)


            class MsEidMembership(Entity):
                """
                MS registration EID membership list (list of locators
                known to the MS as allowed to send traffic in the
                instance)
                
                .. attribute:: rloc  (key)
                
                	RLOC which is the allowed member
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: member_since
                
                	Time when this RLOC was added to the list of allowed locators
                	**type**\: str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: is_gleaned
                
                	Indicates if MS gleaned this RLOC from received EID prefix registration
                	**type**\: bool
                
                .. attribute:: is_configured
                
                	Indicates if this RLOC membership was provided via configuration
                	**type**\: bool
                
                

                """

                _prefix = 'lisp-ios-xe-oper'
                _revision = '2017-10-25'

                def __init__(self):
                    super(LispState.LispRouters.Instances.MsEidMembership, self).__init__()

                    self.yang_name = "ms-eid-membership"
                    self.yang_parent_name = "instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['rloc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rloc', YLeaf(YType.str, 'rloc')),
                        ('member_since', YLeaf(YType.str, 'member-since')),
                        ('is_gleaned', YLeaf(YType.boolean, 'is-gleaned')),
                        ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                    ])
                    self.rloc = None
                    self.member_since = None
                    self.is_gleaned = None
                    self.is_configured = None
                    self._segment_path = lambda: "ms-eid-membership" + "[rloc='" + str(self.rloc) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(LispState.LispRouters.Instances.MsEidMembership, ['rloc', 'member_since', 'is_gleaned', 'is_configured'], name, value)


            class EtrEidMembership(Entity):
                """
                ETR EID membership list (list of locators known to the ETR
                as allowed to send traffic in the instance)
                
                .. attribute:: rloc  (key)
                
                	RLOC which is the allowed member
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: member_since
                
                	Time when this RLOC was added to the list of allowed locators
                	**type**\: str
                
                	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
                
                .. attribute:: is_learned_from_ms
                
                	Indicates if ETR learned about this RLOC membership via message received from a Map\-Server
                	**type**\: bool
                
                .. attribute:: is_configured
                
                	Indicates if this RLOC membership was provided via configuration
                	**type**\: bool
                
                

                """

                _prefix = 'lisp-ios-xe-oper'
                _revision = '2017-10-25'

                def __init__(self):
                    super(LispState.LispRouters.Instances.EtrEidMembership, self).__init__()

                    self.yang_name = "etr-eid-membership"
                    self.yang_parent_name = "instances"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = ['rloc']
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('rloc', YLeaf(YType.str, 'rloc')),
                        ('member_since', YLeaf(YType.str, 'member-since')),
                        ('is_learned_from_ms', YLeaf(YType.boolean, 'is-learned-from-ms')),
                        ('is_configured', YLeaf(YType.boolean, 'is-configured')),
                    ])
                    self.rloc = None
                    self.member_since = None
                    self.is_learned_from_ms = None
                    self.is_configured = None
                    self._segment_path = lambda: "etr-eid-membership" + "[rloc='" + str(self.rloc) + "']"

                def __setattr__(self, name, value):
                    self._perform_setattr(LispState.LispRouters.Instances.EtrEidMembership, ['rloc', 'member_since', 'is_learned_from_ms', 'is_configured'], name, value)


        class Sessions(Entity):
            """
            List of Reliable Registration sessions
            
            .. attribute:: local_address  (key)
            
            	Address of the local socket
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: peer_address  (key)
            
            	Address of the peer
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: local_port  (key)
            
            	Port of the local socket
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: peer_port  (key)
            
            	Port used by the peer
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: state
            
            	Up/down state of the session
            	**type**\:  :py:class:`LispSessionStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispSessionStateType>`
            
            .. attribute:: last_state_change_time
            
            	Timestamp when the session's state last changed
            	**type**\: str
            
            	**pattern:** \\d{4}\-\\d{2}\-\\d{2}T\\d{2}\:\\d{2}\:\\d{2}(\\.\\d+)?(Z\|[\\+\\\-]\\d{2}\:\\d{2})
            
            .. attribute:: is_role_active
            
            	Is session opening role Active or Passive; TRUE means session role is Active
            	**type**\: bool
            
            .. attribute:: is_routable
            
            	Is route to peer's address known
            	**type**\: bool
            
            .. attribute:: messages_in
            
            	Number of messages received over this session
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: messages_out
            
            	Number of messages sent over this session
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: bytes_in
            
            	Number of bytes received over this session
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: bytes_out
            
            	Number of bytes sent over this session
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'lisp-ios-xe-oper'
            _revision = '2017-10-25'

            def __init__(self):
                super(LispState.LispRouters.Sessions, self).__init__()

                self.yang_name = "sessions"
                self.yang_parent_name = "lisp-routers"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['local_address','peer_address','local_port','peer_port']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('local_address', YLeaf(YType.str, 'local-address')),
                    ('peer_address', YLeaf(YType.str, 'peer-address')),
                    ('local_port', YLeaf(YType.uint16, 'local-port')),
                    ('peer_port', YLeaf(YType.uint16, 'peer-port')),
                    ('state', YLeaf(YType.enumeration, 'state')),
                    ('last_state_change_time', YLeaf(YType.str, 'last-state-change-time')),
                    ('is_role_active', YLeaf(YType.boolean, 'is-role-active')),
                    ('is_routable', YLeaf(YType.boolean, 'is-routable')),
                    ('messages_in', YLeaf(YType.uint64, 'messages-in')),
                    ('messages_out', YLeaf(YType.uint64, 'messages-out')),
                    ('bytes_in', YLeaf(YType.uint64, 'bytes-in')),
                    ('bytes_out', YLeaf(YType.uint64, 'bytes-out')),
                ])
                self.local_address = None
                self.peer_address = None
                self.local_port = None
                self.peer_port = None
                self.state = None
                self.last_state_change_time = None
                self.is_role_active = None
                self.is_routable = None
                self.messages_in = None
                self.messages_out = None
                self.bytes_in = None
                self.bytes_out = None
                self._segment_path = lambda: "sessions" + "[local-address='" + str(self.local_address) + "']" + "[peer-address='" + str(self.peer_address) + "']" + "[local-port='" + str(self.local_port) + "']" + "[peer-port='" + str(self.peer_port) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(LispState.LispRouters.Sessions, ['local_address', 'peer_address', 'local_port', 'peer_port', 'state', 'last_state_change_time', 'is_role_active', 'is_routable', 'messages_in', 'messages_out', 'bytes_in', 'bytes_out'], name, value)


        class LocalRlocs(Entity):
            """
            This list represents the set of routing locators
            configured on this device
            
            .. attribute:: afi  (key)
            
            	LISP Address\-Family of the address
            	**type**\:  :py:class:`LispAddressFamilyType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispAddressFamilyType>`
            
            .. attribute:: address  (key)
            
            	LISP address. Format is defined by the AF
            	**type**\: str
            
            .. attribute:: state
            
            	Up/down state of the locator
            	**type**\:  :py:class:`LispRlocStateType <ydk.models.cisco_ios_xe.Cisco_IOS_XE_lisp_oper.LispRlocStateType>`
            
            .. attribute:: is_local
            
            	Indicates if RLOC is local to the device or to another xTR in the site; TRUE means RLOC is local to the device
            	**type**\: bool
            
            

            """

            _prefix = 'lisp-ios-xe-oper'
            _revision = '2017-10-25'

            def __init__(self):
                super(LispState.LispRouters.LocalRlocs, self).__init__()

                self.yang_name = "local-rlocs"
                self.yang_parent_name = "lisp-routers"
                self.is_top_level_class = False
                self.has_list_ancestor = True
                self.ylist_key_names = ['afi','address']
                self._child_container_classes = OrderedDict([])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('afi', YLeaf(YType.enumeration, 'afi')),
                    ('address', YLeaf(YType.str, 'address')),
                    ('state', YLeaf(YType.enumeration, 'state')),
                    ('is_local', YLeaf(YType.boolean, 'is-local')),
                ])
                self.afi = None
                self.address = None
                self.state = None
                self.is_local = None
                self._segment_path = lambda: "local-rlocs" + "[afi='" + str(self.afi) + "']" + "[address='" + str(self.address) + "']"

            def __setattr__(self, name, value):
                self._perform_setattr(LispState.LispRouters.LocalRlocs, ['afi', 'address', 'state', 'is_local'], name, value)

    def clone_ptr(self):
        self._top_entity = LispState()
        return self._top_entity

