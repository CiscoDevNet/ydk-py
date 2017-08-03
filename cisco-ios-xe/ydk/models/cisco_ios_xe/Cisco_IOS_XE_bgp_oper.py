""" Cisco_IOS_XE_bgp_oper 

This module contains a collection of YANG definitions
for bgp operational data.
Copyright (c) 2016\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
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
    
    .. attribute:: address_families
    
    	BGP address family
    	**type**\:   :py:class:`AddressFamilies <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies>`
    
    .. attribute:: bgp_route_vrfs
    
    	BGP VRFs
    	**type**\:   :py:class:`BgpRouteVrfs <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs>`
    
    .. attribute:: neighbors
    
    	BGP neighbor information
    	**type**\:   :py:class:`Neighbors <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors>`
    
    

    """

    _prefix = 'bgp-ios-xe-oper'
    _revision = '2017-04-01'

    def __init__(self):
        super(BgpStateData, self).__init__()
        self._top_entity = None

        self.yang_name = "bgp-state-data"
        self.yang_parent_name = "Cisco-IOS-XE-bgp-oper"

        self.address_families = BgpStateData.AddressFamilies()
        self.address_families.parent = self
        self._children_name_map["address_families"] = "address-families"
        self._children_yang_names.add("address-families")

        self.bgp_route_vrfs = BgpStateData.BgpRouteVrfs()
        self.bgp_route_vrfs.parent = self
        self._children_name_map["bgp_route_vrfs"] = "bgp-route-vrfs"
        self._children_yang_names.add("bgp-route-vrfs")

        self.neighbors = BgpStateData.Neighbors()
        self.neighbors.parent = self
        self._children_name_map["neighbors"] = "neighbors"
        self._children_yang_names.add("neighbors")


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

            self.neighbor = YList(self)

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
                        super(BgpStateData.Neighbors, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BgpStateData.Neighbors, self).__setattr__(name, value)


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
            
            .. attribute:: bgp_neighbor_counters
            
            	BGP neighbor session counters
            	**type**\:   :py:class:`BgpNeighborCounters <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters>`
            
            .. attribute:: bgp_version
            
            	BGP version being used to communicate with the remote router
            	**type**\:  int
            
            	**range:** 0..65535
            
            .. attribute:: connection
            
            	BGP neighbor connection
            	**type**\:   :py:class:`Connection <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Connection>`
            
            .. attribute:: description
            
            	Neighbor description string
            	**type**\:  str
            
            .. attribute:: installed_prefixes
            
            	The number of installed prefixes
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: last_read
            
            	Time since BGP last received a message from the neighbor
            	**type**\:  str
            
            .. attribute:: last_write
            
            	Time since BGP last sent a message to the neighbor
            	**type**\:  str
            
            .. attribute:: link
            
            	Neighbor link type
            	**type**\:   :py:class:`BgpLink <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpLink>`
            
            .. attribute:: negotiated_cap
            
            	Negotiated capabilities for neighbor session
            	**type**\:  list of str
            
            .. attribute:: negotiated_keepalive_timers
            
            	Negotiated keepalive timers status of BGP neighbor
            	**type**\:   :py:class:`NegotiatedKeepaliveTimers <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers>`
            
            .. attribute:: prefix_activity
            
            	BGP neighbor activity
            	**type**\:   :py:class:`PrefixActivity <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity>`
            
            .. attribute:: session_state
            
            	BGP neighbor session state
            	**type**\:   :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
            
            .. attribute:: transport
            
            	BGP neighbor transport
            	**type**\:   :py:class:`Transport <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.Transport>`
            
            .. attribute:: up_time
            
            	Amout of time the bgp session has been up since being established
            	**type**\:  str
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(BgpStateData.Neighbors.Neighbor, self).__init__()

                self.yang_name = "neighbor"
                self.yang_parent_name = "neighbors"

                self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.neighbor_id = YLeaf(YType.str, "neighbor-id")

                self.bgp_version = YLeaf(YType.uint16, "bgp-version")

                self.description = YLeaf(YType.str, "description")

                self.installed_prefixes = YLeaf(YType.uint32, "installed-prefixes")

                self.last_read = YLeaf(YType.str, "last-read")

                self.last_write = YLeaf(YType.str, "last-write")

                self.link = YLeaf(YType.enumeration, "link")

                self.negotiated_cap = YLeafList(YType.str, "negotiated-cap")

                self.session_state = YLeaf(YType.enumeration, "session-state")

                self.up_time = YLeaf(YType.str, "up-time")

                self.bgp_neighbor_counters = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters()
                self.bgp_neighbor_counters.parent = self
                self._children_name_map["bgp_neighbor_counters"] = "bgp-neighbor-counters"
                self._children_yang_names.add("bgp-neighbor-counters")

                self.connection = BgpStateData.Neighbors.Neighbor.Connection()
                self.connection.parent = self
                self._children_name_map["connection"] = "connection"
                self._children_yang_names.add("connection")

                self.negotiated_keepalive_timers = BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers()
                self.negotiated_keepalive_timers.parent = self
                self._children_name_map["negotiated_keepalive_timers"] = "negotiated-keepalive-timers"
                self._children_yang_names.add("negotiated-keepalive-timers")

                self.prefix_activity = BgpStateData.Neighbors.Neighbor.PrefixActivity()
                self.prefix_activity.parent = self
                self._children_name_map["prefix_activity"] = "prefix-activity"
                self._children_yang_names.add("prefix-activity")

                self.transport = BgpStateData.Neighbors.Neighbor.Transport()
                self.transport.parent = self
                self._children_name_map["transport"] = "transport"
                self._children_yang_names.add("transport")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("afi_safi",
                                "vrf_name",
                                "neighbor_id",
                                "bgp_version",
                                "description",
                                "installed_prefixes",
                                "last_read",
                                "last_write",
                                "link",
                                "negotiated_cap",
                                "session_state",
                                "up_time") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BgpStateData.Neighbors.Neighbor, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BgpStateData.Neighbors.Neighbor, self).__setattr__(name, value)


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

                    self.hold_time = YLeaf(YType.uint16, "hold-time")

                    self.keepalive_interval = YLeaf(YType.uint16, "keepalive-interval")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("hold_time",
                                    "keepalive_interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.hold_time.is_set or
                        self.keepalive_interval.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.hold_time.yfilter != YFilter.not_set or
                        self.keepalive_interval.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "negotiated-keepalive-timers" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.hold_time.is_set or self.hold_time.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.hold_time.get_name_leafdata())
                    if (self.keepalive_interval.is_set or self.keepalive_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.keepalive_interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hold-time" or name == "keepalive-interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "hold-time"):
                        self.hold_time = value
                        self.hold_time.value_namespace = name_space
                        self.hold_time.value_namespace_prefix = name_space_prefix
                    if(value_path == "keepalive-interval"):
                        self.keepalive_interval = value
                        self.keepalive_interval.value_namespace = name_space
                        self.keepalive_interval.value_namespace_prefix = name_space_prefix


            class BgpNeighborCounters(Entity):
                """
                BGP neighbor session counters
                
                .. attribute:: inq_depth
                
                	Input Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: outq_depth
                
                	Output Q depth
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: received
                
                	Number of mesaged received
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received>`
                
                .. attribute:: sent
                
                	Number of mesaged sent
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, self).__init__()

                    self.yang_name = "bgp-neighbor-counters"
                    self.yang_parent_name = "neighbor"

                    self.inq_depth = YLeaf(YType.uint32, "inq-depth")

                    self.outq_depth = YLeaf(YType.uint32, "outq-depth")

                    self.received = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received()
                    self.received.parent = self
                    self._children_name_map["received"] = "received"
                    self._children_yang_names.add("received")

                    self.sent = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent()
                    self.sent.parent = self
                    self._children_name_map["sent"] = "sent"
                    self._children_yang_names.add("sent")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("inq_depth",
                                    "outq_depth") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters, self).__setattr__(name, value)


                class Sent(Entity):
                    """
                    Number of mesaged sent
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opens
                    
                    	OPEN message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "bgp-neighbor-counters"

                        self.keepalives = YLeaf(YType.uint32, "keepalives")

                        self.notifications = YLeaf(YType.uint32, "notifications")

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.route_refreshes = YLeaf(YType.uint32, "route-refreshes")

                        self.updates = YLeaf(YType.uint32, "updates")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("keepalives",
                                        "notifications",
                                        "opens",
                                        "route_refreshes",
                                        "updates") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.keepalives.is_set or
                            self.notifications.is_set or
                            self.opens.is_set or
                            self.route_refreshes.is_set or
                            self.updates.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.keepalives.yfilter != YFilter.not_set or
                            self.notifications.yfilter != YFilter.not_set or
                            self.opens.yfilter != YFilter.not_set or
                            self.route_refreshes.yfilter != YFilter.not_set or
                            self.updates.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sent" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.keepalives.is_set or self.keepalives.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keepalives.get_name_leafdata())
                        if (self.notifications.is_set or self.notifications.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.notifications.get_name_leafdata())
                        if (self.opens.is_set or self.opens.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opens.get_name_leafdata())
                        if (self.route_refreshes.is_set or self.route_refreshes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_refreshes.get_name_leafdata())
                        if (self.updates.is_set or self.updates.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.updates.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "keepalives" or name == "notifications" or name == "opens" or name == "route-refreshes" or name == "updates"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "keepalives"):
                            self.keepalives = value
                            self.keepalives.value_namespace = name_space
                            self.keepalives.value_namespace_prefix = name_space_prefix
                        if(value_path == "notifications"):
                            self.notifications = value
                            self.notifications.value_namespace = name_space
                            self.notifications.value_namespace_prefix = name_space_prefix
                        if(value_path == "opens"):
                            self.opens = value
                            self.opens.value_namespace = name_space
                            self.opens.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-refreshes"):
                            self.route_refreshes = value
                            self.route_refreshes.value_namespace = name_space
                            self.route_refreshes.value_namespace_prefix = name_space_prefix
                        if(value_path == "updates"):
                            self.updates = value
                            self.updates.value_namespace = name_space
                            self.updates.value_namespace_prefix = name_space_prefix


                class Received(Entity):
                    """
                    Number of mesaged received
                    
                    .. attribute:: keepalives
                    
                    	KEEPALIVE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: notifications
                    
                    	NOTIFICATION message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: opens
                    
                    	OPEN message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: route_refreshes
                    
                    	Route refresh message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: updates
                    
                    	UPDATE message count
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "bgp-neighbor-counters"

                        self.keepalives = YLeaf(YType.uint32, "keepalives")

                        self.notifications = YLeaf(YType.uint32, "notifications")

                        self.opens = YLeaf(YType.uint32, "opens")

                        self.route_refreshes = YLeaf(YType.uint32, "route-refreshes")

                        self.updates = YLeaf(YType.uint32, "updates")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("keepalives",
                                        "notifications",
                                        "opens",
                                        "route_refreshes",
                                        "updates") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.keepalives.is_set or
                            self.notifications.is_set or
                            self.opens.is_set or
                            self.route_refreshes.is_set or
                            self.updates.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.keepalives.yfilter != YFilter.not_set or
                            self.notifications.yfilter != YFilter.not_set or
                            self.opens.yfilter != YFilter.not_set or
                            self.route_refreshes.yfilter != YFilter.not_set or
                            self.updates.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "received" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.keepalives.is_set or self.keepalives.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.keepalives.get_name_leafdata())
                        if (self.notifications.is_set or self.notifications.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.notifications.get_name_leafdata())
                        if (self.opens.is_set or self.opens.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.opens.get_name_leafdata())
                        if (self.route_refreshes.is_set or self.route_refreshes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.route_refreshes.get_name_leafdata())
                        if (self.updates.is_set or self.updates.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.updates.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "keepalives" or name == "notifications" or name == "opens" or name == "route-refreshes" or name == "updates"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "keepalives"):
                            self.keepalives = value
                            self.keepalives.value_namespace = name_space
                            self.keepalives.value_namespace_prefix = name_space_prefix
                        if(value_path == "notifications"):
                            self.notifications = value
                            self.notifications.value_namespace = name_space
                            self.notifications.value_namespace_prefix = name_space_prefix
                        if(value_path == "opens"):
                            self.opens = value
                            self.opens.value_namespace = name_space
                            self.opens.value_namespace_prefix = name_space_prefix
                        if(value_path == "route-refreshes"):
                            self.route_refreshes = value
                            self.route_refreshes.value_namespace = name_space
                            self.route_refreshes.value_namespace_prefix = name_space_prefix
                        if(value_path == "updates"):
                            self.updates = value
                            self.updates.value_namespace = name_space
                            self.updates.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.inq_depth.is_set or
                        self.outq_depth.is_set or
                        (self.received is not None and self.received.has_data()) or
                        (self.sent is not None and self.sent.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.inq_depth.yfilter != YFilter.not_set or
                        self.outq_depth.yfilter != YFilter.not_set or
                        (self.received is not None and self.received.has_operation()) or
                        (self.sent is not None and self.sent.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgp-neighbor-counters" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.inq_depth.is_set or self.inq_depth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.inq_depth.get_name_leafdata())
                    if (self.outq_depth.is_set or self.outq_depth.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.outq_depth.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "received"):
                        if (self.received is None):
                            self.received = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"
                        return self.received

                    if (child_yang_name == "sent"):
                        if (self.sent is None):
                            self.sent = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters.Sent()
                            self.sent.parent = self
                            self._children_name_map["sent"] = "sent"
                        return self.sent

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "received" or name == "sent" or name == "inq-depth" or name == "outq-depth"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "inq-depth"):
                        self.inq_depth = value
                        self.inq_depth.value_namespace = name_space
                        self.inq_depth.value_namespace_prefix = name_space_prefix
                    if(value_path == "outq-depth"):
                        self.outq_depth = value
                        self.outq_depth.value_namespace = name_space
                        self.outq_depth.value_namespace_prefix = name_space_prefix


            class Connection(Entity):
                """
                BGP neighbor connection
                
                .. attribute:: last_reset
                
                	Time since peering session was last reset
                	**type**\:  str
                
                .. attribute:: mode
                
                	BGP transport connection mode
                	**type**\:   :py:class:`BgpMode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpMode>`
                
                .. attribute:: reset_reason
                
                	The reason for the last reset
                	**type**\:  str
                
                .. attribute:: state
                
                	TCP FSM state
                	**type**\:   :py:class:`TcpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.TcpFsmState>`
                
                .. attribute:: total_dropped
                
                	The number of times that a valid session has failed or been taken down
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: total_established
                
                	The number of times a TCP and BGP  connection has been successfully established
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Connection, self).__init__()

                    self.yang_name = "connection"
                    self.yang_parent_name = "neighbor"

                    self.last_reset = YLeaf(YType.str, "last-reset")

                    self.mode = YLeaf(YType.enumeration, "mode")

                    self.reset_reason = YLeaf(YType.str, "reset-reason")

                    self.state = YLeaf(YType.enumeration, "state")

                    self.total_dropped = YLeaf(YType.uint32, "total-dropped")

                    self.total_established = YLeaf(YType.uint32, "total-established")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("last_reset",
                                    "mode",
                                    "reset_reason",
                                    "state",
                                    "total_dropped",
                                    "total_established") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.Neighbors.Neighbor.Connection, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.Neighbors.Neighbor.Connection, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.last_reset.is_set or
                        self.mode.is_set or
                        self.reset_reason.is_set or
                        self.state.is_set or
                        self.total_dropped.is_set or
                        self.total_established.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.last_reset.yfilter != YFilter.not_set or
                        self.mode.yfilter != YFilter.not_set or
                        self.reset_reason.yfilter != YFilter.not_set or
                        self.state.yfilter != YFilter.not_set or
                        self.total_dropped.yfilter != YFilter.not_set or
                        self.total_established.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "connection" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.last_reset.is_set or self.last_reset.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.last_reset.get_name_leafdata())
                    if (self.mode.is_set or self.mode.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mode.get_name_leafdata())
                    if (self.reset_reason.is_set or self.reset_reason.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.reset_reason.get_name_leafdata())
                    if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.state.get_name_leafdata())
                    if (self.total_dropped.is_set or self.total_dropped.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_dropped.get_name_leafdata())
                    if (self.total_established.is_set or self.total_established.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_established.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "last-reset" or name == "mode" or name == "reset-reason" or name == "state" or name == "total-dropped" or name == "total-established"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "last-reset"):
                        self.last_reset = value
                        self.last_reset.value_namespace = name_space
                        self.last_reset.value_namespace_prefix = name_space_prefix
                    if(value_path == "mode"):
                        self.mode = value
                        self.mode.value_namespace = name_space
                        self.mode.value_namespace_prefix = name_space_prefix
                    if(value_path == "reset-reason"):
                        self.reset_reason = value
                        self.reset_reason.value_namespace = name_space
                        self.reset_reason.value_namespace_prefix = name_space_prefix
                    if(value_path == "state"):
                        self.state = value
                        self.state.value_namespace = name_space
                        self.state.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-dropped"):
                        self.total_dropped = value
                        self.total_dropped.value_namespace = name_space
                        self.total_dropped.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-established"):
                        self.total_established = value
                        self.total_established.value_namespace = name_space
                        self.total_established.value_namespace_prefix = name_space_prefix


            class Transport(Entity):
                """
                BGP neighbor transport
                
                .. attribute:: foreign_host
                
                	Remote address of the BGP session
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
                
                	Indication whether path MTU discovrey is enabled
                	**type**\:  bool
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.Transport, self).__init__()

                    self.yang_name = "transport"
                    self.yang_parent_name = "neighbor"

                    self.foreign_host = YLeaf(YType.str, "foreign-host")

                    self.foreign_port = YLeaf(YType.uint32, "foreign-port")

                    self.local_host = YLeaf(YType.str, "local-host")

                    self.local_port = YLeaf(YType.uint32, "local-port")

                    self.mss = YLeaf(YType.uint32, "mss")

                    self.path_mtu_discovery = YLeaf(YType.boolean, "path-mtu-discovery")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("foreign_host",
                                    "foreign_port",
                                    "local_host",
                                    "local_port",
                                    "mss",
                                    "path_mtu_discovery") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.Neighbors.Neighbor.Transport, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.Neighbors.Neighbor.Transport, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.foreign_host.is_set or
                        self.foreign_port.is_set or
                        self.local_host.is_set or
                        self.local_port.is_set or
                        self.mss.is_set or
                        self.path_mtu_discovery.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.foreign_host.yfilter != YFilter.not_set or
                        self.foreign_port.yfilter != YFilter.not_set or
                        self.local_host.yfilter != YFilter.not_set or
                        self.local_port.yfilter != YFilter.not_set or
                        self.mss.yfilter != YFilter.not_set or
                        self.path_mtu_discovery.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "transport" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.foreign_host.is_set or self.foreign_host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.foreign_host.get_name_leafdata())
                    if (self.foreign_port.is_set or self.foreign_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.foreign_port.get_name_leafdata())
                    if (self.local_host.is_set or self.local_host.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_host.get_name_leafdata())
                    if (self.local_port.is_set or self.local_port.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.local_port.get_name_leafdata())
                    if (self.mss.is_set or self.mss.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.mss.get_name_leafdata())
                    if (self.path_mtu_discovery.is_set or self.path_mtu_discovery.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.path_mtu_discovery.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "foreign-host" or name == "foreign-port" or name == "local-host" or name == "local-port" or name == "mss" or name == "path-mtu-discovery"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "foreign-host"):
                        self.foreign_host = value
                        self.foreign_host.value_namespace = name_space
                        self.foreign_host.value_namespace_prefix = name_space_prefix
                    if(value_path == "foreign-port"):
                        self.foreign_port = value
                        self.foreign_port.value_namespace = name_space
                        self.foreign_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-host"):
                        self.local_host = value
                        self.local_host.value_namespace = name_space
                        self.local_host.value_namespace_prefix = name_space_prefix
                    if(value_path == "local-port"):
                        self.local_port = value
                        self.local_port.value_namespace = name_space
                        self.local_port.value_namespace_prefix = name_space_prefix
                    if(value_path == "mss"):
                        self.mss = value
                        self.mss.value_namespace = name_space
                        self.mss.value_namespace_prefix = name_space_prefix
                    if(value_path == "path-mtu-discovery"):
                        self.path_mtu_discovery = value
                        self.path_mtu_discovery.value_namespace = name_space
                        self.path_mtu_discovery.value_namespace_prefix = name_space_prefix


            class PrefixActivity(Entity):
                """
                BGP neighbor activity
                
                .. attribute:: received
                
                	Number of prefixes received
                	**type**\:   :py:class:`Received <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Received>`
                
                .. attribute:: sent
                
                	Number of prefixes sent
                	**type**\:   :py:class:`Sent <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent>`
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.Neighbors.Neighbor.PrefixActivity, self).__init__()

                    self.yang_name = "prefix-activity"
                    self.yang_parent_name = "neighbor"

                    self.received = BgpStateData.Neighbors.Neighbor.PrefixActivity.Received()
                    self.received.parent = self
                    self._children_name_map["received"] = "received"
                    self._children_yang_names.add("received")

                    self.sent = BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent()
                    self.sent.parent = self
                    self._children_name_map["sent"] = "sent"
                    self._children_yang_names.add("sent")


                class Sent(Entity):
                    """
                    Number of prefixes sent
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: current_prefixes
                    
                    	The current number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, self).__init__()

                        self.yang_name = "sent"
                        self.yang_parent_name = "prefix-activity"

                        self.bestpaths = YLeaf(YType.uint64, "bestpaths")

                        self.current_prefixes = YLeaf(YType.uint64, "current-prefixes")

                        self.explicit_withdraw = YLeaf(YType.uint64, "explicit-withdraw")

                        self.implicit_withdraw = YLeaf(YType.uint64, "implicit-withdraw")

                        self.multipaths = YLeaf(YType.uint64, "multipaths")

                        self.total_prefixes = YLeaf(YType.uint64, "total-prefixes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bestpaths",
                                        "current_prefixes",
                                        "explicit_withdraw",
                                        "implicit_withdraw",
                                        "multipaths",
                                        "total_prefixes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bestpaths.is_set or
                            self.current_prefixes.is_set or
                            self.explicit_withdraw.is_set or
                            self.implicit_withdraw.is_set or
                            self.multipaths.is_set or
                            self.total_prefixes.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bestpaths.yfilter != YFilter.not_set or
                            self.current_prefixes.yfilter != YFilter.not_set or
                            self.explicit_withdraw.yfilter != YFilter.not_set or
                            self.implicit_withdraw.yfilter != YFilter.not_set or
                            self.multipaths.yfilter != YFilter.not_set or
                            self.total_prefixes.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "sent" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bestpaths.is_set or self.bestpaths.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bestpaths.get_name_leafdata())
                        if (self.current_prefixes.is_set or self.current_prefixes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_prefixes.get_name_leafdata())
                        if (self.explicit_withdraw.is_set or self.explicit_withdraw.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.explicit_withdraw.get_name_leafdata())
                        if (self.implicit_withdraw.is_set or self.implicit_withdraw.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.implicit_withdraw.get_name_leafdata())
                        if (self.multipaths.is_set or self.multipaths.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multipaths.get_name_leafdata())
                        if (self.total_prefixes.is_set or self.total_prefixes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_prefixes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bestpaths" or name == "current-prefixes" or name == "explicit-withdraw" or name == "implicit-withdraw" or name == "multipaths" or name == "total-prefixes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bestpaths"):
                            self.bestpaths = value
                            self.bestpaths.value_namespace = name_space
                            self.bestpaths.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-prefixes"):
                            self.current_prefixes = value
                            self.current_prefixes.value_namespace = name_space
                            self.current_prefixes.value_namespace_prefix = name_space_prefix
                        if(value_path == "explicit-withdraw"):
                            self.explicit_withdraw = value
                            self.explicit_withdraw.value_namespace = name_space
                            self.explicit_withdraw.value_namespace_prefix = name_space_prefix
                        if(value_path == "implicit-withdraw"):
                            self.implicit_withdraw = value
                            self.implicit_withdraw.value_namespace = name_space
                            self.implicit_withdraw.value_namespace_prefix = name_space_prefix
                        if(value_path == "multipaths"):
                            self.multipaths = value
                            self.multipaths.value_namespace = name_space
                            self.multipaths.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-prefixes"):
                            self.total_prefixes = value
                            self.total_prefixes.value_namespace = name_space
                            self.total_prefixes.value_namespace_prefix = name_space_prefix


                class Received(Entity):
                    """
                    Number of prefixes received
                    
                    .. attribute:: bestpaths
                    
                    	The number of received prefixes installed as best paths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: current_prefixes
                    
                    	The current number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: explicit_withdraw
                    
                    	The number of times a prefix has been withdrawn because it is no longer feasible
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: implicit_withdraw
                    
                    	The number of times a prefix has been withdrawn and readvertised
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: multipaths
                    
                    	The number of received prefixes installed as multipaths
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: total_prefixes
                    
                    	The total number of accepted prefixes
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, self).__init__()

                        self.yang_name = "received"
                        self.yang_parent_name = "prefix-activity"

                        self.bestpaths = YLeaf(YType.uint64, "bestpaths")

                        self.current_prefixes = YLeaf(YType.uint64, "current-prefixes")

                        self.explicit_withdraw = YLeaf(YType.uint64, "explicit-withdraw")

                        self.implicit_withdraw = YLeaf(YType.uint64, "implicit-withdraw")

                        self.multipaths = YLeaf(YType.uint64, "multipaths")

                        self.total_prefixes = YLeaf(YType.uint64, "total-prefixes")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("bestpaths",
                                        "current_prefixes",
                                        "explicit_withdraw",
                                        "implicit_withdraw",
                                        "multipaths",
                                        "total_prefixes") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.Neighbors.Neighbor.PrefixActivity.Received, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.bestpaths.is_set or
                            self.current_prefixes.is_set or
                            self.explicit_withdraw.is_set or
                            self.implicit_withdraw.is_set or
                            self.multipaths.is_set or
                            self.total_prefixes.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.bestpaths.yfilter != YFilter.not_set or
                            self.current_prefixes.yfilter != YFilter.not_set or
                            self.explicit_withdraw.yfilter != YFilter.not_set or
                            self.implicit_withdraw.yfilter != YFilter.not_set or
                            self.multipaths.yfilter != YFilter.not_set or
                            self.total_prefixes.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "received" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.bestpaths.is_set or self.bestpaths.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bestpaths.get_name_leafdata())
                        if (self.current_prefixes.is_set or self.current_prefixes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.current_prefixes.get_name_leafdata())
                        if (self.explicit_withdraw.is_set or self.explicit_withdraw.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.explicit_withdraw.get_name_leafdata())
                        if (self.implicit_withdraw.is_set or self.implicit_withdraw.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.implicit_withdraw.get_name_leafdata())
                        if (self.multipaths.is_set or self.multipaths.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.multipaths.get_name_leafdata())
                        if (self.total_prefixes.is_set or self.total_prefixes.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.total_prefixes.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bestpaths" or name == "current-prefixes" or name == "explicit-withdraw" or name == "implicit-withdraw" or name == "multipaths" or name == "total-prefixes"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "bestpaths"):
                            self.bestpaths = value
                            self.bestpaths.value_namespace = name_space
                            self.bestpaths.value_namespace_prefix = name_space_prefix
                        if(value_path == "current-prefixes"):
                            self.current_prefixes = value
                            self.current_prefixes.value_namespace = name_space
                            self.current_prefixes.value_namespace_prefix = name_space_prefix
                        if(value_path == "explicit-withdraw"):
                            self.explicit_withdraw = value
                            self.explicit_withdraw.value_namespace = name_space
                            self.explicit_withdraw.value_namespace_prefix = name_space_prefix
                        if(value_path == "implicit-withdraw"):
                            self.implicit_withdraw = value
                            self.implicit_withdraw.value_namespace = name_space
                            self.implicit_withdraw.value_namespace_prefix = name_space_prefix
                        if(value_path == "multipaths"):
                            self.multipaths = value
                            self.multipaths.value_namespace = name_space
                            self.multipaths.value_namespace_prefix = name_space_prefix
                        if(value_path == "total-prefixes"):
                            self.total_prefixes = value
                            self.total_prefixes.value_namespace = name_space
                            self.total_prefixes.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        (self.received is not None and self.received.has_data()) or
                        (self.sent is not None and self.sent.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        (self.received is not None and self.received.has_operation()) or
                        (self.sent is not None and self.sent.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefix-activity" + path_buffer

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

                    if (child_yang_name == "received"):
                        if (self.received is None):
                            self.received = BgpStateData.Neighbors.Neighbor.PrefixActivity.Received()
                            self.received.parent = self
                            self._children_name_map["received"] = "received"
                        return self.received

                    if (child_yang_name == "sent"):
                        if (self.sent is None):
                            self.sent = BgpStateData.Neighbors.Neighbor.PrefixActivity.Sent()
                            self.sent.parent = self
                            self._children_name_map["sent"] = "sent"
                        return self.sent

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "received" or name == "sent"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                for leaf in self.negotiated_cap.getYLeafs():
                    if (leaf.yfilter != YFilter.not_set):
                        return True
                return (
                    self.afi_safi.is_set or
                    self.vrf_name.is_set or
                    self.neighbor_id.is_set or
                    self.bgp_version.is_set or
                    self.description.is_set or
                    self.installed_prefixes.is_set or
                    self.last_read.is_set or
                    self.last_write.is_set or
                    self.link.is_set or
                    self.session_state.is_set or
                    self.up_time.is_set or
                    (self.bgp_neighbor_counters is not None and self.bgp_neighbor_counters.has_data()) or
                    (self.connection is not None and self.connection.has_data()) or
                    (self.negotiated_keepalive_timers is not None and self.negotiated_keepalive_timers.has_data()) or
                    (self.prefix_activity is not None and self.prefix_activity.has_data()) or
                    (self.transport is not None and self.transport.has_data()))

            def has_operation(self):
                for leaf in self.negotiated_cap.getYLeafs():
                    if (leaf.is_set):
                        return True
                return (
                    self.yfilter != YFilter.not_set or
                    self.afi_safi.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.neighbor_id.yfilter != YFilter.not_set or
                    self.bgp_version.yfilter != YFilter.not_set or
                    self.description.yfilter != YFilter.not_set or
                    self.installed_prefixes.yfilter != YFilter.not_set or
                    self.last_read.yfilter != YFilter.not_set or
                    self.last_write.yfilter != YFilter.not_set or
                    self.link.yfilter != YFilter.not_set or
                    self.negotiated_cap.yfilter != YFilter.not_set or
                    self.session_state.yfilter != YFilter.not_set or
                    self.up_time.yfilter != YFilter.not_set or
                    (self.bgp_neighbor_counters is not None and self.bgp_neighbor_counters.has_operation()) or
                    (self.connection is not None and self.connection.has_operation()) or
                    (self.negotiated_keepalive_timers is not None and self.negotiated_keepalive_timers.has_operation()) or
                    (self.prefix_activity is not None and self.prefix_activity.has_operation()) or
                    (self.transport is not None and self.transport.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "neighbor" + "[afi-safi='" + self.afi_safi.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + "[neighbor-id='" + self.neighbor_id.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/neighbors/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.afi_safi.is_set or self.afi_safi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.afi_safi.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.neighbor_id.is_set or self.neighbor_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.neighbor_id.get_name_leafdata())
                if (self.bgp_version.is_set or self.bgp_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp_version.get_name_leafdata())
                if (self.description.is_set or self.description.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.description.get_name_leafdata())
                if (self.installed_prefixes.is_set or self.installed_prefixes.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.installed_prefixes.get_name_leafdata())
                if (self.last_read.is_set or self.last_read.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_read.get_name_leafdata())
                if (self.last_write.is_set or self.last_write.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.last_write.get_name_leafdata())
                if (self.link.is_set or self.link.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.link.get_name_leafdata())
                if (self.session_state.is_set or self.session_state.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.session_state.get_name_leafdata())
                if (self.up_time.is_set or self.up_time.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.up_time.get_name_leafdata())

                leaf_name_data.extend(self.negotiated_cap.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bgp-neighbor-counters"):
                    if (self.bgp_neighbor_counters is None):
                        self.bgp_neighbor_counters = BgpStateData.Neighbors.Neighbor.BgpNeighborCounters()
                        self.bgp_neighbor_counters.parent = self
                        self._children_name_map["bgp_neighbor_counters"] = "bgp-neighbor-counters"
                    return self.bgp_neighbor_counters

                if (child_yang_name == "connection"):
                    if (self.connection is None):
                        self.connection = BgpStateData.Neighbors.Neighbor.Connection()
                        self.connection.parent = self
                        self._children_name_map["connection"] = "connection"
                    return self.connection

                if (child_yang_name == "negotiated-keepalive-timers"):
                    if (self.negotiated_keepalive_timers is None):
                        self.negotiated_keepalive_timers = BgpStateData.Neighbors.Neighbor.NegotiatedKeepaliveTimers()
                        self.negotiated_keepalive_timers.parent = self
                        self._children_name_map["negotiated_keepalive_timers"] = "negotiated-keepalive-timers"
                    return self.negotiated_keepalive_timers

                if (child_yang_name == "prefix-activity"):
                    if (self.prefix_activity is None):
                        self.prefix_activity = BgpStateData.Neighbors.Neighbor.PrefixActivity()
                        self.prefix_activity.parent = self
                        self._children_name_map["prefix_activity"] = "prefix-activity"
                    return self.prefix_activity

                if (child_yang_name == "transport"):
                    if (self.transport is None):
                        self.transport = BgpStateData.Neighbors.Neighbor.Transport()
                        self.transport.parent = self
                        self._children_name_map["transport"] = "transport"
                    return self.transport

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgp-neighbor-counters" or name == "connection" or name == "negotiated-keepalive-timers" or name == "prefix-activity" or name == "transport" or name == "afi-safi" or name == "vrf-name" or name == "neighbor-id" or name == "bgp-version" or name == "description" or name == "installed-prefixes" or name == "last-read" or name == "last-write" or name == "link" or name == "negotiated-cap" or name == "session-state" or name == "up-time"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "afi-safi"):
                    self.afi_safi = value
                    self.afi_safi.value_namespace = name_space
                    self.afi_safi.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "neighbor-id"):
                    self.neighbor_id = value
                    self.neighbor_id.value_namespace = name_space
                    self.neighbor_id.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp-version"):
                    self.bgp_version = value
                    self.bgp_version.value_namespace = name_space
                    self.bgp_version.value_namespace_prefix = name_space_prefix
                if(value_path == "description"):
                    self.description = value
                    self.description.value_namespace = name_space
                    self.description.value_namespace_prefix = name_space_prefix
                if(value_path == "installed-prefixes"):
                    self.installed_prefixes = value
                    self.installed_prefixes.value_namespace = name_space
                    self.installed_prefixes.value_namespace_prefix = name_space_prefix
                if(value_path == "last-read"):
                    self.last_read = value
                    self.last_read.value_namespace = name_space
                    self.last_read.value_namespace_prefix = name_space_prefix
                if(value_path == "last-write"):
                    self.last_write = value
                    self.last_write.value_namespace = name_space
                    self.last_write.value_namespace_prefix = name_space_prefix
                if(value_path == "link"):
                    self.link = value
                    self.link.value_namespace = name_space
                    self.link.value_namespace_prefix = name_space_prefix
                if(value_path == "negotiated-cap"):
                    self.negotiated_cap.append(value)
                if(value_path == "session-state"):
                    self.session_state = value
                    self.session_state.value_namespace = name_space
                    self.session_state.value_namespace_prefix = name_space_prefix
                if(value_path == "up-time"):
                    self.up_time = value
                    self.up_time.value_namespace = name_space
                    self.up_time.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.neighbor:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.neighbor:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "neighbors" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "neighbor"):
                for c in self.neighbor:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BgpStateData.Neighbors.Neighbor()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.neighbor.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "neighbor"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.address_family = YList(self)

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
                        super(BgpStateData.AddressFamilies, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BgpStateData.AddressFamilies, self).__setattr__(name, value)


        class AddressFamily(Entity):
            """
            List of BGP address families
            
            .. attribute:: afi_safi  <key>
            
            	Afi\-safi value
            	**type**\:   :py:class:`AfiSafi <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_common_oper.AfiSafi>`
            
            .. attribute:: vrf_name  <key>
            
            	VRF name
            	**type**\:  str
            
            .. attribute:: activities
            
            	BGP activity information
            	**type**\:   :py:class:`Activities <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Activities>`
            
            .. attribute:: as_path
            
            	AS path entry statistics
            	**type**\:   :py:class:`AsPath <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.AsPath>`
            
            .. attribute:: bgp_neighbor_summaries
            
            	Neighbor summary
            	**type**\:   :py:class:`BgpNeighborSummaries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries>`
            
            .. attribute:: bgp_table_version
            
            	BGP table version number
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: filter_list
            
            	Filter list entry statistics
            	**type**\:   :py:class:`FilterList <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.FilterList>`
            
            .. attribute:: path
            
            	Path entry statistics
            	**type**\:   :py:class:`Path <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Path>`
            
            .. attribute:: prefixes
            
            	Prefix entry statistics
            	**type**\:   :py:class:`Prefixes <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.Prefixes>`
            
            .. attribute:: route_map
            
            	Route map entry statistics
            	**type**\:   :py:class:`RouteMap <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.AddressFamilies.AddressFamily.RouteMap>`
            
            .. attribute:: router_id
            
            	Router ID
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
            
            	Total memory in use
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            

            """

            _prefix = 'bgp-ios-xe-oper'
            _revision = '2017-04-01'

            def __init__(self):
                super(BgpStateData.AddressFamilies.AddressFamily, self).__init__()

                self.yang_name = "address-family"
                self.yang_parent_name = "address-families"

                self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                self.vrf_name = YLeaf(YType.str, "vrf-name")

                self.bgp_table_version = YLeaf(YType.uint64, "bgp-table-version")

                self.router_id = YLeaf(YType.str, "router-id")

                self.routing_table_version = YLeaf(YType.uint64, "routing-table-version")

                self.total_memory = YLeaf(YType.uint64, "total-memory")

                self.activities = BgpStateData.AddressFamilies.AddressFamily.Activities()
                self.activities.parent = self
                self._children_name_map["activities"] = "activities"
                self._children_yang_names.add("activities")

                self.as_path = BgpStateData.AddressFamilies.AddressFamily.AsPath()
                self.as_path.parent = self
                self._children_name_map["as_path"] = "as-path"
                self._children_yang_names.add("as-path")

                self.bgp_neighbor_summaries = BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries()
                self.bgp_neighbor_summaries.parent = self
                self._children_name_map["bgp_neighbor_summaries"] = "bgp-neighbor-summaries"
                self._children_yang_names.add("bgp-neighbor-summaries")

                self.filter_list = BgpStateData.AddressFamilies.AddressFamily.FilterList()
                self.filter_list.parent = self
                self._children_name_map["filter_list"] = "filter-list"
                self._children_yang_names.add("filter-list")

                self.path = BgpStateData.AddressFamilies.AddressFamily.Path()
                self.path.parent = self
                self._children_name_map["path"] = "path"
                self._children_yang_names.add("path")

                self.prefixes = BgpStateData.AddressFamilies.AddressFamily.Prefixes()
                self.prefixes.parent = self
                self._children_name_map["prefixes"] = "prefixes"
                self._children_yang_names.add("prefixes")

                self.route_map = BgpStateData.AddressFamilies.AddressFamily.RouteMap()
                self.route_map.parent = self
                self._children_name_map["route_map"] = "route-map"
                self._children_yang_names.add("route-map")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("afi_safi",
                                "vrf_name",
                                "bgp_table_version",
                                "router_id",
                                "routing_table_version",
                                "total_memory") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BgpStateData.AddressFamilies.AddressFamily, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BgpStateData.AddressFamilies.AddressFamily, self).__setattr__(name, value)


            class Prefixes(Entity):
                """
                Prefix entry statistics
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Prefixes, self).__init__()

                    self.yang_name = "prefixes"
                    self.yang_parent_name = "address-family"

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_usage",
                                    "total_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.Prefixes, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.Prefixes, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_usage.is_set or
                        self.total_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_usage.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "prefixes" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-usage" or name == "total-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-usage"):
                        self.memory_usage = value
                        self.memory_usage.value_namespace = name_space
                        self.memory_usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix


            class Path(Entity):
                """
                Path entry statistics
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.Path, self).__init__()

                    self.yang_name = "path"
                    self.yang_parent_name = "address-family"

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_usage",
                                    "total_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.Path, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.Path, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_usage.is_set or
                        self.total_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_usage.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "path" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-usage" or name == "total-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-usage"):
                        self.memory_usage = value
                        self.memory_usage.value_namespace = name_space
                        self.memory_usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix


            class AsPath(Entity):
                """
                AS path entry statistics
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.AsPath, self).__init__()

                    self.yang_name = "as-path"
                    self.yang_parent_name = "address-family"

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_usage",
                                    "total_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.AsPath, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.AsPath, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_usage.is_set or
                        self.total_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_usage.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "as-path" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-usage" or name == "total-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-usage"):
                        self.memory_usage = value
                        self.memory_usage.value_namespace = name_space
                        self.memory_usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix


            class RouteMap(Entity):
                """
                Route map entry statistics
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.RouteMap, self).__init__()

                    self.yang_name = "route-map"
                    self.yang_parent_name = "address-family"

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_usage",
                                    "total_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.RouteMap, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.RouteMap, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_usage.is_set or
                        self.total_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_usage.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "route-map" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-usage" or name == "total-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-usage"):
                        self.memory_usage = value
                        self.memory_usage.value_namespace = name_space
                        self.memory_usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix


            class FilterList(Entity):
                """
                Filter list entry statistics
                
                .. attribute:: memory_usage
                
                	Total memory usage in byte
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: total_entries
                
                	The total number of prefix entries
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'bgp-ios-xe-oper'
                _revision = '2017-04-01'

                def __init__(self):
                    super(BgpStateData.AddressFamilies.AddressFamily.FilterList, self).__init__()

                    self.yang_name = "filter-list"
                    self.yang_parent_name = "address-family"

                    self.memory_usage = YLeaf(YType.uint64, "memory-usage")

                    self.total_entries = YLeaf(YType.uint64, "total-entries")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("memory_usage",
                                    "total_entries") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.FilterList, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.FilterList, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.memory_usage.is_set or
                        self.total_entries.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.memory_usage.yfilter != YFilter.not_set or
                        self.total_entries.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "filter-list" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.memory_usage.is_set or self.memory_usage.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.memory_usage.get_name_leafdata())
                    if (self.total_entries.is_set or self.total_entries.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.total_entries.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "memory-usage" or name == "total-entries"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "memory-usage"):
                        self.memory_usage = value
                        self.memory_usage.value_namespace = name_space
                        self.memory_usage.value_namespace_prefix = name_space_prefix
                    if(value_path == "total-entries"):
                        self.total_entries = value
                        self.total_entries.value_namespace = name_space
                        self.total_entries.value_namespace_prefix = name_space_prefix


            class Activities(Entity):
                """
                BGP activity information
                
                .. attribute:: paths
                
                	Total number of paths
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: prefixes
                
                	Total number of prefixes
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

                    self.paths = YLeaf(YType.uint64, "paths")

                    self.prefixes = YLeaf(YType.uint64, "prefixes")

                    self.scan_interval = YLeaf(YType.str, "scan-interval")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("paths",
                                    "prefixes",
                                    "scan_interval") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(BgpStateData.AddressFamilies.AddressFamily.Activities, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.Activities, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.paths.is_set or
                        self.prefixes.is_set or
                        self.scan_interval.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.paths.yfilter != YFilter.not_set or
                        self.prefixes.yfilter != YFilter.not_set or
                        self.scan_interval.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "activities" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.paths.is_set or self.paths.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.paths.get_name_leafdata())
                    if (self.prefixes.is_set or self.prefixes.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.prefixes.get_name_leafdata())
                    if (self.scan_interval.is_set or self.scan_interval.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.scan_interval.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "paths" or name == "prefixes" or name == "scan-interval"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "paths"):
                        self.paths = value
                        self.paths.value_namespace = name_space
                        self.paths.value_namespace_prefix = name_space_prefix
                    if(value_path == "prefixes"):
                        self.prefixes = value
                        self.prefixes.value_namespace = name_space
                        self.prefixes.value_namespace_prefix = name_space_prefix
                    if(value_path == "scan-interval"):
                        self.scan_interval = value
                        self.scan_interval.value_namespace = name_space
                        self.scan_interval.value_namespace_prefix = name_space_prefix


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

                    self.bgp_neighbor_summary = YList(self)

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
                                super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries, self).__setattr__(name, value)


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
                    
                    .. attribute:: dynamically_configured
                    
                    	Indication of whether the neighbor was dyanmically configured
                    	**type**\:  bool
                    
                    .. attribute:: input_queue
                    
                    	Number of messages in input queue
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_received
                    
                    	Number of messages received from this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: messages_sent
                    
                    	Number of messages sent to this neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: output_queue
                    
                    	Number of messages in output queue
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: prefixes_received
                    
                    	Number of prefixes received from the neighbor
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: state
                    
                    	BGP session state
                    	**type**\:   :py:class:`BgpFsmState <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpFsmState>`
                    
                    .. attribute:: table_version
                    
                    	BGP table version
                    	**type**\:  int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: up_time
                    
                    	Neighbor session uptime
                    	**type**\:  str
                    
                    

                    """

                    _prefix = 'bgp-ios-xe-oper'
                    _revision = '2017-04-01'

                    def __init__(self):
                        super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, self).__init__()

                        self.yang_name = "bgp-neighbor-summary"
                        self.yang_parent_name = "bgp-neighbor-summaries"

                        self.id = YLeaf(YType.str, "id")

                        self.bgp_version = YLeaf(YType.uint32, "bgp-version")

                        self.dynamically_configured = YLeaf(YType.boolean, "dynamically-configured")

                        self.input_queue = YLeaf(YType.uint64, "input-queue")

                        self.messages_received = YLeaf(YType.uint64, "messages-received")

                        self.messages_sent = YLeaf(YType.uint64, "messages-sent")

                        self.output_queue = YLeaf(YType.uint64, "output-queue")

                        self.prefixes_received = YLeaf(YType.uint64, "prefixes-received")

                        self.state = YLeaf(YType.enumeration, "state")

                        self.table_version = YLeaf(YType.uint64, "table-version")

                        self.up_time = YLeaf(YType.str, "up-time")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("id",
                                        "bgp_version",
                                        "dynamically_configured",
                                        "input_queue",
                                        "messages_received",
                                        "messages_sent",
                                        "output_queue",
                                        "prefixes_received",
                                        "state",
                                        "table_version",
                                        "up_time") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary, self).__setattr__(name, value)

                    def has_data(self):
                        return (
                            self.id.is_set or
                            self.bgp_version.is_set or
                            self.dynamically_configured.is_set or
                            self.input_queue.is_set or
                            self.messages_received.is_set or
                            self.messages_sent.is_set or
                            self.output_queue.is_set or
                            self.prefixes_received.is_set or
                            self.state.is_set or
                            self.table_version.is_set or
                            self.up_time.is_set)

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.bgp_version.yfilter != YFilter.not_set or
                            self.dynamically_configured.yfilter != YFilter.not_set or
                            self.input_queue.yfilter != YFilter.not_set or
                            self.messages_received.yfilter != YFilter.not_set or
                            self.messages_sent.yfilter != YFilter.not_set or
                            self.output_queue.yfilter != YFilter.not_set or
                            self.prefixes_received.yfilter != YFilter.not_set or
                            self.state.yfilter != YFilter.not_set or
                            self.table_version.yfilter != YFilter.not_set or
                            self.up_time.yfilter != YFilter.not_set)

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgp-neighbor-summary" + "[id='" + self.id.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.bgp_version.is_set or self.bgp_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.bgp_version.get_name_leafdata())
                        if (self.dynamically_configured.is_set or self.dynamically_configured.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dynamically_configured.get_name_leafdata())
                        if (self.input_queue.is_set or self.input_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.input_queue.get_name_leafdata())
                        if (self.messages_received.is_set or self.messages_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.messages_received.get_name_leafdata())
                        if (self.messages_sent.is_set or self.messages_sent.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.messages_sent.get_name_leafdata())
                        if (self.output_queue.is_set or self.output_queue.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.output_queue.get_name_leafdata())
                        if (self.prefixes_received.is_set or self.prefixes_received.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.prefixes_received.get_name_leafdata())
                        if (self.state.is_set or self.state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.state.get_name_leafdata())
                        if (self.table_version.is_set or self.table_version.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.table_version.get_name_leafdata())
                        if (self.up_time.is_set or self.up_time.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.up_time.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "id" or name == "bgp-version" or name == "dynamically-configured" or name == "input-queue" or name == "messages-received" or name == "messages-sent" or name == "output-queue" or name == "prefixes-received" or name == "state" or name == "table-version" or name == "up-time"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "bgp-version"):
                            self.bgp_version = value
                            self.bgp_version.value_namespace = name_space
                            self.bgp_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "dynamically-configured"):
                            self.dynamically_configured = value
                            self.dynamically_configured.value_namespace = name_space
                            self.dynamically_configured.value_namespace_prefix = name_space_prefix
                        if(value_path == "input-queue"):
                            self.input_queue = value
                            self.input_queue.value_namespace = name_space
                            self.input_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "messages-received"):
                            self.messages_received = value
                            self.messages_received.value_namespace = name_space
                            self.messages_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "messages-sent"):
                            self.messages_sent = value
                            self.messages_sent.value_namespace = name_space
                            self.messages_sent.value_namespace_prefix = name_space_prefix
                        if(value_path == "output-queue"):
                            self.output_queue = value
                            self.output_queue.value_namespace = name_space
                            self.output_queue.value_namespace_prefix = name_space_prefix
                        if(value_path == "prefixes-received"):
                            self.prefixes_received = value
                            self.prefixes_received.value_namespace = name_space
                            self.prefixes_received.value_namespace_prefix = name_space_prefix
                        if(value_path == "state"):
                            self.state = value
                            self.state.value_namespace = name_space
                            self.state.value_namespace_prefix = name_space_prefix
                        if(value_path == "table-version"):
                            self.table_version = value
                            self.table_version.value_namespace = name_space
                            self.table_version.value_namespace_prefix = name_space_prefix
                        if(value_path == "up-time"):
                            self.up_time = value
                            self.up_time.value_namespace = name_space
                            self.up_time.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bgp_neighbor_summary:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bgp_neighbor_summary:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgp-neighbor-summaries" + path_buffer

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

                    if (child_yang_name == "bgp-neighbor-summary"):
                        for c in self.bgp_neighbor_summary:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries.BgpNeighborSummary()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bgp_neighbor_summary.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-neighbor-summary"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.afi_safi.is_set or
                    self.vrf_name.is_set or
                    self.bgp_table_version.is_set or
                    self.router_id.is_set or
                    self.routing_table_version.is_set or
                    self.total_memory.is_set or
                    (self.activities is not None and self.activities.has_data()) or
                    (self.as_path is not None and self.as_path.has_data()) or
                    (self.bgp_neighbor_summaries is not None and self.bgp_neighbor_summaries.has_data()) or
                    (self.filter_list is not None and self.filter_list.has_data()) or
                    (self.path is not None and self.path.has_data()) or
                    (self.prefixes is not None and self.prefixes.has_data()) or
                    (self.route_map is not None and self.route_map.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.afi_safi.yfilter != YFilter.not_set or
                    self.vrf_name.yfilter != YFilter.not_set or
                    self.bgp_table_version.yfilter != YFilter.not_set or
                    self.router_id.yfilter != YFilter.not_set or
                    self.routing_table_version.yfilter != YFilter.not_set or
                    self.total_memory.yfilter != YFilter.not_set or
                    (self.activities is not None and self.activities.has_operation()) or
                    (self.as_path is not None and self.as_path.has_operation()) or
                    (self.bgp_neighbor_summaries is not None and self.bgp_neighbor_summaries.has_operation()) or
                    (self.filter_list is not None and self.filter_list.has_operation()) or
                    (self.path is not None and self.path.has_operation()) or
                    (self.prefixes is not None and self.prefixes.has_operation()) or
                    (self.route_map is not None and self.route_map.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "address-family" + "[afi-safi='" + self.afi_safi.get() + "']" + "[vrf-name='" + self.vrf_name.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/address-families/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.afi_safi.is_set or self.afi_safi.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.afi_safi.get_name_leafdata())
                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf_name.get_name_leafdata())
                if (self.bgp_table_version.is_set or self.bgp_table_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.bgp_table_version.get_name_leafdata())
                if (self.router_id.is_set or self.router_id.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.router_id.get_name_leafdata())
                if (self.routing_table_version.is_set or self.routing_table_version.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.routing_table_version.get_name_leafdata())
                if (self.total_memory.is_set or self.total_memory.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.total_memory.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "activities"):
                    if (self.activities is None):
                        self.activities = BgpStateData.AddressFamilies.AddressFamily.Activities()
                        self.activities.parent = self
                        self._children_name_map["activities"] = "activities"
                    return self.activities

                if (child_yang_name == "as-path"):
                    if (self.as_path is None):
                        self.as_path = BgpStateData.AddressFamilies.AddressFamily.AsPath()
                        self.as_path.parent = self
                        self._children_name_map["as_path"] = "as-path"
                    return self.as_path

                if (child_yang_name == "bgp-neighbor-summaries"):
                    if (self.bgp_neighbor_summaries is None):
                        self.bgp_neighbor_summaries = BgpStateData.AddressFamilies.AddressFamily.BgpNeighborSummaries()
                        self.bgp_neighbor_summaries.parent = self
                        self._children_name_map["bgp_neighbor_summaries"] = "bgp-neighbor-summaries"
                    return self.bgp_neighbor_summaries

                if (child_yang_name == "filter-list"):
                    if (self.filter_list is None):
                        self.filter_list = BgpStateData.AddressFamilies.AddressFamily.FilterList()
                        self.filter_list.parent = self
                        self._children_name_map["filter_list"] = "filter-list"
                    return self.filter_list

                if (child_yang_name == "path"):
                    if (self.path is None):
                        self.path = BgpStateData.AddressFamilies.AddressFamily.Path()
                        self.path.parent = self
                        self._children_name_map["path"] = "path"
                    return self.path

                if (child_yang_name == "prefixes"):
                    if (self.prefixes is None):
                        self.prefixes = BgpStateData.AddressFamilies.AddressFamily.Prefixes()
                        self.prefixes.parent = self
                        self._children_name_map["prefixes"] = "prefixes"
                    return self.prefixes

                if (child_yang_name == "route-map"):
                    if (self.route_map is None):
                        self.route_map = BgpStateData.AddressFamilies.AddressFamily.RouteMap()
                        self.route_map.parent = self
                        self._children_name_map["route_map"] = "route-map"
                    return self.route_map

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "activities" or name == "as-path" or name == "bgp-neighbor-summaries" or name == "filter-list" or name == "path" or name == "prefixes" or name == "route-map" or name == "afi-safi" or name == "vrf-name" or name == "bgp-table-version" or name == "router-id" or name == "routing-table-version" or name == "total-memory"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "afi-safi"):
                    self.afi_safi = value
                    self.afi_safi.value_namespace = name_space
                    self.afi_safi.value_namespace_prefix = name_space_prefix
                if(value_path == "vrf-name"):
                    self.vrf_name = value
                    self.vrf_name.value_namespace = name_space
                    self.vrf_name.value_namespace_prefix = name_space_prefix
                if(value_path == "bgp-table-version"):
                    self.bgp_table_version = value
                    self.bgp_table_version.value_namespace = name_space
                    self.bgp_table_version.value_namespace_prefix = name_space_prefix
                if(value_path == "router-id"):
                    self.router_id = value
                    self.router_id.value_namespace = name_space
                    self.router_id.value_namespace_prefix = name_space_prefix
                if(value_path == "routing-table-version"):
                    self.routing_table_version = value
                    self.routing_table_version.value_namespace = name_space
                    self.routing_table_version.value_namespace_prefix = name_space_prefix
                if(value_path == "total-memory"):
                    self.total_memory = value
                    self.total_memory.value_namespace = name_space
                    self.total_memory.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.address_family:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.address_family:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "address-families" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "address-family"):
                for c in self.address_family:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BgpStateData.AddressFamilies.AddressFamily()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.address_family.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "address-family"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


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

            self.bgp_route_vrf = YList(self)

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
                        super(BgpStateData.BgpRouteVrfs, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(BgpStateData.BgpRouteVrfs, self).__setattr__(name, value)


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

                self.vrf = YLeaf(YType.str, "vrf")

                self.bgp_route_afs = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs()
                self.bgp_route_afs.parent = self
                self._children_name_map["bgp_route_afs"] = "bgp-route-afs"
                self._children_yang_names.add("bgp-route-afs")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("vrf") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf, self).__setattr__(name, value)


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

                    self.bgp_route_af = YList(self)

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
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs, self).__setattr__(name, value)


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

                        self.afi_safi = YLeaf(YType.enumeration, "afi-safi")

                        self.bgp_route_filters = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters()
                        self.bgp_route_filters.parent = self
                        self._children_name_map["bgp_route_filters"] = "bgp-route-filters"
                        self._children_yang_names.add("bgp-route-filters")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("afi_safi") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf, self).__setattr__(name, value)


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

                            self.bgp_route_filter = YList(self)

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
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters, self).__setattr__(name, value)


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

                                self.route_filter = YLeaf(YType.enumeration, "route-filter")

                                self.bgp_route_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries()
                                self.bgp_route_entries.parent = self
                                self._children_name_map["bgp_route_entries"] = "bgp-route-entries"
                                self._children_yang_names.add("bgp-route-entries")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("route_filter") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter, self).__setattr__(name, value)


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

                                    self.bgp_route_entry = YList(self)

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
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries, self).__setattr__(name, value)


                                class BgpRouteEntry(Entity):
                                    """
                                    List of BGP route entries
                                    
                                    .. attribute:: prefix  <key>
                                    
                                    	Routing table entry prefix
                                    	**type**\:  str
                                    
                                    .. attribute:: advertised_to
                                    
                                    	Whom is thie prefix advertized to
                                    	**type**\:  str
                                    
                                    .. attribute:: available_paths
                                    
                                    	Number of paths available for BGP prefix
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: bgp_path_entries
                                    
                                    	Prefix next hop details
                                    	**type**\:   :py:class:`BgpPathEntries <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries>`
                                    
                                    .. attribute:: version
                                    
                                    	Routing table version
                                    	**type**\:  int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'bgp-ios-xe-oper'
                                    _revision = '2017-04-01'

                                    def __init__(self):
                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, self).__init__()

                                        self.yang_name = "bgp-route-entry"
                                        self.yang_parent_name = "bgp-route-entries"

                                        self.prefix = YLeaf(YType.str, "prefix")

                                        self.advertised_to = YLeaf(YType.str, "advertised-to")

                                        self.available_paths = YLeaf(YType.uint32, "available-paths")

                                        self.version = YLeaf(YType.uint32, "version")

                                        self.bgp_path_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries()
                                        self.bgp_path_entries.parent = self
                                        self._children_name_map["bgp_path_entries"] = "bgp-path-entries"
                                        self._children_yang_names.add("bgp-path-entries")

                                    def __setattr__(self, name, value):
                                        self._check_monkey_patching_error(name, value)
                                        with _handle_type_error():
                                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                    "Please use list append or extend method."
                                                                    .format(value))
                                            if isinstance(value, Enum.YLeaf):
                                                value = value.name
                                            if name in ("prefix",
                                                        "advertised_to",
                                                        "available_paths",
                                                        "version") and name in self.__dict__:
                                                if isinstance(value, YLeaf):
                                                    self.__dict__[name].set(value.get())
                                                elif isinstance(value, YLeafList):
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, self).__setattr__(name, value)
                                                else:
                                                    self.__dict__[name].set(value)
                                            else:
                                                if hasattr(value, "parent") and name != "parent":
                                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                        value.parent = self
                                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                                        value.parent = self
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry, self).__setattr__(name, value)


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

                                            self.bgp_path_entry = YList(self)

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
                                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, self).__setattr__(name, value)
                                                    else:
                                                        self.__dict__[name].set(value)
                                                else:
                                                    if hasattr(value, "parent") and name != "parent":
                                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                            value.parent = self
                                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                                            value.parent = self
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries, self).__setattr__(name, value)


                                        class BgpPathEntry(Entity):
                                            """
                                            List of prefix next hop details
                                            
                                            .. attribute:: nexthop  <key>
                                            
                                            	Next hop for this path
                                            	**type**\:  str
                                            
                                            .. attribute:: as_path
                                            
                                            	AS path
                                            	**type**\:  str
                                            
                                            .. attribute:: community
                                            
                                            	Community label for the path
                                            	**type**\:  str
                                            
                                            .. attribute:: local_pref
                                            
                                            	Local preference for this path
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: metric
                                            
                                            	Metric associated with the path
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            .. attribute:: origin
                                            
                                            	Path origin
                                            	**type**\:   :py:class:`BgpOriginCode <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpOriginCode>`
                                            
                                            .. attribute:: path_status
                                            
                                            	Path status
                                            	**type**\:   :py:class:`PathStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_oper.BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus>`
                                            
                                            .. attribute:: rpki_status
                                            
                                            	RPKI path status
                                            	**type**\:   :py:class:`BgpRpkiStatus <ydk.models.cisco_ios_xe.Cisco_IOS_XE_bgp_route_oper.BgpRpkiStatus>`
                                            
                                            .. attribute:: weight
                                            
                                            	Path weight
                                            	**type**\:  int
                                            
                                            	**range:** 0..4294967295
                                            
                                            

                                            """

                                            _prefix = 'bgp-ios-xe-oper'
                                            _revision = '2017-04-01'

                                            def __init__(self):
                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, self).__init__()

                                                self.yang_name = "bgp-path-entry"
                                                self.yang_parent_name = "bgp-path-entries"

                                                self.nexthop = YLeaf(YType.str, "nexthop")

                                                self.as_path = YLeaf(YType.str, "as-path")

                                                self.community = YLeaf(YType.str, "community")

                                                self.local_pref = YLeaf(YType.uint32, "local-pref")

                                                self.metric = YLeaf(YType.uint32, "metric")

                                                self.origin = YLeaf(YType.enumeration, "origin")

                                                self.rpki_status = YLeaf(YType.enumeration, "rpki-status")

                                                self.weight = YLeaf(YType.uint32, "weight")

                                                self.path_status = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus()
                                                self.path_status.parent = self
                                                self._children_name_map["path_status"] = "path-status"
                                                self._children_yang_names.add("path-status")

                                            def __setattr__(self, name, value):
                                                self._check_monkey_patching_error(name, value)
                                                with _handle_type_error():
                                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                            "Please use list append or extend method."
                                                                            .format(value))
                                                    if isinstance(value, Enum.YLeaf):
                                                        value = value.name
                                                    if name in ("nexthop",
                                                                "as_path",
                                                                "community",
                                                                "local_pref",
                                                                "metric",
                                                                "origin",
                                                                "rpki_status",
                                                                "weight") and name in self.__dict__:
                                                        if isinstance(value, YLeaf):
                                                            self.__dict__[name].set(value.get())
                                                        elif isinstance(value, YLeafList):
                                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, self).__setattr__(name, value)
                                                        else:
                                                            self.__dict__[name].set(value)
                                                    else:
                                                        if hasattr(value, "parent") and name != "parent":
                                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                value.parent = self
                                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                value.parent = self
                                                        super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry, self).__setattr__(name, value)


                                            class PathStatus(Entity):
                                                """
                                                Path status
                                                
                                                .. attribute:: additional_path
                                                
                                                	Additional path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: backup_path
                                                
                                                	Backup path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: best_external
                                                
                                                	Best externa path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: bestpath
                                                
                                                	Best path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: damped
                                                
                                                	Damped path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: history
                                                
                                                	History path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: internal
                                                
                                                	Internal path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: multipath
                                                
                                                	Multipath path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_compressed
                                                
                                                	RIB compressed path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rib_fail
                                                
                                                	RIB\-fail path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: rt_filter
                                                
                                                	RT filter path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: sourced
                                                
                                                	Sourced path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: stale
                                                
                                                	Stale path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: suppressed
                                                
                                                	Suppressed path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                .. attribute:: valid
                                                
                                                	Valid path
                                                	**type**\:  :py:class:`Empty<ydk.types.Empty>`
                                                
                                                

                                                """

                                                _prefix = 'bgp-ios-xe-oper'
                                                _revision = '2017-04-01'

                                                def __init__(self):
                                                    super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, self).__init__()

                                                    self.yang_name = "path-status"
                                                    self.yang_parent_name = "bgp-path-entry"

                                                    self.additional_path = YLeaf(YType.empty, "additional-path")

                                                    self.backup_path = YLeaf(YType.empty, "backup-path")

                                                    self.best_external = YLeaf(YType.empty, "best-external")

                                                    self.bestpath = YLeaf(YType.empty, "bestpath")

                                                    self.damped = YLeaf(YType.empty, "damped")

                                                    self.history = YLeaf(YType.empty, "history")

                                                    self.internal = YLeaf(YType.empty, "internal")

                                                    self.multipath = YLeaf(YType.empty, "multipath")

                                                    self.rib_compressed = YLeaf(YType.empty, "rib-compressed")

                                                    self.rib_fail = YLeaf(YType.empty, "rib-fail")

                                                    self.rt_filter = YLeaf(YType.empty, "rt-filter")

                                                    self.sourced = YLeaf(YType.empty, "sourced")

                                                    self.stale = YLeaf(YType.empty, "stale")

                                                    self.suppressed = YLeaf(YType.empty, "suppressed")

                                                    self.valid = YLeaf(YType.empty, "valid")

                                                def __setattr__(self, name, value):
                                                    self._check_monkey_patching_error(name, value)
                                                    with _handle_type_error():
                                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                                "Please use list append or extend method."
                                                                                .format(value))
                                                        if isinstance(value, Enum.YLeaf):
                                                            value = value.name
                                                        if name in ("additional_path",
                                                                    "backup_path",
                                                                    "best_external",
                                                                    "bestpath",
                                                                    "damped",
                                                                    "history",
                                                                    "internal",
                                                                    "multipath",
                                                                    "rib_compressed",
                                                                    "rib_fail",
                                                                    "rt_filter",
                                                                    "sourced",
                                                                    "stale",
                                                                    "suppressed",
                                                                    "valid") and name in self.__dict__:
                                                            if isinstance(value, YLeaf):
                                                                self.__dict__[name].set(value.get())
                                                            elif isinstance(value, YLeafList):
                                                                super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, self).__setattr__(name, value)
                                                            else:
                                                                self.__dict__[name].set(value)
                                                        else:
                                                            if hasattr(value, "parent") and name != "parent":
                                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                                    value.parent = self
                                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                                    value.parent = self
                                                            super(BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus, self).__setattr__(name, value)

                                                def has_data(self):
                                                    return (
                                                        self.additional_path.is_set or
                                                        self.backup_path.is_set or
                                                        self.best_external.is_set or
                                                        self.bestpath.is_set or
                                                        self.damped.is_set or
                                                        self.history.is_set or
                                                        self.internal.is_set or
                                                        self.multipath.is_set or
                                                        self.rib_compressed.is_set or
                                                        self.rib_fail.is_set or
                                                        self.rt_filter.is_set or
                                                        self.sourced.is_set or
                                                        self.stale.is_set or
                                                        self.suppressed.is_set or
                                                        self.valid.is_set)

                                                def has_operation(self):
                                                    return (
                                                        self.yfilter != YFilter.not_set or
                                                        self.additional_path.yfilter != YFilter.not_set or
                                                        self.backup_path.yfilter != YFilter.not_set or
                                                        self.best_external.yfilter != YFilter.not_set or
                                                        self.bestpath.yfilter != YFilter.not_set or
                                                        self.damped.yfilter != YFilter.not_set or
                                                        self.history.yfilter != YFilter.not_set or
                                                        self.internal.yfilter != YFilter.not_set or
                                                        self.multipath.yfilter != YFilter.not_set or
                                                        self.rib_compressed.yfilter != YFilter.not_set or
                                                        self.rib_fail.yfilter != YFilter.not_set or
                                                        self.rt_filter.yfilter != YFilter.not_set or
                                                        self.sourced.yfilter != YFilter.not_set or
                                                        self.stale.yfilter != YFilter.not_set or
                                                        self.suppressed.yfilter != YFilter.not_set or
                                                        self.valid.yfilter != YFilter.not_set)

                                                def get_segment_path(self):
                                                    path_buffer = ""
                                                    path_buffer = "path-status" + path_buffer

                                                    return path_buffer

                                                def get_entity_path(self, ancestor):
                                                    path_buffer = ""
                                                    if (ancestor is None):
                                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                    else:
                                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                    leaf_name_data = LeafDataList()
                                                    if (self.additional_path.is_set or self.additional_path.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.additional_path.get_name_leafdata())
                                                    if (self.backup_path.is_set or self.backup_path.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.backup_path.get_name_leafdata())
                                                    if (self.best_external.is_set or self.best_external.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.best_external.get_name_leafdata())
                                                    if (self.bestpath.is_set or self.bestpath.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.bestpath.get_name_leafdata())
                                                    if (self.damped.is_set or self.damped.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.damped.get_name_leafdata())
                                                    if (self.history.is_set or self.history.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.history.get_name_leafdata())
                                                    if (self.internal.is_set or self.internal.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.internal.get_name_leafdata())
                                                    if (self.multipath.is_set or self.multipath.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.multipath.get_name_leafdata())
                                                    if (self.rib_compressed.is_set or self.rib_compressed.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rib_compressed.get_name_leafdata())
                                                    if (self.rib_fail.is_set or self.rib_fail.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rib_fail.get_name_leafdata())
                                                    if (self.rt_filter.is_set or self.rt_filter.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.rt_filter.get_name_leafdata())
                                                    if (self.sourced.is_set or self.sourced.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.sourced.get_name_leafdata())
                                                    if (self.stale.is_set or self.stale.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.stale.get_name_leafdata())
                                                    if (self.suppressed.is_set or self.suppressed.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.suppressed.get_name_leafdata())
                                                    if (self.valid.is_set or self.valid.yfilter != YFilter.not_set):
                                                        leaf_name_data.append(self.valid.get_name_leafdata())

                                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                                    return entity_path

                                                def get_child_by_name(self, child_yang_name, segment_path):
                                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                    if child is not None:
                                                        return child

                                                    return None

                                                def has_leaf_or_child_of_name(self, name):
                                                    if(name == "additional-path" or name == "backup-path" or name == "best-external" or name == "bestpath" or name == "damped" or name == "history" or name == "internal" or name == "multipath" or name == "rib-compressed" or name == "rib-fail" or name == "rt-filter" or name == "sourced" or name == "stale" or name == "suppressed" or name == "valid"):
                                                        return True
                                                    return False

                                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                                    if(value_path == "additional-path"):
                                                        self.additional_path = value
                                                        self.additional_path.value_namespace = name_space
                                                        self.additional_path.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "backup-path"):
                                                        self.backup_path = value
                                                        self.backup_path.value_namespace = name_space
                                                        self.backup_path.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "best-external"):
                                                        self.best_external = value
                                                        self.best_external.value_namespace = name_space
                                                        self.best_external.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "bestpath"):
                                                        self.bestpath = value
                                                        self.bestpath.value_namespace = name_space
                                                        self.bestpath.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "damped"):
                                                        self.damped = value
                                                        self.damped.value_namespace = name_space
                                                        self.damped.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "history"):
                                                        self.history = value
                                                        self.history.value_namespace = name_space
                                                        self.history.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "internal"):
                                                        self.internal = value
                                                        self.internal.value_namespace = name_space
                                                        self.internal.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "multipath"):
                                                        self.multipath = value
                                                        self.multipath.value_namespace = name_space
                                                        self.multipath.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rib-compressed"):
                                                        self.rib_compressed = value
                                                        self.rib_compressed.value_namespace = name_space
                                                        self.rib_compressed.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rib-fail"):
                                                        self.rib_fail = value
                                                        self.rib_fail.value_namespace = name_space
                                                        self.rib_fail.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "rt-filter"):
                                                        self.rt_filter = value
                                                        self.rt_filter.value_namespace = name_space
                                                        self.rt_filter.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "sourced"):
                                                        self.sourced = value
                                                        self.sourced.value_namespace = name_space
                                                        self.sourced.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "stale"):
                                                        self.stale = value
                                                        self.stale.value_namespace = name_space
                                                        self.stale.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "suppressed"):
                                                        self.suppressed = value
                                                        self.suppressed.value_namespace = name_space
                                                        self.suppressed.value_namespace_prefix = name_space_prefix
                                                    if(value_path == "valid"):
                                                        self.valid = value
                                                        self.valid.value_namespace = name_space
                                                        self.valid.value_namespace_prefix = name_space_prefix

                                            def has_data(self):
                                                return (
                                                    self.nexthop.is_set or
                                                    self.as_path.is_set or
                                                    self.community.is_set or
                                                    self.local_pref.is_set or
                                                    self.metric.is_set or
                                                    self.origin.is_set or
                                                    self.rpki_status.is_set or
                                                    self.weight.is_set or
                                                    (self.path_status is not None and self.path_status.has_data()))

                                            def has_operation(self):
                                                return (
                                                    self.yfilter != YFilter.not_set or
                                                    self.nexthop.yfilter != YFilter.not_set or
                                                    self.as_path.yfilter != YFilter.not_set or
                                                    self.community.yfilter != YFilter.not_set or
                                                    self.local_pref.yfilter != YFilter.not_set or
                                                    self.metric.yfilter != YFilter.not_set or
                                                    self.origin.yfilter != YFilter.not_set or
                                                    self.rpki_status.yfilter != YFilter.not_set or
                                                    self.weight.yfilter != YFilter.not_set or
                                                    (self.path_status is not None and self.path_status.has_operation()))

                                            def get_segment_path(self):
                                                path_buffer = ""
                                                path_buffer = "bgp-path-entry" + "[nexthop='" + self.nexthop.get() + "']" + path_buffer

                                                return path_buffer

                                            def get_entity_path(self, ancestor):
                                                path_buffer = ""
                                                if (ancestor is None):
                                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                                else:
                                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                                leaf_name_data = LeafDataList()
                                                if (self.nexthop.is_set or self.nexthop.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.nexthop.get_name_leafdata())
                                                if (self.as_path.is_set or self.as_path.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.as_path.get_name_leafdata())
                                                if (self.community.is_set or self.community.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.community.get_name_leafdata())
                                                if (self.local_pref.is_set or self.local_pref.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.local_pref.get_name_leafdata())
                                                if (self.metric.is_set or self.metric.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.metric.get_name_leafdata())
                                                if (self.origin.is_set or self.origin.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.origin.get_name_leafdata())
                                                if (self.rpki_status.is_set or self.rpki_status.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.rpki_status.get_name_leafdata())
                                                if (self.weight.is_set or self.weight.yfilter != YFilter.not_set):
                                                    leaf_name_data.append(self.weight.get_name_leafdata())

                                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                                return entity_path

                                            def get_child_by_name(self, child_yang_name, segment_path):
                                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                                if child is not None:
                                                    return child

                                                if (child_yang_name == "path-status"):
                                                    if (self.path_status is None):
                                                        self.path_status = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry.PathStatus()
                                                        self.path_status.parent = self
                                                        self._children_name_map["path_status"] = "path-status"
                                                    return self.path_status

                                                return None

                                            def has_leaf_or_child_of_name(self, name):
                                                if(name == "path-status" or name == "nexthop" or name == "as-path" or name == "community" or name == "local-pref" or name == "metric" or name == "origin" or name == "rpki-status" or name == "weight"):
                                                    return True
                                                return False

                                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                                if(value_path == "nexthop"):
                                                    self.nexthop = value
                                                    self.nexthop.value_namespace = name_space
                                                    self.nexthop.value_namespace_prefix = name_space_prefix
                                                if(value_path == "as-path"):
                                                    self.as_path = value
                                                    self.as_path.value_namespace = name_space
                                                    self.as_path.value_namespace_prefix = name_space_prefix
                                                if(value_path == "community"):
                                                    self.community = value
                                                    self.community.value_namespace = name_space
                                                    self.community.value_namespace_prefix = name_space_prefix
                                                if(value_path == "local-pref"):
                                                    self.local_pref = value
                                                    self.local_pref.value_namespace = name_space
                                                    self.local_pref.value_namespace_prefix = name_space_prefix
                                                if(value_path == "metric"):
                                                    self.metric = value
                                                    self.metric.value_namespace = name_space
                                                    self.metric.value_namespace_prefix = name_space_prefix
                                                if(value_path == "origin"):
                                                    self.origin = value
                                                    self.origin.value_namespace = name_space
                                                    self.origin.value_namespace_prefix = name_space_prefix
                                                if(value_path == "rpki-status"):
                                                    self.rpki_status = value
                                                    self.rpki_status.value_namespace = name_space
                                                    self.rpki_status.value_namespace_prefix = name_space_prefix
                                                if(value_path == "weight"):
                                                    self.weight = value
                                                    self.weight.value_namespace = name_space
                                                    self.weight.value_namespace_prefix = name_space_prefix

                                        def has_data(self):
                                            for c in self.bgp_path_entry:
                                                if (c.has_data()):
                                                    return True
                                            return False

                                        def has_operation(self):
                                            for c in self.bgp_path_entry:
                                                if (c.has_operation()):
                                                    return True
                                            return self.yfilter != YFilter.not_set

                                        def get_segment_path(self):
                                            path_buffer = ""
                                            path_buffer = "bgp-path-entries" + path_buffer

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

                                            if (child_yang_name == "bgp-path-entry"):
                                                for c in self.bgp_path_entry:
                                                    segment = c.get_segment_path()
                                                    if (segment_path == segment):
                                                        return c
                                                c = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries.BgpPathEntry()
                                                c.parent = self
                                                local_reference_key = "ydk::seg::%s" % segment_path
                                                self._local_refs[local_reference_key] = c
                                                self.bgp_path_entry.append(c)
                                                return c

                                            return None

                                        def has_leaf_or_child_of_name(self, name):
                                            if(name == "bgp-path-entry"):
                                                return True
                                            return False

                                        def set_value(self, value_path, value, name_space, name_space_prefix):
                                            pass

                                    def has_data(self):
                                        return (
                                            self.prefix.is_set or
                                            self.advertised_to.is_set or
                                            self.available_paths.is_set or
                                            self.version.is_set or
                                            (self.bgp_path_entries is not None and self.bgp_path_entries.has_data()))

                                    def has_operation(self):
                                        return (
                                            self.yfilter != YFilter.not_set or
                                            self.prefix.yfilter != YFilter.not_set or
                                            self.advertised_to.yfilter != YFilter.not_set or
                                            self.available_paths.yfilter != YFilter.not_set or
                                            self.version.yfilter != YFilter.not_set or
                                            (self.bgp_path_entries is not None and self.bgp_path_entries.has_operation()))

                                    def get_segment_path(self):
                                        path_buffer = ""
                                        path_buffer = "bgp-route-entry" + "[prefix='" + self.prefix.get() + "']" + path_buffer

                                        return path_buffer

                                    def get_entity_path(self, ancestor):
                                        path_buffer = ""
                                        if (ancestor is None):
                                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                        else:
                                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                        leaf_name_data = LeafDataList()
                                        if (self.prefix.is_set or self.prefix.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.prefix.get_name_leafdata())
                                        if (self.advertised_to.is_set or self.advertised_to.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.advertised_to.get_name_leafdata())
                                        if (self.available_paths.is_set or self.available_paths.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.available_paths.get_name_leafdata())
                                        if (self.version.is_set or self.version.yfilter != YFilter.not_set):
                                            leaf_name_data.append(self.version.get_name_leafdata())

                                        entity_path = EntityPath(path_buffer, leaf_name_data)
                                        return entity_path

                                    def get_child_by_name(self, child_yang_name, segment_path):
                                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                        if child is not None:
                                            return child

                                        if (child_yang_name == "bgp-path-entries"):
                                            if (self.bgp_path_entries is None):
                                                self.bgp_path_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry.BgpPathEntries()
                                                self.bgp_path_entries.parent = self
                                                self._children_name_map["bgp_path_entries"] = "bgp-path-entries"
                                            return self.bgp_path_entries

                                        return None

                                    def has_leaf_or_child_of_name(self, name):
                                        if(name == "bgp-path-entries" or name == "prefix" or name == "advertised-to" or name == "available-paths" or name == "version"):
                                            return True
                                        return False

                                    def set_value(self, value_path, value, name_space, name_space_prefix):
                                        if(value_path == "prefix"):
                                            self.prefix = value
                                            self.prefix.value_namespace = name_space
                                            self.prefix.value_namespace_prefix = name_space_prefix
                                        if(value_path == "advertised-to"):
                                            self.advertised_to = value
                                            self.advertised_to.value_namespace = name_space
                                            self.advertised_to.value_namespace_prefix = name_space_prefix
                                        if(value_path == "available-paths"):
                                            self.available_paths = value
                                            self.available_paths.value_namespace = name_space
                                            self.available_paths.value_namespace_prefix = name_space_prefix
                                        if(value_path == "version"):
                                            self.version = value
                                            self.version.value_namespace = name_space
                                            self.version.value_namespace_prefix = name_space_prefix

                                def has_data(self):
                                    for c in self.bgp_route_entry:
                                        if (c.has_data()):
                                            return True
                                    return False

                                def has_operation(self):
                                    for c in self.bgp_route_entry:
                                        if (c.has_operation()):
                                            return True
                                    return self.yfilter != YFilter.not_set

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "bgp-route-entries" + path_buffer

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

                                    if (child_yang_name == "bgp-route-entry"):
                                        for c in self.bgp_route_entry:
                                            segment = c.get_segment_path()
                                            if (segment_path == segment):
                                                return c
                                        c = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries.BgpRouteEntry()
                                        c.parent = self
                                        local_reference_key = "ydk::seg::%s" % segment_path
                                        self._local_refs[local_reference_key] = c
                                        self.bgp_route_entry.append(c)
                                        return c

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "bgp-route-entry"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    pass

                            def has_data(self):
                                return (
                                    self.route_filter.is_set or
                                    (self.bgp_route_entries is not None and self.bgp_route_entries.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.route_filter.yfilter != YFilter.not_set or
                                    (self.bgp_route_entries is not None and self.bgp_route_entries.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "bgp-route-filter" + "[route-filter='" + self.route_filter.get() + "']" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.route_filter.is_set or self.route_filter.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.route_filter.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "bgp-route-entries"):
                                    if (self.bgp_route_entries is None):
                                        self.bgp_route_entries = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter.BgpRouteEntries()
                                        self.bgp_route_entries.parent = self
                                        self._children_name_map["bgp_route_entries"] = "bgp-route-entries"
                                    return self.bgp_route_entries

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "bgp-route-entries" or name == "route-filter"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "route-filter"):
                                    self.route_filter = value
                                    self.route_filter.value_namespace = name_space
                                    self.route_filter.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            for c in self.bgp_route_filter:
                                if (c.has_data()):
                                    return True
                            return False

                        def has_operation(self):
                            for c in self.bgp_route_filter:
                                if (c.has_operation()):
                                    return True
                            return self.yfilter != YFilter.not_set

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "bgp-route-filters" + path_buffer

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

                            if (child_yang_name == "bgp-route-filter"):
                                for c in self.bgp_route_filter:
                                    segment = c.get_segment_path()
                                    if (segment_path == segment):
                                        return c
                                c = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters.BgpRouteFilter()
                                c.parent = self
                                local_reference_key = "ydk::seg::%s" % segment_path
                                self._local_refs[local_reference_key] = c
                                self.bgp_route_filter.append(c)
                                return c

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "bgp-route-filter"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            pass

                    def has_data(self):
                        return (
                            self.afi_safi.is_set or
                            (self.bgp_route_filters is not None and self.bgp_route_filters.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.afi_safi.yfilter != YFilter.not_set or
                            (self.bgp_route_filters is not None and self.bgp_route_filters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "bgp-route-af" + "[afi-safi='" + self.afi_safi.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.afi_safi.is_set or self.afi_safi.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.afi_safi.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "bgp-route-filters"):
                            if (self.bgp_route_filters is None):
                                self.bgp_route_filters = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf.BgpRouteFilters()
                                self.bgp_route_filters.parent = self
                                self._children_name_map["bgp_route_filters"] = "bgp-route-filters"
                            return self.bgp_route_filters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "bgp-route-filters" or name == "afi-safi"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "afi-safi"):
                            self.afi_safi = value
                            self.afi_safi.value_namespace = name_space
                            self.afi_safi.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.bgp_route_af:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.bgp_route_af:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "bgp-route-afs" + path_buffer

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

                    if (child_yang_name == "bgp-route-af"):
                        for c in self.bgp_route_af:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs.BgpRouteAf()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.bgp_route_af.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "bgp-route-af"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.vrf.is_set or
                    (self.bgp_route_afs is not None and self.bgp_route_afs.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.vrf.yfilter != YFilter.not_set or
                    (self.bgp_route_afs is not None and self.bgp_route_afs.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "bgp-route-vrf" + "[vrf='" + self.vrf.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/bgp-route-vrfs/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.vrf.is_set or self.vrf.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.vrf.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "bgp-route-afs"):
                    if (self.bgp_route_afs is None):
                        self.bgp_route_afs = BgpStateData.BgpRouteVrfs.BgpRouteVrf.BgpRouteAfs()
                        self.bgp_route_afs.parent = self
                        self._children_name_map["bgp_route_afs"] = "bgp-route-afs"
                    return self.bgp_route_afs

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "bgp-route-afs" or name == "vrf"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "vrf"):
                    self.vrf = value
                    self.vrf.value_namespace = name_space
                    self.vrf.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.bgp_route_vrf:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.bgp_route_vrf:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "bgp-route-vrfs" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "bgp-route-vrf"):
                for c in self.bgp_route_vrf:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = BgpStateData.BgpRouteVrfs.BgpRouteVrf()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.bgp_route_vrf.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "bgp-route-vrf"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.address_families is not None and self.address_families.has_data()) or
            (self.bgp_route_vrfs is not None and self.bgp_route_vrfs.has_data()) or
            (self.neighbors is not None and self.neighbors.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.address_families is not None and self.address_families.has_operation()) or
            (self.bgp_route_vrfs is not None and self.bgp_route_vrfs.has_operation()) or
            (self.neighbors is not None and self.neighbors.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XE-bgp-oper:bgp-state-data" + path_buffer

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

        if (child_yang_name == "address-families"):
            if (self.address_families is None):
                self.address_families = BgpStateData.AddressFamilies()
                self.address_families.parent = self
                self._children_name_map["address_families"] = "address-families"
            return self.address_families

        if (child_yang_name == "bgp-route-vrfs"):
            if (self.bgp_route_vrfs is None):
                self.bgp_route_vrfs = BgpStateData.BgpRouteVrfs()
                self.bgp_route_vrfs.parent = self
                self._children_name_map["bgp_route_vrfs"] = "bgp-route-vrfs"
            return self.bgp_route_vrfs

        if (child_yang_name == "neighbors"):
            if (self.neighbors is None):
                self.neighbors = BgpStateData.Neighbors()
                self.neighbors.parent = self
                self._children_name_map["neighbors"] = "neighbors"
            return self.neighbors

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "address-families" or name == "bgp-route-vrfs" or name == "neighbors"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = BgpStateData()
        return self._top_entity

