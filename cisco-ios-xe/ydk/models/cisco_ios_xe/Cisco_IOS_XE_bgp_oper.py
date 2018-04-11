""" Cisco_IOS_XE_bgp_oper 

This module contains a collection of YANG definitions
for bgp operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpFsmState(Enum):
    """
    BgpFsmState (Enum Class)

    BGP FSM State

    .. data:: fsm_idle = 0

    	neighbor is in Idle state

    .. data:: fsm_connect = 1

    	neighbor is in Connect state

    .. data:: fsm_active = 2

    	neighbor is in Active state

    .. data:: fsm_opensent = 3

    	neighbor is in OpenSent state

    .. data:: fsm_openconfirm = 4

    	neighbor is in OpenConfirm state

    .. data:: fsm_established = 5

    	neighbor is in Established state

    .. data:: fsm_nonnegotiated = 6

    	neighbor is Non Negotiated

    """

    fsm_idle = Enum.YLeaf(0, "fsm-idle")

    fsm_connect = Enum.YLeaf(1, "fsm-connect")

    fsm_active = Enum.YLeaf(2, "fsm-active")

    fsm_opensent = Enum.YLeaf(3, "fsm-opensent")

    fsm_openconfirm = Enum.YLeaf(4, "fsm-openconfirm")

    fsm_established = Enum.YLeaf(5, "fsm-established")

    fsm_nonnegotiated = Enum.YLeaf(6, "fsm-nonnegotiated")


class BgpLink(Enum):
    """
    BgpLink (Enum Class)

    Operational state relevent to bgp global neighbor

    .. data:: internal = 0

    	iBGP neighbors

    .. data:: external = 1

    	eBGP neighbors

    """

    internal = Enum.YLeaf(0, "internal")

    external = Enum.YLeaf(1, "external")


class BgpMode(Enum):
    """
    BgpMode (Enum Class)

    BGP mode

    .. data:: mode_active = 0

    	active connection

    .. data:: mode_passive = 1

    	passive connection

    """

    mode_active = Enum.YLeaf(0, "mode-active")

    mode_passive = Enum.YLeaf(1, "mode-passive")



class BgpStateData(Entity):
    """
    BGP operational state data
    
    .. attribute:: neighbors
    
    	BGP neighbor information
    	**type**\:  :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors>`
    
    .. attribute:: address_families
    
    	BGP address family
    	**type**\:  :py:class:`AddressFamilies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies>`
    
    .. attribute:: bgp_route_vrfs
    
    	BGP VRFs
    	**type**\:  :py:class:`BgpRouteVrfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs>`
    
    .. attribute:: bgp_route_rds
    
    	BGP RDs
    	**type**\:  :py:class:`BgpRouteRds <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds>`
    
    

    """

    _prefix = 'bgp-ios-xe-oper'
    _revision = '2017-09-25'

    def __init__(self):
        super(BgpStateData, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp-state-data"
        self.yang_parent_name = "Cisco-IOS-XE-bgp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_container_classes = OrderedDict([("neighbors", ("neighbors", BgpStateData.Neighbors)), ("address-families", ("address_families", BgpStateData.AddressFamilies)), ("bgp-route-vrfs", ("bgp_route_vrfs", BgpStateData.BgpRouteVrfs)), ("bgp-route-rds", ("bgp_route_rds", BgpStateData.BgpRouteRds))])
        self._child_list_classes = OrderedDict([])
        self._leafs = OrderedDict()

        self.neighbors = BgpStateData.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")

        self.address_families = BgpStateData.AddressFamilies()
        self.address_families.parent = self
        self._children_name_map["address_families"] = "address-families"
        self._children_yang_names.add("address-families")

        self.bgp_route_vrfs = BgpStateData.BgpRouteVrfs()
        self.bgp_route_vrfs.parent = self
        self._children_name_map["bgp_route_vrfs"] = "bgp-route-vrfs"
        self._children_yang_names.add("bgp-route-vrfs")

        self.bgp_route_rds = BgpStateData.BgpRouteRds()
        self.bgp_route_rds.parent = self
        self._children_name_map["bgp_route_rds"] = "bgp-route-rds"
        self._children_yang_names.add("bgp-route-rds")
        self._segment_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data"


    class Neighbors(Entity):
        """
        BGP neighbor information
        
        .. attribute:: neighbor
        
        	List of BGP neighbors
        	**type**\: list of  		 :py:class:`Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(BgpStateData.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("neighbor", ("neighbor", BgpStateData.Neighbors.Neighbor))])
            self._leafs = OrderedDict()

            self.neighbor = YList(self)
            self._segment_path = lambda: "neighbors"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.Neighbors, [], name, value)


        class Neighbor(Entity):
            """
            List of BGP neighbors
            
            .. attribute:: afi_safi  (key)
            
            	Afi\-safi key
            	**type**\:  :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            .. attribute:: neighbor_id  (key)
            
            	Neighbor identifier
            	**type**\: str
            
            .. attribute:: description
            
            	Neighbor description string
            	**type**\: str
            
            .. attribute:: bgp_version
            
            	BGP version being used to communicate with the remote router
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: link
            
            	Neighbor link type
            	**type**\:  :py:class:`BgpLink <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpLink>`
            
            .. attribute:: up_time
            
            	Amout of time the bgp session has been up since being established
            	**type**\: str
            
            .. attribute:: last_write
            
            	Time since BGP last sent a message to the neighbor
            	**type**\: str
            
            .. attribute:: last_read
            
            	Time since BGP last received a message from the neighbor
            	**type**\: str
            
            .. attribute:: installed_prefixes
            
            	The number of installed prefixes
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_state
            
            	BGP neighbor session state
            	**type**\:  :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
            
            .. attribute:: negotiated_keepalive_timers
            
            	Negotiated keepalive timers status of BGP neighbor
            	**type**\:  :py:class:`NegotiatedKeepaliveTimers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers>`
            
            .. attribute:: negotiated_cap
            
            	Negotiated capabilities for neighbor session
            	**type**\: list of str
            
            .. attribute:: bgp_neighbor_counters
            
            	BGP neighbor session counters
            	**type**\:  :py:class:`BgpNeighborCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters>`
            
            .. attribute:: connection
            
            	BGP neighbor connection
            	**type**\:  :py:class:`Connection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Connection>`
            
            .. attribute:: transport
            
            	BGP neighbor transport
            	**type**\:  :py:class:`Transport <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Transport>`
            
            .. attribute:: prefix_activity
            
            	BGP neighbor activity
            	**type**\:  :py:class:`PrefixActivity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity>`
            
            .. attribute:: as_
            
            	BGP neighbor AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(BgpStateData.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['afi_safi','vrf_name','neighbor_id']
                self._child_container_classes = OrderedDict([("negotiated-keepalive-timers", ("negotiated_keepalive_timers", BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers)), ("bgp-neighbor-counters", ("bgp_neighbor_counters", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters)), ("connection", ("connection", BgpStateData.Neighbors.Neighbor.Connection)), ("transport", ("transport", BgpStateData.Neighbors.Neighbor.Transport)), ("prefix-activity", ("prefix_activity", BgpStateData.Neighbors.Neighbor.PrefixActivity))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('afi_safi', YLeaf(YType.enumeration, 'afi-safi')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('neighbor_id', YLeaf(YType.str, 'neighbor-id')),
                    ('description', YLeaf(YType.str, 'description')),
                    ('bgp_version', YLeaf(YType.uint16, 'bgp-version')),
                    ('link', YLeaf(YType.enumeration, 'link')),
                    ('up_time', YLeaf(YType.str, 'up-time')),
                    ('last_write', YLeaf(YType.str, 'last-write')),
                    ('last_read', YLeaf(YType.str, 'last-read')),
                    ('installed_prefixes', YLeaf(YType.uint32, 'installed-prefixes')),
                    ('session_state', YLeaf(YType.enumeration, 'session-state')),
                    ('negotiated_cap', YLeafList(YType.str, 'negotiated-cap')),
                    ('as_', YLeaf(YType.uint32, 'as')),
                ])
                self.afi_safi = None
                self.vrf_name = None
                self.neighbor_id = None
                self.description = None
                self.bgp_version = None
                self.link = None
                self.up_time = None
                self.last_write = None
                self.last_read = None
                self.installed_prefixes = None
                self.session_state = None
                self.negotiated_cap = []
                self.as_ = None

                self.negotiated_keepalive_timers = BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers()
                self.negotiated_keepalive_timers.parent = self
                self._children_name_map["negotiated_keepalive_timers"] = "negotiated-keepalive-timers"
                self._children_yang_names.add("negotiated-keepalive-timers")

                self.bgp_neighbor_counters = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters()
                self.bgp_neighbor_counters.parent = self
                self._children_name_map["bgp_neighbor_counters"] = "bgp-neighbor-counters"
                self._children_yang_names.add("bgp-neighbor-counters")

                self.connection = BgpStateData.Neighbors.Neighbor.Connection()
                self.connection.parent = self
                self._children_name_map["connection"] = "connection"
                self._children_yang_names.add("connection")

                self.transport = BgpStateData.Neighbors.Neighbor.Transport()
                self.transport.parent = self
                self._children_name_map["transport"] = "transport"
                self._children_yang_names.add("transport")

                self.prefix_activity = BgpStateData.Neighbors.Neighbor.PrefixActivity()
                self.prefix_activity.parent = self
                self._children_name_map["prefix_activity"] = "prefix-activity"
                self._children_yang_names.add("prefix-activity")
                self._segment_path = lambda: "neighbor" + "[afi-safi='" + str(self.afi_safi) + "']" + "[vrf-name='" + str(self.vrf_name) + "']" + "[neighbor-id='" + str(self.neighbor_id) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/neighbors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.Neighbors.Neighbor, ['afi_safi', 'vrf_name', 'neighbor_id', 'description', 'bgp_version', 'link', 'up_time', 'last_write', 'last_read', 'installed_prefixes', 'session_state', 'negotiated_cap', 'as_'], name, value)


            class NegotiatedKeepaliveTimers(Entity):
                """
                Negotiated keepalive timers status of BGP neighbor
                
                .. attribute:: hold_time
                
                	Hold time
                	**type**\: int
                
                	**range:** 0..65535
                
                .. attribute:: keepalive_interval
                
                	Keepalive interval
                	**type**\: int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, self).__init__()

                    self.yang_name = "negotiated-keepalive-timers"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('hold_time', YLeaf(YType.uint16, 'hold-time')),
                        ('keepalive_interval', YLeaf(YType.uint16, 'keepalive-interval')),
                    ])
                    self.hold_time = None
                    self.keepalive_interval = None
                    self._segment_path = lambda: "negotiated-keepalive-timers"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, ['hold_time', 'keepalive_interval'], name, value)


            class BgpNeighborCounters(Entity):
                """
                BGP neighbor session counters
                
                .. attribute:: sent
                
                	Number of mesaged sent
                	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent>`
                
                .. attribute:: received
                
                	Number of mesaged received
                	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received>`
                
                .. attribute:: inq_depth
                
                	Input Q depth
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: outq_depth
                
                	Output Q depth
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, self).__init__()

                    self.yang_name = "bgp-neighbor-counters"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sent", ("sent", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent)), ("received", ("received", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('inq_depth', YLeaf(YType.uint32, 'inq-depth')),
                        ('outq_depth', YLeaf(YType.uint32, 'outq-depth')),
                    ])
                    self.inq_depth = None
                    self.outq_depth = None

                    self.sent = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent()
                    self.sent.parent = self
                    self._children_name_map["sent"] = "sent"
                    self._children_yang_names.add("sent")

                    self.received = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received()
                    self.received.parent = self
                    self._children_name_map["received"] = "received"
                    self._children_yang_names.add("received")
                    self._segment_path = lambda: "bgp-neighbor-counters"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, ['inq_depth', 'outq_depth'], name, value)


                class Sent(Entity):
                    """
                    Number of mesaged sent
                    
                    .. attribute:: opens
                    
                    	OPEN message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "bgp-neighbor-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('opens', YLeaf(YType.uint32, 'opens')),
                            ('updates', YLeaf(YType.uint32, 'updates')),
                            ('notifications', YLeaf(YType.uint32, 'notifications')),
                            ('keepalives', YLeaf(YType.uint32, 'keepalives')),
                            ('route_refreshes', YLeaf(YType.uint32, 'route-refreshes')),
                        ])
                        self.opens = None
                        self.updates = None
                        self.notifications = None
                        self.keepalives = None
                        self.route_refreshes = None
                        self._segment_path = lambda: "sent"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, ['opens', 'updates', 'notifications', 'keepalives', 'route_refreshes'], name, value)


                class Received(Entity):
                    """
                    Number of mesaged received
                    
                    .. attribute:: opens
                    
                    	OPEN message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "bgp-neighbor-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('opens', YLeaf(YType.uint32, 'opens')),
                            ('updates', YLeaf(YType.uint32, 'updates')),
                            ('notifications', YLeaf(YType.uint32, 'notifications')),
                            ('keepalives', YLeaf(YType.uint32, 'keepalives')),
                            ('route_refreshes', YLeaf(YType.uint32, 'route-refreshes')),
                        ])
                        self.opens = None
                        self.updates = None
                        self.notifications = None
                        self.keepalives = None
                        self.route_refreshes = None
                        self._segment_path = lambda: "received"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, ['opens', 'updates', 'notifications', 'keepalives', 'route_refreshes'], name, value)


            class Connection(Entity):
                """
                BGP neighbor connection
                
                .. attribute:: state
                
                	TCP FSM state
                	**type**\:  :py:class:`TcpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.TcpFsmState>`
                
                .. attribute:: mode
                
                	BGP transport connection mode
                	**type**\:  :py:class:`BgpMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpMode>`
                
                .. attribute:: total_established
                
                	The number of times a TCP and BGP  connection has been successfully established
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_dropped
                
                	The number of times that a valid session has failed or been taken down
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_reset
                
                	Time since peering session was last reset
                	**type**\: str
                
                .. attribute:: reset_reason
                
                	The reason for the last reset
                	**type**\: str
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Connection, self).__init__()

                    self.yang_name = "connection"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('state', YLeaf(YType.enumeration, 'state')),
                        ('mode', YLeaf(YType.enumeration, 'mode')),
                        ('total_established', YLeaf(YType.uint32, 'total-established')),
                        ('total_dropped', YLeaf(YType.uint32, 'total-dropped')),
                        ('last_reset', YLeaf(YType.str, 'last-reset')),
                        ('reset_reason', YLeaf(YType.str, 'reset-reason')),
                    ])
                    self.state = None
                    self.mode = None
                    self.total_established = None
                    self.total_dropped = None
                    self.last_reset = None
                    self.reset_reason = None
                    self._segment_path = lambda: "connection"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.Connection, ['state', 'mode', 'total_established', 'total_dropped', 'last_reset', 'reset_reason'], name, value)


            class Transport(Entity):
                """
                BGP neighbor transport
                
                .. attribute:: path_mtu_discovery
                
                	Indication whether path MTU discovrey is enabled
                	**type**\: bool
                
                .. attribute:: local_port
                
                	Local TCP port used for TCP session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_host
                
                	Local address used for the TCP session
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: foreign_port
                
                	Remote port used by the peer for the TCP session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: foreign_host
                
                	Remote address of the BGP session
                	**type**\: union of the below types:
                
                		**type**\: str
                
                			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                
                		**type**\: str
                
                			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                
                .. attribute:: mss
                
                	Maximum Data segment size
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('path_mtu_discovery', YLeaf(YType.boolean, 'path-mtu-discovery')),
                        ('local_port', YLeaf(YType.uint32, 'local-port')),
                        ('local_host', YLeaf(YType.str, 'local-host')),
                        ('foreign_port', YLeaf(YType.uint32, 'foreign-port')),
                        ('foreign_host', YLeaf(YType.str, 'foreign-host')),
                        ('mss', YLeaf(YType.uint32, 'mss')),
                    ])
                    self.path_mtu_discovery = None
                    self.local_port = None
                    self.local_host = None
                    self.foreign_port = None
                    self.foreign_host = None
                    self.mss = None
                    self._segment_path = lambda: "transport"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.Transport, ['path_mtu_discovery', 'local_port', 'local_host', 'foreign_port', 'foreign_host', 'mss'], name, value)


            class PrefixActivity(Entity):
                """
                BGP neighbor activity
                
                .. attribute:: sent
                
                	Number of prefixes sent
                	**type**\:  :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent>`
                
                .. attribute:: received
                
                	Number of prefixes received
                	**type**\:  :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Received>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.PrefixActivity, self).__init__()

                    self.yang_name = "prefix-activity"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([("sent", ("sent", BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent)), ("received", ("received", BgpStateData.Neighbors.Neighbor.PrefixActivity.Received))])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict()

                    self.sent = BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent()
                    self.sent.parent = self
                    self._children_name_map["sent"] = "sent"
                    self._children_yang_names.add("sent")

                    self.received = BgpStateData.Neighbors.Neighbor.PrefixActivity.Received()
                    self.received.parent = self
                    self._children_name_map["received"] = "received"
                    self._children_yang_names.add("received")
                    self._segment_path = lambda: "prefix-activity"


                class Sent(Entity):
                    """
                    Number of prefixes sent
                    
                    .. attribute:: current_prefixes
                    
                    	The current number of accepted prefixes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "prefix-activity"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('current_prefixes', YLeaf(YType.uint64, 'current-prefixes')),
                            ('total_prefixes', YLeaf(YType.uint64, 'total-prefixes')),
                            ('implicit_withdraw', YLeaf(YType.uint64, 'implicit-withdraw')),
                            ('explicit_withdraw', YLeaf(YType.uint64, 'explicit-withdraw')),
                            ('bestpaths', YLeaf(YType.uint64, 'bestpaths')),
                            ('multipaths', YLeaf(YType.uint64, 'multipaths')),
                        ])
                        self.current_prefixes = None
                        self.total_prefixes = None
                        self.implicit_withdraw = None
                        self.explicit_withdraw = None
                        self.bestpaths = None
                        self.multipaths = None
                        self._segment_path = lambda: "sent"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, ['current_prefixes', 'total_prefixes', 'implicit_withdraw', 'explicit_withdraw', 'bestpaths', 'multipaths'], name, value)


                class Received(Entity):
                    """
                    Number of prefixes received
                    
                    .. attribute:: current_prefixes
                    
                    	The current number of accepted prefixes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "prefix-activity"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('current_prefixes', YLeaf(YType.uint64, 'current-prefixes')),
                            ('total_prefixes', YLeaf(YType.uint64, 'total-prefixes')),
                            ('implicit_withdraw', YLeaf(YType.uint64, 'implicit-withdraw')),
                            ('explicit_withdraw', YLeaf(YType.uint64, 'explicit-withdraw')),
                            ('bestpaths', YLeaf(YType.uint64, 'bestpaths')),
                            ('multipaths', YLeaf(YType.uint64, 'multipaths')),
                        ])
                        self.current_prefixes = None
                        self.total_prefixes = None
                        self.implicit_withdraw = None
                        self.explicit_withdraw = None
                        self.bestpaths = None
                        self.multipaths = None
                        self._segment_path = lambda: "received"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, ['current_prefixes', 'total_prefixes', 'implicit_withdraw', 'explicit_withdraw', 'bestpaths', 'multipaths'], name, value)


    class AddressFamilies(Entity):
        """
        BGP address family
        
        .. attribute:: address_family
        
        	List of BGP address families
        	**type**\: list of  		 :py:class:`AddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(BgpStateData.AddressFamilies, self).__init__()

            self.yang_name = "address-families"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("address-family", ("address_family", BgpStateData.AddressFamilies.AddressFamily))])
            self._leafs = OrderedDict()

            self.address_family = YList(self)
            self._segment_path = lambda: "address-families"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.AddressFamilies, [], name, value)


        class AddressFamily(Entity):
            """
            List of BGP address families
            
            .. attribute:: afi_safi  (key)
            
            	Afi\-safi value
            	**type**\:  :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
            
            .. attribute:: vrf_name  (key)
            
            	VRF name
            	**type**\: str
            
            .. attribute:: router_id
            
            	Router ID
            	**type**\: union of the below types:
            
            		**type**\: str
            
            			**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
            
            		**type**\: str
            
            			**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
            
            .. attribute:: bgp_table_version
            
            	BGP table version number
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: routing_table_version
            
            	Routing table version number
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: prefixes
            
            	Prefix entry statistics
            	**type**\:  :py:class:`Prefixes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Prefixes>`
            
            .. attribute:: path
            
            	Path entry statistics
            	**type**\:  :py:class:`Path <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Path>`
            
            .. attribute:: as_path
            
            	AS path entry statistics
            	**type**\:  :py:class:`AsPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.AsPath>`
            
            .. attribute:: route_map
            
            	Route map entry statistics
            	**type**\:  :py:class:`RouteMap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.RouteMap>`
            
            .. attribute:: filter_list
            
            	Filter list entry statistics
            	**type**\:  :py:class:`FilterList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.FilterList>`
            
            .. attribute:: activities
            
            	BGP activity information
            	**type**\:  :py:class:`Activities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Activities>`
            
            .. attribute:: total_memory
            
            	Total memory in use
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: bgp_neighbor_summaries
            
            	Neighbor summary
            	**type**\:  :py:class:`BgpNeighborSummaries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries>`
            
            .. attribute:: local_as
            
            	Local AS number
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(BgpStateData.AddressFamilies.AddressFamily, self).__init__()

                self.yang_name = "address-family"
                self.yang_parent_name = "address-families"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['afi_safi','vrf_name']
                self._child_container_classes = OrderedDict([("prefixes", ("prefixes", BgpStateData.AddressFamilies.AddressFamily.Prefixes)), ("path", ("path", BgpStateData.AddressFamilies.AddressFamily.Path)), ("as-path", ("as_path", BgpStateData.AddressFamilies.AddressFamily.AsPath)), ("route-map", ("route_map", BgpStateData.AddressFamilies.AddressFamily.RouteMap)), ("filter-list", ("filter_list", BgpStateData.AddressFamilies.AddressFamily.FilterList)), ("activities", ("activities", BgpStateData.AddressFamilies.AddressFamily.Activities)), ("bgp-neighbor-summaries", ("bgp_neighbor_summaries", BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('afi_safi', YLeaf(YType.enumeration, 'afi-safi')),
                    ('vrf_name', YLeaf(YType.str, 'vrf-name')),
                    ('router_id', YLeaf(YType.str, 'router-id')),
                    ('bgp_table_version', YLeaf(YType.uint64, 'bgp-table-version')),
                    ('routing_table_version', YLeaf(YType.uint64, 'routing-table-version')),
                    ('total_memory', YLeaf(YType.uint64, 'total-memory')),
                    ('local_as', YLeaf(YType.uint32, 'local-as')),
                ])
                self.afi_safi = None
                self.vrf_name = None
                self.router_id = None
                self.bgp_table_version = None
                self.routing_table_version = None
                self.total_memory = None
                self.local_as = None

                self.prefixes = BgpStateData.AddressFamilies.AddressFamily.Prefixes()
                self.prefixes.parent = self
                self._children_name_map["prefixes"] = "prefixes"
                self._children_yang_names.add("prefixes")

                self.path = BgpStateData.AddressFamilies.AddressFamily.Path()
                self.path.parent = self
                self._children_name_map["path"] = "path"
                self._children_yang_names.add("path")

                self.as_path = BgpStateData.AddressFamilies.AddressFamily.AsPath()
                self.as_path.parent = self
                self._children_name_map["as_path"] = "as-path"
                self._children_yang_names.add("as-path")

                self.route_map = BgpStateData.AddressFamilies.AddressFamily.RouteMap()
                self.route_map.parent = self
                self._children_name_map["route_map"] = "route-map"
                self._children_yang_names.add("route-map")

                self.filter_list = BgpStateData.AddressFamilies.AddressFamily.FilterList()
                self.filter_list.parent = self
                self._children_name_map["filter_list"] = "filter-list"
                self._children_yang_names.add("filter-list")

                self.activities = BgpStateData.AddressFamilies.AddressFamily.Activities()
                self.activities.parent = self
                self._children_name_map["activities"] = "activities"
                self._children_yang_names.add("activities")

                self.bgp_neighbor_summaries = BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries()
                self.bgp_neighbor_summaries.parent = self
                self._children_name_map["bgp_neighbor_summaries"] = "bgp-neighbor-summaries"
                self._children_yang_names.add("bgp-neighbor-summaries")
                self._segment_path = lambda: "address-family" + "[afi-safi='" + str(self.afi_safi) + "']" + "[vrf-name='" + str(self.vrf_name) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/address-families/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily, ['afi_safi', 'vrf_name', 'router_id', 'bgp_table_version', 'routing_table_version', 'total_memory', 'local_as'], name, value)


            class Prefixes(Entity):
                """
                Prefix entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Prefixes, self).__init__()

                    self.yang_name = "prefixes"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_entries', YLeaf(YType.uint64, 'total-entries')),
                        ('memory_usage', YLeaf(YType.uint64, 'memory-usage')),
                    ])
                    self.total_entries = None
                    self.memory_usage = None
                    self._segment_path = lambda: "prefixes"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Prefixes, ['total_entries', 'memory_usage'], name, value)


            class Path(Entity):
                """
                Path entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Path, self).__init__()

                    self.yang_name = "path"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_entries', YLeaf(YType.uint64, 'total-entries')),
                        ('memory_usage', YLeaf(YType.uint64, 'memory-usage')),
                    ])
                    self.total_entries = None
                    self.memory_usage = None
                    self._segment_path = lambda: "path"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Path, ['total_entries', 'memory_usage'], name, value)


            class AsPath(Entity):
                """
                AS path entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.AsPath, self).__init__()

                    self.yang_name = "as-path"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_entries', YLeaf(YType.uint64, 'total-entries')),
                        ('memory_usage', YLeaf(YType.uint64, 'memory-usage')),
                    ])
                    self.total_entries = None
                    self.memory_usage = None
                    self._segment_path = lambda: "as-path"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.AsPath, ['total_entries', 'memory_usage'], name, value)


            class RouteMap(Entity):
                """
                Route map entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.RouteMap, self).__init__()

                    self.yang_name = "route-map"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_entries', YLeaf(YType.uint64, 'total-entries')),
                        ('memory_usage', YLeaf(YType.uint64, 'memory-usage')),
                    ])
                    self.total_entries = None
                    self.memory_usage = None
                    self._segment_path = lambda: "route-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.RouteMap, ['total_entries', 'memory_usage'], name, value)


            class FilterList(Entity):
                """
                Filter list entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.FilterList, self).__init__()

                    self.yang_name = "filter-list"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('total_entries', YLeaf(YType.uint64, 'total-entries')),
                        ('memory_usage', YLeaf(YType.uint64, 'memory-usage')),
                    ])
                    self.total_entries = None
                    self.memory_usage = None
                    self._segment_path = lambda: "filter-list"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.FilterList, ['total_entries', 'memory_usage'], name, value)


            class Activities(Entity):
                """
                BGP activity information
                
                .. attribute:: prefixes
                
                	Total number of prefixes
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: paths
                
                	Total number of paths
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: scan_interval
                
                	Scan interval in seconds
                	**type**\: str
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Activities, self).__init__()

                    self.yang_name = "activities"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('prefixes', YLeaf(YType.uint64, 'prefixes')),
                        ('paths', YLeaf(YType.uint64, 'paths')),
                        ('scan_interval', YLeaf(YType.str, 'scan-interval')),
                    ])
                    self.prefixes = None
                    self.paths = None
                    self.scan_interval = None
                    self._segment_path = lambda: "activities"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Activities, ['prefixes', 'paths', 'scan_interval'], name, value)


            class BgpNeighborSummaries(Entity):
                """
                Neighbor summary
                
                .. attribute:: bgp_neighbor_summary
                
                	List of neighbor summaries
                	**type**\: list of  		 :py:class:`BgpNeighborSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, self).__init__()

                    self.yang_name = "bgp-neighbor-summaries"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bgp-neighbor-summary", ("bgp_neighbor_summary", BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary))])
                    self._leafs = OrderedDict()

                    self.bgp_neighbor_summary = YList(self)
                    self._segment_path = lambda: "bgp-neighbor-summaries"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, [], name, value)


                class BgpNeighborSummary(Entity):
                    """
                    List of neighbor summaries
                    
                    .. attribute:: id  (key)
                    
                    	Neighbor address
                    	**type**\: str
                    
                    .. attribute:: bgp_version
                    
                    	BGP protocol version
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_received
                    
                    	Number of messages received from this neighbor
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_sent
                    
                    	Number of messages sent to this neighbor
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: table_version
                    
                    	BGP table version
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: input_queue
                    
                    	Number of messages in input queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_queue
                    
                    	Number of messages in output queue
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: up_time
                    
                    	Neighbor session uptime
                    	**type**\: str
                    
                    .. attribute:: state
                    
                    	BGP session state
                    	**type**\:  :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
                    
                    .. attribute:: prefixes_received
                    
                    	Number of prefixes received from the neighbor
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dynamically_configured
                    
                    	Indication of whether the neighbor was dyanmically configured
                    	**type**\: bool
                    
                    .. attribute:: as_
                    
                    	BGP neighbor AS number
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, self).__init__()

                        self.yang_name = "bgp-neighbor-summary"
                        self.yang_parent_name = "bgp-neighbor-summaries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['id']
                        self._child_container_classes = OrderedDict([])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('id', YLeaf(YType.str, 'id')),
                            ('bgp_version', YLeaf(YType.uint32, 'bgp-version')),
                            ('messages_received', YLeaf(YType.uint64, 'messages-received')),
                            ('messages_sent', YLeaf(YType.uint64, 'messages-sent')),
                            ('table_version', YLeaf(YType.uint64, 'table-version')),
                            ('input_queue', YLeaf(YType.uint64, 'input-queue')),
                            ('output_queue', YLeaf(YType.uint64, 'output-queue')),
                            ('up_time', YLeaf(YType.str, 'up-time')),
                            ('state', YLeaf(YType.enumeration, 'state')),
                            ('prefixes_received', YLeaf(YType.uint64, 'prefixes-received')),
                            ('dynamically_configured', YLeaf(YType.boolean, 'dynamically-configured')),
                            ('as_', YLeaf(YType.uint32, 'as')),
                        ])
                        self.id = None
                        self.bgp_version = None
                        self.messages_received = None
                        self.messages_sent = None
                        self.table_version = None
                        self.input_queue = None
                        self.output_queue = None
                        self.up_time = None
                        self.state = None
                        self.prefixes_received = None
                        self.dynamically_configured = None
                        self.as_ = None
                        self._segment_path = lambda: "bgp-neighbor-summary" + "[id='" + str(self.id) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, ['id', 'bgp_version', 'messages_received', 'messages_sent', 'table_version', 'input_queue', 'output_queue', 'up_time', 'state', 'prefixes_received', 'dynamically_configured', 'as_'], name, value)


    class BgpRouteVrfs(Entity):
        """
        BGP VRFs
        
        .. attribute:: bgp_route_vrf
        
        	List of BGP VRFs
        	**type**\: list of  		 :py:class:`BgpRouteVrf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(BgpStateData.BgpRouteVrfs, self).__init__()

            self.yang_name = "bgp-route-vrfs"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bgp-route-vrf", ("bgp_route_vrf", BgpStateData.BgpRouteVrfs.BgpRouteVrf))])
            self._leafs = OrderedDict()

            self.bgp_route_vrf = YList(self)
            self._segment_path = lambda: "bgp-route-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.BgpRouteVrfs, [], name, value)


        class BgpRouteVrf(Entity):
            """
            List of BGP VRFs
            
            .. attribute:: vrf  (key)
            
            	BGP vrf
            	**type**\: str
            
            .. attribute:: bgp_route_afs
            
            	BGP address families
            	**type**\:  :py:class:`BgpRouteAfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs>`
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf, self).__init__()

                self.yang_name = "bgp-route-vrf"
                self.yang_parent_name = "bgp-route-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['vrf']
                self._child_container_classes = OrderedDict([("bgp-route-afs", ("bgp_route_afs", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('vrf', YLeaf(YType.str, 'vrf')),
                ])
                self.vrf = None

                self.bgp_route_afs = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs()
                self.bgp_route_afs.parent = self
                self._children_name_map["bgp_route_afs"] = "bgp-route-afs"
                self._children_yang_names.add("bgp-route-afs")
                self._segment_path = lambda: "bgp-route-vrf" + "[vrf='" + str(self.vrf) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/bgp-route-vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf, ['vrf'], name, value)


            class BgpRouteAfs(Entity):
                """
                BGP address families
                
                .. attribute:: bgp_route_af
                
                	List of BGP address families
                	**type**\: list of  		 :py:class:`BgpRouteAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, self).__init__()

                    self.yang_name = "bgp-route-afs"
                    self.yang_parent_name = "bgp-route-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bgp-route-af", ("bgp_route_af", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf))])
                    self._leafs = OrderedDict()

                    self.bgp_route_af = YList(self)
                    self._segment_path = lambda: "bgp-route-afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, [], name, value)


                class BgpRouteAf(Entity):
                    """
                    List of BGP address families
                    
                    .. attribute:: afi_safi  (key)
                    
                    	BGP address family
                    	**type**\:  :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
                    
                    .. attribute:: bgp_route_filters
                    
                    	BGP route filters
                    	**type**\:  :py:class:`BgpRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters>`
                    
                    .. attribute:: bgp_route_neighbors
                    
                    	BGP route neighbors
                    	**type**\:  :py:class:`BgpRouteNeighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors>`
                    
                    .. attribute:: bgp_peer_groups
                    
                    	BGP peer groups
                    	**type**\:  :py:class:`BgpPeerGroups <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups>`
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, self).__init__()

                        self.yang_name = "bgp-route-af"
                        self.yang_parent_name = "bgp-route-afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi_safi']
                        self._child_container_classes = OrderedDict([("bgp-route-filters", ("bgp_route_filters", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters)), ("bgp-route-neighbors", ("bgp_route_neighbors", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors)), ("bgp-peer-groups", ("bgp_peer_groups", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi', YLeaf(YType.enumeration, 'afi-safi')),
                        ])
                        self.afi_safi = None

                        self.bgp_route_filters = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters()
                        self.bgp_route_filters.parent = self
                        self._children_name_map["bgp_route_filters"] = "bgp-route-filters"
                        self._children_yang_names.add("bgp-route-filters")

                        self.bgp_route_neighbors = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors()
                        self.bgp_route_neighbors.parent = self
                        self._children_name_map["bgp_route_neighbors"] = "bgp-route-neighbors"
                        self._children_yang_names.add("bgp-route-neighbors")

                        self.bgp_peer_groups = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups()
                        self.bgp_peer_groups.parent = self
                        self._children_name_map["bgp_peer_groups"] = "bgp-peer-groups"
                        self._children_yang_names.add("bgp-peer-groups")
                        self._segment_path = lambda: "bgp-route-af" + "[afi-safi='" + str(self.afi_safi) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, ['afi_safi'], name, value)


                    class BgpRouteFilters(Entity):
                        """
                        BGP route filters
                        
                        .. attribute:: bgp_route_filter
                        
                        	List of BGP route filters
                        	**type**\: list of  		 :py:class:`BgpRouteFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-09-25'

                        def __init__(self):
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, self).__init__()

                            self.yang_name = "bgp-route-filters"
                            self.yang_parent_name = "bgp-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("bgp-route-filter", ("bgp_route_filter", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter))])
                            self._leafs = OrderedDict()

                            self.bgp_route_filter = YList(self)
                            self._segment_path = lambda: "bgp-route-filters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, [], name, value)


                        class BgpRouteFilter(Entity):
                            """
                            List of BGP route filters
                            
                            .. attribute:: route_filter  (key)
                            
                            	BGP route filter
                            	**type**\:  :py:class:`BgpRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRouteFilters>`
                            
                            .. attribute:: bgp_route_entries
                            
                            	BGP route entries
                            	**type**\:  :py:class:`BgpRouteEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries>`
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-09-25'

                            def __init__(self):
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, self).__init__()

                                self.yang_name = "bgp-route-filter"
                                self.yang_parent_name = "bgp-route-filters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['route_filter']
                                self._child_container_classes = OrderedDict([("bgp-route-entries", ("bgp_route_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_filter', YLeaf(YType.enumeration, 'route-filter')),
                                ])
                                self.route_filter = None

                                self.bgp_route_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries()
                                self.bgp_route_entries.parent = self
                                self._children_name_map["bgp_route_entries"] = "bgp-route-entries"
                                self._children_yang_names.add("bgp-route-entries")
                                self._segment_path = lambda: "bgp-route-filter" + "[route-filter='" + str(self.route_filter) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, ['route_filter'], name, value)


                            class BgpRouteEntries(Entity):
                                """
                                BGP route entries
                                
                                .. attribute:: bgp_route_entry
                                
                                	List of BGP route entries
                                	**type**\: list of  		 :py:class:`BgpRouteEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry>`
                                
                                

                                """

                                _prefix = 'bgp-ios-xe-oper'
                                _revision = '2017-09-25'

                                def __init__(self):
                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, self).__init__()

                                    self.yang_name = "bgp-route-entries"
                                    self.yang_parent_name = "bgp-route-filter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bgp-route-entry", ("bgp_route_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry))])
                                    self._leafs = OrderedDict()

                                    self.bgp_route_entry = YList(self)
                                    self._segment_path = lambda: "bgp-route-entries"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, [], name, value)


                                class BgpRouteEntry(Entity):
                                    """
                                    List of BGP route entries
                                    
                                    .. attribute:: prefix  (key)
                                    
                                    	Routing table entry prefix
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	Routing table version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: available_paths
                                    
                                    	Number of paths available for BGP prefix
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: advertised_to
                                    
                                    	Whom is thie prefix advertized to
                                    	**type**\: str
                                    
                                    .. attribute:: bgp_path_entries
                                    
                                    	Prefix next hop details
                                    	**type**\:  :py:class:`BgpPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries>`
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-09-25'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, self).__init__()

                                        self.yang_name = "bgp-route-entry"
                                        self.yang_parent_name = "bgp-route-entries"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['prefix']
                                        self._child_container_classes = OrderedDict([("bgp-path-entries", ("bgp_path_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('version', YLeaf(YType.uint32, 'version')),
                                            ('available_paths', YLeaf(YType.uint32, 'available-paths')),
                                            ('advertised_to', YLeaf(YType.str, 'advertised-to')),
                                        ])
                                        self.prefix = None
                                        self.version = None
                                        self.available_paths = None
                                        self.advertised_to = None

                                        self.bgp_path_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries()
                                        self.bgp_path_entries.parent = self
                                        self._children_name_map["bgp_path_entries"] = "bgp-path-entries"
                                        self._children_yang_names.add("bgp-path-entries")
                                        self._segment_path = lambda: "bgp-route-entry" + "[prefix='" + str(self.prefix) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, ['prefix', 'version', 'available_paths', 'advertised_to'], name, value)


                                    class BgpPathEntries(Entity):
                                        """
                                        Prefix next hop details
                                        
                                        .. attribute:: bgp_path_entry
                                        
                                        	List of prefix next hop details
                                        	**type**\: list of  		 :py:class:`BgpPathEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry>`
                                        
                                        

                                        """

                                        _prefix = 'bgp-ios-xe-oper'
                                        _revision = '2017-09-25'

                                        def __init__(self):
                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, self).__init__()

                                            self.yang_name = "bgp-path-entries"
                                            self.yang_parent_name = "bgp-route-entry"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bgp-path-entry", ("bgp_path_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry))])
                                            self._leafs = OrderedDict()

                                            self.bgp_path_entry = YList(self)
                                            self._segment_path = lambda: "bgp-path-entries"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, [], name, value)


                                        class BgpPathEntry(Entity):
                                            """
                                            List of prefix next hop details
                                            
                                            .. attribute:: nexthop  (key)
                                            
                                            	Next hop for this path
                                            	**type**\: str
                                            
                                            .. attribute:: metric
                                            
                                            	Metric associated with the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: local_pref
                                            
                                            	Local preference for this path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: weight
                                            
                                            	Path weight
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_path
                                            
                                            	AS path
                                            	**type**\: str
                                            
                                            .. attribute:: origin
                                            
                                            	Path origin
                                            	**type**\:  :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                            
                                            .. attribute:: path_status
                                            
                                            	Path status
                                            	**type**\:  :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus>`
                                            
                                            .. attribute:: rpki_status
                                            
                                            	RPKI path status
                                            	**type**\:  :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                            
                                            .. attribute:: community
                                            
                                            	Community label for the path
                                            	**type**\: str
                                            
                                            .. attribute:: mpls_in
                                            
                                            	MPLS label in for the path
                                            	**type**\: str
                                            
                                            .. attribute:: mpls_out
                                            
                                            	MPLS label out for the path
                                            	**type**\: str
                                            
                                            .. attribute:: sr_profile_name
                                            
                                            	SR profile name for the path
                                            	**type**\: str
                                            
                                            .. attribute:: sr_binding_sid
                                            
                                            	SR binding sid for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sr_label_indx
                                            
                                            	SR label index for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4_path
                                            
                                            	path using 4\-octet AS numbers
                                            	**type**\: str
                                            
                                            .. attribute:: atomic_aggregate
                                            
                                            	attribute indicating whether or not the prefix is an atomic aggregate
                                            	**type**\: bool
                                            
                                            .. attribute:: aggr_as_number
                                            
                                            	AS number of autonomous system them performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: aggr_as4_number
                                            
                                            	AS4 number of autonomous system them performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: aggr_address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            .. attribute:: originator_id
                                            
                                            	the router ID of the originator of the route in the local AS
                                            	**type**\: str
                                            
                                            .. attribute:: cluster_list
                                            
                                            	the reflection path the route has passed
                                            	**type**\: str
                                            
                                            .. attribute:: extended_community
                                            
                                            	BGP extended community attribute
                                            	**type**\: str
                                            
                                            .. attribute:: ext_aigp_metric
                                            
                                            	the accumulated IGP metric for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: path_id
                                            
                                            	path identifier used to uniquely identify a route
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-09-25'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, self).__init__()

                                                self.yang_name = "bgp-path-entry"
                                                self.yang_parent_name = "bgp-path-entries"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['nexthop']
                                                self._child_container_classes = OrderedDict([("path-status", ("path_status", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('nexthop', YLeaf(YType.str, 'nexthop')),
                                                    ('metric', YLeaf(YType.uint32, 'metric')),
                                                    ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                    ('weight', YLeaf(YType.uint32, 'weight')),
                                                    ('as_path', YLeaf(YType.str, 'as-path')),
                                                    ('origin', YLeaf(YType.enumeration, 'origin')),
                                                    ('rpki_status', YLeaf(YType.enumeration, 'rpki-status')),
                                                    ('community', YLeaf(YType.str, 'community')),
                                                    ('mpls_in', YLeaf(YType.str, 'mpls-in')),
                                                    ('mpls_out', YLeaf(YType.str, 'mpls-out')),
                                                    ('sr_profile_name', YLeaf(YType.str, 'sr-profile-name')),
                                                    ('sr_binding_sid', YLeaf(YType.uint32, 'sr-binding-sid')),
                                                    ('sr_label_indx', YLeaf(YType.uint32, 'sr-label-indx')),
                                                    ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                    ('atomic_aggregate', YLeaf(YType.boolean, 'atomic-aggregate')),
                                                    ('aggr_as_number', YLeaf(YType.uint32, 'aggr-as-number')),
                                                    ('aggr_as4_number', YLeaf(YType.uint32, 'aggr-as4-number')),
                                                    ('aggr_address', YLeaf(YType.str, 'aggr-address')),
                                                    ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                    ('cluster_list', YLeaf(YType.str, 'cluster-list')),
                                                    ('extended_community', YLeaf(YType.str, 'extended-community')),
                                                    ('ext_aigp_metric', YLeaf(YType.uint64, 'ext-aigp-metric')),
                                                    ('path_id', YLeaf(YType.uint32, 'path-id')),
                                                ])
                                                self.nexthop = None
                                                self.metric = None
                                                self.local_pref = None
                                                self.weight = None
                                                self.as_path = None
                                                self.origin = None
                                                self.rpki_status = None
                                                self.community = None
                                                self.mpls_in = None
                                                self.mpls_out = None
                                                self.sr_profile_name = None
                                                self.sr_binding_sid = None
                                                self.sr_label_indx = None
                                                self.as4_path = None
                                                self.atomic_aggregate = None
                                                self.aggr_as_number = None
                                                self.aggr_as4_number = None
                                                self.aggr_address = None
                                                self.originator_id = None
                                                self.cluster_list = None
                                                self.extended_community = None
                                                self.ext_aigp_metric = None
                                                self.path_id = None

                                                self.path_status = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus()
                                                self.path_status.parent = self
                                                self._children_name_map["path_status"] = "path-status"
                                                self._children_yang_names.add("path-status")
                                                self._segment_path = lambda: "bgp-path-entry" + "[nexthop='" + str(self.nexthop) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, ['nexthop', 'metric', 'local_pref', 'weight', 'as_path', 'origin', 'rpki_status', 'community', 'mpls_in', 'mpls_out', 'sr_profile_name', 'sr_binding_sid', 'sr_label_indx', 'as4_path', 'atomic_aggregate', 'aggr_as_number', 'aggr_as4_number', 'aggr_address', 'originator_id', 'cluster_list', 'extended_community', 'ext_aigp_metric', 'path_id'], name, value)


                                            class PathStatus(Entity):
                                                """
                                                Path status
                                                
                                                .. attribute:: suppressed
                                                
                                                	Suppressed path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: damped
                                                
                                                	Damped path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: history
                                                
                                                	History path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: valid
                                                
                                                	Valid path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: sourced
                                                
                                                	Sourced path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: bestpath
                                                
                                                	Best path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: internal
                                                
                                                	Internal path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_fail
                                                
                                                	RIB\-fail path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: stale
                                                
                                                	Stale path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: multipath
                                                
                                                	Multipath path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: backup_path
                                                
                                                	Backup path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rt_filter
                                                
                                                	RT filter path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: best_external
                                                
                                                	Best externa path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: additional_path
                                                
                                                	Additional path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_compressed
                                                
                                                	RIB compressed path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-09-25'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, self).__init__()

                                                    self.yang_name = "path-status"
                                                    self.yang_parent_name = "bgp-path-entry"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('suppressed', YLeaf(YType.empty, 'suppressed')),
                                                        ('damped', YLeaf(YType.empty, 'damped')),
                                                        ('history', YLeaf(YType.empty, 'history')),
                                                        ('valid', YLeaf(YType.empty, 'valid')),
                                                        ('sourced', YLeaf(YType.empty, 'sourced')),
                                                        ('bestpath', YLeaf(YType.empty, 'bestpath')),
                                                        ('internal', YLeaf(YType.empty, 'internal')),
                                                        ('rib_fail', YLeaf(YType.empty, 'rib-fail')),
                                                        ('stale', YLeaf(YType.empty, 'stale')),
                                                        ('multipath', YLeaf(YType.empty, 'multipath')),
                                                        ('backup_path', YLeaf(YType.empty, 'backup-path')),
                                                        ('rt_filter', YLeaf(YType.empty, 'rt-filter')),
                                                        ('best_external', YLeaf(YType.empty, 'best-external')),
                                                        ('additional_path', YLeaf(YType.empty, 'additional-path')),
                                                        ('rib_compressed', YLeaf(YType.empty, 'rib-compressed')),
                                                    ])
                                                    self.suppressed = None
                                                    self.damped = None
                                                    self.history = None
                                                    self.valid = None
                                                    self.sourced = None
                                                    self.bestpath = None
                                                    self.internal = None
                                                    self.rib_fail = None
                                                    self.stale = None
                                                    self.multipath = None
                                                    self.backup_path = None
                                                    self.rt_filter = None
                                                    self.best_external = None
                                                    self.additional_path = None
                                                    self.rib_compressed = None
                                                    self._segment_path = lambda: "path-status"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, ['suppressed', 'damped', 'history', 'valid', 'sourced', 'bestpath', 'internal', 'rib_fail', 'stale', 'multipath', 'backup_path', 'rt_filter', 'best_external', 'additional_path', 'rib_compressed'], name, value)


                    class BgpRouteNeighbors(Entity):
                        """
                        BGP route neighbors
                        
                        .. attribute:: bgp_route_neighbor
                        
                        	List of BGP route neighbors
                        	**type**\: list of  		 :py:class:`BgpRouteNeighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-09-25'

                        def __init__(self):
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors, self).__init__()

                            self.yang_name = "bgp-route-neighbors"
                            self.yang_parent_name = "bgp-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("bgp-route-neighbor", ("bgp_route_neighbor", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor))])
                            self._leafs = OrderedDict()

                            self.bgp_route_neighbor = YList(self)
                            self._segment_path = lambda: "bgp-route-neighbors"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors, [], name, value)


                        class BgpRouteNeighbor(Entity):
                            """
                            List of BGP route neighbors
                            
                            .. attribute:: nbr_id  (key)
                            
                            	BGP neighbor ID
                            	**type**\: str
                            
                            .. attribute:: bgp_neighbor_route_filters
                            
                            	BGP neighbor route filters
                            	**type**\:  :py:class:`BgpNeighborRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters>`
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-09-25'

                            def __init__(self):
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor, self).__init__()

                                self.yang_name = "bgp-route-neighbor"
                                self.yang_parent_name = "bgp-route-neighbors"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['nbr_id']
                                self._child_container_classes = OrderedDict([("bgp-neighbor-route-filters", ("bgp_neighbor_route_filters", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('nbr_id', YLeaf(YType.str, 'nbr-id')),
                                ])
                                self.nbr_id = None

                                self.bgp_neighbor_route_filters = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters()
                                self.bgp_neighbor_route_filters.parent = self
                                self._children_name_map["bgp_neighbor_route_filters"] = "bgp-neighbor-route-filters"
                                self._children_yang_names.add("bgp-neighbor-route-filters")
                                self._segment_path = lambda: "bgp-route-neighbor" + "[nbr-id='" + str(self.nbr_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor, ['nbr_id'], name, value)


                            class BgpNeighborRouteFilters(Entity):
                                """
                                BGP neighbor route filters
                                
                                .. attribute:: bgp_neighbor_route_filter
                                
                                	List of BGP neighbor route filters
                                	**type**\: list of  		 :py:class:`BgpNeighborRouteFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter>`
                                
                                

                                """

                                _prefix = 'bgp-ios-xe-oper'
                                _revision = '2017-09-25'

                                def __init__(self):
                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters, self).__init__()

                                    self.yang_name = "bgp-neighbor-route-filters"
                                    self.yang_parent_name = "bgp-route-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bgp-neighbor-route-filter", ("bgp_neighbor_route_filter", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter))])
                                    self._leafs = OrderedDict()

                                    self.bgp_neighbor_route_filter = YList(self)
                                    self._segment_path = lambda: "bgp-neighbor-route-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters, [], name, value)


                                class BgpNeighborRouteFilter(Entity):
                                    """
                                    List of BGP neighbor route filters
                                    
                                    .. attribute:: nbr_fltr  (key)
                                    
                                    	BGP neighbor route filter
                                    	**type**\:  :py:class:`BgpNeighborRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpNeighborRouteFilters>`
                                    
                                    .. attribute:: bgp_neighbor_route_entries
                                    
                                    	BGP neighbor route entries
                                    	**type**\:  :py:class:`BgpNeighborRouteEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries>`
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-09-25'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter, self).__init__()

                                        self.yang_name = "bgp-neighbor-route-filter"
                                        self.yang_parent_name = "bgp-neighbor-route-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['nbr_fltr']
                                        self._child_container_classes = OrderedDict([("bgp-neighbor-route-entries", ("bgp_neighbor_route_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('nbr_fltr', YLeaf(YType.enumeration, 'nbr-fltr')),
                                        ])
                                        self.nbr_fltr = None

                                        self.bgp_neighbor_route_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries()
                                        self.bgp_neighbor_route_entries.parent = self
                                        self._children_name_map["bgp_neighbor_route_entries"] = "bgp-neighbor-route-entries"
                                        self._children_yang_names.add("bgp-neighbor-route-entries")
                                        self._segment_path = lambda: "bgp-neighbor-route-filter" + "[nbr-fltr='" + str(self.nbr_fltr) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter, ['nbr_fltr'], name, value)


                                    class BgpNeighborRouteEntries(Entity):
                                        """
                                        BGP neighbor route entries
                                        
                                        .. attribute:: bgp_neighbor_route_entry
                                        
                                        	List of BGP neighbor route entries
                                        	**type**\: list of  		 :py:class:`BgpNeighborRouteEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry>`
                                        
                                        

                                        """

                                        _prefix = 'bgp-ios-xe-oper'
                                        _revision = '2017-09-25'

                                        def __init__(self):
                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries, self).__init__()

                                            self.yang_name = "bgp-neighbor-route-entries"
                                            self.yang_parent_name = "bgp-neighbor-route-filter"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bgp-neighbor-route-entry", ("bgp_neighbor_route_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry))])
                                            self._leafs = OrderedDict()

                                            self.bgp_neighbor_route_entry = YList(self)
                                            self._segment_path = lambda: "bgp-neighbor-route-entries"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries, [], name, value)


                                        class BgpNeighborRouteEntry(Entity):
                                            """
                                            List of BGP neighbor route entries
                                            
                                            .. attribute:: prefix  (key)
                                            
                                            	Neighbor routing table entry prefix
                                            	**type**\: str
                                            
                                            .. attribute:: version
                                            
                                            	Neighbor routing table version
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: available_paths
                                            
                                            	Number of paths available for BGP prefix
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: advertised_to
                                            
                                            	Who this prefix was advertized to
                                            	**type**\: str
                                            
                                            .. attribute:: bgp_neighbor_path_entries
                                            
                                            	Prefix next hop details
                                            	**type**\:  :py:class:`BgpNeighborPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries>`
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-09-25'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry, self).__init__()

                                                self.yang_name = "bgp-neighbor-route-entry"
                                                self.yang_parent_name = "bgp-neighbor-route-entries"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['prefix']
                                                self._child_container_classes = OrderedDict([("bgp-neighbor-path-entries", ("bgp_neighbor_path_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                                    ('version', YLeaf(YType.uint32, 'version')),
                                                    ('available_paths', YLeaf(YType.uint32, 'available-paths')),
                                                    ('advertised_to', YLeaf(YType.str, 'advertised-to')),
                                                ])
                                                self.prefix = None
                                                self.version = None
                                                self.available_paths = None
                                                self.advertised_to = None

                                                self.bgp_neighbor_path_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries()
                                                self.bgp_neighbor_path_entries.parent = self
                                                self._children_name_map["bgp_neighbor_path_entries"] = "bgp-neighbor-path-entries"
                                                self._children_yang_names.add("bgp-neighbor-path-entries")
                                                self._segment_path = lambda: "bgp-neighbor-route-entry" + "[prefix='" + str(self.prefix) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry, ['prefix', 'version', 'available_paths', 'advertised_to'], name, value)


                                            class BgpNeighborPathEntries(Entity):
                                                """
                                                Prefix next hop details
                                                
                                                .. attribute:: bgp_neighbor_path_entry
                                                
                                                	List of prefix next hop details
                                                	**type**\: list of  		 :py:class:`BgpNeighborPathEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-09-25'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries, self).__init__()

                                                    self.yang_name = "bgp-neighbor-path-entries"
                                                    self.yang_parent_name = "bgp-neighbor-route-entry"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([("bgp-neighbor-path-entry", ("bgp_neighbor_path_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry))])
                                                    self._leafs = OrderedDict()

                                                    self.bgp_neighbor_path_entry = YList(self)
                                                    self._segment_path = lambda: "bgp-neighbor-path-entries"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries, [], name, value)


                                                class BgpNeighborPathEntry(Entity):
                                                    """
                                                    List of prefix next hop details
                                                    
                                                    .. attribute:: nexthop  (key)
                                                    
                                                    	Next hop for this path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric associated with the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: local_pref
                                                    
                                                    	Local preference for this path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: weight
                                                    
                                                    	Path weight
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: as_path
                                                    
                                                    	AS path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: origin
                                                    
                                                    	Path origin
                                                    	**type**\:  :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                                    
                                                    .. attribute:: path_status
                                                    
                                                    	Path status
                                                    	**type**\:  :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry.PathStatus>`
                                                    
                                                    .. attribute:: rpki_status
                                                    
                                                    	RPKI path status
                                                    	**type**\:  :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                                    
                                                    .. attribute:: community
                                                    
                                                    	Community label for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: mpls_in
                                                    
                                                    	MPLS label in for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: mpls_out
                                                    
                                                    	MPLS label out for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: sr_profile_name
                                                    
                                                    	SR profile name for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: sr_binding_sid
                                                    
                                                    	SR binding sid for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: sr_label_indx
                                                    
                                                    	SR label index for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: as4_path
                                                    
                                                    	path using 4\-octet AS numbers
                                                    	**type**\: str
                                                    
                                                    .. attribute:: atomic_aggregate
                                                    
                                                    	attribute indicating whether or not the prefix is an atomic aggregate
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: aggr_as_number
                                                    
                                                    	AS number of autonomous system them performed the aggregation
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: aggr_as4_number
                                                    
                                                    	AS4 number of autonomous system them performed the aggregation
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: aggr_address
                                                    
                                                    	IP address of the router that performed the aggregation
                                                    	**type**\: str
                                                    
                                                    .. attribute:: originator_id
                                                    
                                                    	the router ID of the originator of the route in the local AS
                                                    	**type**\: str
                                                    
                                                    .. attribute:: cluster_list
                                                    
                                                    	the reflection path the route has passed
                                                    	**type**\: str
                                                    
                                                    .. attribute:: extended_community
                                                    
                                                    	BGP extended community attribute
                                                    	**type**\: str
                                                    
                                                    .. attribute:: ext_aigp_metric
                                                    
                                                    	the accumulated IGP metric for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: path_id
                                                    
                                                    	path identifier used to uniquely identify a route
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'bgp-ios-xe-oper'
                                                    _revision = '2017-09-25'

                                                    def __init__(self):
                                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry, self).__init__()

                                                        self.yang_name = "bgp-neighbor-path-entry"
                                                        self.yang_parent_name = "bgp-neighbor-path-entries"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['nexthop']
                                                        self._child_container_classes = OrderedDict([("path-status", ("path_status", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry.PathStatus))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('nexthop', YLeaf(YType.str, 'nexthop')),
                                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                                            ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                            ('weight', YLeaf(YType.uint32, 'weight')),
                                                            ('as_path', YLeaf(YType.str, 'as-path')),
                                                            ('origin', YLeaf(YType.enumeration, 'origin')),
                                                            ('rpki_status', YLeaf(YType.enumeration, 'rpki-status')),
                                                            ('community', YLeaf(YType.str, 'community')),
                                                            ('mpls_in', YLeaf(YType.str, 'mpls-in')),
                                                            ('mpls_out', YLeaf(YType.str, 'mpls-out')),
                                                            ('sr_profile_name', YLeaf(YType.str, 'sr-profile-name')),
                                                            ('sr_binding_sid', YLeaf(YType.uint32, 'sr-binding-sid')),
                                                            ('sr_label_indx', YLeaf(YType.uint32, 'sr-label-indx')),
                                                            ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                            ('atomic_aggregate', YLeaf(YType.boolean, 'atomic-aggregate')),
                                                            ('aggr_as_number', YLeaf(YType.uint32, 'aggr-as-number')),
                                                            ('aggr_as4_number', YLeaf(YType.uint32, 'aggr-as4-number')),
                                                            ('aggr_address', YLeaf(YType.str, 'aggr-address')),
                                                            ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                            ('cluster_list', YLeaf(YType.str, 'cluster-list')),
                                                            ('extended_community', YLeaf(YType.str, 'extended-community')),
                                                            ('ext_aigp_metric', YLeaf(YType.uint64, 'ext-aigp-metric')),
                                                            ('path_id', YLeaf(YType.uint32, 'path-id')),
                                                        ])
                                                        self.nexthop = None
                                                        self.metric = None
                                                        self.local_pref = None
                                                        self.weight = None
                                                        self.as_path = None
                                                        self.origin = None
                                                        self.rpki_status = None
                                                        self.community = None
                                                        self.mpls_in = None
                                                        self.mpls_out = None
                                                        self.sr_profile_name = None
                                                        self.sr_binding_sid = None
                                                        self.sr_label_indx = None
                                                        self.as4_path = None
                                                        self.atomic_aggregate = None
                                                        self.aggr_as_number = None
                                                        self.aggr_as4_number = None
                                                        self.aggr_address = None
                                                        self.originator_id = None
                                                        self.cluster_list = None
                                                        self.extended_community = None
                                                        self.ext_aigp_metric = None
                                                        self.path_id = None

                                                        self.path_status = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry.PathStatus()
                                                        self.path_status.parent = self
                                                        self._children_name_map["path_status"] = "path-status"
                                                        self._children_yang_names.add("path-status")
                                                        self._segment_path = lambda: "bgp-neighbor-path-entry" + "[nexthop='" + str(self.nexthop) + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry, ['nexthop', 'metric', 'local_pref', 'weight', 'as_path', 'origin', 'rpki_status', 'community', 'mpls_in', 'mpls_out', 'sr_profile_name', 'sr_binding_sid', 'sr_label_indx', 'as4_path', 'atomic_aggregate', 'aggr_as_number', 'aggr_as4_number', 'aggr_address', 'originator_id', 'cluster_list', 'extended_community', 'ext_aigp_metric', 'path_id'], name, value)


                                                    class PathStatus(Entity):
                                                        """
                                                        Path status
                                                        
                                                        .. attribute:: suppressed
                                                        
                                                        	Suppressed path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: damped
                                                        
                                                        	Damped path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: history
                                                        
                                                        	History path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: valid
                                                        
                                                        	Valid path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: sourced
                                                        
                                                        	Sourced path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: bestpath
                                                        
                                                        	Best path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: internal
                                                        
                                                        	Internal path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rib_fail
                                                        
                                                        	RIB\-fail path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: stale
                                                        
                                                        	Stale path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: multipath
                                                        
                                                        	Multipath path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: backup_path
                                                        
                                                        	Backup path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rt_filter
                                                        
                                                        	RT filter path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: best_external
                                                        
                                                        	Best externa path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: additional_path
                                                        
                                                        	Additional path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rib_compressed
                                                        
                                                        	RIB compressed path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'bgp-ios-xe-oper'
                                                        _revision = '2017-09-25'

                                                        def __init__(self):
                                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry.PathStatus, self).__init__()

                                                            self.yang_name = "path-status"
                                                            self.yang_parent_name = "bgp-neighbor-path-entry"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('suppressed', YLeaf(YType.empty, 'suppressed')),
                                                                ('damped', YLeaf(YType.empty, 'damped')),
                                                                ('history', YLeaf(YType.empty, 'history')),
                                                                ('valid', YLeaf(YType.empty, 'valid')),
                                                                ('sourced', YLeaf(YType.empty, 'sourced')),
                                                                ('bestpath', YLeaf(YType.empty, 'bestpath')),
                                                                ('internal', YLeaf(YType.empty, 'internal')),
                                                                ('rib_fail', YLeaf(YType.empty, 'rib-fail')),
                                                                ('stale', YLeaf(YType.empty, 'stale')),
                                                                ('multipath', YLeaf(YType.empty, 'multipath')),
                                                                ('backup_path', YLeaf(YType.empty, 'backup-path')),
                                                                ('rt_filter', YLeaf(YType.empty, 'rt-filter')),
                                                                ('best_external', YLeaf(YType.empty, 'best-external')),
                                                                ('additional_path', YLeaf(YType.empty, 'additional-path')),
                                                                ('rib_compressed', YLeaf(YType.empty, 'rib-compressed')),
                                                            ])
                                                            self.suppressed = None
                                                            self.damped = None
                                                            self.history = None
                                                            self.valid = None
                                                            self.sourced = None
                                                            self.bestpath = None
                                                            self.internal = None
                                                            self.rib_fail = None
                                                            self.stale = None
                                                            self.multipath = None
                                                            self.backup_path = None
                                                            self.rt_filter = None
                                                            self.best_external = None
                                                            self.additional_path = None
                                                            self.rib_compressed = None
                                                            self._segment_path = lambda: "path-status"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteNeighbors.BgpRouteNeighbor.BgpNeighborRouteFilters.BgpNeighborRouteFilter.BgpNeighborRouteEntries.BgpNeighborRouteEntry.BgpNeighborPathEntries.BgpNeighborPathEntry.PathStatus, ['suppressed', 'damped', 'history', 'valid', 'sourced', 'bestpath', 'internal', 'rib_fail', 'stale', 'multipath', 'backup_path', 'rt_filter', 'best_external', 'additional_path', 'rib_compressed'], name, value)


                    class BgpPeerGroups(Entity):
                        """
                        BGP peer groups
                        
                        .. attribute:: bgp_peer_group
                        
                        	List of BGP peer groups
                        	**type**\: list of  		 :py:class:`BgpPeerGroup <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups.BgpPeerGroup>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-09-25'

                        def __init__(self):
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups, self).__init__()

                            self.yang_name = "bgp-peer-groups"
                            self.yang_parent_name = "bgp-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("bgp-peer-group", ("bgp_peer_group", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups.BgpPeerGroup))])
                            self._leafs = OrderedDict()

                            self.bgp_peer_group = YList(self)
                            self._segment_path = lambda: "bgp-peer-groups"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups, [], name, value)


                        class BgpPeerGroup(Entity):
                            """
                            List of BGP peer groups
                            
                            .. attribute:: name  (key)
                            
                            	BGP peer group name
                            	**type**\: str
                            
                            .. attribute:: description
                            
                            	Peer Group description string
                            	**type**\: str
                            
                            .. attribute:: remote_as
                            
                            	Peer Group Remote as value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: bgp_version
                            
                            	BGP version being used to communicate with the remote router
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: min_time
                            
                            	Peer Group minimum time
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: num_of_sessions
                            
                            	Number of Sessions for peer group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_estab_sessions
                            
                            	Number of established sessions  for peer group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: num_sso_sessions
                            
                            	Number of SSO sesssions for peer group
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: peer_members
                            
                            	BGP peer group members
                            	**type**\: list of str
                            
                            .. attribute:: fmt_grp_ix
                            
                            	BGP peer group Formatted Group Index value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: adv_ix
                            
                            	BGP peer group Advertised Index value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: aspath_in
                            
                            	BGP peer group aspath  filter in value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: aspath_out
                            
                            	BGP peer group aspath  filter out value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: routemap_in
                            
                            	BGP peer group Route Map in value
                            	**type**\: str
                            
                            .. attribute:: routemap_out
                            
                            	BGP peer group Route Map out value
                            	**type**\: str
                            
                            .. attribute:: updated_messages
                            
                            	BGP peer group Updated Messages value
                            	**type**\: int
                            
                            	**range:** 0..18446744073709551615
                            
                            .. attribute:: rep_count
                            
                            	BGP peer group Replicated Count value
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: slowpeer_detection_value
                            
                            	BGP peer group slow peer Threshold value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: weight
                            
                            	BGP weight value
                            	**type**\: int
                            
                            	**range:** 0..65535
                            
                            .. attribute:: send_community
                            
                            	BGP Send Community status
                            	**type**\: bool
                            
                            .. attribute:: extended_community
                            
                            	BGP Extended Community status
                            	**type**\: bool
                            
                            .. attribute:: remove_private_as
                            
                            	BGP Remove PrivateAs status
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-09-25'

                            def __init__(self):
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups.BgpPeerGroup, self).__init__()

                                self.yang_name = "bgp-peer-group"
                                self.yang_parent_name = "bgp-peer-groups"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['name']
                                self._child_container_classes = OrderedDict([])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('name', YLeaf(YType.str, 'name')),
                                    ('description', YLeaf(YType.str, 'description')),
                                    ('remote_as', YLeaf(YType.uint32, 'remote-as')),
                                    ('bgp_version', YLeaf(YType.uint16, 'bgp-version')),
                                    ('min_time', YLeaf(YType.uint16, 'min-time')),
                                    ('num_of_sessions', YLeaf(YType.uint32, 'num-of-sessions')),
                                    ('num_estab_sessions', YLeaf(YType.uint32, 'num-estab-sessions')),
                                    ('num_sso_sessions', YLeaf(YType.uint32, 'num-sso-sessions')),
                                    ('peer_members', YLeafList(YType.str, 'peer-members')),
                                    ('fmt_grp_ix', YLeaf(YType.uint16, 'fmt-grp-ix')),
                                    ('adv_ix', YLeaf(YType.uint16, 'adv-ix')),
                                    ('aspath_in', YLeaf(YType.uint32, 'aspath-in')),
                                    ('aspath_out', YLeaf(YType.uint32, 'aspath-out')),
                                    ('routemap_in', YLeaf(YType.str, 'routemap-in')),
                                    ('routemap_out', YLeaf(YType.str, 'routemap-out')),
                                    ('updated_messages', YLeaf(YType.uint64, 'updated-messages')),
                                    ('rep_count', YLeaf(YType.uint32, 'rep-count')),
                                    ('slowpeer_detection_value', YLeaf(YType.uint16, 'slowpeer-detection-value')),
                                    ('weight', YLeaf(YType.uint16, 'weight')),
                                    ('send_community', YLeaf(YType.boolean, 'send-community')),
                                    ('extended_community', YLeaf(YType.boolean, 'extended-community')),
                                    ('remove_private_as', YLeaf(YType.boolean, 'remove-private-as')),
                                ])
                                self.name = None
                                self.description = None
                                self.remote_as = None
                                self.bgp_version = None
                                self.min_time = None
                                self.num_of_sessions = None
                                self.num_estab_sessions = None
                                self.num_sso_sessions = None
                                self.peer_members = []
                                self.fmt_grp_ix = None
                                self.adv_ix = None
                                self.aspath_in = None
                                self.aspath_out = None
                                self.routemap_in = None
                                self.routemap_out = None
                                self.updated_messages = None
                                self.rep_count = None
                                self.slowpeer_detection_value = None
                                self.weight = None
                                self.send_community = None
                                self.extended_community = None
                                self.remove_private_as = None
                                self._segment_path = lambda: "bgp-peer-group" + "[name='" + str(self.name) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpPeerGroups.BgpPeerGroup, ['name', 'description', 'remote_as', 'bgp_version', 'min_time', 'num_of_sessions', 'num_estab_sessions', 'num_sso_sessions', 'peer_members', 'fmt_grp_ix', 'adv_ix', 'aspath_in', 'aspath_out', 'routemap_in', 'routemap_out', 'updated_messages', 'rep_count', 'slowpeer_detection_value', 'weight', 'send_community', 'extended_community', 'remove_private_as'], name, value)


    class BgpRouteRds(Entity):
        """
        BGP RDs
        
        .. attribute:: bgp_route_rd
        
        	List of BGP RDs
        	**type**\: list of  		 :py:class:`BgpRouteRd <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-09-25'

        def __init__(self):
            super(BgpStateData.BgpRouteRds, self).__init__()

            self.yang_name = "bgp-route-rds"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_container_classes = OrderedDict([])
            self._child_list_classes = OrderedDict([("bgp-route-rd", ("bgp_route_rd", BgpStateData.BgpRouteRds.BgpRouteRd))])
            self._leafs = OrderedDict()

            self.bgp_route_rd = YList(self)
            self._segment_path = lambda: "bgp-route-rds"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.BgpRouteRds, [], name, value)


        class BgpRouteRd(Entity):
            """
            List of BGP RDs
            
            .. attribute:: rd_value  (key)
            
            	BGP rd value
            	**type**\: str
            
            .. attribute:: bgp_rd_route_afs
            
            	BGP rd address families
            	**type**\:  :py:class:`BgpRdRouteAfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs>`
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-09-25'

            def __init__(self):
                super(BgpStateData.BgpRouteRds.BgpRouteRd, self).__init__()

                self.yang_name = "bgp-route-rd"
                self.yang_parent_name = "bgp-route-rds"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['rd_value']
                self._child_container_classes = OrderedDict([("bgp-rd-route-afs", ("bgp_rd_route_afs", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs))])
                self._child_list_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('rd_value', YLeaf(YType.str, 'rd-value')),
                ])
                self.rd_value = None

                self.bgp_rd_route_afs = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs()
                self.bgp_rd_route_afs.parent = self
                self._children_name_map["bgp_rd_route_afs"] = "bgp-rd-route-afs"
                self._children_yang_names.add("bgp-rd-route-afs")
                self._segment_path = lambda: "bgp-route-rd" + "[rd-value='" + str(self.rd_value) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/bgp-route-rds/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd, ['rd_value'], name, value)


            class BgpRdRouteAfs(Entity):
                """
                BGP rd address families
                
                .. attribute:: bgp_rd_route_af
                
                	List of BGP RD address families
                	**type**\: list of  		 :py:class:`BgpRdRouteAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-09-25'

                def __init__(self):
                    super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs, self).__init__()

                    self.yang_name = "bgp-rd-route-afs"
                    self.yang_parent_name = "bgp-route-rd"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_container_classes = OrderedDict([])
                    self._child_list_classes = OrderedDict([("bgp-rd-route-af", ("bgp_rd_route_af", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf))])
                    self._leafs = OrderedDict()

                    self.bgp_rd_route_af = YList(self)
                    self._segment_path = lambda: "bgp-rd-route-afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs, [], name, value)


                class BgpRdRouteAf(Entity):
                    """
                    List of BGP RD address families
                    
                    .. attribute:: afi_safi  (key)
                    
                    	BGP address family
                    	**type**\:  :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
                    
                    .. attribute:: bgp_rd_route_filters
                    
                    	BGP RD route filters
                    	**type**\:  :py:class:`BgpRdRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters>`
                    
                    .. attribute:: bgp_rd_route_neighbors
                    
                    	BGP RD route neighbors
                    	**type**\:  :py:class:`BgpRdRouteNeighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors>`
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-09-25'

                    def __init__(self):
                        super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf, self).__init__()

                        self.yang_name = "bgp-rd-route-af"
                        self.yang_parent_name = "bgp-rd-route-afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['afi_safi']
                        self._child_container_classes = OrderedDict([("bgp-rd-route-filters", ("bgp_rd_route_filters", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters)), ("bgp-rd-route-neighbors", ("bgp_rd_route_neighbors", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors))])
                        self._child_list_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('afi_safi', YLeaf(YType.enumeration, 'afi-safi')),
                        ])
                        self.afi_safi = None

                        self.bgp_rd_route_filters = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters()
                        self.bgp_rd_route_filters.parent = self
                        self._children_name_map["bgp_rd_route_filters"] = "bgp-rd-route-filters"
                        self._children_yang_names.add("bgp-rd-route-filters")

                        self.bgp_rd_route_neighbors = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors()
                        self.bgp_rd_route_neighbors.parent = self
                        self._children_name_map["bgp_rd_route_neighbors"] = "bgp-rd-route-neighbors"
                        self._children_yang_names.add("bgp-rd-route-neighbors")
                        self._segment_path = lambda: "bgp-rd-route-af" + "[afi-safi='" + str(self.afi_safi) + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf, ['afi_safi'], name, value)


                    class BgpRdRouteFilters(Entity):
                        """
                        BGP RD route filters
                        
                        .. attribute:: bgp_rd_route_filter
                        
                        	List of BGP RD route filters
                        	**type**\: list of  		 :py:class:`BgpRdRouteFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-09-25'

                        def __init__(self):
                            super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters, self).__init__()

                            self.yang_name = "bgp-rd-route-filters"
                            self.yang_parent_name = "bgp-rd-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("bgp-rd-route-filter", ("bgp_rd_route_filter", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter))])
                            self._leafs = OrderedDict()

                            self.bgp_rd_route_filter = YList(self)
                            self._segment_path = lambda: "bgp-rd-route-filters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters, [], name, value)


                        class BgpRdRouteFilter(Entity):
                            """
                            List of BGP RD route filters
                            
                            .. attribute:: route_filter  (key)
                            
                            	BGP RD route filter
                            	**type**\:  :py:class:`BgpRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRouteFilters>`
                            
                            .. attribute:: bgp_rd_route_entries
                            
                            	BGP RD route entries
                            	**type**\:  :py:class:`BgpRdRouteEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries>`
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-09-25'

                            def __init__(self):
                                super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter, self).__init__()

                                self.yang_name = "bgp-rd-route-filter"
                                self.yang_parent_name = "bgp-rd-route-filters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['route_filter']
                                self._child_container_classes = OrderedDict([("bgp-rd-route-entries", ("bgp_rd_route_entries", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('route_filter', YLeaf(YType.enumeration, 'route-filter')),
                                ])
                                self.route_filter = None

                                self.bgp_rd_route_entries = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries()
                                self.bgp_rd_route_entries.parent = self
                                self._children_name_map["bgp_rd_route_entries"] = "bgp-rd-route-entries"
                                self._children_yang_names.add("bgp-rd-route-entries")
                                self._segment_path = lambda: "bgp-rd-route-filter" + "[route-filter='" + str(self.route_filter) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter, ['route_filter'], name, value)


                            class BgpRdRouteEntries(Entity):
                                """
                                BGP RD route entries
                                
                                .. attribute:: bgp_rd_route_entry
                                
                                	List of BGP RD route entries
                                	**type**\: list of  		 :py:class:`BgpRdRouteEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry>`
                                
                                

                                """

                                _prefix = 'bgp-ios-xe-oper'
                                _revision = '2017-09-25'

                                def __init__(self):
                                    super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries, self).__init__()

                                    self.yang_name = "bgp-rd-route-entries"
                                    self.yang_parent_name = "bgp-rd-route-filter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bgp-rd-route-entry", ("bgp_rd_route_entry", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry))])
                                    self._leafs = OrderedDict()

                                    self.bgp_rd_route_entry = YList(self)
                                    self._segment_path = lambda: "bgp-rd-route-entries"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries, [], name, value)


                                class BgpRdRouteEntry(Entity):
                                    """
                                    List of BGP RD route entries
                                    
                                    .. attribute:: prefix  (key)
                                    
                                    	RD Routing table entry prefix
                                    	**type**\: str
                                    
                                    .. attribute:: version
                                    
                                    	RD Routing table version
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: available_paths
                                    
                                    	Number of  paths available for BGP prefix
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: advertised_to
                                    
                                    	Whom is thie prefix advertized to
                                    	**type**\: str
                                    
                                    .. attribute:: bgp_rd_path_entries
                                    
                                    	Prefix next hop details
                                    	**type**\:  :py:class:`BgpRdPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries>`
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-09-25'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry, self).__init__()

                                        self.yang_name = "bgp-rd-route-entry"
                                        self.yang_parent_name = "bgp-rd-route-entries"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['prefix']
                                        self._child_container_classes = OrderedDict([("bgp-rd-path-entries", ("bgp_rd_path_entries", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('prefix', YLeaf(YType.str, 'prefix')),
                                            ('version', YLeaf(YType.uint32, 'version')),
                                            ('available_paths', YLeaf(YType.uint32, 'available-paths')),
                                            ('advertised_to', YLeaf(YType.str, 'advertised-to')),
                                        ])
                                        self.prefix = None
                                        self.version = None
                                        self.available_paths = None
                                        self.advertised_to = None

                                        self.bgp_rd_path_entries = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries()
                                        self.bgp_rd_path_entries.parent = self
                                        self._children_name_map["bgp_rd_path_entries"] = "bgp-rd-path-entries"
                                        self._children_yang_names.add("bgp-rd-path-entries")
                                        self._segment_path = lambda: "bgp-rd-route-entry" + "[prefix='" + str(self.prefix) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry, ['prefix', 'version', 'available_paths', 'advertised_to'], name, value)


                                    class BgpRdPathEntries(Entity):
                                        """
                                        Prefix next hop details
                                        
                                        .. attribute:: bgp_rd_path_entry
                                        
                                        	List of prefix next hop details
                                        	**type**\: list of  		 :py:class:`BgpRdPathEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry>`
                                        
                                        

                                        """

                                        _prefix = 'bgp-ios-xe-oper'
                                        _revision = '2017-09-25'

                                        def __init__(self):
                                            super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries, self).__init__()

                                            self.yang_name = "bgp-rd-path-entries"
                                            self.yang_parent_name = "bgp-rd-route-entry"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bgp-rd-path-entry", ("bgp_rd_path_entry", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry))])
                                            self._leafs = OrderedDict()

                                            self.bgp_rd_path_entry = YList(self)
                                            self._segment_path = lambda: "bgp-rd-path-entries"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries, [], name, value)


                                        class BgpRdPathEntry(Entity):
                                            """
                                            List of prefix next hop details
                                            
                                            .. attribute:: nexthop  (key)
                                            
                                            	Next hop for this path
                                            	**type**\: str
                                            
                                            .. attribute:: metric
                                            
                                            	Metric associated with the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: local_pref
                                            
                                            	Local preference for this path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: weight
                                            
                                            	Path weight
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_path
                                            
                                            	AS path
                                            	**type**\: str
                                            
                                            .. attribute:: origin
                                            
                                            	Path origin
                                            	**type**\:  :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                            
                                            .. attribute:: path_status
                                            
                                            	Path status
                                            	**type**\:  :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry.PathStatus>`
                                            
                                            .. attribute:: rpki_status
                                            
                                            	RPKI path status
                                            	**type**\:  :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                            
                                            .. attribute:: community
                                            
                                            	Community label for the path
                                            	**type**\: str
                                            
                                            .. attribute:: mpls_in
                                            
                                            	MPLS label in for the path
                                            	**type**\: str
                                            
                                            .. attribute:: mpls_out
                                            
                                            	MPLS label out for the path
                                            	**type**\: str
                                            
                                            .. attribute:: sr_profile_name
                                            
                                            	SR profile name for the path
                                            	**type**\: str
                                            
                                            .. attribute:: sr_binding_sid
                                            
                                            	SR binding sid for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: sr_label_indx
                                            
                                            	SR label index for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as4_path
                                            
                                            	path using 4\-octet AS numbers
                                            	**type**\: str
                                            
                                            .. attribute:: atomic_aggregate
                                            
                                            	attribute indicating whether or not the prefix is an atomic aggregate
                                            	**type**\: bool
                                            
                                            .. attribute:: aggr_as_number
                                            
                                            	AS number of autonomous system them performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: aggr_as4_number
                                            
                                            	AS4 number of autonomous system them performed the aggregation
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: aggr_address
                                            
                                            	IP address of the router that performed the aggregation
                                            	**type**\: str
                                            
                                            .. attribute:: originator_id
                                            
                                            	the router ID of the originator of the route in the local AS
                                            	**type**\: str
                                            
                                            .. attribute:: cluster_list
                                            
                                            	the reflection path the route has passed
                                            	**type**\: str
                                            
                                            .. attribute:: extended_community
                                            
                                            	BGP extended community attribute
                                            	**type**\: str
                                            
                                            .. attribute:: ext_aigp_metric
                                            
                                            	the accumulated IGP metric for the path
                                            	**type**\: int
                                            
                                            	**range:** 0..18446744073709551615
                                            
                                            .. attribute:: path_id
                                            
                                            	path identifier used to uniquely identify a route
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-09-25'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry, self).__init__()

                                                self.yang_name = "bgp-rd-path-entry"
                                                self.yang_parent_name = "bgp-rd-path-entries"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['nexthop']
                                                self._child_container_classes = OrderedDict([("path-status", ("path_status", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry.PathStatus))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('nexthop', YLeaf(YType.str, 'nexthop')),
                                                    ('metric', YLeaf(YType.uint32, 'metric')),
                                                    ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                    ('weight', YLeaf(YType.uint32, 'weight')),
                                                    ('as_path', YLeaf(YType.str, 'as-path')),
                                                    ('origin', YLeaf(YType.enumeration, 'origin')),
                                                    ('rpki_status', YLeaf(YType.enumeration, 'rpki-status')),
                                                    ('community', YLeaf(YType.str, 'community')),
                                                    ('mpls_in', YLeaf(YType.str, 'mpls-in')),
                                                    ('mpls_out', YLeaf(YType.str, 'mpls-out')),
                                                    ('sr_profile_name', YLeaf(YType.str, 'sr-profile-name')),
                                                    ('sr_binding_sid', YLeaf(YType.uint32, 'sr-binding-sid')),
                                                    ('sr_label_indx', YLeaf(YType.uint32, 'sr-label-indx')),
                                                    ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                    ('atomic_aggregate', YLeaf(YType.boolean, 'atomic-aggregate')),
                                                    ('aggr_as_number', YLeaf(YType.uint32, 'aggr-as-number')),
                                                    ('aggr_as4_number', YLeaf(YType.uint32, 'aggr-as4-number')),
                                                    ('aggr_address', YLeaf(YType.str, 'aggr-address')),
                                                    ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                    ('cluster_list', YLeaf(YType.str, 'cluster-list')),
                                                    ('extended_community', YLeaf(YType.str, 'extended-community')),
                                                    ('ext_aigp_metric', YLeaf(YType.uint64, 'ext-aigp-metric')),
                                                    ('path_id', YLeaf(YType.uint32, 'path-id')),
                                                ])
                                                self.nexthop = None
                                                self.metric = None
                                                self.local_pref = None
                                                self.weight = None
                                                self.as_path = None
                                                self.origin = None
                                                self.rpki_status = None
                                                self.community = None
                                                self.mpls_in = None
                                                self.mpls_out = None
                                                self.sr_profile_name = None
                                                self.sr_binding_sid = None
                                                self.sr_label_indx = None
                                                self.as4_path = None
                                                self.atomic_aggregate = None
                                                self.aggr_as_number = None
                                                self.aggr_as4_number = None
                                                self.aggr_address = None
                                                self.originator_id = None
                                                self.cluster_list = None
                                                self.extended_community = None
                                                self.ext_aigp_metric = None
                                                self.path_id = None

                                                self.path_status = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry.PathStatus()
                                                self.path_status.parent = self
                                                self._children_name_map["path_status"] = "path-status"
                                                self._children_yang_names.add("path-status")
                                                self._segment_path = lambda: "bgp-rd-path-entry" + "[nexthop='" + str(self.nexthop) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry, ['nexthop', 'metric', 'local_pref', 'weight', 'as_path', 'origin', 'rpki_status', 'community', 'mpls_in', 'mpls_out', 'sr_profile_name', 'sr_binding_sid', 'sr_label_indx', 'as4_path', 'atomic_aggregate', 'aggr_as_number', 'aggr_as4_number', 'aggr_address', 'originator_id', 'cluster_list', 'extended_community', 'ext_aigp_metric', 'path_id'], name, value)


                                            class PathStatus(Entity):
                                                """
                                                Path status
                                                
                                                .. attribute:: suppressed
                                                
                                                	Suppressed path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: damped
                                                
                                                	Damped path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: history
                                                
                                                	History path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: valid
                                                
                                                	Valid path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: sourced
                                                
                                                	Sourced path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: bestpath
                                                
                                                	Best path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: internal
                                                
                                                	Internal path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_fail
                                                
                                                	RIB\-fail path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: stale
                                                
                                                	Stale path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: multipath
                                                
                                                	Multipath path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: backup_path
                                                
                                                	Backup path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rt_filter
                                                
                                                	RT filter path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: best_external
                                                
                                                	Best externa path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: additional_path
                                                
                                                	Additional path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_compressed
                                                
                                                	RIB compressed path
                                                	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-09-25'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry.PathStatus, self).__init__()

                                                    self.yang_name = "path-status"
                                                    self.yang_parent_name = "bgp-rd-path-entry"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([])
                                                    self._leafs = OrderedDict([
                                                        ('suppressed', YLeaf(YType.empty, 'suppressed')),
                                                        ('damped', YLeaf(YType.empty, 'damped')),
                                                        ('history', YLeaf(YType.empty, 'history')),
                                                        ('valid', YLeaf(YType.empty, 'valid')),
                                                        ('sourced', YLeaf(YType.empty, 'sourced')),
                                                        ('bestpath', YLeaf(YType.empty, 'bestpath')),
                                                        ('internal', YLeaf(YType.empty, 'internal')),
                                                        ('rib_fail', YLeaf(YType.empty, 'rib-fail')),
                                                        ('stale', YLeaf(YType.empty, 'stale')),
                                                        ('multipath', YLeaf(YType.empty, 'multipath')),
                                                        ('backup_path', YLeaf(YType.empty, 'backup-path')),
                                                        ('rt_filter', YLeaf(YType.empty, 'rt-filter')),
                                                        ('best_external', YLeaf(YType.empty, 'best-external')),
                                                        ('additional_path', YLeaf(YType.empty, 'additional-path')),
                                                        ('rib_compressed', YLeaf(YType.empty, 'rib-compressed')),
                                                    ])
                                                    self.suppressed = None
                                                    self.damped = None
                                                    self.history = None
                                                    self.valid = None
                                                    self.sourced = None
                                                    self.bestpath = None
                                                    self.internal = None
                                                    self.rib_fail = None
                                                    self.stale = None
                                                    self.multipath = None
                                                    self.backup_path = None
                                                    self.rt_filter = None
                                                    self.best_external = None
                                                    self.additional_path = None
                                                    self.rib_compressed = None
                                                    self._segment_path = lambda: "path-status"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteFilters.BgpRdRouteFilter.BgpRdRouteEntries.BgpRdRouteEntry.BgpRdPathEntries.BgpRdPathEntry.PathStatus, ['suppressed', 'damped', 'history', 'valid', 'sourced', 'bestpath', 'internal', 'rib_fail', 'stale', 'multipath', 'backup_path', 'rt_filter', 'best_external', 'additional_path', 'rib_compressed'], name, value)


                    class BgpRdRouteNeighbors(Entity):
                        """
                        BGP RD route neighbors
                        
                        .. attribute:: bgp_rd_route_neighbor
                        
                        	List of BGP RD route neighbors
                        	**type**\: list of  		 :py:class:`BgpRdRouteNeighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-09-25'

                        def __init__(self):
                            super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors, self).__init__()

                            self.yang_name = "bgp-rd-route-neighbors"
                            self.yang_parent_name = "bgp-rd-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_container_classes = OrderedDict([])
                            self._child_list_classes = OrderedDict([("bgp-rd-route-neighbor", ("bgp_rd_route_neighbor", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor))])
                            self._leafs = OrderedDict()

                            self.bgp_rd_route_neighbor = YList(self)
                            self._segment_path = lambda: "bgp-rd-route-neighbors"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors, [], name, value)


                        class BgpRdRouteNeighbor(Entity):
                            """
                            List of BGP RD route neighbors
                            
                            .. attribute:: neighbor_id  (key)
                            
                            	BGP RD neighbor ID
                            	**type**\: str
                            
                            .. attribute:: bgp_rd_neighbor_route_filters
                            
                            	BGP RD neighbor route filters
                            	**type**\:  :py:class:`BgpRdNeighborRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters>`
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-09-25'

                            def __init__(self):
                                super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor, self).__init__()

                                self.yang_name = "bgp-rd-route-neighbor"
                                self.yang_parent_name = "bgp-rd-route-neighbors"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['neighbor_id']
                                self._child_container_classes = OrderedDict([("bgp-rd-neighbor-route-filters", ("bgp_rd_neighbor_route_filters", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters))])
                                self._child_list_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('neighbor_id', YLeaf(YType.str, 'neighbor-id')),
                                ])
                                self.neighbor_id = None

                                self.bgp_rd_neighbor_route_filters = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters()
                                self.bgp_rd_neighbor_route_filters.parent = self
                                self._children_name_map["bgp_rd_neighbor_route_filters"] = "bgp-rd-neighbor-route-filters"
                                self._children_yang_names.add("bgp-rd-neighbor-route-filters")
                                self._segment_path = lambda: "bgp-rd-route-neighbor" + "[neighbor-id='" + str(self.neighbor_id) + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor, ['neighbor_id'], name, value)


                            class BgpRdNeighborRouteFilters(Entity):
                                """
                                BGP RD neighbor route filters
                                
                                .. attribute:: bgp_rd_neighbor_route_filter
                                
                                	List of BGP RD neighbor route filters
                                	**type**\: list of  		 :py:class:`BgpRdNeighborRouteFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter>`
                                
                                

                                """

                                _prefix = 'bgp-ios-xe-oper'
                                _revision = '2017-09-25'

                                def __init__(self):
                                    super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters, self).__init__()

                                    self.yang_name = "bgp-rd-neighbor-route-filters"
                                    self.yang_parent_name = "bgp-rd-route-neighbor"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_container_classes = OrderedDict([])
                                    self._child_list_classes = OrderedDict([("bgp-rd-neighbor-route-filter", ("bgp_rd_neighbor_route_filter", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter))])
                                    self._leafs = OrderedDict()

                                    self.bgp_rd_neighbor_route_filter = YList(self)
                                    self._segment_path = lambda: "bgp-rd-neighbor-route-filters"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters, [], name, value)


                                class BgpRdNeighborRouteFilter(Entity):
                                    """
                                    List of BGP RD neighbor route filters
                                    
                                    .. attribute:: neighbor_filter  (key)
                                    
                                    	BGP RD neighbor route filter
                                    	**type**\:  :py:class:`BgpNeighborRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpNeighborRouteFilters>`
                                    
                                    .. attribute:: bgp_rd_neighbor_route_entries
                                    
                                    	BGP RD neighbor route entries
                                    	**type**\:  :py:class:`BgpRdNeighborRouteEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries>`
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-09-25'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter, self).__init__()

                                        self.yang_name = "bgp-rd-neighbor-route-filter"
                                        self.yang_parent_name = "bgp-rd-neighbor-route-filters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = ['neighbor_filter']
                                        self._child_container_classes = OrderedDict([("bgp-rd-neighbor-route-entries", ("bgp_rd_neighbor_route_entries", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries))])
                                        self._child_list_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('neighbor_filter', YLeaf(YType.enumeration, 'neighbor-filter')),
                                        ])
                                        self.neighbor_filter = None

                                        self.bgp_rd_neighbor_route_entries = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries()
                                        self.bgp_rd_neighbor_route_entries.parent = self
                                        self._children_name_map["bgp_rd_neighbor_route_entries"] = "bgp-rd-neighbor-route-entries"
                                        self._children_yang_names.add("bgp-rd-neighbor-route-entries")
                                        self._segment_path = lambda: "bgp-rd-neighbor-route-filter" + "[neighbor-filter='" + str(self.neighbor_filter) + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter, ['neighbor_filter'], name, value)


                                    class BgpRdNeighborRouteEntries(Entity):
                                        """
                                        BGP RD neighbor route entries
                                        
                                        .. attribute:: bgp_rd_neighbor_route_entry
                                        
                                        	List of BGP RD neighbor route entries
                                        	**type**\: list of  		 :py:class:`BgpRdNeighborRouteEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry>`
                                        
                                        

                                        """

                                        _prefix = 'bgp-ios-xe-oper'
                                        _revision = '2017-09-25'

                                        def __init__(self):
                                            super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries, self).__init__()

                                            self.yang_name = "bgp-rd-neighbor-route-entries"
                                            self.yang_parent_name = "bgp-rd-neighbor-route-filter"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_container_classes = OrderedDict([])
                                            self._child_list_classes = OrderedDict([("bgp-rd-neighbor-route-entry", ("bgp_rd_neighbor_route_entry", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry))])
                                            self._leafs = OrderedDict()

                                            self.bgp_rd_neighbor_route_entry = YList(self)
                                            self._segment_path = lambda: "bgp-rd-neighbor-route-entries"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries, [], name, value)


                                        class BgpRdNeighborRouteEntry(Entity):
                                            """
                                            List of BGP RD neighbor route entries
                                            
                                            .. attribute:: prefix  (key)
                                            
                                            	RD neighbor routing table entry prefix
                                            	**type**\: str
                                            
                                            .. attribute:: version
                                            
                                            	RD neighbor routing table version
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: available_paths
                                            
                                            	Number of  paths available for BGP prefix
                                            	**type**\: int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: advertised_to
                                            
                                            	Who this prefix was advertized to
                                            	**type**\: str
                                            
                                            .. attribute:: bgp_rd_neighbor_path_entries
                                            
                                            	Prefix next hop details
                                            	**type**\:  :py:class:`BgpRdNeighborPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries>`
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-09-25'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry, self).__init__()

                                                self.yang_name = "bgp-rd-neighbor-route-entry"
                                                self.yang_parent_name = "bgp-rd-neighbor-route-entries"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self.ylist_key_names = ['prefix']
                                                self._child_container_classes = OrderedDict([("bgp-rd-neighbor-path-entries", ("bgp_rd_neighbor_path_entries", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries))])
                                                self._child_list_classes = OrderedDict([])
                                                self._leafs = OrderedDict([
                                                    ('prefix', YLeaf(YType.str, 'prefix')),
                                                    ('version', YLeaf(YType.uint32, 'version')),
                                                    ('available_paths', YLeaf(YType.uint32, 'available-paths')),
                                                    ('advertised_to', YLeaf(YType.str, 'advertised-to')),
                                                ])
                                                self.prefix = None
                                                self.version = None
                                                self.available_paths = None
                                                self.advertised_to = None

                                                self.bgp_rd_neighbor_path_entries = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries()
                                                self.bgp_rd_neighbor_path_entries.parent = self
                                                self._children_name_map["bgp_rd_neighbor_path_entries"] = "bgp-rd-neighbor-path-entries"
                                                self._children_yang_names.add("bgp-rd-neighbor-path-entries")
                                                self._segment_path = lambda: "bgp-rd-neighbor-route-entry" + "[prefix='" + str(self.prefix) + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry, ['prefix', 'version', 'available_paths', 'advertised_to'], name, value)


                                            class BgpRdNeighborPathEntries(Entity):
                                                """
                                                Prefix next hop details
                                                
                                                .. attribute:: bgp_rd_neighbor_path_entry
                                                
                                                	List of prefix next hop details
                                                	**type**\: list of  		 :py:class:`BgpRdNeighborPathEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-09-25'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries, self).__init__()

                                                    self.yang_name = "bgp-rd-neighbor-path-entries"
                                                    self.yang_parent_name = "bgp-rd-neighbor-route-entry"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self.ylist_key_names = []
                                                    self._child_container_classes = OrderedDict([])
                                                    self._child_list_classes = OrderedDict([("bgp-rd-neighbor-path-entry", ("bgp_rd_neighbor_path_entry", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry))])
                                                    self._leafs = OrderedDict()

                                                    self.bgp_rd_neighbor_path_entry = YList(self)
                                                    self._segment_path = lambda: "bgp-rd-neighbor-path-entries"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries, [], name, value)


                                                class BgpRdNeighborPathEntry(Entity):
                                                    """
                                                    List of prefix next hop details
                                                    
                                                    .. attribute:: nexthop  (key)
                                                    
                                                    	Next hop for this path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: metric
                                                    
                                                    	Metric associated with the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: local_pref
                                                    
                                                    	Local preference for this path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: weight
                                                    
                                                    	Path weight
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: as_path
                                                    
                                                    	AS path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: origin
                                                    
                                                    	Path origin
                                                    	**type**\:  :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                                    
                                                    .. attribute:: path_status
                                                    
                                                    	Path status
                                                    	**type**\:  :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry.PathStatus>`
                                                    
                                                    .. attribute:: rpki_status
                                                    
                                                    	RPKI path status
                                                    	**type**\:  :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                                    
                                                    .. attribute:: community
                                                    
                                                    	Community label for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: mpls_in
                                                    
                                                    	MPLS label in for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: mpls_out
                                                    
                                                    	MPLS label out for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: sr_profile_name
                                                    
                                                    	SR profile name for the path
                                                    	**type**\: str
                                                    
                                                    .. attribute:: sr_binding_sid
                                                    
                                                    	SR binding sid for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: sr_label_indx
                                                    
                                                    	SR label index for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: as4_path
                                                    
                                                    	path using 4\-octet AS numbers
                                                    	**type**\: str
                                                    
                                                    .. attribute:: atomic_aggregate
                                                    
                                                    	attribute indicating whether or not the prefix is an atomic aggregate
                                                    	**type**\: bool
                                                    
                                                    .. attribute:: aggr_as_number
                                                    
                                                    	AS number of autonomous system them performed the aggregation
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: aggr_as4_number
                                                    
                                                    	AS4 number of autonomous system them performed the aggregation
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    .. attribute:: aggr_address
                                                    
                                                    	IP address of the router that performed the aggregation
                                                    	**type**\: str
                                                    
                                                    .. attribute:: originator_id
                                                    
                                                    	the router ID of the originator of the route in the local AS
                                                    	**type**\: str
                                                    
                                                    .. attribute:: cluster_list
                                                    
                                                    	the reflection path the route has passed
                                                    	**type**\: str
                                                    
                                                    .. attribute:: extended_community
                                                    
                                                    	BGP extended community attribute
                                                    	**type**\: str
                                                    
                                                    .. attribute:: ext_aigp_metric
                                                    
                                                    	the accumulated IGP metric for the path
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..18446744073709551615
                                                    
                                                    .. attribute:: path_id
                                                    
                                                    	path identifier used to uniquely identify a route
                                                    	**type**\: int
                                                    
                                                    	**range:** 0..4294967295
                                                    
                                                    

                                                    """

                                                    _prefix = 'bgp-ios-xe-oper'
                                                    _revision = '2017-09-25'

                                                    def __init__(self):
                                                        super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry, self).__init__()

                                                        self.yang_name = "bgp-rd-neighbor-path-entry"
                                                        self.yang_parent_name = "bgp-rd-neighbor-path-entries"
                                                        self.is_top_level_class = False
                                                        self.has_list_ancestor = True
                                                        self.ylist_key_names = ['nexthop']
                                                        self._child_container_classes = OrderedDict([("path-status", ("path_status", BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry.PathStatus))])
                                                        self._child_list_classes = OrderedDict([])
                                                        self._leafs = OrderedDict([
                                                            ('nexthop', YLeaf(YType.str, 'nexthop')),
                                                            ('metric', YLeaf(YType.uint32, 'metric')),
                                                            ('local_pref', YLeaf(YType.uint32, 'local-pref')),
                                                            ('weight', YLeaf(YType.uint32, 'weight')),
                                                            ('as_path', YLeaf(YType.str, 'as-path')),
                                                            ('origin', YLeaf(YType.enumeration, 'origin')),
                                                            ('rpki_status', YLeaf(YType.enumeration, 'rpki-status')),
                                                            ('community', YLeaf(YType.str, 'community')),
                                                            ('mpls_in', YLeaf(YType.str, 'mpls-in')),
                                                            ('mpls_out', YLeaf(YType.str, 'mpls-out')),
                                                            ('sr_profile_name', YLeaf(YType.str, 'sr-profile-name')),
                                                            ('sr_binding_sid', YLeaf(YType.uint32, 'sr-binding-sid')),
                                                            ('sr_label_indx', YLeaf(YType.uint32, 'sr-label-indx')),
                                                            ('as4_path', YLeaf(YType.str, 'as4-path')),
                                                            ('atomic_aggregate', YLeaf(YType.boolean, 'atomic-aggregate')),
                                                            ('aggr_as_number', YLeaf(YType.uint32, 'aggr-as-number')),
                                                            ('aggr_as4_number', YLeaf(YType.uint32, 'aggr-as4-number')),
                                                            ('aggr_address', YLeaf(YType.str, 'aggr-address')),
                                                            ('originator_id', YLeaf(YType.str, 'originator-id')),
                                                            ('cluster_list', YLeaf(YType.str, 'cluster-list')),
                                                            ('extended_community', YLeaf(YType.str, 'extended-community')),
                                                            ('ext_aigp_metric', YLeaf(YType.uint64, 'ext-aigp-metric')),
                                                            ('path_id', YLeaf(YType.uint32, 'path-id')),
                                                        ])
                                                        self.nexthop = None
                                                        self.metric = None
                                                        self.local_pref = None
                                                        self.weight = None
                                                        self.as_path = None
                                                        self.origin = None
                                                        self.rpki_status = None
                                                        self.community = None
                                                        self.mpls_in = None
                                                        self.mpls_out = None
                                                        self.sr_profile_name = None
                                                        self.sr_binding_sid = None
                                                        self.sr_label_indx = None
                                                        self.as4_path = None
                                                        self.atomic_aggregate = None
                                                        self.aggr_as_number = None
                                                        self.aggr_as4_number = None
                                                        self.aggr_address = None
                                                        self.originator_id = None
                                                        self.cluster_list = None
                                                        self.extended_community = None
                                                        self.ext_aigp_metric = None
                                                        self.path_id = None

                                                        self.path_status = BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry.PathStatus()
                                                        self.path_status.parent = self
                                                        self._children_name_map["path_status"] = "path-status"
                                                        self._children_yang_names.add("path-status")
                                                        self._segment_path = lambda: "bgp-rd-neighbor-path-entry" + "[nexthop='" + str(self.nexthop) + "']"

                                                    def __setattr__(self, name, value):
                                                        self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry, ['nexthop', 'metric', 'local_pref', 'weight', 'as_path', 'origin', 'rpki_status', 'community', 'mpls_in', 'mpls_out', 'sr_profile_name', 'sr_binding_sid', 'sr_label_indx', 'as4_path', 'atomic_aggregate', 'aggr_as_number', 'aggr_as4_number', 'aggr_address', 'originator_id', 'cluster_list', 'extended_community', 'ext_aigp_metric', 'path_id'], name, value)


                                                    class PathStatus(Entity):
                                                        """
                                                        Path status
                                                        
                                                        .. attribute:: suppressed
                                                        
                                                        	Suppressed path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: damped
                                                        
                                                        	Damped path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: history
                                                        
                                                        	History path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: valid
                                                        
                                                        	Valid path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: sourced
                                                        
                                                        	Sourced path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: bestpath
                                                        
                                                        	Best path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: internal
                                                        
                                                        	Internal path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rib_fail
                                                        
                                                        	RIB\-fail path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: stale
                                                        
                                                        	Stale path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: multipath
                                                        
                                                        	Multipath path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: backup_path
                                                        
                                                        	Backup path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rt_filter
                                                        
                                                        	RT filter path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: best_external
                                                        
                                                        	Best externa path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: additional_path
                                                        
                                                        	Additional path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        .. attribute:: rib_compressed
                                                        
                                                        	RIB compressed path
                                                        	**type**\: :py:class:`Empty<ydk.types.Empty>`
                                                        
                                                        

                                                        """

                                                        _prefix = 'bgp-ios-xe-oper'
                                                        _revision = '2017-09-25'

                                                        def __init__(self):
                                                            super(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry.PathStatus, self).__init__()

                                                            self.yang_name = "path-status"
                                                            self.yang_parent_name = "bgp-rd-neighbor-path-entry"
                                                            self.is_top_level_class = False
                                                            self.has_list_ancestor = True
                                                            self.ylist_key_names = []
                                                            self._child_container_classes = OrderedDict([])
                                                            self._child_list_classes = OrderedDict([])
                                                            self._leafs = OrderedDict([
                                                                ('suppressed', YLeaf(YType.empty, 'suppressed')),
                                                                ('damped', YLeaf(YType.empty, 'damped')),
                                                                ('history', YLeaf(YType.empty, 'history')),
                                                                ('valid', YLeaf(YType.empty, 'valid')),
                                                                ('sourced', YLeaf(YType.empty, 'sourced')),
                                                                ('bestpath', YLeaf(YType.empty, 'bestpath')),
                                                                ('internal', YLeaf(YType.empty, 'internal')),
                                                                ('rib_fail', YLeaf(YType.empty, 'rib-fail')),
                                                                ('stale', YLeaf(YType.empty, 'stale')),
                                                                ('multipath', YLeaf(YType.empty, 'multipath')),
                                                                ('backup_path', YLeaf(YType.empty, 'backup-path')),
                                                                ('rt_filter', YLeaf(YType.empty, 'rt-filter')),
                                                                ('best_external', YLeaf(YType.empty, 'best-external')),
                                                                ('additional_path', YLeaf(YType.empty, 'additional-path')),
                                                                ('rib_compressed', YLeaf(YType.empty, 'rib-compressed')),
                                                            ])
                                                            self.suppressed = None
                                                            self.damped = None
                                                            self.history = None
                                                            self.valid = None
                                                            self.sourced = None
                                                            self.bestpath = None
                                                            self.internal = None
                                                            self.rib_fail = None
                                                            self.stale = None
                                                            self.multipath = None
                                                            self.backup_path = None
                                                            self.rt_filter = None
                                                            self.best_external = None
                                                            self.additional_path = None
                                                            self.rib_compressed = None
                                                            self._segment_path = lambda: "path-status"

                                                        def __setattr__(self, name, value):
                                                            self._perform_setattr(BgpStateData.BgpRouteRds.BgpRouteRd.BgpRdRouteAfs.BgpRdRouteAf.BgpRdRouteNeighbors.BgpRdRouteNeighbor.BgpRdNeighborRouteFilters.BgpRdNeighborRouteFilter.BgpRdNeighborRouteEntries.BgpRdNeighborRouteEntry.BgpRdNeighborPathEntries.BgpRdNeighborPathEntry.PathStatus, ['suppressed', 'damped', 'history', 'valid', 'sourced', 'bestpath', 'internal', 'rib_fail', 'stale', 'multipath', 'backup_path', 'rt_filter', 'best_external', 'additional_path', 'rib_compressed'], name, value)

    def clone_ptr(self):
        self._top_entity = BgpStateData()
        return self._top_entity

