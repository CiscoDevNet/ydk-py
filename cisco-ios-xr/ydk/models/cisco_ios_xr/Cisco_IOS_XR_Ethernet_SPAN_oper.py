""" Cisco_IOS_XR_Ethernet_SPAN_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package operational data.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: Monitor Session operational data

Copyright (c) 2013\-2016 by Cisco Systems, Inc.
All rights reserved.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class DestinationClass(Enum):
    """
    DestinationClass

    Destination class

    .. data:: interface_class = 0

    	Destination is an interface

    .. data:: pseudowire_class = 1

    	Destination is a pseudowire

    .. data:: next_hop_ipv4_class = 2

    	Destination is a next-hop IPv4 address

    .. data:: next_hop_ipv6_class = 3

    	Destination is a next-hop IPv6 address

    .. data:: invalid_class = 255

    	Destination is not specified

    """

    interface_class = Enum.YLeaf(0, "interface-class")

    pseudowire_class = Enum.YLeaf(1, "pseudowire-class")

    next_hop_ipv4_class = Enum.YLeaf(2, "next-hop-ipv4-class")

    next_hop_ipv6_class = Enum.YLeaf(3, "next-hop-ipv6-class")

    invalid_class = Enum.YLeaf(255, "invalid-class")


class ImStateEnum(Enum):
    """
    ImStateEnum

    Im state enum

    .. data:: im_state_not_ready = 0

    	im state not ready

    .. data:: im_state_admin_down = 1

    	im state admin down

    .. data:: im_state_down = 2

    	im state down

    .. data:: im_state_up = 3

    	im state up

    .. data:: im_state_shutdown = 4

    	im state shutdown

    .. data:: im_state_err_disable = 5

    	im state err disable

    .. data:: im_state_down_immediate = 6

    	im state down immediate

    .. data:: im_state_down_immediate_admin = 7

    	im state down immediate admin

    .. data:: im_state_down_graceful = 8

    	im state down graceful

    .. data:: im_state_begin_shutdown = 9

    	im state begin shutdown

    .. data:: im_state_end_shutdown = 10

    	im state end shutdown

    .. data:: im_state_begin_error_disable = 11

    	im state begin error disable

    .. data:: im_state_end_error_disable = 12

    	im state end error disable

    .. data:: im_state_begin_down_graceful = 13

    	im state begin down graceful

    .. data:: im_state_reset = 14

    	im state reset

    .. data:: im_state_operational = 15

    	im state operational

    .. data:: im_state_not_operational = 16

    	im state not operational

    .. data:: im_state_unknown = 17

    	im state unknown

    .. data:: im_state_last = 18

    	im state last

    """

    im_state_not_ready = Enum.YLeaf(0, "im-state-not-ready")

    im_state_admin_down = Enum.YLeaf(1, "im-state-admin-down")

    im_state_down = Enum.YLeaf(2, "im-state-down")

    im_state_up = Enum.YLeaf(3, "im-state-up")

    im_state_shutdown = Enum.YLeaf(4, "im-state-shutdown")

    im_state_err_disable = Enum.YLeaf(5, "im-state-err-disable")

    im_state_down_immediate = Enum.YLeaf(6, "im-state-down-immediate")

    im_state_down_immediate_admin = Enum.YLeaf(7, "im-state-down-immediate-admin")

    im_state_down_graceful = Enum.YLeaf(8, "im-state-down-graceful")

    im_state_begin_shutdown = Enum.YLeaf(9, "im-state-begin-shutdown")

    im_state_end_shutdown = Enum.YLeaf(10, "im-state-end-shutdown")

    im_state_begin_error_disable = Enum.YLeaf(11, "im-state-begin-error-disable")

    im_state_end_error_disable = Enum.YLeaf(12, "im-state-end-error-disable")

    im_state_begin_down_graceful = Enum.YLeaf(13, "im-state-begin-down-graceful")

    im_state_reset = Enum.YLeaf(14, "im-state-reset")

    im_state_operational = Enum.YLeaf(15, "im-state-operational")

    im_state_not_operational = Enum.YLeaf(16, "im-state-not-operational")

    im_state_unknown = Enum.YLeaf(17, "im-state-unknown")

    im_state_last = Enum.YLeaf(18, "im-state-last")


class MirrorInterval(Enum):
    """
    MirrorInterval

    Monitor\-session mirror intervals

    .. data:: mirror_interval_all = 0

    	Mirror all packets

    .. data:: mirror_interval512 = 1

    	Mirror Interval 512

    .. data:: mirror_interval1k = 2

    	Mirror Interval 1K

    .. data:: mirror_interval2k = 3

    	Mirror Interval 2K

    .. data:: mirror_interval4k = 4

    	Mirror Interval 4K

    .. data:: mirror_interval8k = 5

    	Mirror Interval 8K

    .. data:: mirror_interval16k = 6

    	Mirror Interval 16K

    """

    mirror_interval_all = Enum.YLeaf(0, "mirror-interval-all")

    mirror_interval512 = Enum.YLeaf(1, "mirror-interval512")

    mirror_interval1k = Enum.YLeaf(2, "mirror-interval1k")

    mirror_interval2k = Enum.YLeaf(3, "mirror-interval2k")

    mirror_interval4k = Enum.YLeaf(4, "mirror-interval4k")

    mirror_interval8k = Enum.YLeaf(5, "mirror-interval8k")

    mirror_interval16k = Enum.YLeaf(6, "mirror-interval16k")


class SessionClass(Enum):
    """
    SessionClass

    Session class

    .. data:: ethernet_class = 0

    	Ethernet mirroring session

    .. data:: ipv4_class = 1

    	IPv4 mirroring session

    .. data:: ipv6_class = 2

    	IPv6 mirroring session

    .. data:: invalid_class = 65535

    	Invalid session class

    """

    ethernet_class = Enum.YLeaf(0, "ethernet-class")

    ipv4_class = Enum.YLeaf(1, "ipv4-class")

    ipv6_class = Enum.YLeaf(2, "ipv6-class")

    invalid_class = Enum.YLeaf(65535, "invalid-class")


class TrafficDirection(Enum):
    """
    TrafficDirection

    Monitor\-session traffic directions

    .. data:: invalid = 0

    	Invalid

    .. data:: rx_only = 1

    	Received

    .. data:: tx_only = 2

    	Transmitted

    .. data:: both = 3

    	Both

    """

    invalid = Enum.YLeaf(0, "invalid")

    rx_only = Enum.YLeaf(1, "rx-only")

    tx_only = Enum.YLeaf(2, "tx-only")

    both = Enum.YLeaf(3, "both")



class SpanMonitorSession(Entity):
    """
    Monitor Session operational data
    
    .. attribute:: global_
    
    	Global operational data
    	**type**\:   :py:class:`Global_ <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:   :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes>`
    
    

    """

    _prefix = 'ethernet-span-oper'
    _revision = '2015-11-09'

    def __init__(self):
        super(SpanMonitorSession, self).__init__()
        self._top_entity = None

        self.yang_name = "span-monitor-session"
        self.yang_parent_name = "Cisco-IOS-XR-Ethernet-SPAN-oper"

        self.global_ = SpanMonitorSession.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.nodes = SpanMonitorSession.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")


    class Global_(Entity):
        """
        Global operational data
        
        .. attribute:: global_sessions
        
        	Global Monitor Sessions table
        	**type**\:   :py:class:`GlobalSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions>`
        
        .. attribute:: statistics
        
        	Table of statistics for source interfaces
        	**type**\:   :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.Statistics>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Global_, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "span-monitor-session"

            self.global_sessions = SpanMonitorSession.Global_.GlobalSessions()
            self.global_sessions.parent = self
            self._children_name_map["global_sessions"] = "global-sessions"
            self._children_yang_names.add("global-sessions")

            self.statistics = SpanMonitorSession.Global_.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")


        class Statistics(Entity):
            """
            Table of statistics for source interfaces
            
            .. attribute:: statistic
            
            	Statistics for a particular source interface
            	**type**\: list of    :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.Statistics.Statistic>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Global_.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "global"

                self.statistic = YList(self)

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
                            super(SpanMonitorSession.Global_.Statistics, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SpanMonitorSession.Global_.Statistics, self).__setattr__(name, value)


            class Statistic(Entity):
                """
                Statistics for a particular source interface
                
                .. attribute:: session  <key>
                
                	Session Name
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: interface  <key>
                
                	Interface
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: octets_not_mirrored
                
                	Octets Not Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_not_mirrored
                
                	Packets Not Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_octets_mirrored
                
                	RX Octets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_packets_mirrored
                
                	RX Packets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_octets_mirrored
                
                	TX Octets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets_mirrored
                
                	TX Packets Mirrored
                	**type**\:  int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Global_.Statistics.Statistic, self).__init__()

                    self.yang_name = "statistic"
                    self.yang_parent_name = "statistics"

                    self.session = YLeaf(YType.str, "session")

                    self.interface = YLeaf(YType.str, "interface")

                    self.octets_not_mirrored = YLeaf(YType.uint64, "octets-not-mirrored")

                    self.packets_not_mirrored = YLeaf(YType.uint64, "packets-not-mirrored")

                    self.rx_octets_mirrored = YLeaf(YType.uint64, "rx-octets-mirrored")

                    self.rx_packets_mirrored = YLeaf(YType.uint64, "rx-packets-mirrored")

                    self.tx_octets_mirrored = YLeaf(YType.uint64, "tx-octets-mirrored")

                    self.tx_packets_mirrored = YLeaf(YType.uint64, "tx-packets-mirrored")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("session",
                                    "interface",
                                    "octets_not_mirrored",
                                    "packets_not_mirrored",
                                    "rx_octets_mirrored",
                                    "rx_packets_mirrored",
                                    "tx_octets_mirrored",
                                    "tx_packets_mirrored") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SpanMonitorSession.Global_.Statistics.Statistic, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Global_.Statistics.Statistic, self).__setattr__(name, value)

                def has_data(self):
                    return (
                        self.session.is_set or
                        self.interface.is_set or
                        self.octets_not_mirrored.is_set or
                        self.packets_not_mirrored.is_set or
                        self.rx_octets_mirrored.is_set or
                        self.rx_packets_mirrored.is_set or
                        self.tx_octets_mirrored.is_set or
                        self.tx_packets_mirrored.is_set)

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.session.yfilter != YFilter.not_set or
                        self.interface.yfilter != YFilter.not_set or
                        self.octets_not_mirrored.yfilter != YFilter.not_set or
                        self.packets_not_mirrored.yfilter != YFilter.not_set or
                        self.rx_octets_mirrored.yfilter != YFilter.not_set or
                        self.rx_packets_mirrored.yfilter != YFilter.not_set or
                        self.tx_octets_mirrored.yfilter != YFilter.not_set or
                        self.tx_packets_mirrored.yfilter != YFilter.not_set)

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "statistic" + "[session='" + self.session.get() + "']" + "[interface='" + self.interface.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/statistics/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.session.is_set or self.session.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session.get_name_leafdata())
                    if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface.get_name_leafdata())
                    if (self.octets_not_mirrored.is_set or self.octets_not_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.octets_not_mirrored.get_name_leafdata())
                    if (self.packets_not_mirrored.is_set or self.packets_not_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.packets_not_mirrored.get_name_leafdata())
                    if (self.rx_octets_mirrored.is_set or self.rx_octets_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_octets_mirrored.get_name_leafdata())
                    if (self.rx_packets_mirrored.is_set or self.rx_packets_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.rx_packets_mirrored.get_name_leafdata())
                    if (self.tx_octets_mirrored.is_set or self.tx_octets_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_octets_mirrored.get_name_leafdata())
                    if (self.tx_packets_mirrored.is_set or self.tx_packets_mirrored.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.tx_packets_mirrored.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "session" or name == "interface" or name == "octets-not-mirrored" or name == "packets-not-mirrored" or name == "rx-octets-mirrored" or name == "rx-packets-mirrored" or name == "tx-octets-mirrored" or name == "tx-packets-mirrored"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "session"):
                        self.session = value
                        self.session.value_namespace = name_space
                        self.session.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface"):
                        self.interface = value
                        self.interface.value_namespace = name_space
                        self.interface.value_namespace_prefix = name_space_prefix
                    if(value_path == "octets-not-mirrored"):
                        self.octets_not_mirrored = value
                        self.octets_not_mirrored.value_namespace = name_space
                        self.octets_not_mirrored.value_namespace_prefix = name_space_prefix
                    if(value_path == "packets-not-mirrored"):
                        self.packets_not_mirrored = value
                        self.packets_not_mirrored.value_namespace = name_space
                        self.packets_not_mirrored.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-octets-mirrored"):
                        self.rx_octets_mirrored = value
                        self.rx_octets_mirrored.value_namespace = name_space
                        self.rx_octets_mirrored.value_namespace_prefix = name_space_prefix
                    if(value_path == "rx-packets-mirrored"):
                        self.rx_packets_mirrored = value
                        self.rx_packets_mirrored.value_namespace = name_space
                        self.rx_packets_mirrored.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-octets-mirrored"):
                        self.tx_octets_mirrored = value
                        self.tx_octets_mirrored.value_namespace = name_space
                        self.tx_octets_mirrored.value_namespace_prefix = name_space_prefix
                    if(value_path == "tx-packets-mirrored"):
                        self.tx_packets_mirrored = value
                        self.tx_packets_mirrored.value_namespace = name_space
                        self.tx_packets_mirrored.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.statistic:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.statistic:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "statistics" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "statistic"):
                    for c in self.statistic:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = SpanMonitorSession.Global_.Statistics.Statistic()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.statistic.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "statistic"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass


        class GlobalSessions(Entity):
            """
            Global Monitor Sessions table
            
            .. attribute:: global_session
            
            	Information about a globally\-configured monitor session
            	**type**\: list of    :py:class:`GlobalSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Global_.GlobalSessions, self).__init__()

                self.yang_name = "global-sessions"
                self.yang_parent_name = "global"

                self.global_session = YList(self)

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
                            super(SpanMonitorSession.Global_.GlobalSessions, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SpanMonitorSession.Global_.GlobalSessions, self).__setattr__(name, value)


            class GlobalSession(Entity):
                """
                Information about a globally\-configured
                monitor session
                
                .. attribute:: session  <key>
                
                	Session Name
                	**type**\:  str
                
                	**length:** 1..79
                
                .. attribute:: destination_data
                
                	Destination data
                	**type**\:   :py:class:`DestinationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData>`
                
                .. attribute:: destination_error
                
                	Last error observed for the destination 
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_id
                
                	Destination ID
                	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId>`
                
                .. attribute:: destination_interface_handle
                
                	Destination interface handle (deprecated by DestinationID, invalid for pseudowires)
                	**type**\:  str
                
                	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                
                .. attribute:: destination_interface_name
                
                	Destination interface name (deprecated by DestinationData, invalid for pseudowires)
                	**type**\:  str
                
                .. attribute:: id
                
                	Numerical ID assigned to session
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: interface_error
                
                	Last error observed for the destination interface (deprecated by DestinationError)
                	**type**\:  int
                
                	**range:** 0..4294967295
                
                .. attribute:: name
                
                	Session Name
                	**type**\:  str
                
                .. attribute:: session_class
                
                	Session class
                	**type**\:   :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession, self).__init__()

                    self.yang_name = "global-session"
                    self.yang_parent_name = "global-sessions"

                    self.session = YLeaf(YType.str, "session")

                    self.destination_error = YLeaf(YType.uint32, "destination-error")

                    self.destination_interface_handle = YLeaf(YType.str, "destination-interface-handle")

                    self.destination_interface_name = YLeaf(YType.str, "destination-interface-name")

                    self.id = YLeaf(YType.uint32, "id")

                    self.interface_error = YLeaf(YType.uint32, "interface-error")

                    self.name = YLeaf(YType.str, "name")

                    self.session_class = YLeaf(YType.enumeration, "session-class")

                    self.destination_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData()
                    self.destination_data.parent = self
                    self._children_name_map["destination_data"] = "destination-data"
                    self._children_yang_names.add("destination-data")

                    self.destination_id = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId()
                    self.destination_id.parent = self
                    self._children_name_map["destination_id"] = "destination-id"
                    self._children_yang_names.add("destination-id")

                def __setattr__(self, name, value):
                    self._check_monkey_patching_error(name, value)
                    with _handle_type_error():
                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                "Please use list append or extend method."
                                                .format(value))
                        if isinstance(value, Enum.YLeaf):
                            value = value.name
                        if name in ("session",
                                    "destination_error",
                                    "destination_interface_handle",
                                    "destination_interface_name",
                                    "id",
                                    "interface_error",
                                    "name",
                                    "session_class") and name in self.__dict__:
                            if isinstance(value, YLeaf):
                                self.__dict__[name].set(value.get())
                            elif isinstance(value, YLeafList):
                                super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession, self).__setattr__(name, value)


                class DestinationData(Entity):
                    """
                    Destination data
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                    
                    .. attribute:: interface_data
                    
                    	Interface data
                    	**type**\:   :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData>`
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: next_hop_ipv4_data
                    
                    	Next\-hop IPv4 data
                    	**type**\:   :py:class:`NextHopIpv4Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data>`
                    
                    .. attribute:: next_hop_ipv6_data
                    
                    	Next\-hop IPv6 data
                    	**type**\:   :py:class:`NextHopIpv6Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data>`
                    
                    .. attribute:: pseudowire_data
                    
                    	Pseudowire data
                    	**type**\:   :py:class:`PseudowireData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData, self).__init__()

                        self.yang_name = "destination-data"
                        self.yang_parent_name = "global-session"

                        self.destination_class = YLeaf(YType.enumeration, "destination-class")

                        self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                        self.interface_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData()
                        self.interface_data.parent = self
                        self._children_name_map["interface_data"] = "interface-data"
                        self._children_yang_names.add("interface-data")

                        self.next_hop_ipv4_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data()
                        self.next_hop_ipv4_data.parent = self
                        self._children_name_map["next_hop_ipv4_data"] = "next-hop-ipv4-data"
                        self._children_yang_names.add("next-hop-ipv4-data")

                        self.next_hop_ipv6_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data()
                        self.next_hop_ipv6_data.parent = self
                        self._children_name_map["next_hop_ipv6_data"] = "next-hop-ipv6-data"
                        self._children_yang_names.add("next-hop-ipv6-data")

                        self.pseudowire_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData()
                        self.pseudowire_data.parent = self
                        self._children_name_map["pseudowire_data"] = "pseudowire-data"
                        self._children_yang_names.add("pseudowire-data")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_class",
                                        "invalid_value") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData, self).__setattr__(name, value)


                    class InterfaceData(Entity):
                        """
                        Interface data
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\:  str
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData, self).__init__()

                            self.yang_name = "interface-data"
                            self.yang_parent_name = "destination-data"

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_state = YLeaf(YType.enumeration, "interface-state")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("interface_name",
                                            "interface_state") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.interface_name.is_set or
                                self.interface_state.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.interface_name.yfilter != YFilter.not_set or
                                self.interface_state.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "interface-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.interface_name.is_set or self.interface_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_name.get_name_leafdata())
                            if (self.interface_state.is_set or self.interface_state.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface_state.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "interface-name" or name == "interface-state"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "interface-name"):
                                self.interface_name = value
                                self.interface_name.value_namespace = name_space
                                self.interface_name.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface-state"):
                                self.interface_state = value
                                self.interface_state.value_namespace = name_space
                                self.interface_state.value_namespace_prefix = name_space_prefix


                    class PseudowireData(Entity):
                        """
                        Pseudowire data
                        
                        .. attribute:: pseudowire_is_up
                        
                        	Pseudowire State
                        	**type**\:  bool
                        
                        .. attribute:: pseudowire_name
                        
                        	Pseudowire Name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData, self).__init__()

                            self.yang_name = "pseudowire-data"
                            self.yang_parent_name = "destination-data"

                            self.pseudowire_is_up = YLeaf(YType.boolean, "pseudowire-is-up")

                            self.pseudowire_name = YLeaf(YType.str, "pseudowire-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("pseudowire_is_up",
                                            "pseudowire_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.pseudowire_is_up.is_set or
                                self.pseudowire_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.pseudowire_is_up.yfilter != YFilter.not_set or
                                self.pseudowire_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "pseudowire-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.pseudowire_is_up.is_set or self.pseudowire_is_up.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pseudowire_is_up.get_name_leafdata())
                            if (self.pseudowire_name.is_set or self.pseudowire_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pseudowire_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "pseudowire-is-up" or name == "pseudowire-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "pseudowire-is-up"):
                                self.pseudowire_is_up = value
                                self.pseudowire_is_up.value_namespace = name_space
                                self.pseudowire_is_up.value_namespace_prefix = name_space_prefix
                            if(value_path == "pseudowire-name"):
                                self.pseudowire_name = value
                                self.pseudowire_name.value_namespace = name_space
                                self.pseudowire_name.value_namespace_prefix = name_space_prefix


                    class NextHopIpv4Data(Entity):
                        """
                        Next\-hop IPv4 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\:  bool
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, self).__init__()

                            self.yang_name = "next-hop-ipv4-data"
                            self.yang_parent_name = "destination-data"

                            self.address_is_reachable = YLeaf(YType.boolean, "address-is-reachable")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address_is_reachable",
                                            "ipv4_address",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address_is_reachable.is_set or
                                self.ipv4_address.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address_is_reachable.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop-ipv4-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address_is_reachable.is_set or self.address_is_reachable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_is_reachable.get_name_leafdata())
                            if (self.ipv4_address.is_set or self.ipv4_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv4_address.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-is-reachable" or name == "ipv4-address" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address-is-reachable"):
                                self.address_is_reachable = value
                                self.address_is_reachable.value_namespace = name_space
                                self.address_is_reachable.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix


                    class NextHopIpv6Data(Entity):
                        """
                        Next\-hop IPv6 data
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\:  bool
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, self).__init__()

                            self.yang_name = "next-hop-ipv6-data"
                            self.yang_parent_name = "destination-data"

                            self.address_is_reachable = YLeaf(YType.boolean, "address-is-reachable")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("address_is_reachable",
                                            "ipv6_address",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.address_is_reachable.is_set or
                                self.ipv6_address.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.address_is_reachable.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "next-hop-ipv6-data" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.address_is_reachable.is_set or self.address_is_reachable.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.address_is_reachable.get_name_leafdata())
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "address-is-reachable" or name == "ipv6-address" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "address-is-reachable"):
                                self.address_is_reachable = value
                                self.address_is_reachable.value_namespace = name_space
                                self.address_is_reachable.value_namespace_prefix = name_space_prefix
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.destination_class.is_set or
                            self.invalid_value.is_set or
                            (self.interface_data is not None and self.interface_data.has_data()) or
                            (self.next_hop_ipv4_data is not None and self.next_hop_ipv4_data.has_data()) or
                            (self.next_hop_ipv6_data is not None and self.next_hop_ipv6_data.has_data()) or
                            (self.pseudowire_data is not None and self.pseudowire_data.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_class.yfilter != YFilter.not_set or
                            self.invalid_value.yfilter != YFilter.not_set or
                            (self.interface_data is not None and self.interface_data.has_operation()) or
                            (self.next_hop_ipv4_data is not None and self.next_hop_ipv4_data.has_operation()) or
                            (self.next_hop_ipv6_data is not None and self.next_hop_ipv6_data.has_operation()) or
                            (self.pseudowire_data is not None and self.pseudowire_data.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-data" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_class.get_name_leafdata())
                        if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_value.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "interface-data"):
                            if (self.interface_data is None):
                                self.interface_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData()
                                self.interface_data.parent = self
                                self._children_name_map["interface_data"] = "interface-data"
                            return self.interface_data

                        if (child_yang_name == "next-hop-ipv4-data"):
                            if (self.next_hop_ipv4_data is None):
                                self.next_hop_ipv4_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data()
                                self.next_hop_ipv4_data.parent = self
                                self._children_name_map["next_hop_ipv4_data"] = "next-hop-ipv4-data"
                            return self.next_hop_ipv4_data

                        if (child_yang_name == "next-hop-ipv6-data"):
                            if (self.next_hop_ipv6_data is None):
                                self.next_hop_ipv6_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data()
                                self.next_hop_ipv6_data.parent = self
                                self._children_name_map["next_hop_ipv6_data"] = "next-hop-ipv6-data"
                            return self.next_hop_ipv6_data

                        if (child_yang_name == "pseudowire-data"):
                            if (self.pseudowire_data is None):
                                self.pseudowire_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData()
                                self.pseudowire_data.parent = self
                                self._children_name_map["pseudowire_data"] = "pseudowire-data"
                            return self.pseudowire_data

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "interface-data" or name == "next-hop-ipv4-data" or name == "next-hop-ipv6-data" or name == "pseudowire-data" or name == "destination-class" or name == "invalid-value"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-class"):
                            self.destination_class = value
                            self.destination_class.value_namespace = name_space
                            self.destination_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-value"):
                            self.invalid_value = value
                            self.invalid_value.value_namespace = name_space
                            self.invalid_value.value_namespace_prefix = name_space_prefix


                class DestinationId(Entity):
                    """
                    Destination ID
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                    
                    .. attribute:: interface
                    
                    	Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: ipv4_address_and_vrf
                    
                    	IPv4 address
                    	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf>`
                    
                    .. attribute:: ipv6_address_and_vrf
                    
                    	IPv6 address
                    	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf>`
                    
                    .. attribute:: pseudowire_id
                    
                    	Pseudowire XCID
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId, self).__init__()

                        self.yang_name = "destination-id"
                        self.yang_parent_name = "global-session"

                        self.destination_class = YLeaf(YType.enumeration, "destination-class")

                        self.interface = YLeaf(YType.str, "interface")

                        self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                        self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                        self.ipv4_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf()
                        self.ipv4_address_and_vrf.parent = self
                        self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                        self._children_yang_names.add("ipv4-address-and-vrf")

                        self.ipv6_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf()
                        self.ipv6_address_and_vrf.parent = self
                        self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                        self._children_yang_names.add("ipv6-address-and-vrf")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_class",
                                        "interface",
                                        "invalid_value",
                                        "pseudowire_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId, self).__setattr__(name, value)


                    class Ipv4AddressAndVrf(Entity):
                        """
                        IPv4 address
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\:  str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, self).__init__()

                            self.yang_name = "ipv4-address-and-vrf"
                            self.yang_parent_name = "destination-id"

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ipv4_address.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv4_address.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv4-address-and-vrf" + path_buffer

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
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-address" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv4-address"):
                                self.ipv4_address = value
                                self.ipv4_address.value_namespace = name_space
                                self.ipv4_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix


                    class Ipv6AddressAndVrf(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\:  str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\:  str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, self).__init__()

                            self.yang_name = "ipv6-address-and-vrf"
                            self.yang_parent_name = "destination-id"

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("ipv6_address",
                                            "vrf_name") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.ipv6_address.is_set or
                                self.vrf_name.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.ipv6_address.yfilter != YFilter.not_set or
                                self.vrf_name.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "ipv6-address-and-vrf" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                            if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.vrf_name.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv6-address" or name == "vrf-name"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "ipv6-address"):
                                self.ipv6_address = value
                                self.ipv6_address.value_namespace = name_space
                                self.ipv6_address.value_namespace_prefix = name_space_prefix
                            if(value_path == "vrf-name"):
                                self.vrf_name = value
                                self.vrf_name.value_namespace = name_space
                                self.vrf_name.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.destination_class.is_set or
                            self.interface.is_set or
                            self.invalid_value.is_set or
                            self.pseudowire_id.is_set or
                            (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_data()) or
                            (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_class.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.invalid_value.yfilter != YFilter.not_set or
                            self.pseudowire_id.yfilter != YFilter.not_set or
                            (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_operation()) or
                            (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "destination-id" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_class.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.invalid_value.get_name_leafdata())
                        if (self.pseudowire_id.is_set or self.pseudowire_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pseudowire_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "ipv4-address-and-vrf"):
                            if (self.ipv4_address_and_vrf is None):
                                self.ipv4_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf()
                                self.ipv4_address_and_vrf.parent = self
                                self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                            return self.ipv4_address_and_vrf

                        if (child_yang_name == "ipv6-address-and-vrf"):
                            if (self.ipv6_address_and_vrf is None):
                                self.ipv6_address_and_vrf = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf()
                                self.ipv6_address_and_vrf.parent = self
                                self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            return self.ipv6_address_and_vrf

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "ipv4-address-and-vrf" or name == "ipv6-address-and-vrf" or name == "destination-class" or name == "interface" or name == "invalid-value" or name == "pseudowire-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-class"):
                            self.destination_class = value
                            self.destination_class.value_namespace = name_space
                            self.destination_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "invalid-value"):
                            self.invalid_value = value
                            self.invalid_value.value_namespace = name_space
                            self.invalid_value.value_namespace_prefix = name_space_prefix
                        if(value_path == "pseudowire-id"):
                            self.pseudowire_id = value
                            self.pseudowire_id.value_namespace = name_space
                            self.pseudowire_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    return (
                        self.session.is_set or
                        self.destination_error.is_set or
                        self.destination_interface_handle.is_set or
                        self.destination_interface_name.is_set or
                        self.id.is_set or
                        self.interface_error.is_set or
                        self.name.is_set or
                        self.session_class.is_set or
                        (self.destination_data is not None and self.destination_data.has_data()) or
                        (self.destination_id is not None and self.destination_id.has_data()))

                def has_operation(self):
                    return (
                        self.yfilter != YFilter.not_set or
                        self.session.yfilter != YFilter.not_set or
                        self.destination_error.yfilter != YFilter.not_set or
                        self.destination_interface_handle.yfilter != YFilter.not_set or
                        self.destination_interface_name.yfilter != YFilter.not_set or
                        self.id.yfilter != YFilter.not_set or
                        self.interface_error.yfilter != YFilter.not_set or
                        self.name.yfilter != YFilter.not_set or
                        self.session_class.yfilter != YFilter.not_set or
                        (self.destination_data is not None and self.destination_data.has_operation()) or
                        (self.destination_id is not None and self.destination_id.has_operation()))

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "global-session" + "[session='" + self.session.get() + "']" + path_buffer

                    return path_buffer

                def get_entity_path(self, ancestor):
                    path_buffer = ""
                    if (ancestor is None):
                        path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/global-sessions/%s" % self.get_segment_path()
                    else:
                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                    leaf_name_data = LeafDataList()
                    if (self.session.is_set or self.session.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session.get_name_leafdata())
                    if (self.destination_error.is_set or self.destination_error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_error.get_name_leafdata())
                    if (self.destination_interface_handle.is_set or self.destination_interface_handle.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_interface_handle.get_name_leafdata())
                    if (self.destination_interface_name.is_set or self.destination_interface_name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.destination_interface_name.get_name_leafdata())
                    if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.id.get_name_leafdata())
                    if (self.interface_error.is_set or self.interface_error.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.interface_error.get_name_leafdata())
                    if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.name.get_name_leafdata())
                    if (self.session_class.is_set or self.session_class.yfilter != YFilter.not_set):
                        leaf_name_data.append(self.session_class.get_name_leafdata())

                    entity_path = EntityPath(path_buffer, leaf_name_data)
                    return entity_path

                def get_child_by_name(self, child_yang_name, segment_path):
                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                    if child is not None:
                        return child

                    if (child_yang_name == "destination-data"):
                        if (self.destination_data is None):
                            self.destination_data = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData()
                            self.destination_data.parent = self
                            self._children_name_map["destination_data"] = "destination-data"
                        return self.destination_data

                    if (child_yang_name == "destination-id"):
                        if (self.destination_id is None):
                            self.destination_id = SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId()
                            self.destination_id.parent = self
                            self._children_name_map["destination_id"] = "destination-id"
                        return self.destination_id

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "destination-data" or name == "destination-id" or name == "session" or name == "destination-error" or name == "destination-interface-handle" or name == "destination-interface-name" or name == "id" or name == "interface-error" or name == "name" or name == "session-class"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    if(value_path == "session"):
                        self.session = value
                        self.session.value_namespace = name_space
                        self.session.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-error"):
                        self.destination_error = value
                        self.destination_error.value_namespace = name_space
                        self.destination_error.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-interface-handle"):
                        self.destination_interface_handle = value
                        self.destination_interface_handle.value_namespace = name_space
                        self.destination_interface_handle.value_namespace_prefix = name_space_prefix
                    if(value_path == "destination-interface-name"):
                        self.destination_interface_name = value
                        self.destination_interface_name.value_namespace = name_space
                        self.destination_interface_name.value_namespace_prefix = name_space_prefix
                    if(value_path == "id"):
                        self.id = value
                        self.id.value_namespace = name_space
                        self.id.value_namespace_prefix = name_space_prefix
                    if(value_path == "interface-error"):
                        self.interface_error = value
                        self.interface_error.value_namespace = name_space
                        self.interface_error.value_namespace_prefix = name_space_prefix
                    if(value_path == "name"):
                        self.name = value
                        self.name.value_namespace = name_space
                        self.name.value_namespace_prefix = name_space_prefix
                    if(value_path == "session-class"):
                        self.session_class = value
                        self.session_class.value_namespace = name_space
                        self.session_class.value_namespace_prefix = name_space_prefix

            def has_data(self):
                for c in self.global_session:
                    if (c.has_data()):
                        return True
                return False

            def has_operation(self):
                for c in self.global_session:
                    if (c.has_operation()):
                        return True
                return self.yfilter != YFilter.not_set

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "global-sessions" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "global-session"):
                    for c in self.global_session:
                        segment = c.get_segment_path()
                        if (segment_path == segment):
                            return c
                    c = SpanMonitorSession.Global_.GlobalSessions.GlobalSession()
                    c.parent = self
                    local_reference_key = "ydk::seg::%s" % segment_path
                    self._local_refs[local_reference_key] = c
                    self.global_session.append(c)
                    return c

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "global-session"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                pass

        def has_data(self):
            return (
                (self.global_sessions is not None and self.global_sessions.has_data()) or
                (self.statistics is not None and self.statistics.has_data()))

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                (self.global_sessions is not None and self.global_sessions.has_operation()) or
                (self.statistics is not None and self.statistics.has_operation()))

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "global" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "global-sessions"):
                if (self.global_sessions is None):
                    self.global_sessions = SpanMonitorSession.Global_.GlobalSessions()
                    self.global_sessions.parent = self
                    self._children_name_map["global_sessions"] = "global-sessions"
                return self.global_sessions

            if (child_yang_name == "statistics"):
                if (self.statistics is None):
                    self.statistics = SpanMonitorSession.Global_.Statistics()
                    self.statistics.parent = self
                    self._children_name_map["statistics"] = "statistics"
                return self.statistics

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "global-sessions" or name == "statistics"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of    :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "span-monitor-session"

            self.node = YList(self)

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
                        super(SpanMonitorSession.Nodes, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(SpanMonitorSession.Nodes, self).__setattr__(name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  <key>
            
            	Node
            	**type**\:  str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: attachments
            
            	Table of source interfaces configured as attached to a session
            	**type**\:   :py:class:`Attachments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments>`
            
            .. attribute:: hardware_sessions
            
            	Table of sessions set up in the hardware.  When all sessions are operating correctly the entries in this table should match those entries in GlobalSessionTable that have a destination configured
            	**type**\:   :py:class:`HardwareSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions>`
            
            .. attribute:: interfaces
            
            	Table of source interfaces set up in the hardware.  The entries in this table should match the entries in AttachmentTable when all sessions are operating correctly
            	**type**\:   :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"

                self.node = YLeaf(YType.str, "node")

                self.attachments = SpanMonitorSession.Nodes.Node.Attachments()
                self.attachments.parent = self
                self._children_name_map["attachments"] = "attachments"
                self._children_yang_names.add("attachments")

                self.hardware_sessions = SpanMonitorSession.Nodes.Node.HardwareSessions()
                self.hardware_sessions.parent = self
                self._children_name_map["hardware_sessions"] = "hardware-sessions"
                self._children_yang_names.add("hardware-sessions")

                self.interfaces = SpanMonitorSession.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._children_yang_names.add("interfaces")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("node") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(SpanMonitorSession.Nodes.Node, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(SpanMonitorSession.Nodes.Node, self).__setattr__(name, value)


            class Attachments(Entity):
                """
                Table of source interfaces configured as
                attached to a session
                
                .. attribute:: attachment
                
                	Information about a particular source interface configured as attached to monitor session
                	**type**\: list of    :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.Attachments, self).__init__()

                    self.yang_name = "attachments"
                    self.yang_parent_name = "node"

                    self.attachment = YList(self)

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
                                super(SpanMonitorSession.Nodes.Node.Attachments, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Nodes.Node.Attachments, self).__setattr__(name, value)


                class Attachment(Entity):
                    """
                    Information about a particular source
                    interface configured as attached to monitor
                    session
                    
                    .. attribute:: session  <key>
                    
                    	Session Name
                    	**type**\:  str
                    
                    	**length:** 1..79
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: dest_pw_type_not_supported
                    
                    	The destination PW type is not supported
                    	**type**\:  bool
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: global_class
                    
                    	Global session class
                    	**type**\:   :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: local_class
                    
                    	Local attachment class
                    	**type**\:   :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: name
                    
                    	Session Name
                    	**type**\:  str
                    
                    .. attribute:: pfi_error
                    
                    	Last error returned from PFI for this interface
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_is_configured
                    
                    	The Session is configured globally
                    	**type**\:  bool
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: source_interface_is_a_destination
                    
                    	This source interface is a destination for another monitor\-session
                    	**type**\:  bool
                    
                    .. attribute:: source_interface_state
                    
                    	Source interface state
                    	**type**\:   :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnum>`
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by TrafficParameters)
                    	**type**\:   :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                    
                    .. attribute:: traffic_parameters
                    
                    	Traffic mirroring parameters
                    	**type**\:   :py:class:`TrafficParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment, self).__init__()

                        self.yang_name = "attachment"
                        self.yang_parent_name = "attachments"

                        self.session = YLeaf(YType.str, "session")

                        self.interface = YLeaf(YType.str, "interface")

                        self.dest_pw_type_not_supported = YLeaf(YType.boolean, "dest-pw-type-not-supported")

                        self.destination_interface = YLeaf(YType.str, "destination-interface")

                        self.global_class = YLeaf(YType.enumeration, "global-class")

                        self.id = YLeaf(YType.uint32, "id")

                        self.local_class = YLeaf(YType.enumeration, "local-class")

                        self.name = YLeaf(YType.str, "name")

                        self.pfi_error = YLeaf(YType.uint32, "pfi-error")

                        self.session_is_configured = YLeaf(YType.boolean, "session-is-configured")

                        self.source_interface = YLeaf(YType.str, "source-interface")

                        self.source_interface_is_a_destination = YLeaf(YType.boolean, "source-interface-is-a-destination")

                        self.source_interface_state = YLeaf(YType.enumeration, "source-interface-state")

                        self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")

                        self.destination_id = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"
                        self._children_yang_names.add("destination-id")

                        self.traffic_parameters = SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters()
                        self.traffic_parameters.parent = self
                        self._children_name_map["traffic_parameters"] = "traffic-parameters"
                        self._children_yang_names.add("traffic-parameters")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("session",
                                        "interface",
                                        "dest_pw_type_not_supported",
                                        "destination_interface",
                                        "global_class",
                                        "id",
                                        "local_class",
                                        "name",
                                        "pfi_error",
                                        "session_is_configured",
                                        "source_interface",
                                        "source_interface_is_a_destination",
                                        "source_interface_state",
                                        "traffic_direction") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SpanMonitorSession.Nodes.Node.Attachments.Attachment, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SpanMonitorSession.Nodes.Node.Attachments.Attachment, self).__setattr__(name, value)


                    class TrafficParameters(Entity):
                        """
                        Traffic mirroring parameters
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\:  bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:   :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\:  bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:   :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, self).__init__()

                            self.yang_name = "traffic-parameters"
                            self.yang_parent_name = "attachment"

                            self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                            self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                            self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                            self.port_level = YLeaf(YType.boolean, "port-level")

                            self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_acl_enabled",
                                            "mirror_bytes",
                                            "mirror_interval",
                                            "port_level",
                                            "traffic_direction") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.is_acl_enabled.is_set or
                                self.mirror_bytes.is_set or
                                self.mirror_interval.is_set or
                                self.port_level.is_set or
                                self.traffic_direction.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_acl_enabled.yfilter != YFilter.not_set or
                                self.mirror_bytes.yfilter != YFilter.not_set or
                                self.mirror_interval.yfilter != YFilter.not_set or
                                self.port_level.yfilter != YFilter.not_set or
                                self.traffic_direction.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "traffic-parameters" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_acl_enabled.is_set or self.is_acl_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_acl_enabled.get_name_leafdata())
                            if (self.mirror_bytes.is_set or self.mirror_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mirror_bytes.get_name_leafdata())
                            if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mirror_interval.get_name_leafdata())
                            if (self.port_level.is_set or self.port_level.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_level.get_name_leafdata())
                            if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.traffic_direction.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "is-acl-enabled" or name == "mirror-bytes" or name == "mirror-interval" or name == "port-level" or name == "traffic-direction"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-acl-enabled"):
                                self.is_acl_enabled = value
                                self.is_acl_enabled.value_namespace = name_space
                                self.is_acl_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "mirror-bytes"):
                                self.mirror_bytes = value
                                self.mirror_bytes.value_namespace = name_space
                                self.mirror_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "mirror-interval"):
                                self.mirror_interval = value
                                self.mirror_interval.value_namespace = name_space
                                self.mirror_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-level"):
                                self.port_level = value
                                self.port_level.value_namespace = name_space
                                self.port_level.value_namespace_prefix = name_space_prefix
                            if(value_path == "traffic-direction"):
                                self.traffic_direction = value
                                self.traffic_direction.value_namespace = name_space
                                self.traffic_direction.value_namespace_prefix = name_space_prefix


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId, self).__init__()

                            self.yang_name = "destination-id"
                            self.yang_parent_name = "attachment"

                            self.destination_class = YLeaf(YType.enumeration, "destination-class")

                            self.interface = YLeaf(YType.str, "interface")

                            self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                            self._children_yang_names.add("ipv4-address-and-vrf")

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._children_yang_names.add("ipv6-address-and-vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_class",
                                            "interface",
                                            "invalid_value",
                                            "pseudowire_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId, self).__setattr__(name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv4_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-address-and-vrf" + path_buffer

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
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ipv6_address",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv6_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-address-and-vrf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv6-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.destination_class.is_set or
                                self.interface.is_set or
                                self.invalid_value.is_set or
                                self.pseudowire_id.is_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_data()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_class.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.invalid_value.yfilter != YFilter.not_set or
                                self.pseudowire_id.yfilter != YFilter.not_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_operation()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_class.get_name_leafdata())
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.invalid_value.get_name_leafdata())
                            if (self.pseudowire_id.is_set or self.pseudowire_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pseudowire_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-address-and-vrf"):
                                if (self.ipv4_address_and_vrf is None):
                                    self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf()
                                    self.ipv4_address_and_vrf.parent = self
                                    self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                                return self.ipv4_address_and_vrf

                            if (child_yang_name == "ipv6-address-and-vrf"):
                                if (self.ipv6_address_and_vrf is None):
                                    self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf()
                                    self.ipv6_address_and_vrf.parent = self
                                    self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                return self.ipv6_address_and_vrf

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-address-and-vrf" or name == "ipv6-address-and-vrf" or name == "destination-class" or name == "interface" or name == "invalid-value" or name == "pseudowire-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-class"):
                                self.destination_class = value
                                self.destination_class.value_namespace = name_space
                                self.destination_class.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "invalid-value"):
                                self.invalid_value = value
                                self.invalid_value.value_namespace = name_space
                                self.invalid_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "pseudowire-id"):
                                self.pseudowire_id = value
                                self.pseudowire_id.value_namespace = name_space
                                self.pseudowire_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.session.is_set or
                            self.interface.is_set or
                            self.dest_pw_type_not_supported.is_set or
                            self.destination_interface.is_set or
                            self.global_class.is_set or
                            self.id.is_set or
                            self.local_class.is_set or
                            self.name.is_set or
                            self.pfi_error.is_set or
                            self.session_is_configured.is_set or
                            self.source_interface.is_set or
                            self.source_interface_is_a_destination.is_set or
                            self.source_interface_state.is_set or
                            self.traffic_direction.is_set or
                            (self.destination_id is not None and self.destination_id.has_data()) or
                            (self.traffic_parameters is not None and self.traffic_parameters.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.session.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.dest_pw_type_not_supported.yfilter != YFilter.not_set or
                            self.destination_interface.yfilter != YFilter.not_set or
                            self.global_class.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.local_class.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.pfi_error.yfilter != YFilter.not_set or
                            self.session_is_configured.yfilter != YFilter.not_set or
                            self.source_interface.yfilter != YFilter.not_set or
                            self.source_interface_is_a_destination.yfilter != YFilter.not_set or
                            self.source_interface_state.yfilter != YFilter.not_set or
                            self.traffic_direction.yfilter != YFilter.not_set or
                            (self.destination_id is not None and self.destination_id.has_operation()) or
                            (self.traffic_parameters is not None and self.traffic_parameters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "attachment" + "[session='" + self.session.get() + "']" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.session.is_set or self.session.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session.get_name_leafdata())
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.dest_pw_type_not_supported.is_set or self.dest_pw_type_not_supported.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.dest_pw_type_not_supported.get_name_leafdata())
                        if (self.destination_interface.is_set or self.destination_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_interface.get_name_leafdata())
                        if (self.global_class.is_set or self.global_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.global_class.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.local_class.is_set or self.local_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.local_class.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.pfi_error.is_set or self.pfi_error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.pfi_error.get_name_leafdata())
                        if (self.session_is_configured.is_set or self.session_is_configured.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_is_configured.get_name_leafdata())
                        if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_interface.get_name_leafdata())
                        if (self.source_interface_is_a_destination.is_set or self.source_interface_is_a_destination.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_interface_is_a_destination.get_name_leafdata())
                        if (self.source_interface_state.is_set or self.source_interface_state.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_interface_state.get_name_leafdata())
                        if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_direction.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "destination-id"):
                            if (self.destination_id is None):
                                self.destination_id = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId()
                                self.destination_id.parent = self
                                self._children_name_map["destination_id"] = "destination-id"
                            return self.destination_id

                        if (child_yang_name == "traffic-parameters"):
                            if (self.traffic_parameters is None):
                                self.traffic_parameters = SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters()
                                self.traffic_parameters.parent = self
                                self._children_name_map["traffic_parameters"] = "traffic-parameters"
                            return self.traffic_parameters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-id" or name == "traffic-parameters" or name == "session" or name == "interface" or name == "dest-pw-type-not-supported" or name == "destination-interface" or name == "global-class" or name == "id" or name == "local-class" or name == "name" or name == "pfi-error" or name == "session-is-configured" or name == "source-interface" or name == "source-interface-is-a-destination" or name == "source-interface-state" or name == "traffic-direction"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "session"):
                            self.session = value
                            self.session.value_namespace = name_space
                            self.session.value_namespace_prefix = name_space_prefix
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "dest-pw-type-not-supported"):
                            self.dest_pw_type_not_supported = value
                            self.dest_pw_type_not_supported.value_namespace = name_space
                            self.dest_pw_type_not_supported.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-interface"):
                            self.destination_interface = value
                            self.destination_interface.value_namespace = name_space
                            self.destination_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "global-class"):
                            self.global_class = value
                            self.global_class.value_namespace = name_space
                            self.global_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "local-class"):
                            self.local_class = value
                            self.local_class.value_namespace = name_space
                            self.local_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "pfi-error"):
                            self.pfi_error = value
                            self.pfi_error.value_namespace = name_space
                            self.pfi_error.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-is-configured"):
                            self.session_is_configured = value
                            self.session_is_configured.value_namespace = name_space
                            self.session_is_configured.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-interface"):
                            self.source_interface = value
                            self.source_interface.value_namespace = name_space
                            self.source_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-interface-is-a-destination"):
                            self.source_interface_is_a_destination = value
                            self.source_interface_is_a_destination.value_namespace = name_space
                            self.source_interface_is_a_destination.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-interface-state"):
                            self.source_interface_state = value
                            self.source_interface_state.value_namespace = name_space
                            self.source_interface_state.value_namespace_prefix = name_space_prefix
                        if(value_path == "traffic-direction"):
                            self.traffic_direction = value
                            self.traffic_direction.value_namespace = name_space
                            self.traffic_direction.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.attachment:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.attachment:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "attachments" + path_buffer

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

                    if (child_yang_name == "attachment"):
                        for c in self.attachment:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SpanMonitorSession.Nodes.Node.Attachments.Attachment()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.attachment.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "attachment"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class HardwareSessions(Entity):
                """
                Table of sessions set up in the hardware. 
                When all sessions are operating correctly the
                entries in this table should match those
                entries in GlobalSessionTable that have a
                destination configured
                
                .. attribute:: hardware_session
                
                	Information about a particular session that is set up in the hardware
                	**type**\: list of    :py:class:`HardwareSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.HardwareSessions, self).__init__()

                    self.yang_name = "hardware-sessions"
                    self.yang_parent_name = "node"

                    self.hardware_session = YList(self)

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
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Nodes.Node.HardwareSessions, self).__setattr__(name, value)


                class HardwareSession(Entity):
                    """
                    Information about a particular session that
                    is set up in the hardware
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: id
                    
                    	Assigned numerical ID for this session
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Configured Session Name
                    	**type**\:  str
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this session while programming the hardware
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: session_class
                    
                    	Sesssion class
                    	**type**\:   :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: session_class_xr
                    
                    	Session class
                    	**type**\:   :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\:  int
                    
                    	**range:** \-2147483648..2147483647
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, self).__init__()

                        self.yang_name = "hardware-session"
                        self.yang_parent_name = "hardware-sessions"

                        self.destination_interface = YLeaf(YType.str, "destination-interface")

                        self.id = YLeaf(YType.uint32, "id")

                        self.name = YLeaf(YType.str, "name")

                        self.platform_error = YLeaf(YType.uint32, "platform-error")

                        self.session_class = YLeaf(YType.enumeration, "session-class")

                        self.session_class_xr = YLeaf(YType.enumeration, "session-class-xr")

                        self.session_id = YLeaf(YType.int32, "session-id")

                        self.destination_id = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"
                        self._children_yang_names.add("destination-id")

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("destination_interface",
                                        "id",
                                        "name",
                                        "platform_error",
                                        "session_class",
                                        "session_class_xr",
                                        "session_id") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, self).__setattr__(name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId, self).__init__()

                            self.yang_name = "destination-id"
                            self.yang_parent_name = "hardware-session"

                            self.destination_class = YLeaf(YType.enumeration, "destination-class")

                            self.interface = YLeaf(YType.str, "interface")

                            self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                            self._children_yang_names.add("ipv4-address-and-vrf")

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._children_yang_names.add("ipv6-address-and-vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_class",
                                            "interface",
                                            "invalid_value",
                                            "pseudowire_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId, self).__setattr__(name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv4_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-address-and-vrf" + path_buffer

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
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ipv6_address",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv6_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-address-and-vrf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv6-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.destination_class.is_set or
                                self.interface.is_set or
                                self.invalid_value.is_set or
                                self.pseudowire_id.is_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_data()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_class.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.invalid_value.yfilter != YFilter.not_set or
                                self.pseudowire_id.yfilter != YFilter.not_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_operation()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_class.get_name_leafdata())
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.invalid_value.get_name_leafdata())
                            if (self.pseudowire_id.is_set or self.pseudowire_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pseudowire_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-address-and-vrf"):
                                if (self.ipv4_address_and_vrf is None):
                                    self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf()
                                    self.ipv4_address_and_vrf.parent = self
                                    self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                                return self.ipv4_address_and_vrf

                            if (child_yang_name == "ipv6-address-and-vrf"):
                                if (self.ipv6_address_and_vrf is None):
                                    self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf()
                                    self.ipv6_address_and_vrf.parent = self
                                    self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                return self.ipv6_address_and_vrf

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-address-and-vrf" or name == "ipv6-address-and-vrf" or name == "destination-class" or name == "interface" or name == "invalid-value" or name == "pseudowire-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-class"):
                                self.destination_class = value
                                self.destination_class.value_namespace = name_space
                                self.destination_class.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "invalid-value"):
                                self.invalid_value = value
                                self.invalid_value.value_namespace = name_space
                                self.invalid_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "pseudowire-id"):
                                self.pseudowire_id = value
                                self.pseudowire_id.value_namespace = name_space
                                self.pseudowire_id.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        return (
                            self.destination_interface.is_set or
                            self.id.is_set or
                            self.name.is_set or
                            self.platform_error.is_set or
                            self.session_class.is_set or
                            self.session_class_xr.is_set or
                            self.session_id.is_set or
                            (self.destination_id is not None and self.destination_id.has_data()))

                    def has_operation(self):
                        return (
                            self.yfilter != YFilter.not_set or
                            self.destination_interface.yfilter != YFilter.not_set or
                            self.id.yfilter != YFilter.not_set or
                            self.name.yfilter != YFilter.not_set or
                            self.platform_error.yfilter != YFilter.not_set or
                            self.session_class.yfilter != YFilter.not_set or
                            self.session_class_xr.yfilter != YFilter.not_set or
                            self.session_id.yfilter != YFilter.not_set or
                            (self.destination_id is not None and self.destination_id.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "hardware-session" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.destination_interface.is_set or self.destination_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_interface.get_name_leafdata())
                        if (self.id.is_set or self.id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.id.get_name_leafdata())
                        if (self.name.is_set or self.name.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.name.get_name_leafdata())
                        if (self.platform_error.is_set or self.platform_error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.platform_error.get_name_leafdata())
                        if (self.session_class.is_set or self.session_class.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_class.get_name_leafdata())
                        if (self.session_class_xr.is_set or self.session_class_xr.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_class_xr.get_name_leafdata())
                        if (self.session_id.is_set or self.session_id.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.session_id.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "destination-id"):
                            if (self.destination_id is None):
                                self.destination_id = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId()
                                self.destination_id.parent = self
                                self._children_name_map["destination_id"] = "destination-id"
                            return self.destination_id

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "destination-id" or name == "destination-interface" or name == "id" or name == "name" or name == "platform-error" or name == "session-class" or name == "session-class-xr" or name == "session-id"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "destination-interface"):
                            self.destination_interface = value
                            self.destination_interface.value_namespace = name_space
                            self.destination_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "id"):
                            self.id = value
                            self.id.value_namespace = name_space
                            self.id.value_namespace_prefix = name_space_prefix
                        if(value_path == "name"):
                            self.name = value
                            self.name.value_namespace = name_space
                            self.name.value_namespace_prefix = name_space_prefix
                        if(value_path == "platform-error"):
                            self.platform_error = value
                            self.platform_error.value_namespace = name_space
                            self.platform_error.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-class"):
                            self.session_class = value
                            self.session_class.value_namespace = name_space
                            self.session_class.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-class-xr"):
                            self.session_class_xr = value
                            self.session_class_xr.value_namespace = name_space
                            self.session_class_xr.value_namespace_prefix = name_space_prefix
                        if(value_path == "session-id"):
                            self.session_id = value
                            self.session_id.value_namespace = name_space
                            self.session_id.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.hardware_session:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.hardware_session:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "hardware-sessions" + path_buffer

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

                    if (child_yang_name == "hardware-session"):
                        for c in self.hardware_session:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.hardware_session.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "hardware-session"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass


            class Interfaces(Entity):
                """
                Table of source interfaces set up in the
                hardware.  The entries in this table should
                match the entries in AttachmentTable when all
                sessions are operating correctly
                
                .. attribute:: interface
                
                	Information about a particular interface that is set up in the hardware
                	**type**\: list of    :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"

                    self.interface = YList(self)

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
                                super(SpanMonitorSession.Nodes.Node.Interfaces, self).__setattr__(name, value)
                            else:
                                self.__dict__[name].set(value)
                        else:
                            if hasattr(value, "parent") and name != "parent":
                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                    value.parent = self
                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                    value.parent = self
                            super(SpanMonitorSession.Nodes.Node.Interfaces, self).__setattr__(name, value)


                class Interface(Entity):
                    """
                    Information about a particular interface that
                    is set up in the hardware
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: attachment
                    
                    	Attachment information
                    	**type**\: list of    :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment>`
                    
                    .. attribute:: destination_id
                    
                    	Destination ID (deprecated by Attachment)
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by Attachment)
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this interface while programming the hardware
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by Attachment)
                    	**type**\:   :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                    
                    .. attribute:: traffic_mirroring_parameters
                    
                    	Traffic mirroring parameters (deprecated by Attachment)
                    	**type**\:   :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"

                        self.interface = YLeaf(YType.str, "interface")

                        self.destination_interface = YLeaf(YType.str, "destination-interface")

                        self.platform_error = YLeaf(YType.uint32, "platform-error")

                        self.source_interface = YLeaf(YType.str, "source-interface")

                        self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")

                        self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"
                        self._children_yang_names.add("destination-id")

                        self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters()
                        self.traffic_mirroring_parameters.parent = self
                        self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                        self._children_yang_names.add("traffic-mirroring-parameters")

                        self.attachment = YList(self)

                    def __setattr__(self, name, value):
                        self._check_monkey_patching_error(name, value)
                        with _handle_type_error():
                            if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                    "Please use list append or extend method."
                                                    .format(value))
                            if isinstance(value, Enum.YLeaf):
                                value = value.name
                            if name in ("interface",
                                        "destination_interface",
                                        "platform_error",
                                        "source_interface",
                                        "traffic_direction") and name in self.__dict__:
                                if isinstance(value, YLeaf):
                                    self.__dict__[name].set(value.get())
                                elif isinstance(value, YLeafList):
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)
                                else:
                                    self.__dict__[name].set(value)
                            else:
                                if hasattr(value, "parent") and name != "parent":
                                    if hasattr(value, "is_presence_container") and value.is_presence_container:
                                        value.parent = self
                                    elif value.parent is None and value.yang_name in self._children_yang_names:
                                        value.parent = self
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface, self).__setattr__(name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID (deprecated by Attachment)
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId, self).__init__()

                            self.yang_name = "destination-id"
                            self.yang_parent_name = "interface"

                            self.destination_class = YLeaf(YType.enumeration, "destination-class")

                            self.interface = YLeaf(YType.str, "interface")

                            self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                            self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                            self._children_yang_names.add("ipv4-address-and-vrf")

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._children_yang_names.add("ipv6-address-and-vrf")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("destination_class",
                                            "interface",
                                            "invalid_value",
                                            "pseudowire_id") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId, self).__setattr__(name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\:  str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv4_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv4_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv4-address-and-vrf" + path_buffer

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
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv4-address"):
                                    self.ipv4_address = value
                                    self.ipv4_address.value_namespace = name_space
                                    self.ipv4_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\:  str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\:  str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("ipv6_address",
                                                "vrf_name") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.ipv6_address.is_set or
                                    self.vrf_name.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.ipv6_address.yfilter != YFilter.not_set or
                                    self.vrf_name.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "ipv6-address-and-vrf" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv6-address" or name == "vrf-name"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "ipv6-address"):
                                    self.ipv6_address = value
                                    self.ipv6_address.value_namespace = name_space
                                    self.ipv6_address.value_namespace_prefix = name_space_prefix
                                if(value_path == "vrf-name"):
                                    self.vrf_name = value
                                    self.vrf_name.value_namespace = name_space
                                    self.vrf_name.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.destination_class.is_set or
                                self.interface.is_set or
                                self.invalid_value.is_set or
                                self.pseudowire_id.is_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_data()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.destination_class.yfilter != YFilter.not_set or
                                self.interface.yfilter != YFilter.not_set or
                                self.invalid_value.yfilter != YFilter.not_set or
                                self.pseudowire_id.yfilter != YFilter.not_set or
                                (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_operation()) or
                                (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "destination-id" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.destination_class.get_name_leafdata())
                            if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.interface.get_name_leafdata())
                            if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.invalid_value.get_name_leafdata())
                            if (self.pseudowire_id.is_set or self.pseudowire_id.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.pseudowire_id.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "ipv4-address-and-vrf"):
                                if (self.ipv4_address_and_vrf is None):
                                    self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf()
                                    self.ipv4_address_and_vrf.parent = self
                                    self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                                return self.ipv4_address_and_vrf

                            if (child_yang_name == "ipv6-address-and-vrf"):
                                if (self.ipv6_address_and_vrf is None):
                                    self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf()
                                    self.ipv6_address_and_vrf.parent = self
                                    self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                return self.ipv6_address_and_vrf

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "ipv4-address-and-vrf" or name == "ipv6-address-and-vrf" or name == "destination-class" or name == "interface" or name == "invalid-value" or name == "pseudowire-id"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "destination-class"):
                                self.destination_class = value
                                self.destination_class.value_namespace = name_space
                                self.destination_class.value_namespace_prefix = name_space_prefix
                            if(value_path == "interface"):
                                self.interface = value
                                self.interface.value_namespace = name_space
                                self.interface.value_namespace_prefix = name_space_prefix
                            if(value_path == "invalid-value"):
                                self.invalid_value = value
                                self.invalid_value.value_namespace = name_space
                                self.invalid_value.value_namespace_prefix = name_space_prefix
                            if(value_path == "pseudowire-id"):
                                self.pseudowire_id = value
                                self.pseudowire_id.value_namespace = name_space
                                self.pseudowire_id.value_namespace_prefix = name_space_prefix


                    class TrafficMirroringParameters(Entity):
                        """
                        Traffic mirroring parameters (deprecated by
                        Attachment)
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\:  bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\:  int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:   :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\:  bool
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:   :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, self).__init__()

                            self.yang_name = "traffic-mirroring-parameters"
                            self.yang_parent_name = "interface"

                            self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                            self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                            self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                            self.port_level = YLeaf(YType.boolean, "port-level")

                            self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("is_acl_enabled",
                                            "mirror_bytes",
                                            "mirror_interval",
                                            "port_level",
                                            "traffic_direction") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, self).__setattr__(name, value)

                        def has_data(self):
                            return (
                                self.is_acl_enabled.is_set or
                                self.mirror_bytes.is_set or
                                self.mirror_interval.is_set or
                                self.port_level.is_set or
                                self.traffic_direction.is_set)

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.is_acl_enabled.yfilter != YFilter.not_set or
                                self.mirror_bytes.yfilter != YFilter.not_set or
                                self.mirror_interval.yfilter != YFilter.not_set or
                                self.port_level.yfilter != YFilter.not_set or
                                self.traffic_direction.yfilter != YFilter.not_set)

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "traffic-mirroring-parameters" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.is_acl_enabled.is_set or self.is_acl_enabled.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.is_acl_enabled.get_name_leafdata())
                            if (self.mirror_bytes.is_set or self.mirror_bytes.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mirror_bytes.get_name_leafdata())
                            if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.mirror_interval.get_name_leafdata())
                            if (self.port_level.is_set or self.port_level.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.port_level.get_name_leafdata())
                            if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.traffic_direction.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "is-acl-enabled" or name == "mirror-bytes" or name == "mirror-interval" or name == "port-level" or name == "traffic-direction"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "is-acl-enabled"):
                                self.is_acl_enabled = value
                                self.is_acl_enabled.value_namespace = name_space
                                self.is_acl_enabled.value_namespace_prefix = name_space_prefix
                            if(value_path == "mirror-bytes"):
                                self.mirror_bytes = value
                                self.mirror_bytes.value_namespace = name_space
                                self.mirror_bytes.value_namespace_prefix = name_space_prefix
                            if(value_path == "mirror-interval"):
                                self.mirror_interval = value
                                self.mirror_interval.value_namespace = name_space
                                self.mirror_interval.value_namespace_prefix = name_space_prefix
                            if(value_path == "port-level"):
                                self.port_level = value
                                self.port_level.value_namespace = name_space
                                self.port_level.value_namespace_prefix = name_space_prefix
                            if(value_path == "traffic-direction"):
                                self.traffic_direction = value
                                self.traffic_direction.value_namespace = name_space
                                self.traffic_direction.value_namespace_prefix = name_space_prefix


                    class Attachment(Entity):
                        """
                        Attachment information
                        
                        .. attribute:: class_
                        
                        	Attachment class
                        	**type**\:   :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                        
                        .. attribute:: destination_id
                        
                        	Destination ID
                        	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId>`
                        
                        .. attribute:: traffic_mirroring_parameters
                        
                        	Traffic mirroring parameters
                        	**type**\:   :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "interface"

                            self.class_ = YLeaf(YType.enumeration, "class")

                            self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId()
                            self.destination_id.parent = self
                            self._children_name_map["destination_id"] = "destination-id"
                            self._children_yang_names.add("destination-id")

                            self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters()
                            self.traffic_mirroring_parameters.parent = self
                            self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                            self._children_yang_names.add("traffic-mirroring-parameters")

                        def __setattr__(self, name, value):
                            self._check_monkey_patching_error(name, value)
                            with _handle_type_error():
                                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                        "Please use list append or extend method."
                                                        .format(value))
                                if isinstance(value, Enum.YLeaf):
                                    value = value.name
                                if name in ("class_") and name in self.__dict__:
                                    if isinstance(value, YLeaf):
                                        self.__dict__[name].set(value.get())
                                    elif isinstance(value, YLeafList):
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, self).__setattr__(name, value)
                                    else:
                                        self.__dict__[name].set(value)
                                else:
                                    if hasattr(value, "parent") and name != "parent":
                                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                                            value.parent = self
                                        elif value.parent is None and value.yang_name in self._children_yang_names:
                                            value.parent = self
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, self).__setattr__(name, value)


                        class DestinationId(Entity):
                            """
                            Destination ID
                            
                            .. attribute:: destination_class
                            
                            	DestinationClass
                            	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                            
                            .. attribute:: interface
                            
                            	Interface Handle
                            	**type**\:  str
                            
                            	**pattern:** (([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){3,4}\\d+\\.\\d+)\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]\*\\d+))\|(([a\-zA\-Z0\-9\_]\*\\d+/){2}([a\-zA\-Z0\-9\_]+))\|([a\-zA\-Z0\-9\_\-]\*\\d+)\|([a\-zA\-Z0\-9\_\-]\*\\d+\\.\\d+)\|(mpls)\|(dwdm)
                            
                            .. attribute:: invalid_value
                            
                            	Invalid Parameter
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: ipv4_address_and_vrf
                            
                            	IPv4 address
                            	**type**\:   :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf>`
                            
                            .. attribute:: ipv6_address_and_vrf
                            
                            	IPv6 address
                            	**type**\:   :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf>`
                            
                            .. attribute:: pseudowire_id
                            
                            	Pseudowire XCID
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId, self).__init__()

                                self.yang_name = "destination-id"
                                self.yang_parent_name = "attachment"

                                self.destination_class = YLeaf(YType.enumeration, "destination-class")

                                self.interface = YLeaf(YType.str, "interface")

                                self.invalid_value = YLeaf(YType.uint32, "invalid-value")

                                self.pseudowire_id = YLeaf(YType.uint32, "pseudowire-id")

                                self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf()
                                self.ipv4_address_and_vrf.parent = self
                                self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                                self._children_yang_names.add("ipv4-address-and-vrf")

                                self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf()
                                self.ipv6_address_and_vrf.parent = self
                                self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                self._children_yang_names.add("ipv6-address-and-vrf")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("destination_class",
                                                "interface",
                                                "invalid_value",
                                                "pseudowire_id") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId, self).__setattr__(name, value)


                            class Ipv4AddressAndVrf(Entity):
                                """
                                IPv4 address
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\:  str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                    self.yang_name = "ipv4-address-and-vrf"
                                    self.yang_parent_name = "destination-id"

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

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
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ipv4_address.is_set or
                                        self.vrf_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ipv4_address.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv4-address-and-vrf" + path_buffer

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
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ipv4-address" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ipv4-address"):
                                        self.ipv4_address = value
                                        self.ipv4_address.value_namespace = name_space
                                        self.ipv4_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix


                            class Ipv6AddressAndVrf(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\:  str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\:  str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                    self.yang_name = "ipv6-address-and-vrf"
                                    self.yang_parent_name = "destination-id"

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")

                                def __setattr__(self, name, value):
                                    self._check_monkey_patching_error(name, value)
                                    with _handle_type_error():
                                        if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                            raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                                "Please use list append or extend method."
                                                                .format(value))
                                        if isinstance(value, Enum.YLeaf):
                                            value = value.name
                                        if name in ("ipv6_address",
                                                    "vrf_name") and name in self.__dict__:
                                            if isinstance(value, YLeaf):
                                                self.__dict__[name].set(value.get())
                                            elif isinstance(value, YLeafList):
                                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)
                                            else:
                                                self.__dict__[name].set(value)
                                        else:
                                            if hasattr(value, "parent") and name != "parent":
                                                if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                    value.parent = self
                                                elif value.parent is None and value.yang_name in self._children_yang_names:
                                                    value.parent = self
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, self).__setattr__(name, value)

                                def has_data(self):
                                    return (
                                        self.ipv6_address.is_set or
                                        self.vrf_name.is_set)

                                def has_operation(self):
                                    return (
                                        self.yfilter != YFilter.not_set or
                                        self.ipv6_address.yfilter != YFilter.not_set or
                                        self.vrf_name.yfilter != YFilter.not_set)

                                def get_segment_path(self):
                                    path_buffer = ""
                                    path_buffer = "ipv6-address-and-vrf" + path_buffer

                                    return path_buffer

                                def get_entity_path(self, ancestor):
                                    path_buffer = ""
                                    if (ancestor is None):
                                        raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                    else:
                                        path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                    leaf_name_data = LeafDataList()
                                    if (self.ipv6_address.is_set or self.ipv6_address.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.ipv6_address.get_name_leafdata())
                                    if (self.vrf_name.is_set or self.vrf_name.yfilter != YFilter.not_set):
                                        leaf_name_data.append(self.vrf_name.get_name_leafdata())

                                    entity_path = EntityPath(path_buffer, leaf_name_data)
                                    return entity_path

                                def get_child_by_name(self, child_yang_name, segment_path):
                                    child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                    if child is not None:
                                        return child

                                    return None

                                def has_leaf_or_child_of_name(self, name):
                                    if(name == "ipv6-address" or name == "vrf-name"):
                                        return True
                                    return False

                                def set_value(self, value_path, value, name_space, name_space_prefix):
                                    if(value_path == "ipv6-address"):
                                        self.ipv6_address = value
                                        self.ipv6_address.value_namespace = name_space
                                        self.ipv6_address.value_namespace_prefix = name_space_prefix
                                    if(value_path == "vrf-name"):
                                        self.vrf_name = value
                                        self.vrf_name.value_namespace = name_space
                                        self.vrf_name.value_namespace_prefix = name_space_prefix

                            def has_data(self):
                                return (
                                    self.destination_class.is_set or
                                    self.interface.is_set or
                                    self.invalid_value.is_set or
                                    self.pseudowire_id.is_set or
                                    (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_data()) or
                                    (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_data()))

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.destination_class.yfilter != YFilter.not_set or
                                    self.interface.yfilter != YFilter.not_set or
                                    self.invalid_value.yfilter != YFilter.not_set or
                                    self.pseudowire_id.yfilter != YFilter.not_set or
                                    (self.ipv4_address_and_vrf is not None and self.ipv4_address_and_vrf.has_operation()) or
                                    (self.ipv6_address_and_vrf is not None and self.ipv6_address_and_vrf.has_operation()))

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "destination-id" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.destination_class.is_set or self.destination_class.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.destination_class.get_name_leafdata())
                                if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.interface.get_name_leafdata())
                                if (self.invalid_value.is_set or self.invalid_value.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.invalid_value.get_name_leafdata())
                                if (self.pseudowire_id.is_set or self.pseudowire_id.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.pseudowire_id.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                if (child_yang_name == "ipv4-address-and-vrf"):
                                    if (self.ipv4_address_and_vrf is None):
                                        self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf()
                                        self.ipv4_address_and_vrf.parent = self
                                        self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"
                                    return self.ipv4_address_and_vrf

                                if (child_yang_name == "ipv6-address-and-vrf"):
                                    if (self.ipv6_address_and_vrf is None):
                                        self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf()
                                        self.ipv6_address_and_vrf.parent = self
                                        self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                    return self.ipv6_address_and_vrf

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "ipv4-address-and-vrf" or name == "ipv6-address-and-vrf" or name == "destination-class" or name == "interface" or name == "invalid-value" or name == "pseudowire-id"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "destination-class"):
                                    self.destination_class = value
                                    self.destination_class.value_namespace = name_space
                                    self.destination_class.value_namespace_prefix = name_space_prefix
                                if(value_path == "interface"):
                                    self.interface = value
                                    self.interface.value_namespace = name_space
                                    self.interface.value_namespace_prefix = name_space_prefix
                                if(value_path == "invalid-value"):
                                    self.invalid_value = value
                                    self.invalid_value.value_namespace = name_space
                                    self.invalid_value.value_namespace_prefix = name_space_prefix
                                if(value_path == "pseudowire-id"):
                                    self.pseudowire_id = value
                                    self.pseudowire_id.value_namespace = name_space
                                    self.pseudowire_id.value_namespace_prefix = name_space_prefix


                        class TrafficMirroringParameters(Entity):
                            """
                            Traffic mirroring parameters
                            
                            .. attribute:: is_acl_enabled
                            
                            	ACL enabled
                            	**type**\:  bool
                            
                            .. attribute:: mirror_bytes
                            
                            	Number of bytes to mirror
                            	**type**\:  int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: mirror_interval
                            
                            	Interval between mirrored packets
                            	**type**\:   :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                            
                            .. attribute:: port_level
                            
                            	Port level mirroring
                            	**type**\:  bool
                            
                            .. attribute:: traffic_direction
                            
                            	Direction
                            	**type**\:   :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, self).__init__()

                                self.yang_name = "traffic-mirroring-parameters"
                                self.yang_parent_name = "attachment"

                                self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                                self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                                self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                                self.port_level = YLeaf(YType.boolean, "port-level")

                                self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")

                            def __setattr__(self, name, value):
                                self._check_monkey_patching_error(name, value)
                                with _handle_type_error():
                                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                                            "Please use list append or extend method."
                                                            .format(value))
                                    if isinstance(value, Enum.YLeaf):
                                        value = value.name
                                    if name in ("is_acl_enabled",
                                                "mirror_bytes",
                                                "mirror_interval",
                                                "port_level",
                                                "traffic_direction") and name in self.__dict__:
                                        if isinstance(value, YLeaf):
                                            self.__dict__[name].set(value.get())
                                        elif isinstance(value, YLeafList):
                                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, self).__setattr__(name, value)
                                        else:
                                            self.__dict__[name].set(value)
                                    else:
                                        if hasattr(value, "parent") and name != "parent":
                                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                                value.parent = self
                                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                                value.parent = self
                                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, self).__setattr__(name, value)

                            def has_data(self):
                                return (
                                    self.is_acl_enabled.is_set or
                                    self.mirror_bytes.is_set or
                                    self.mirror_interval.is_set or
                                    self.port_level.is_set or
                                    self.traffic_direction.is_set)

                            def has_operation(self):
                                return (
                                    self.yfilter != YFilter.not_set or
                                    self.is_acl_enabled.yfilter != YFilter.not_set or
                                    self.mirror_bytes.yfilter != YFilter.not_set or
                                    self.mirror_interval.yfilter != YFilter.not_set or
                                    self.port_level.yfilter != YFilter.not_set or
                                    self.traffic_direction.yfilter != YFilter.not_set)

                            def get_segment_path(self):
                                path_buffer = ""
                                path_buffer = "traffic-mirroring-parameters" + path_buffer

                                return path_buffer

                            def get_entity_path(self, ancestor):
                                path_buffer = ""
                                if (ancestor is None):
                                    raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                                else:
                                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                                leaf_name_data = LeafDataList()
                                if (self.is_acl_enabled.is_set or self.is_acl_enabled.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.is_acl_enabled.get_name_leafdata())
                                if (self.mirror_bytes.is_set or self.mirror_bytes.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mirror_bytes.get_name_leafdata())
                                if (self.mirror_interval.is_set or self.mirror_interval.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.mirror_interval.get_name_leafdata())
                                if (self.port_level.is_set or self.port_level.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.port_level.get_name_leafdata())
                                if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                                    leaf_name_data.append(self.traffic_direction.get_name_leafdata())

                                entity_path = EntityPath(path_buffer, leaf_name_data)
                                return entity_path

                            def get_child_by_name(self, child_yang_name, segment_path):
                                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                                if child is not None:
                                    return child

                                return None

                            def has_leaf_or_child_of_name(self, name):
                                if(name == "is-acl-enabled" or name == "mirror-bytes" or name == "mirror-interval" or name == "port-level" or name == "traffic-direction"):
                                    return True
                                return False

                            def set_value(self, value_path, value, name_space, name_space_prefix):
                                if(value_path == "is-acl-enabled"):
                                    self.is_acl_enabled = value
                                    self.is_acl_enabled.value_namespace = name_space
                                    self.is_acl_enabled.value_namespace_prefix = name_space_prefix
                                if(value_path == "mirror-bytes"):
                                    self.mirror_bytes = value
                                    self.mirror_bytes.value_namespace = name_space
                                    self.mirror_bytes.value_namespace_prefix = name_space_prefix
                                if(value_path == "mirror-interval"):
                                    self.mirror_interval = value
                                    self.mirror_interval.value_namespace = name_space
                                    self.mirror_interval.value_namespace_prefix = name_space_prefix
                                if(value_path == "port-level"):
                                    self.port_level = value
                                    self.port_level.value_namespace = name_space
                                    self.port_level.value_namespace_prefix = name_space_prefix
                                if(value_path == "traffic-direction"):
                                    self.traffic_direction = value
                                    self.traffic_direction.value_namespace = name_space
                                    self.traffic_direction.value_namespace_prefix = name_space_prefix

                        def has_data(self):
                            return (
                                self.class_.is_set or
                                (self.destination_id is not None and self.destination_id.has_data()) or
                                (self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters.has_data()))

                        def has_operation(self):
                            return (
                                self.yfilter != YFilter.not_set or
                                self.class_.yfilter != YFilter.not_set or
                                (self.destination_id is not None and self.destination_id.has_operation()) or
                                (self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters.has_operation()))

                        def get_segment_path(self):
                            path_buffer = ""
                            path_buffer = "attachment" + path_buffer

                            return path_buffer

                        def get_entity_path(self, ancestor):
                            path_buffer = ""
                            if (ancestor is None):
                                raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                            else:
                                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                            leaf_name_data = LeafDataList()
                            if (self.class_.is_set or self.class_.yfilter != YFilter.not_set):
                                leaf_name_data.append(self.class_.get_name_leafdata())

                            entity_path = EntityPath(path_buffer, leaf_name_data)
                            return entity_path

                        def get_child_by_name(self, child_yang_name, segment_path):
                            child = self._get_child_by_seg_name([child_yang_name, segment_path])
                            if child is not None:
                                return child

                            if (child_yang_name == "destination-id"):
                                if (self.destination_id is None):
                                    self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId()
                                    self.destination_id.parent = self
                                    self._children_name_map["destination_id"] = "destination-id"
                                return self.destination_id

                            if (child_yang_name == "traffic-mirroring-parameters"):
                                if (self.traffic_mirroring_parameters is None):
                                    self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters()
                                    self.traffic_mirroring_parameters.parent = self
                                    self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                                return self.traffic_mirroring_parameters

                            return None

                        def has_leaf_or_child_of_name(self, name):
                            if(name == "destination-id" or name == "traffic-mirroring-parameters" or name == "class"):
                                return True
                            return False

                        def set_value(self, value_path, value, name_space, name_space_prefix):
                            if(value_path == "class"):
                                self.class_ = value
                                self.class_.value_namespace = name_space
                                self.class_.value_namespace_prefix = name_space_prefix

                    def has_data(self):
                        for c in self.attachment:
                            if (c.has_data()):
                                return True
                        return (
                            self.interface.is_set or
                            self.destination_interface.is_set or
                            self.platform_error.is_set or
                            self.source_interface.is_set or
                            self.traffic_direction.is_set or
                            (self.destination_id is not None and self.destination_id.has_data()) or
                            (self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters.has_data()))

                    def has_operation(self):
                        for c in self.attachment:
                            if (c.has_operation()):
                                return True
                        return (
                            self.yfilter != YFilter.not_set or
                            self.interface.yfilter != YFilter.not_set or
                            self.destination_interface.yfilter != YFilter.not_set or
                            self.platform_error.yfilter != YFilter.not_set or
                            self.source_interface.yfilter != YFilter.not_set or
                            self.traffic_direction.yfilter != YFilter.not_set or
                            (self.destination_id is not None and self.destination_id.has_operation()) or
                            (self.traffic_mirroring_parameters is not None and self.traffic_mirroring_parameters.has_operation()))

                    def get_segment_path(self):
                        path_buffer = ""
                        path_buffer = "interface" + "[interface='" + self.interface.get() + "']" + path_buffer

                        return path_buffer

                    def get_entity_path(self, ancestor):
                        path_buffer = ""
                        if (ancestor is None):
                            raise YPYModelError("ancestor cannot be None as one of the ancestors is a list")
                        else:
                            path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                        leaf_name_data = LeafDataList()
                        if (self.interface.is_set or self.interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.interface.get_name_leafdata())
                        if (self.destination_interface.is_set or self.destination_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.destination_interface.get_name_leafdata())
                        if (self.platform_error.is_set or self.platform_error.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.platform_error.get_name_leafdata())
                        if (self.source_interface.is_set or self.source_interface.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.source_interface.get_name_leafdata())
                        if (self.traffic_direction.is_set or self.traffic_direction.yfilter != YFilter.not_set):
                            leaf_name_data.append(self.traffic_direction.get_name_leafdata())

                        entity_path = EntityPath(path_buffer, leaf_name_data)
                        return entity_path

                    def get_child_by_name(self, child_yang_name, segment_path):
                        child = self._get_child_by_seg_name([child_yang_name, segment_path])
                        if child is not None:
                            return child

                        if (child_yang_name == "attachment"):
                            for c in self.attachment:
                                segment = c.get_segment_path()
                                if (segment_path == segment):
                                    return c
                            c = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment()
                            c.parent = self
                            local_reference_key = "ydk::seg::%s" % segment_path
                            self._local_refs[local_reference_key] = c
                            self.attachment.append(c)
                            return c

                        if (child_yang_name == "destination-id"):
                            if (self.destination_id is None):
                                self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId()
                                self.destination_id.parent = self
                                self._children_name_map["destination_id"] = "destination-id"
                            return self.destination_id

                        if (child_yang_name == "traffic-mirroring-parameters"):
                            if (self.traffic_mirroring_parameters is None):
                                self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters()
                                self.traffic_mirroring_parameters.parent = self
                                self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                            return self.traffic_mirroring_parameters

                        return None

                    def has_leaf_or_child_of_name(self, name):
                        if(name == "attachment" or name == "destination-id" or name == "traffic-mirroring-parameters" or name == "interface" or name == "destination-interface" or name == "platform-error" or name == "source-interface" or name == "traffic-direction"):
                            return True
                        return False

                    def set_value(self, value_path, value, name_space, name_space_prefix):
                        if(value_path == "interface"):
                            self.interface = value
                            self.interface.value_namespace = name_space
                            self.interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "destination-interface"):
                            self.destination_interface = value
                            self.destination_interface.value_namespace = name_space
                            self.destination_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "platform-error"):
                            self.platform_error = value
                            self.platform_error.value_namespace = name_space
                            self.platform_error.value_namespace_prefix = name_space_prefix
                        if(value_path == "source-interface"):
                            self.source_interface = value
                            self.source_interface.value_namespace = name_space
                            self.source_interface.value_namespace_prefix = name_space_prefix
                        if(value_path == "traffic-direction"):
                            self.traffic_direction = value
                            self.traffic_direction.value_namespace = name_space
                            self.traffic_direction.value_namespace_prefix = name_space_prefix

                def has_data(self):
                    for c in self.interface:
                        if (c.has_data()):
                            return True
                    return False

                def has_operation(self):
                    for c in self.interface:
                        if (c.has_operation()):
                            return True
                    return self.yfilter != YFilter.not_set

                def get_segment_path(self):
                    path_buffer = ""
                    path_buffer = "interfaces" + path_buffer

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

                    if (child_yang_name == "interface"):
                        for c in self.interface:
                            segment = c.get_segment_path()
                            if (segment_path == segment):
                                return c
                        c = SpanMonitorSession.Nodes.Node.Interfaces.Interface()
                        c.parent = self
                        local_reference_key = "ydk::seg::%s" % segment_path
                        self._local_refs[local_reference_key] = c
                        self.interface.append(c)
                        return c

                    return None

                def has_leaf_or_child_of_name(self, name):
                    if(name == "interface"):
                        return True
                    return False

                def set_value(self, value_path, value, name_space, name_space_prefix):
                    pass

            def has_data(self):
                return (
                    self.node.is_set or
                    (self.attachments is not None and self.attachments.has_data()) or
                    (self.hardware_sessions is not None and self.hardware_sessions.has_data()) or
                    (self.interfaces is not None and self.interfaces.has_data()))

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.node.yfilter != YFilter.not_set or
                    (self.attachments is not None and self.attachments.has_operation()) or
                    (self.hardware_sessions is not None and self.hardware_sessions.has_operation()) or
                    (self.interfaces is not None and self.interfaces.has_operation()))

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "node" + "[node='" + self.node.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/nodes/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.node.is_set or self.node.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.node.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                if (child_yang_name == "attachments"):
                    if (self.attachments is None):
                        self.attachments = SpanMonitorSession.Nodes.Node.Attachments()
                        self.attachments.parent = self
                        self._children_name_map["attachments"] = "attachments"
                    return self.attachments

                if (child_yang_name == "hardware-sessions"):
                    if (self.hardware_sessions is None):
                        self.hardware_sessions = SpanMonitorSession.Nodes.Node.HardwareSessions()
                        self.hardware_sessions.parent = self
                        self._children_name_map["hardware_sessions"] = "hardware-sessions"
                    return self.hardware_sessions

                if (child_yang_name == "interfaces"):
                    if (self.interfaces is None):
                        self.interfaces = SpanMonitorSession.Nodes.Node.Interfaces()
                        self.interfaces.parent = self
                        self._children_name_map["interfaces"] = "interfaces"
                    return self.interfaces

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "attachments" or name == "hardware-sessions" or name == "interfaces" or name == "node"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "node"):
                    self.node = value
                    self.node.value_namespace = name_space
                    self.node.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.node:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.node:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "nodes" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "node"):
                for c in self.node:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = SpanMonitorSession.Nodes.Node()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.node.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "node"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.global_ is not None and self.global_.has_data()) or
            (self.nodes is not None and self.nodes.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.global_ is not None and self.global_.has_operation()) or
            (self.nodes is not None and self.nodes.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session" + path_buffer

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

        if (child_yang_name == "global"):
            if (self.global_ is None):
                self.global_ = SpanMonitorSession.Global_()
                self.global_.parent = self
                self._children_name_map["global_"] = "global"
            return self.global_

        if (child_yang_name == "nodes"):
            if (self.nodes is None):
                self.nodes = SpanMonitorSession.Nodes()
                self.nodes.parent = self
                self._children_name_map["nodes"] = "nodes"
            return self.nodes

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "global" or name == "nodes"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = SpanMonitorSession()
        return self._top_entity

