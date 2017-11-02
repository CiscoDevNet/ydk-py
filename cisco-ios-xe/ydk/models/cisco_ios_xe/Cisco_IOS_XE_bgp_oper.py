""" Cisco_IOS_XE_bgp_oper 

This module contains a collection of YANG definitions
for bgp operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class BgpFsmState(Enum):
    """
    BgpFsmState

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
    BgpLink

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
    BgpMode

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
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors>`
    
    .. attribute:: address_families
    
    	BGP address family
    	**type**\:   :py:class:`AddressFamilies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies>`
    
    .. attribute:: bgp_route_vrfs
    
    	BGP VRFs
    	**type**\:   :py:class:`BgpRouteVrfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs>`
    
    

    """

    _prefix = 'bgp-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(BgpStateData, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp-state-data"
        self.yang_parent_name = "Cisco-IOS-XE-bgp-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"neighbors" : ("neighbors", BgpStateData.Neighbors), "address-families" : ("address_families", BgpStateData.AddressFamilies), "bgp-route-vrfs" : ("bgp_route_vrfs", BgpStateData.BgpRouteVrfs)}
        self._child_list_classes = {}

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
        self._segment_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data"


    class Neighbors(Entity):
        """
        BGP neighbor information
        
        .. attribute:: neighbor
        
        	List of BGP neighbors
        	**type**\: list of    :py:class:`Neighbor <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(BgpStateData.Neighbors, self).__init__()

            self.yang_name = "neighbors"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"neighbor" : ("neighbor", BgpStateData.Neighbors.Neighbor)}

            self.neighbor = YList(self)
            self._segment_path = lambda: "neighbors"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.Neighbors, [], name, value)


        class Neighbor(Entity):
            """
            List of BGP neighbors
            
            .. attribute:: afi_safi  <key>
            
            	Afi\-safi key
            	**type**\:   :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: neighbor_id  <key>
            
            	Neighbor identifier
            	**type**\:  str
            
            .. attribute:: description
            
            	Neighbor description string
            	**type**\:  str
            
            .. attribute:: bgp_version
            
            	BGP version being used to communicate with the remote router
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: link
            
            	Neighbor link type
            	**type**\:   :py:class:`BgpLink <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpLink>`
            
            .. attribute:: up_time
            
            	Amout of time the bgp session has been up since being established
            	**type**\:  str
            
            .. attribute:: last_write
            
            	Time since BGP last sent a message to the neighbor
            	**type**\:  str
            
            .. attribute:: last_read
            
            	Time since BGP last received a message from the neighbor
            	**type**\:  str
            
            .. attribute:: installed_prefixes
            
            	The number of installed prefixes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: session_state
            
            	BGP neighbor session state
            	**type**\:   :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
            
            .. attribute:: negotiated_keepalive_timers
            
            	Negotiated keepalive timers status of BGP neighbor
            	**type**\:   :py:class:`NegotiatedKeepaliveTimers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers>`
            
            .. attribute:: negotiated_cap
            
            	Negotiated capabilities for neighbor session
            	**type**\:  list of str
            
            .. attribute:: bgp_neighbor_counters
            
            	BGP neighbor session counters
            	**type**\:   :py:class:`BgpNeighborCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters>`
            
            .. attribute:: connection
            
            	BGP neighbor connection
            	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Connection>`
            
            .. attribute:: transport
            
            	BGP neighbor transport
            	**type**\:   :py:class:`Transport <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Transport>`
            
            .. attribute:: prefix_activity
            
            	BGP neighbor activity
            	**type**\:   :py:class:`PrefixActivity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity>`
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(BgpStateData.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"negotiated-keepalive-timers" : ("negotiated_keepalive_timers", BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers), "bgp-neighbor-counters" : ("bgp_neighbor_counters", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters), "connection" : ("connection", BgpStateData.Neighbors.Neighbor.Connection), "transport" : ("transport", BgpStateData.Neighbors.Neighbor.Transport), "prefix-activity" : ("prefix_activity", BgpStateData.Neighbors.Neighbor.PrefixActivity)}
                self._child_list_classes = {}

                self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                self.description = YLeaf(YType.str, "description")

                self.bgp_version = YLeaf(YType.uint16, "bgp-version")

                self.link = YLeaf(YType.enumeration, "link")

                self.up_time = YLeaf(YType.str, "up-time")

                self.last_write = YLeaf(YType.str, "last-write")

                self.last_read = YLeaf(YType.str, "last-read")

                self.installed_prefixes = YLeaf(YType.uint32, "installed-prefixes")

                self.session_state = YLeaf(YType.enumeration, "session-state")

                self.negotiated_cap = YLeafList(YType.str, "negotiated-cap")

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
                self._segment_path = lambda: "neighbor" + "[afi-safi='" + self.afi_safi.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + "[neighbor-id='" + self.neighbor_id.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/neighbors/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.Neighbors.Neighbor, ['afi_safi', 'vrf_name', 'neighbor_id', 'description', 'bgp_version', 'link', 'up_time', 'last_write', 'last_read', 'installed_prefixes', 'session_state', 'negotiated_cap'], name, value)


            class NegotiatedKeepaliveTimers(Entity):
                """
                Negotiated keepalive timers status of BGP neighbor
                
                .. attribute:: hold_time
                
                	Hold time
                	**type**\:  int
                
                	**range:** 0..65535
                
                .. attribute:: keepalive_interval
                
                	Keepalive interval
                	**type**\:  int
                
                	**range:** 0..65535
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, self).__init__()

                    self.yang_name = "negotiated-keepalive-timers"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.hold_time = YLeaf(YType.uint16, "hold-time")

                    self.keepalive_interval = YLeaf(YType.uint16, "keepalive-interval")
                    self._segment_path = lambda: "negotiated-keepalive-timers"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, ['hold_time', 'keepalive_interval'], name, value)


            class BgpNeighborCounters(Entity):
                """
                BGP neighbor session counters
                
                .. attribute:: sent
                
                	Number of mesaged sent
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent>`
                
                .. attribute:: received
                
                	Number of mesaged received
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received>`
                
                .. attribute:: inq_depth
                
                	Input Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: outq_depth
                
                	Output Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, self).__init__()

                    self.yang_name = "bgp-neighbor-counters"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"sent" : ("sent", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent), "received" : ("received", BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received)}
                    self._child_list_classes = {}

                    self.inq_depth = YLeaf(YType.uint32, "inq-depth")

                    self.outq_depth = YLeaf(YType.uint32, "outq-depth")

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
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "bgp-neighbor-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.updates = YLeaf(YType.uint32, "updates")

                        self.notifications = YLeaf(YType.uint32, "notifications")

                        self.keepalives = YLeaf(YType.uint32, "keepalives")

                        self.route_refreshes = YLeaf(YType.uint32, "route-refreshes")
                        self._segment_path = lambda: "sent"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, ['opens', 'updates', 'notifications', 'keepalives', 'route_refreshes'], name, value)


                class Received(Entity):
                    """
                    Number of mesaged received
                    
                    .. attribute:: opens
                    
                    	OPEN message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "bgp-neighbor-counters"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.updates = YLeaf(YType.uint32, "updates")

                        self.notifications = YLeaf(YType.uint32, "notifications")

                        self.keepalives = YLeaf(YType.uint32, "keepalives")

                        self.route_refreshes = YLeaf(YType.uint32, "route-refreshes")
                        self._segment_path = lambda: "received"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, ['opens', 'updates', 'notifications', 'keepalives', 'route_refreshes'], name, value)


            class Connection(Entity):
                """
                BGP neighbor connection
                
                .. attribute:: state
                
                	TCP FSM state
                	**type**\:   :py:class:`TcpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.TcpFsmState>`
                
                .. attribute:: mode
                
                	BGP transport connection mode
                	**type**\:   :py:class:`BgpMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpMode>`
                
                .. attribute:: total_established
                
                	The number of times a TCP and BGP  connection has been successfully established
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_dropped
                
                	The number of times that a valid session has failed or been taken down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: last_reset
                
                	Time since peering session was last reset
                	**type**\:  str
                
                .. attribute:: reset_reason
                
                	The reason for the last reset
                	**type**\:  str
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Connection, self).__init__()

                    self.yang_name = "connection"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.state = YLeaf(YType.enumeration, "state")

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.total_established = YLeaf(YType.uint32, "total-established")

                    self.total_dropped = YLeaf(YType.uint32, "total-dropped")

                    self.last_reset = YLeaf(YType.str, "last-reset")

                    self.reset_reason = YLeaf(YType.str, "reset-reason")
                    self._segment_path = lambda: "connection"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.Connection, ['state', 'mode', 'total_established', 'total_dropped', 'last_reset', 'reset_reason'], name, value)


            class Transport(Entity):
                """
                BGP neighbor transport
                
                .. attribute:: path_mtu_discovery
                
                	Indication whether path MTU discovrey is enabled
                	**type**\:  bool
                
                .. attribute:: local_port
                
                	Local TCP port used for TCP session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: local_host
                
                	Local address used for the TCP session
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                
                ----
                	**type**\:  str
                
                
                ----
                .. attribute:: foreign_port
                
                	Remote port used by the peer for the TCP session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: foreign_host
                
                	Remote address of the BGP session
                	**type**\: one of the below types:
                
                	**type**\:  str
                
                
                ----
                	**type**\:  str
                
                
                ----
                .. attribute:: mss
                
                	Maximum Data segment size
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.path_mtu_discovery = YLeaf(YType.boolean, "path-mtu-discovery")

                    self.local_port = YLeaf(YType.uint32, "local-port")

                    self.local_host = YLeaf(YType.str, "local-host")

                    self.foreign_port = YLeaf(YType.uint32, "foreign-port")

                    self.foreign_host = YLeaf(YType.str, "foreign-host")

                    self.mss = YLeaf(YType.uint32, "mss")
                    self._segment_path = lambda: "transport"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.Neighbors.Neighbor.Transport, ['path_mtu_discovery', 'local_port', 'local_host', 'foreign_port', 'foreign_host', 'mss'], name, value)


            class PrefixActivity(Entity):
                """
                BGP neighbor activity
                
                .. attribute:: sent
                
                	Number of prefixes sent
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent>`
                
                .. attribute:: received
                
                	Number of prefixes received
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Received>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.PrefixActivity, self).__init__()

                    self.yang_name = "prefix-activity"
                    self.yang_parent_name = "neighbor"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {"sent" : ("sent", BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent), "received" : ("received", BgpStateData.Neighbors.Neighbor.PrefixActivity.Received)}
                    self._child_list_classes = {}

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
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "prefix-activity"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.current_prefixes = YLeaf(YType.uint64, "current-prefixes")

                        self.total_prefixes = YLeaf(YType.uint64, "total-prefixes")

                        self.implicit_withdraw = YLeaf(YType.uint64, "implicit-withdraw")

                        self.explicit_withdraw = YLeaf(YType.uint64, "explicit-withdraw")

                        self.bestpaths = YLeaf(YType.uint64, "bestpaths")

                        self.multipaths = YLeaf(YType.uint64, "multipaths")
                        self._segment_path = lambda: "sent"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, ['current_prefixes', 'total_prefixes', 'implicit_withdraw', 'explicit_withdraw', 'bestpaths', 'multipaths'], name, value)


                class Received(Entity):
                    """
                    Number of prefixes received
                    
                    .. attribute:: current_prefixes
                    
                    	The current number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "prefix-activity"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.current_prefixes = YLeaf(YType.uint64, "current-prefixes")

                        self.total_prefixes = YLeaf(YType.uint64, "total-prefixes")

                        self.implicit_withdraw = YLeaf(YType.uint64, "implicit-withdraw")

                        self.explicit_withdraw = YLeaf(YType.uint64, "explicit-withdraw")

                        self.bestpaths = YLeaf(YType.uint64, "bestpaths")

                        self.multipaths = YLeaf(YType.uint64, "multipaths")
                        self._segment_path = lambda: "received"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, ['current_prefixes', 'total_prefixes', 'implicit_withdraw', 'explicit_withdraw', 'bestpaths', 'multipaths'], name, value)


    class AddressFamilies(Entity):
        """
        BGP address family
        
        .. attribute:: address_family
        
        	List of BGP address families
        	**type**\: list of    :py:class:`AddressFamily <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(BgpStateData.AddressFamilies, self).__init__()

            self.yang_name = "address-families"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"address-family" : ("address_family", BgpStateData.AddressFamilies.AddressFamily)}

            self.address_family = YList(self)
            self._segment_path = lambda: "address-families"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.AddressFamilies, [], name, value)


        class AddressFamily(Entity):
            """
            List of BGP address families
            
            .. attribute:: afi_safi  <key>
            
            	Afi\-safi value
            	**type**\:   :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: router_id
            
            	Router ID
            	**type**\: one of the below types:
            
            	**type**\:  str
            
            
            ----
            	**type**\:  str
            
            
            ----
            .. attribute:: bgp_table_version
            
            	BGP table version number
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: routing_table_version
            
            	Routing table version number
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: prefixes
            
            	Prefix entry statistics
            	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Prefixes>`
            
            .. attribute:: path
            
            	Path entry statistics
            	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Path>`
            
            .. attribute:: as_path
            
            	AS path entry statistics
            	**type**\:   :py:class:`AsPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.AsPath>`
            
            .. attribute:: route_map
            
            	Route map entry statistics
            	**type**\:   :py:class:`RouteMap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.RouteMap>`
            
            .. attribute:: filter_list
            
            	Filter list entry statistics
            	**type**\:   :py:class:`FilterList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.FilterList>`
            
            .. attribute:: activities
            
            	BGP activity information
            	**type**\:   :py:class:`Activities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Activities>`
            
            .. attribute:: total_memory
            
            	Total memory in use
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: bgp_neighbor_summaries
            
            	Neighbor summary
            	**type**\:   :py:class:`BgpNeighborSummaries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries>`
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(BgpStateData.AddressFamilies.AddressFamily, self).__init__()

                self.yang_name = "address-family"
                self.yang_parent_name = "address-families"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"prefixes" : ("prefixes", BgpStateData.AddressFamilies.AddressFamily.Prefixes), "path" : ("path", BgpStateData.AddressFamilies.AddressFamily.Path), "as-path" : ("as_path", BgpStateData.AddressFamilies.AddressFamily.AsPath), "route-map" : ("route_map", BgpStateData.AddressFamilies.AddressFamily.RouteMap), "filter-list" : ("filter_list", BgpStateData.AddressFamilies.AddressFamily.FilterList), "activities" : ("activities", BgpStateData.AddressFamilies.AddressFamily.Activities), "bgp-neighbor-summaries" : ("bgp_neighbor_summaries", BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries)}
                self._child_list_classes = {}

                self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.router_id = YLeaf(YType.str, "router-id")

                self.bgp_table_version = YLeaf(YType.uint64, "bgp-table-version")

                self.routing_table_version = YLeaf(YType.uint64, "routing-table-version")

                self.total_memory = YLeaf(YType.uint64, "total-memory")

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
                self._segment_path = lambda: "address-family" + "[afi-safi='" + self.afi_safi.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/address-families/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily, ['afi_safi', 'vrf_name', 'router_id', 'bgp_table_version', 'routing_table_version', 'total_memory'], name, value)


            class Prefixes(Entity):
                """
                Prefix entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Prefixes, self).__init__()

                    self.yang_name = "prefixes"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")
                    self._segment_path = lambda: "prefixes"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Prefixes, ['total_entries', 'memory_usage'], name, value)


            class Path(Entity):
                """
                Path entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Path, self).__init__()

                    self.yang_name = "path"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")
                    self._segment_path = lambda: "path"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Path, ['total_entries', 'memory_usage'], name, value)


            class AsPath(Entity):
                """
                AS path entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.AsPath, self).__init__()

                    self.yang_name = "as-path"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")
                    self._segment_path = lambda: "as-path"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.AsPath, ['total_entries', 'memory_usage'], name, value)


            class RouteMap(Entity):
                """
                Route map entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.RouteMap, self).__init__()

                    self.yang_name = "route-map"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")
                    self._segment_path = lambda: "route-map"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.RouteMap, ['total_entries', 'memory_usage'], name, value)


            class FilterList(Entity):
                """
                Filter list entry statistics
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.FilterList, self).__init__()

                    self.yang_name = "filter-list"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")
                    self._segment_path = lambda: "filter-list"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.FilterList, ['total_entries', 'memory_usage'], name, value)


            class Activities(Entity):
                """
                BGP activity information
                
                .. attribute:: prefixes
                
                	Total number of prefixes
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: paths
                
                	Total number of paths
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: scan_interval
                
                	Scan interval in seconds
                	**type**\:  str
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Activities, self).__init__()

                    self.yang_name = "activities"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.prefixes = YLeaf(YType.uint64, "prefixes")

                    self.paths = YLeaf(YType.uint64, "paths")

                    self.scan_interval = YLeaf(YType.str, "scan-interval")
                    self._segment_path = lambda: "activities"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.Activities, ['prefixes', 'paths', 'scan_interval'], name, value)


            class BgpNeighborSummaries(Entity):
                """
                Neighbor summary
                
                .. attribute:: bgp_neighbor_summary
                
                	List of neighbor summaries
                	**type**\: list of    :py:class:`BgpNeighborSummary <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, self).__init__()

                    self.yang_name = "bgp-neighbor-summaries"
                    self.yang_parent_name = "address-family"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bgp-neighbor-summary" : ("bgp_neighbor_summary", BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary)}

                    self.bgp_neighbor_summary = YList(self)
                    self._segment_path = lambda: "bgp-neighbor-summaries"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, [], name, value)


                class BgpNeighborSummary(Entity):
                    """
                    List of neighbor summaries
                    
                    .. attribute:: id  <key>
                    
                    	Neighbor address
                    	**type**\:  str
                    
                    .. attribute:: bgp_version
                    
                    	BGP protocol version
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: messages_received
                    
                    	Number of messages received from this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_sent
                    
                    	Number of messages sent to this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: table_version
                    
                    	BGP table version
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: input_queue
                    
                    	Number of messages in input queue
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_queue
                    
                    	Number of messages in output queue
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: up_time
                    
                    	Neighbor session uptime
                    	**type**\:  str
                    
                    .. attribute:: state
                    
                    	BGP session state
                    	**type**\:   :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
                    
                    .. attribute:: prefixes_received
                    
                    	Number of prefixes received from the neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: dynamically_configured
                    
                    	Indication of whether the neighbor was dyanmically configured
                    	**type**\:  bool
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, self).__init__()

                        self.yang_name = "bgp-neighbor-summary"
                        self.yang_parent_name = "bgp-neighbor-summaries"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {}
                        self._child_list_classes = {}

                        self.id = YLeaf(YType.str, "id")

                        self.bgp_version = YLeaf(YType.uint32, "bgp-version")

                        self.messages_received = YLeaf(YType.uint64, "messages-received")

                        self.messages_sent = YLeaf(YType.uint64, "messages-sent")

                        self.table_version = YLeaf(YType.uint64, "table-version")

                        self.input_queue = YLeaf(YType.uint64, "input-queue")

                        self.output_queue = YLeaf(YType.uint64, "output-queue")

                        self.up_time = YLeaf(YType.str, "up-time")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.prefixes_received = YLeaf(YType.uint64, "prefixes-received")

                        self.dynamically_configured = YLeaf(YType.boolean, "dynamically-configured")
                        self._segment_path = lambda: "bgp-neighbor-summary" + "[id='" + self.id.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, ['id', 'bgp_version', 'messages_received', 'messages_sent', 'table_version', 'input_queue', 'output_queue', 'up_time', 'state', 'prefixes_received', 'dynamically_configured'], name, value)


    class BgpRouteVrfs(Entity):
        """
        BGP VRFs
        
        .. attribute:: bgp_route_vrf
        
        	List of BGP VRFs
        	**type**\: list of    :py:class:`BgpRouteVrf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf>`
        
        

        """

        _prefix = 'bgp-ios-xe-oper'
        _revision = '2017-04-01'

        def __init__(self):
            super(BgpStateData.BgpRouteVrfs, self).__init__()

            self.yang_name = "bgp-route-vrfs"
            self.yang_parent_name = "bgp-state-data"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"bgp-route-vrf" : ("bgp_route_vrf", BgpStateData.BgpRouteVrfs.BgpRouteVrf)}

            self.bgp_route_vrf = YList(self)
            self._segment_path = lambda: "bgp-route-vrfs"
            self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(BgpStateData.BgpRouteVrfs, [], name, value)


        class BgpRouteVrf(Entity):
            """
            List of BGP VRFs
            
            .. attribute:: vrf  <key>
            
            	BGP vrf
            	**type**\:  str
            
            .. attribute:: bgp_route_afs
            
            	BGP address families
            	**type**\:   :py:class:`BgpRouteAfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs>`
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf, self).__init__()

                self.yang_name = "bgp-route-vrf"
                self.yang_parent_name = "bgp-route-vrfs"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"bgp-route-afs" : ("bgp_route_afs", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs)}
                self._child_list_classes = {}

                self.vrf = YLeaf(YType.str, "vrf")

                self.bgp_route_afs = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs()
                self.bgp_route_afs.parent = self
                self._children_name_map["bgp_route_afs"] = "bgp-route-afs"
                self._children_yang_names.add("bgp-route-afs")
                self._segment_path = lambda: "bgp-route-vrf" + "[vrf='" + self.vrf.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XE-bgp-oper:bgp-state-data/bgp-route-vrfs/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf, ['vrf'], name, value)


            class BgpRouteAfs(Entity):
                """
                BGP address families
                
                .. attribute:: bgp_route_af
                
                	List of BGP address families
                	**type**\: list of    :py:class:`BgpRouteAf <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, self).__init__()

                    self.yang_name = "bgp-route-afs"
                    self.yang_parent_name = "bgp-route-vrf"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"bgp-route-af" : ("bgp_route_af", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf)}

                    self.bgp_route_af = YList(self)
                    self._segment_path = lambda: "bgp-route-afs"

                def __setattr__(self, name, value):
                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, [], name, value)


                class BgpRouteAf(Entity):
                    """
                    List of BGP address families
                    
                    .. attribute:: afi_safi  <key>
                    
                    	BGP address family
                    	**type**\:   :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
                    
                    .. attribute:: bgp_route_filters
                    
                    	BGP route filters
                    	**type**\:   :py:class:`BgpRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters>`
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, self).__init__()

                        self.yang_name = "bgp-route-af"
                        self.yang_parent_name = "bgp-route-afs"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"bgp-route-filters" : ("bgp_route_filters", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters)}
                        self._child_list_classes = {}

                        self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                        self.bgp_route_filters = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters()
                        self.bgp_route_filters.parent = self
                        self._children_name_map["bgp_route_filters"] = "bgp-route-filters"
                        self._children_yang_names.add("bgp-route-filters")
                        self._segment_path = lambda: "bgp-route-af" + "[afi-safi='" + self.afi_safi.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, ['afi_safi'], name, value)


                    class BgpRouteFilters(Entity):
                        """
                        BGP route filters
                        
                        .. attribute:: bgp_route_filter
                        
                        	List of BGP route filters
                        	**type**\: list of    :py:class:`BgpRouteFilter <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter>`
                        
                        

                        """

                        _prefix = 'bgp-ios-xe-oper'
                        _revision = '2017-04-01'

                        def __init__(self):
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, self).__init__()

                            self.yang_name = "bgp-route-filters"
                            self.yang_parent_name = "bgp-route-af"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {"bgp-route-filter" : ("bgp_route_filter", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter)}

                            self.bgp_route_filter = YList(self)
                            self._segment_path = lambda: "bgp-route-filters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, [], name, value)


                        class BgpRouteFilter(Entity):
                            """
                            List of BGP route filters
                            
                            .. attribute:: route_filter  <key>
                            
                            	BGP route filter
                            	**type**\:   :py:class:`BgpRouteFilters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRouteFilters>`
                            
                            .. attribute:: bgp_route_entries
                            
                            	BGP route entries
                            	**type**\:   :py:class:`BgpRouteEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries>`
                            
                            

                            """

                            _prefix = 'bgp-ios-xe-oper'
                            _revision = '2017-04-01'

                            def __init__(self):
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, self).__init__()

                                self.yang_name = "bgp-route-filter"
                                self.yang_parent_name = "bgp-route-filters"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"bgp-route-entries" : ("bgp_route_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries)}
                                self._child_list_classes = {}

                                self.route_filter = YLeaf(YType.enumeration, "route-filter")

                                self.bgp_route_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries()
                                self.bgp_route_entries.parent = self
                                self._children_name_map["bgp_route_entries"] = "bgp-route-entries"
                                self._children_yang_names.add("bgp-route-entries")
                                self._segment_path = lambda: "bgp-route-filter" + "[route-filter='" + self.route_filter.get() + "']"

                            def __setattr__(self, name, value):
                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, ['route_filter'], name, value)


                            class BgpRouteEntries(Entity):
                                """
                                BGP route entries
                                
                                .. attribute:: bgp_route_entry
                                
                                	List of BGP route entries
                                	**type**\: list of    :py:class:`BgpRouteEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry>`
                                
                                

                                """

                                _prefix = 'bgp-ios-xe-oper'
                                _revision = '2017-04-01'

                                def __init__(self):
                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, self).__init__()

                                    self.yang_name = "bgp-route-entries"
                                    self.yang_parent_name = "bgp-route-filter"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {"bgp-route-entry" : ("bgp_route_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry)}

                                    self.bgp_route_entry = YList(self)
                                    self._segment_path = lambda: "bgp-route-entries"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, [], name, value)


                                class BgpRouteEntry(Entity):
                                    """
                                    List of BGP route entries
                                    
                                    .. attribute:: prefix  <key>
                                    
                                    	Routing table entry prefix
                                    	**type**\:  str
                                    
                                    .. attribute:: version
                                    
                                    	Routing table version
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: available_paths
                                    
                                    	Number of paths available for BGP prefix
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: advertised_to
                                    
                                    	Whom is thie prefix advertized to
                                    	**type**\:  str
                                    
                                    .. attribute:: bgp_path_entries
                                    
                                    	Prefix next hop details
                                    	**type**\:   :py:class:`BgpPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries>`
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-04-01'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, self).__init__()

                                        self.yang_name = "bgp-route-entry"
                                        self.yang_parent_name = "bgp-route-entries"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self._child_container_classes = {"bgp-path-entries" : ("bgp_path_entries", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries)}
                                        self._child_list_classes = {}

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.version = YLeaf(YType.uint32, "version")

                                        self.available_paths = YLeaf(YType.uint32, "available-paths")

                                        self.advertised_to = YLeaf(YType.str, "advertised-to")

                                        self.bgp_path_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries()
                                        self.bgp_path_entries.parent = self
                                        self._children_name_map["bgp_path_entries"] = "bgp-path-entries"
                                        self._children_yang_names.add("bgp-path-entries")
                                        self._segment_path = lambda: "bgp-route-entry" + "[prefix='" + self.prefix.get() + "']"

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, ['prefix', 'version', 'available_paths', 'advertised_to'], name, value)


                                    class BgpPathEntries(Entity):
                                        """
                                        Prefix next hop details
                                        
                                        .. attribute:: bgp_path_entry
                                        
                                        	List of prefix next hop details
                                        	**type**\: list of    :py:class:`BgpPathEntry <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry>`
                                        
                                        

                                        """

                                        _prefix = 'bgp-ios-xe-oper'
                                        _revision = '2017-04-01'

                                        def __init__(self):
                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, self).__init__()

                                            self.yang_name = "bgp-path-entries"
                                            self.yang_parent_name = "bgp-route-entry"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self._child_container_classes = {}
                                            self._child_list_classes = {"bgp-path-entry" : ("bgp_path_entry", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry)}

                                            self.bgp_path_entry = YList(self)
                                            self._segment_path = lambda: "bgp-path-entries"

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, [], name, value)


                                        class BgpPathEntry(Entity):
                                            """
                                            List of prefix next hop details
                                            
                                            .. attribute:: nexthop  <key>
                                            
                                            	Next hop for this path
                                            	**type**\:  str
                                            
                                            .. attribute:: metric
                                            
                                            	Metric associated with the path
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: local_pref
                                            
                                            	Local preference for this path
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: weight
                                            
                                            	Path weight
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: as_path
                                            
                                            	AS path
                                            	**type**\:  str
                                            
                                            .. attribute:: origin
                                            
                                            	Path origin
                                            	**type**\:   :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                            
                                            .. attribute:: path_status
                                            
                                            	Path status
                                            	**type**\:   :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus>`
                                            
                                            .. attribute:: rpki_status
                                            
                                            	RPKI path status
                                            	**type**\:   :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                            
                                            .. attribute:: community
                                            
                                            	Community label for the path
                                            	**type**\:  str
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-04-01'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, self).__init__()

                                                self.yang_name = "bgp-path-entry"
                                                self.yang_parent_name = "bgp-path-entries"
                                                self.is_top_level_class = False
                                                self.has_list_ancestor = True
                                                self._child_container_classes = {"path-status" : ("path_status", BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus)}
                                                self._child_list_classes = {}

                                                self.nexthop = YLeaf(YType.str, "nexthop")

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.local_pref = YLeaf(YType.uint32, "local-pref")

                                                self.weight = YLeaf(YType.uint32, "weight")

                                                self.as_path = YLeaf(YType.str, "as-path")

                                                self.origin = YLeaf(YType.enumeration, "origin")

                                                self.rpki_status = YLeaf(YType.enumeration, "rpki-status")

                                                self.community = YLeaf(YType.str, "community")

                                                self.path_status = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus()
                                                self.path_status.parent = self
                                                self._children_name_map["path_status"] = "path-status"
                                                self._children_yang_names.add("path-status")
                                                self._segment_path = lambda: "bgp-path-entry" + "[nexthop='" + self.nexthop.get() + "']"

                                            def __setattr__(self, name, value):
                                                self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, ['nexthop', 'metric', 'local_pref', 'weight', 'as_path', 'origin', 'rpki_status', 'community'], name, value)


                                            class PathStatus(Entity):
                                                """
                                                Path status
                                                
                                                .. attribute:: suppressed
                                                
                                                	Suppressed path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: damped
                                                
                                                	Damped path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: history
                                                
                                                	History path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: valid
                                                
                                                	Valid path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: sourced
                                                
                                                	Sourced path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: bestpath
                                                
                                                	Best path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: internal
                                                
                                                	Internal path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_fail
                                                
                                                	RIB\-fail path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: stale
                                                
                                                	Stale path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: multipath
                                                
                                                	Multipath path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: backup_path
                                                
                                                	Backup path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rt_filter
                                                
                                                	RT filter path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: best_external
                                                
                                                	Best externa path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: additional_path
                                                
                                                	Additional path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_compressed
                                                
                                                	RIB compressed path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-04-01'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, self).__init__()

                                                    self.yang_name = "path-status"
                                                    self.yang_parent_name = "bgp-path-entry"
                                                    self.is_top_level_class = False
                                                    self.has_list_ancestor = True
                                                    self._child_container_classes = {}
                                                    self._child_list_classes = {}

                                                    self.suppressed = YLeaf(YType.empty, "suppressed")

                                                    self.damped = YLeaf(YType.empty, "damped")

                                                    self.history = YLeaf(YType.empty, "history")

                                                    self.valid = YLeaf(YType.empty, "valid")

                                                    self.sourced = YLeaf(YType.empty, "sourced")

                                                    self.bestpath = YLeaf(YType.empty, "bestpath")

                                                    self.internal = YLeaf(YType.empty, "internal")

                                                    self.rib_fail = YLeaf(YType.empty, "rib-fail")

                                                    self.stale = YLeaf(YType.empty, "stale")

                                                    self.multipath = YLeaf(YType.empty, "multipath")

                                                    self.backup_path = YLeaf(YType.empty, "backup-path")

                                                    self.rt_filter = YLeaf(YType.empty, "rt-filter")

                                                    self.best_external = YLeaf(YType.empty, "best-external")

                                                    self.additional_path = YLeaf(YType.empty, "additional-path")

                                                    self.rib_compressed = YLeaf(YType.empty, "rib-compressed")
                                                    self._segment_path = lambda: "path-status"

                                                def __setattr__(self, name, value):
                                                    self._perform_setattr(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, ['suppressed', 'damped', 'history', 'valid', 'sourced', 'bestpath', 'internal', 'rib_fail', 'stale', 'multipath', 'backup_path', 'rt_filter', 'best_external', 'additional_path', 'rib_compressed'], name, value)

    def clone_ptr(self):
        self._top_entity = BgpStateData()
        return self._top_entity

