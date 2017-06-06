""" Cisco_IOS_XE_bgp_oper 

This module contains a collection of YANG definitions for
monitoring BGP information.Copyright (c) 2016\-2017 by Cisco Systems, Inc.All rights reserved.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class BgpAfiSafiEnum(Enum):
    """
    BgpAfiSafiEnum

    .. data:: ipv4_mdt = 0

    .. data:: ipv4_multicast = 1

    .. data:: ipv4_unicast = 2

    .. data:: ipv4_mvpn = 3

    .. data:: ipv4_flowspec = 4

    .. data:: ipv6_multicast = 5

    .. data:: ipv6_unicast = 6

    .. data:: ipv6_mvpn = 7

    .. data:: ipv6_flowspec = 8

    .. data:: l2vpn_vpls = 9

    .. data:: l2vpn_e_vpn = 10

    .. data:: nsap_unicast = 11

    .. data:: rtfilter_unicast = 12

    .. data:: vpnv4_multicast = 13

    .. data:: vpnv4_unicast = 14

    .. data:: vpnv6_unicast = 15

    .. data:: vpnv6_multicast = 16

    .. data:: vpnv4_flowspec = 17

    .. data:: vpnv6_flowspec = 18

    """

    ipv4_mdt = 0

    ipv4_multicast = 1

    ipv4_unicast = 2

    ipv4_mvpn = 3

    ipv4_flowspec = 4

    ipv6_multicast = 5

    ipv6_unicast = 6

    ipv6_mvpn = 7

    ipv6_flowspec = 8

    l2vpn_vpls = 9

    l2vpn_e_vpn = 10

    nsap_unicast = 11

    rtfilter_unicast = 12

    vpnv4_multicast = 13

    vpnv4_unicast = 14

    vpnv6_unicast = 15

    vpnv6_multicast = 16

    vpnv4_flowspec = 17

    vpnv6_flowspec = 18


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpAfiSafiEnum']


class BgpFsmStateEnum(Enum):
    """
    BgpFsmStateEnum

    .. data:: idle = 0

    	neighbor is in Idle state

    .. data:: connect = 1

    	neighbor is in Connect state

    .. data:: active = 2

    	neighbor is in Active state

    .. data:: opensent = 3

    	neighbor is in OpenSent state

    .. data:: openconfirm = 4

    	neighbor is in OpenConfirm state

    .. data:: established = 5

    	neighbor is in Established state

    .. data:: nonnegotiated = 6

    	neighbor is Non Negotiated

    """

    idle = 0

    connect = 1

    active = 2

    opensent = 3

    openconfirm = 4

    established = 5

    nonnegotiated = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpFsmStateEnum']


class BgpLinkEnum(Enum):
    """
    BgpLinkEnum

    .. data:: internal = 0

    	iBGP neighbors

    .. data:: external = 1

    	eBGP neighbors

    """

    internal = 0

    external = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpLinkEnum']


class BgpModeEnum(Enum):
    """
    BgpModeEnum

    .. data:: active = 0

    	active connection

    .. data:: passive = 1

    	passive connection

    """

    active = 0

    passive = 1


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpModeEnum']


class BgpOriginCodeEnum(Enum):
    """
    BgpOriginCodeEnum

    .. data:: origin_igp = 0

    	BGP origin code IGP

    .. data:: origin_egp = 1

    	BGP origin code EGP

    .. data:: origin_incomplete = 2

    	BGP origin code incomplete

    """

    origin_igp = 0

    origin_egp = 1

    origin_incomplete = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpOriginCodeEnum']


class BgpRouteOptionEnum(Enum):
    """
    BgpRouteOptionEnum

    .. data:: bgp_all_routes = 0

    	All entries

    .. data:: bgp_cidr_only_routes = 1

    	CIDR ONLY route entries

    .. data:: bgp_dampened_routes = 2

    	Dampened route entries

    .. data:: bgp_rib_fail_routes = 3

    	Rib failure routes

    .. data:: bgp_injected_routes = 4

    	Injected route entries

    .. data:: bgp_pending_routes = 5

    	prefixes pending deletion

    .. data:: bgp_inconsistent_routes = 6

    	inconsistency paths

    """

    bgp_all_routes = 0

    bgp_cidr_only_routes = 1

    bgp_dampened_routes = 2

    bgp_rib_fail_routes = 3

    bgp_injected_routes = 4

    bgp_pending_routes = 5

    bgp_inconsistent_routes = 6


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpRouteOptionEnum']


class BgpRpkiStatusEnum(Enum):
    """
    BgpRpkiStatusEnum

    .. data:: rpki_valid = 0

    .. data:: rpki_invalid = 1

    .. data:: rpki_not_found = 2

    """

    rpki_valid = 0

    rpki_invalid = 1

    rpki_not_found = 2


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpRpkiStatusEnum']


class TcpFsmStateEnum(Enum):
    """
    TcpFsmStateEnum

    .. data:: closed = 0

    	no connection

    .. data:: listen = 1

    	waiting for a connection request from any remote TCP

    .. data:: synsent = 2

    	waiting for a matching connection request

    	after having sent a connection request

    .. data:: synrcvd = 3

    	waiting for a confirming connection request acknowledgment

    	after having both received and sent a connection request

    .. data:: established = 4

    	connection established

    .. data:: finwait1 = 5

    	waiting for a connection termination request

    	from the remote TCP, or an acknowledgment of

    	the connection termination request previously sent

    .. data:: finwait2 = 6

    	waiting for a connection termination request from the

    	remote TCP

    .. data:: closewait = 7

    	waiting for a connection termination request from

    	the local use

    .. data:: lastack = 8

    	waiting for an acknowledgment of the connection termination

    	request previously sent to the remote TCP

    .. data:: closing = 9

    	waiting for a connection termination request acknowledgment

    	from the remote

    .. data:: timewait = 10

    	waiting for enough time to pass to be sure the remote TCP

    	received the acknowledgment of its connection termination

    	request

    """

    closed = 0

    listen = 1

    synsent = 2

    synrcvd = 3

    established = 4

    finwait1 = 5

    finwait2 = 6

    closewait = 7

    lastack = 8

    closing = 9

    timewait = 10


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['TcpFsmStateEnum']



class BgpState(object):
    """
    Data nodes for BGP entries.
    
    .. attribute:: address_families
    
    	
    	**type**\:   :py:class:`AddressFamilies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies>`
    
    .. attribute:: neighbors
    
    	
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors>`
    
    

    """

    _prefix = 'bgp-ios-xe-oper'
    _revision = '2017-02-07'

    def __init__(self):
        self.address_families = BgpState.AddressFamilies()
        self.address_families.parent = self
        self.neighbors = BgpState.Neighbors()
        self.neighbors.parent = self


    class Neighbors(object):
        """
        
        
        .. attribute:: neighbor
        
        	
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.neighbor = YList()
            self.neighbor.parent = self
            self.neighbor.name = 'neighbor'


        class Neighbor(object):
            """
            
            
            .. attribute:: afi_safi  <key>
            
            	
            	**type**\:   :py:class:`BgpAfiSafiEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpAfiSafiEnum>`
            
            .. attribute:: vrf_name  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: neighbor_id  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: bgp_neighbor_counters
            
            	
            	**type**\:   :py:class:`BgpNeighborCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.BgpNeighborCounters>`
            
            .. attribute:: bgp_version
            
            	BGP version being used to communicate with the         remote router
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: connection
            
            	
            	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.Connection>`
            
            .. attribute:: description
            
            	
            	**type**\:  str
            
            .. attribute:: installed_prefixes
            
            	number of installed prefixes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_read
            
            	since BGP last received a message to this neighbor
            	**type**\:  str
            
            .. attribute:: last_write
            
            	since BGP last sent a message from this neighbor
            	**type**\:  str
            
            .. attribute:: link
            
            	
            	**type**\:   :py:class:`BgpLinkEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpLinkEnum>`
            
            .. attribute:: negotiated_cap
            
            	Information for bgp neighbor session negotiated capabilities
            	**type**\:  list of str
            
            .. attribute:: negotiated_keepalive_timers
            
            	
            	**type**\:   :py:class:`NegotiatedKeepaliveTimers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.NegotiatedKeepaliveTimers>`
            
            .. attribute:: prefix_activity
            
            	
            	**type**\:   :py:class:`PrefixActivity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.PrefixActivity>`
            
            .. attribute:: session_state
            
            	
            	**type**\:   :py:class:`BgpFsmStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmStateEnum>`
            
            .. attribute:: transport
            
            	
            	**type**\:   :py:class:`Transport <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.Transport>`
            
            .. attribute:: up_time
            
            	How long the bgp session has been up since         the sessioin was established
            	**type**\:  str
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.afi_safi = None
                self.vrf_name = None
                self.neighbor_id = None
                self.bgp_neighbor_counters = BgpState.Neighbors.Neighbor.BgpNeighborCounters()
                self.bgp_neighbor_counters.parent = self
                self.bgp_version = None
                self.connection = BgpState.Neighbors.Neighbor.Connection()
                self.connection.parent = self
                self.description = None
                self.installed_prefixes = None
                self.last_read = None
                self.last_write = None
                self.link = None
                self.negotiated_cap = YLeafList()
                self.negotiated_cap.parent = self
                self.negotiated_cap.name = 'negotiated_cap'
                self.negotiated_keepalive_timers = BgpState.Neighbors.Neighbor.NegotiatedKeepaliveTimers()
                self.negotiated_keepalive_timers.parent = self
                self.prefix_activity = BgpState.Neighbors.Neighbor.PrefixActivity()
                self.prefix_activity.parent = self
                self.session_state = None
                self.transport = BgpState.Neighbors.Neighbor.Transport()
                self.transport.parent = self
                self.up_time = None


            class NegotiatedKeepaliveTimers(object):
                """
                
                
                .. attribute:: hold_time
                
                	Hold time
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: keepalive_interval
                
                	keepalive interval
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.hold_time = None
                    self.keepalive_interval = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:negotiated-keepalive-timers'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.hold_time is not None:
                        return True

                    if self.keepalive_interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.Neighbors.Neighbor.NegotiatedKeepaliveTimers']['meta_info']


            class BgpNeighborCounters(object):
                """
                
                
                .. attribute:: inq_depth
                
                	Input Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: outq_depth
                
                	Output Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received
                
                	
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.BgpNeighborCounters.Received>`
                
                .. attribute:: sent
                
                	
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.BgpNeighborCounters.Sent>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.inq_depth = None
                    self.outq_depth = None
                    self.received = BgpState.Neighbors.Neighbor.BgpNeighborCounters.Received()
                    self.received.parent = self
                    self.sent = BgpState.Neighbors.Neighbor.BgpNeighborCounters.Sent()
                    self.sent.parent = self


                class Sent(object):
                    """
                    
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opens
                    
                    	OPEN messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.keepalives = None
                        self.notifications = None
                        self.opens = None
                        self.route_refreshes = None
                        self.updates = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:sent'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.keepalives is not None:
                            return True

                        if self.notifications is not None:
                            return True

                        if self.opens is not None:
                            return True

                        if self.route_refreshes is not None:
                            return True

                        if self.updates is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                        return meta._meta_table['BgpState.Neighbors.Neighbor.BgpNeighborCounters.Sent']['meta_info']


                class Received(object):
                    """
                    
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opens
                    
                    	OPEN messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE messages
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.keepalives = None
                        self.notifications = None
                        self.opens = None
                        self.route_refreshes = None
                        self.updates = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:received'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.keepalives is not None:
                            return True

                        if self.notifications is not None:
                            return True

                        if self.opens is not None:
                            return True

                        if self.route_refreshes is not None:
                            return True

                        if self.updates is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                        return meta._meta_table['BgpState.Neighbors.Neighbor.BgpNeighborCounters.Received']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:bgp-neighbor-counters'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.inq_depth is not None:
                        return True

                    if self.outq_depth is not None:
                        return True

                    if self.received is not None and self.received._has_data():
                        return True

                    if self.sent is not None and self.sent._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.Neighbors.Neighbor.BgpNeighborCounters']['meta_info']


            class Connection(object):
                """
                
                
                .. attribute:: last_reset
                
                	since the peering session was last reset
                	**type**\:  str
                
                .. attribute:: mode
                
                	
                	**type**\:   :py:class:`BgpModeEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpModeEnum>`
                
                .. attribute:: reset_reason
                
                	The reason for the last reset
                	**type**\:  str
                
                .. attribute:: state
                
                	TCP FSM state
                	**type**\:   :py:class:`TcpFsmStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.TcpFsmStateEnum>`
                
                .. attribute:: total_dropped
                
                	number of times that a valid session has failed  or been taken down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_established
                
                	number of times a TCP and BGP connection has been  successfully established
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.last_reset = None
                    self.mode = None
                    self.reset_reason = None
                    self.state = None
                    self.total_dropped = None
                    self.total_established = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:connection'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.last_reset is not None:
                        return True

                    if self.mode is not None:
                        return True

                    if self.reset_reason is not None:
                        return True

                    if self.state is not None:
                        return True

                    if self.total_dropped is not None:
                        return True

                    if self.total_established is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.Neighbors.Neighbor.Connection']['meta_info']


            class Transport(object):
                """
                
                
                .. attribute:: foreign_host
                
                	Remote address to which the BGP session has established
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: foreign_port
                
                	Remote port used by the peer for the TCP session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_host
                
                	Local address used for the TCP session
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                
                ----
                	**type**\:  str
                
                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                
                ----
                .. attribute:: local_port
                
                	Local TCP port used for TCP session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: mss
                
                	Maximum Data segment size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: path_mtu_discovery
                
                	
                	**type**\:  bool
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.foreign_host = None
                    self.foreign_port = None
                    self.local_host = None
                    self.local_port = None
                    self.mss = None
                    self.path_mtu_discovery = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:transport'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.foreign_host is not None:
                        return True

                    if self.foreign_port is not None:
                        return True

                    if self.local_host is not None:
                        return True

                    if self.local_port is not None:
                        return True

                    if self.mss is not None:
                        return True

                    if self.path_mtu_discovery is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.Neighbors.Neighbor.Transport']['meta_info']


            class PrefixActivity(object):
                """
                
                
                .. attribute:: received
                
                	
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.PrefixActivity.Received>`
                
                .. attribute:: sent
                
                	
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.Neighbors.Neighbor.PrefixActivity.Sent>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.received = BgpState.Neighbors.Neighbor.PrefixActivity.Received()
                    self.received.parent = self
                    self.sent = BgpState.Neighbors.Neighbor.PrefixActivity.Sent()
                    self.sent.parent = self


                class Sent(object):
                    """
                    
                    
                    .. attribute:: bestpaths
                    
                    	Number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: current_prefixes
                    
                    	Current number of prefixes accepted
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	Number of times that a prefix has been withdrawn  because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	number of times that a prefix has been withdrawn  and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	Number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	Total number of prefixes accepted
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.bestpaths = None
                        self.current_prefixes = None
                        self.explicit_withdraw = None
                        self.implicit_withdraw = None
                        self.multipaths = None
                        self.total_prefixes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:sent'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bestpaths is not None:
                            return True

                        if self.current_prefixes is not None:
                            return True

                        if self.explicit_withdraw is not None:
                            return True

                        if self.implicit_withdraw is not None:
                            return True

                        if self.multipaths is not None:
                            return True

                        if self.total_prefixes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                        return meta._meta_table['BgpState.Neighbors.Neighbor.PrefixActivity.Sent']['meta_info']


                class Received(object):
                    """
                    
                    
                    .. attribute:: bestpaths
                    
                    	Number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: current_prefixes
                    
                    	Current number of prefixes accepted
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	Number of times that a prefix has been withdrawn  because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	number of times that a prefix has been withdrawn  and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	Number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	Total number of prefixes accepted
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.bestpaths = None
                        self.current_prefixes = None
                        self.explicit_withdraw = None
                        self.implicit_withdraw = None
                        self.multipaths = None
                        self.total_prefixes = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')

                        return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:received'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.bestpaths is not None:
                            return True

                        if self.current_prefixes is not None:
                            return True

                        if self.explicit_withdraw is not None:
                            return True

                        if self.implicit_withdraw is not None:
                            return True

                        if self.multipaths is not None:
                            return True

                        if self.total_prefixes is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                        return meta._meta_table['BgpState.Neighbors.Neighbor.PrefixActivity.Received']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:prefix-activity'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.received is not None and self.received._has_data():
                        return True

                    if self.sent is not None and self.sent._has_data():
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.Neighbors.Neighbor.PrefixActivity']['meta_info']

            @property
            def _common_path(self):
                if self.afi_safi is None:
                    raise YPYModelError('Key property afi_safi is None')
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')
                if self.neighbor_id is None:
                    raise YPYModelError('Key property neighbor_id is None')

                return '/Cisco-IOS-XE-bgp-oper:bgp-state/Cisco-IOS-XE-bgp-oper:neighbors/Cisco-IOS-XE-bgp-oper:neighbor[Cisco-IOS-XE-bgp-oper:afi-safi = ' + str(self.afi_safi) + '][Cisco-IOS-XE-bgp-oper:vrf-name = ' + str(self.vrf_name) + '][Cisco-IOS-XE-bgp-oper:neighbor-id = ' + str(self.neighbor_id) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.afi_safi is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.neighbor_id is not None:
                    return True

                if self.bgp_neighbor_counters is not None and self.bgp_neighbor_counters._has_data():
                    return True

                if self.bgp_version is not None:
                    return True

                if self.connection is not None and self.connection._has_data():
                    return True

                if self.description is not None:
                    return True

                if self.installed_prefixes is not None:
                    return True

                if self.last_read is not None:
                    return True

                if self.last_write is not None:
                    return True

                if self.link is not None:
                    return True

                if self.negotiated_cap is not None:
                    for child in self.negotiated_cap:
                        if child is not None:
                            return True

                if self.negotiated_keepalive_timers is not None and self.negotiated_keepalive_timers._has_data():
                    return True

                if self.prefix_activity is not None and self.prefix_activity._has_data():
                    return True

                if self.session_state is not None:
                    return True

                if self.transport is not None and self.transport._has_data():
                    return True

                if self.up_time is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                return meta._meta_table['BgpState.Neighbors.Neighbor']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-bgp-oper:bgp-state/Cisco-IOS-XE-bgp-oper:neighbors'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.neighbor is not None:
                for child_ref in self.neighbor:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
            return meta._meta_table['BgpState.Neighbors']['meta_info']


    class AddressFamilies(object):
        """
        
        
        .. attribute:: address_family
        
        	
        	**type**\: list of    :py:class:`AddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-02-07'

        def __init__(self):
            self.parent = None
            self.address_family = YList()
            self.address_family.parent = self
            self.address_family.name = 'address_family'


        class AddressFamily(object):
            """
            
            
            .. attribute:: afi_safi  <key>
            
            	
            	**type**\:   :py:class:`BgpAfiSafiEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpAfiSafiEnum>`
            
            .. attribute:: vrf_name  <key>
            
            	
            	**type**\:  str
            
            .. attribute:: activities
            
            	BGP activity information
            	**type**\:   :py:class:`Activities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.Activities>`
            
            .. attribute:: as_path
            
            	
            	**type**\:   :py:class:`AsPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.AsPath>`
            
            .. attribute:: bgp_neighbor_summaries
            
            	Summary of neighbor
            	**type**\:   :py:class:`BgpNeighborSummaries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.BgpNeighborSummaries>`
            
            .. attribute:: bgp_table_version
            
            	BGP table version number
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: filter_list
            
            	
            	**type**\:   :py:class:`FilterList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.FilterList>`
            
            .. attribute:: path
            
            	
            	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.Path>`
            
            .. attribute:: prefixes
            
            	
            	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.Prefixes>`
            
            .. attribute:: route_map
            
            	
            	**type**\:   :py:class:`RouteMap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.RouteMap>`
            
            .. attribute:: router_id
            
            	
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            
            ----
            	**type**\:  str
            
            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            
            ----
            .. attribute:: routing_table_version
            
            	Routing table version number
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: total_memory
            
            	
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-02-07'

            def __init__(self):
                self.parent = None
                self.afi_safi = None
                self.vrf_name = None
                self.activities = BgpState.AddressFamilies.AddressFamily.Activities()
                self.activities.parent = self
                self.as_path = BgpState.AddressFamilies.AddressFamily.AsPath()
                self.as_path.parent = self
                self.bgp_neighbor_summaries = BgpState.AddressFamilies.AddressFamily.BgpNeighborSummaries()
                self.bgp_neighbor_summaries.parent = self
                self.bgp_table_version = None
                self.filter_list = BgpState.AddressFamilies.AddressFamily.FilterList()
                self.filter_list.parent = self
                self.path = BgpState.AddressFamilies.AddressFamily.Path()
                self.path.parent = self
                self.prefixes = BgpState.AddressFamilies.AddressFamily.Prefixes()
                self.prefixes.parent = self
                self.route_map = BgpState.AddressFamilies.AddressFamily.RouteMap()
                self.route_map.parent = self
                self.router_id = None
                self.routing_table_version = None
                self.total_memory = None


            class Prefixes(object):
                """
                
                
                .. attribute:: memory_usage
                
                	total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	total prefix entires
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.memory_usage = None
                    self.total_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:prefixes'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_usage is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.Prefixes']['meta_info']


            class Path(object):
                """
                
                
                .. attribute:: memory_usage
                
                	total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	total prefix entires
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.memory_usage = None
                    self.total_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:path'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_usage is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.Path']['meta_info']


            class AsPath(object):
                """
                
                
                .. attribute:: memory_usage
                
                	total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	total prefix entires
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.memory_usage = None
                    self.total_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:as-path'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_usage is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.AsPath']['meta_info']


            class RouteMap(object):
                """
                
                
                .. attribute:: memory_usage
                
                	total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	total prefix entires
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.memory_usage = None
                    self.total_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:route-map'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_usage is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.RouteMap']['meta_info']


            class FilterList(object):
                """
                
                
                .. attribute:: memory_usage
                
                	total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	total prefix entires
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.memory_usage = None
                    self.total_entries = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:filter-list'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.memory_usage is not None:
                        return True

                    if self.total_entries is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.FilterList']['meta_info']


            class Activities(object):
                """
                BGP activity information
                
                .. attribute:: paths
                
                	
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: prefixes
                
                	
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: scan_interval
                
                	scan interval in second
                	**type**\:  str
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.paths = None
                    self.prefixes = None
                    self.scan_interval = None

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:activities'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.paths is not None:
                        return True

                    if self.prefixes is not None:
                        return True

                    if self.scan_interval is not None:
                        return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.Activities']['meta_info']


            class BgpNeighborSummaries(object):
                """
                Summary of neighbor
                
                .. attribute:: bgp_neighbor_summary
                
                	
                	**type**\: list of    :py:class:`BgpNeighborSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpState.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-02-07'

                def __init__(self):
                    self.parent = None
                    self.bgp_neighbor_summary = YList()
                    self.bgp_neighbor_summary.parent = self
                    self.bgp_neighbor_summary.name = 'bgp_neighbor_summary'


                class BgpNeighborSummary(object):
                    """
                    
                    
                    .. attribute:: id  <key>
                    
                    	
                    	**type**\:  str
                    
                    .. attribute:: bgp_version
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: input_queue
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_received
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_sent
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_queue
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: prefixes_received
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: state
                    
                    	
                    	**type**\:   :py:class:`BgpFsmStateEnum <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmStateEnum>`
                    
                    .. attribute:: table_version
                    
                    	
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: up_time
                    
                    	
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-02-07'

                    def __init__(self):
                        self.parent = None
                        self.id = None
                        self.bgp_version = None
                        self.input_queue = None
                        self.messages_received = None
                        self.messages_sent = None
                        self.output_queue = None
                        self.prefixes_received = None
                        self.state = None
                        self.table_version = None
                        self.up_time = None

                    @property
                    def _common_path(self):
                        if self.parent is None:
                            raise YPYModelError('parent is not set . Cannot derive path.')
                        if self.id is None:
                            raise YPYModelError('Key property id is None')

                        return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:bgp-neighbor-summary[Cisco-IOS-XE-bgp-oper:id = ' + str(self.id) + ']'

                    def is_config(self):
                        ''' Returns True if this instance represents config data else returns False '''
                        return False

                    def _has_data(self):
                        if self.id is not None:
                            return True

                        if self.bgp_version is not None:
                            return True

                        if self.input_queue is not None:
                            return True

                        if self.messages_received is not None:
                            return True

                        if self.messages_sent is not None:
                            return True

                        if self.output_queue is not None:
                            return True

                        if self.prefixes_received is not None:
                            return True

                        if self.state is not None:
                            return True

                        if self.table_version is not None:
                            return True

                        if self.up_time is not None:
                            return True

                        return False

                    @staticmethod
                    def _meta_info():
                        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                        return meta._meta_table['BgpState.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary']['meta_info']

                @property
                def _common_path(self):
                    if self.parent is None:
                        raise YPYModelError('parent is not set . Cannot derive path.')

                    return self.parent._common_path +'/Cisco-IOS-XE-bgp-oper:bgp-neighbor-summaries'

                def is_config(self):
                    ''' Returns True if this instance represents config data else returns False '''
                    return False

                def _has_data(self):
                    if self.bgp_neighbor_summary is not None:
                        for child_ref in self.bgp_neighbor_summary:
                            if child_ref._has_data():
                                return True

                    return False

                @staticmethod
                def _meta_info():
                    from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                    return meta._meta_table['BgpState.AddressFamilies.AddressFamily.BgpNeighborSummaries']['meta_info']

            @property
            def _common_path(self):
                if self.afi_safi is None:
                    raise YPYModelError('Key property afi_safi is None')
                if self.vrf_name is None:
                    raise YPYModelError('Key property vrf_name is None')

                return '/Cisco-IOS-XE-bgp-oper:bgp-state/Cisco-IOS-XE-bgp-oper:address-families/Cisco-IOS-XE-bgp-oper:address-family[Cisco-IOS-XE-bgp-oper:afi-safi = ' + str(self.afi_safi) + '][Cisco-IOS-XE-bgp-oper:vrf-name = ' + str(self.vrf_name) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.afi_safi is not None:
                    return True

                if self.vrf_name is not None:
                    return True

                if self.activities is not None and self.activities._has_data():
                    return True

                if self.as_path is not None and self.as_path._has_data():
                    return True

                if self.bgp_neighbor_summaries is not None and self.bgp_neighbor_summaries._has_data():
                    return True

                if self.bgp_table_version is not None:
                    return True

                if self.filter_list is not None and self.filter_list._has_data():
                    return True

                if self.path is not None and self.path._has_data():
                    return True

                if self.prefixes is not None and self.prefixes._has_data():
                    return True

                if self.route_map is not None and self.route_map._has_data():
                    return True

                if self.router_id is not None:
                    return True

                if self.routing_table_version is not None:
                    return True

                if self.total_memory is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
                return meta._meta_table['BgpState.AddressFamilies.AddressFamily']['meta_info']

        @property
        def _common_path(self):

            return '/Cisco-IOS-XE-bgp-oper:bgp-state/Cisco-IOS-XE-bgp-oper:address-families'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.address_family is not None:
                for child_ref in self.address_family:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
            return meta._meta_table['BgpState.AddressFamilies']['meta_info']

    @property
    def _common_path(self):

        return '/Cisco-IOS-XE-bgp-oper:bgp-state'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.address_families is not None and self.address_families._has_data():
            return True

        if self.neighbors is not None and self.neighbors._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _Cisco_IOS_XE_bgp_oper as meta
        return meta._meta_table['BgpState']['meta_info']


