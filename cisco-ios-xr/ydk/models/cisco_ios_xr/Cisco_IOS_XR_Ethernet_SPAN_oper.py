""" Cisco_IOS_XR_Ethernet_SPAN_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package operational data.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: Monitor Session operational data

Copyright (c) 2013\-2017 by Cisco Systems, Inc.
All rights reserved.

"""
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

    .. data:: mplsipv4_class = 3

    	MPLS-IPv4 mirroring session

    .. data:: mplsipv6_class = 4

    	MPLS-IPv6 mirroring session

    .. data:: invalid_class = 65535

    	Invalid session class

    """

    ethernet_class = Enum.YLeaf(0, "ethernet-class")

    ipv4_class = Enum.YLeaf(1, "ipv4-class")

    ipv6_class = Enum.YLeaf(2, "ipv6-class")

    mplsipv4_class = Enum.YLeaf(3, "mplsipv4-class")

    mplsipv6_class = Enum.YLeaf(4, "mplsipv6-class")

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
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"global" : ("global_", SpanMonitorSession.Global_), "nodes" : ("nodes", SpanMonitorSession.Nodes)}
        self._child_list_classes = {}

        self.global_ = SpanMonitorSession.Global_()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"
        self._children_yang_names.add("global")

        self.nodes = SpanMonitorSession.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._children_yang_names.add("nodes")
        self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session"


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {"global-sessions" : ("global_sessions", SpanMonitorSession.Global_.GlobalSessions), "statistics" : ("statistics", SpanMonitorSession.Global_.Statistics)}
            self._child_list_classes = {}

            self.global_sessions = SpanMonitorSession.Global_.GlobalSessions()
            self.global_sessions.parent = self
            self._children_name_map["global_sessions"] = "global-sessions"
            self._children_yang_names.add("global-sessions")

            self.statistics = SpanMonitorSession.Global_.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"
            self._children_yang_names.add("statistics")
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self._segment_path()


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"global-session" : ("global_session", SpanMonitorSession.Global_.GlobalSessions.GlobalSession)}

                self.global_session = YList(self)
                self._segment_path = lambda: "global-sessions"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions, [], name, value)


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
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {"destination-data" : ("destination_data", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData), "destination-id" : ("destination_id", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId)}
                    self._child_list_classes = {}

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
                    self._segment_path = lambda: "global-session" + "[session='" + self.session.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/global-sessions/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession, ['session', 'destination_error', 'destination_interface_handle', 'destination_interface_name', 'id', 'interface_error', 'name', 'session_class'], name, value)


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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"interface-data" : ("interface_data", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData), "next-hop-ipv4-data" : ("next_hop_ipv4_data", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data), "next-hop-ipv6-data" : ("next_hop_ipv6_data", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data), "pseudowire-data" : ("pseudowire_data", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "destination-data"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData, ['destination_class', 'invalid_value'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.interface_name = YLeaf(YType.str, "interface-name")

                            self.interface_state = YLeaf(YType.enumeration, "interface-state")
                            self._segment_path = lambda: "interface-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.InterfaceData, ['interface_name', 'interface_state'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address_is_reachable = YLeaf(YType.boolean, "address-is-reachable")

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "next-hop-ipv4-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, ['address_is_reachable', 'ipv4_address', 'vrf_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.address_is_reachable = YLeaf(YType.boolean, "address-is-reachable")

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "next-hop-ipv6-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, ['address_is_reachable', 'ipv6_address', 'vrf_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.pseudowire_is_up = YLeaf(YType.boolean, "pseudowire-is-up")

                            self.pseudowire_name = YLeaf(YType.str, "pseudowire-name")
                            self._segment_path = lambda: "pseudowire-data"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationData.PseudowireData, ['pseudowire_is_up', 'pseudowire_name'], name, value)


                class DestinationId(Entity):
                    """
                    Destination ID
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                    
                    .. attribute:: interface
                    
                    	Interface Handle
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"ipv4-address-and-vrf" : ("ipv4_address_and_vrf", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf), "ipv6-address-and-vrf" : ("ipv6_address_and_vrf", SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "destination-id"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId, ['destination_class', 'interface', 'invalid_value', 'pseudowire_id'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "ipv4-address-and-vrf"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, ['ipv4_address', 'vrf_name'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                            self.vrf_name = YLeaf(YType.str, "vrf-name")
                            self._segment_path = lambda: "ipv6-address-and-vrf"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global_.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, ['ipv6_address', 'vrf_name'], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {"statistic" : ("statistic", SpanMonitorSession.Global_.Statistics.Statistic)}

                self.statistic = YList(self)
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Global_.Statistics, [], name, value)


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
                
                	**pattern:** [a\-zA\-Z0\-9./\-]+
                
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
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self._child_container_classes = {}
                    self._child_list_classes = {}

                    self.session = YLeaf(YType.str, "session")

                    self.interface = YLeaf(YType.str, "interface")

                    self.octets_not_mirrored = YLeaf(YType.uint64, "octets-not-mirrored")

                    self.packets_not_mirrored = YLeaf(YType.uint64, "packets-not-mirrored")

                    self.rx_octets_mirrored = YLeaf(YType.uint64, "rx-octets-mirrored")

                    self.rx_packets_mirrored = YLeaf(YType.uint64, "rx-packets-mirrored")

                    self.tx_octets_mirrored = YLeaf(YType.uint64, "tx-octets-mirrored")

                    self.tx_packets_mirrored = YLeaf(YType.uint64, "tx-packets-mirrored")
                    self._segment_path = lambda: "statistic" + "[session='" + self.session.get() + "']" + "[interface='" + self.interface.get() + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/statistics/%s" % self._segment_path()

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Global_.Statistics.Statistic, ['session', 'interface', 'octets_not_mirrored', 'packets_not_mirrored', 'rx_octets_mirrored', 'rx_packets_mirrored', 'tx_octets_mirrored', 'tx_packets_mirrored'], name, value)


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
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"node" : ("node", SpanMonitorSession.Nodes.Node)}

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(SpanMonitorSession.Nodes, [], name, value)


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
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {"attachments" : ("attachments", SpanMonitorSession.Nodes.Node.Attachments), "hardware-sessions" : ("hardware_sessions", SpanMonitorSession.Nodes.Node.HardwareSessions), "interfaces" : ("interfaces", SpanMonitorSession.Nodes.Node.Interfaces)}
                self._child_list_classes = {}

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
                self._segment_path = lambda: "node" + "[node='" + self.node.get() + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/nodes/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Nodes.Node, ['node'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"attachment" : ("attachment", SpanMonitorSession.Nodes.Node.Attachments.Attachment)}

                    self.attachment = YList(self)
                    self._segment_path = lambda: "attachments"

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: dest_pw_type_not_supported
                    
                    	The destination PW type is not supported
                    	**type**\:  bool
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"destination-id" : ("destination_id", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId), "traffic-parameters" : ("traffic_parameters", SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "attachment" + "[session='" + self.session.get() + "']" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment, ['session', 'interface', 'dest_pw_type_not_supported', 'destination_interface', 'global_class', 'id', 'local_class', 'name', 'pfi_error', 'session_is_configured', 'source_interface', 'source_interface_is_a_destination', 'source_interface_state', 'traffic_direction'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ipv4-address-and-vrf" : ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf), "ipv6-address-and-vrf" : ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "destination-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId, ['destination_class', 'interface', 'invalid_value', 'pseudowire_id'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv4-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, ['ipv4_address', 'vrf_name'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv6-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, ['ipv6_address', 'vrf_name'], name, value)


                    class TrafficParameters(Entity):
                        """
                        Traffic mirroring parameters
                        
                        .. attribute:: acl_name
                        
                        	ACL name
                        	**type**\:  str
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                            self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                            self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                            self.port_level = YLeaf(YType.boolean, "port-level")

                            self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")
                            self._segment_path = lambda: "traffic-parameters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, ['acl_name', 'is_acl_enabled', 'mirror_bytes', 'mirror_interval', 'port_level', 'traffic_direction'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"hardware-session" : ("hardware_session", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession)}

                    self.hardware_session = YList(self)
                    self._segment_path = lambda: "hardware-sessions"

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions, [], name, value)


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
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"destination-id" : ("destination_id", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId)}
                        self._child_list_classes = {}

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
                        self._segment_path = lambda: "hardware-session"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, ['destination_interface', 'id', 'name', 'platform_error', 'session_class', 'session_class_xr', 'session_id'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ipv4-address-and-vrf" : ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf), "ipv6-address-and-vrf" : ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "destination-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId, ['destination_class', 'interface', 'invalid_value', 'pseudowire_id'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv4-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, ['ipv4_address', 'vrf_name'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv6-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, ['ipv6_address', 'vrf_name'], name, value)


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
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self._child_container_classes = {}
                    self._child_list_classes = {"interface" : ("interface", SpanMonitorSession.Nodes.Node.Interfaces.Interface)}

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular interface that
                    is set up in the hardware
                    
                    .. attribute:: interface  <key>
                    
                    	Interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: attachment
                    
                    	Attachment information
                    	**type**\: list of    :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment>`
                    
                    .. attribute:: destination_id
                    
                    	Destination ID (deprecated by Attachment)
                    	**type**\:   :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by Attachment)
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this interface while programming the hardware
                    	**type**\:  int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\:  str
                    
                    	**pattern:** [a\-zA\-Z0\-9./\-]+
                    
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
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self._child_container_classes = {"destination-id" : ("destination_id", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId), "traffic-mirroring-parameters" : ("traffic_mirroring_parameters", SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters)}
                        self._child_list_classes = {"attachment" : ("attachment", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment)}

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
                        self._segment_path = lambda: "interface" + "[interface='" + self.interface.get() + "']"

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface, ['interface', 'destination_interface', 'platform_error', 'source_interface', 'traffic_direction'], name, value)


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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"destination-id" : ("destination_id", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId), "traffic-mirroring-parameters" : ("traffic_mirroring_parameters", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters)}
                            self._child_list_classes = {}

                            self.class_ = YLeaf(YType.enumeration, "class")

                            self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId()
                            self.destination_id.parent = self
                            self._children_name_map["destination_id"] = "destination-id"
                            self._children_yang_names.add("destination-id")

                            self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters()
                            self.traffic_mirroring_parameters.parent = self
                            self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                            self._children_yang_names.add("traffic-mirroring-parameters")
                            self._segment_path = lambda: "attachment"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, ['class_'], name, value)


                        class DestinationId(Entity):
                            """
                            Destination ID
                            
                            .. attribute:: destination_class
                            
                            	DestinationClass
                            	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                            
                            .. attribute:: interface
                            
                            	Interface Handle
                            	**type**\:  str
                            
                            	**pattern:** [a\-zA\-Z0\-9./\-]+
                            
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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {"ipv4-address-and-vrf" : ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf), "ipv6-address-and-vrf" : ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf)}
                                self._child_list_classes = {}

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
                                self._segment_path = lambda: "destination-id"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId, ['destination_class', 'interface', 'invalid_value', 'pseudowire_id'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                                    self._segment_path = lambda: "ipv4-address-and-vrf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, ['ipv4_address', 'vrf_name'], name, value)


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
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self._child_container_classes = {}
                                    self._child_list_classes = {}

                                    self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                    self.vrf_name = YLeaf(YType.str, "vrf-name")
                                    self._segment_path = lambda: "ipv6-address-and-vrf"

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, ['ipv6_address', 'vrf_name'], name, value)


                        class TrafficMirroringParameters(Entity):
                            """
                            Traffic mirroring parameters
                            
                            .. attribute:: acl_name
                            
                            	ACL name
                            	**type**\:  str
                            
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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.acl_name = YLeaf(YType.str, "acl-name")

                                self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                                self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                                self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                                self.port_level = YLeaf(YType.boolean, "port-level")

                                self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")
                                self._segment_path = lambda: "traffic-mirroring-parameters"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, ['acl_name', 'is_acl_enabled', 'mirror_bytes', 'mirror_interval', 'port_level', 'traffic_direction'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID (deprecated by Attachment)
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:   :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\:  str
                        
                        	**pattern:** [a\-zA\-Z0\-9./\-]+
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {"ipv4-address-and-vrf" : ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf), "ipv6-address-and-vrf" : ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf)}
                            self._child_list_classes = {}

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
                            self._segment_path = lambda: "destination-id"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId, ['destination_class', 'interface', 'invalid_value', 'pseudowire_id'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv4_address = YLeaf(YType.str, "ipv4-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv4-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, ['ipv4_address', 'vrf_name'], name, value)


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
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self._child_container_classes = {}
                                self._child_list_classes = {}

                                self.ipv6_address = YLeaf(YType.str, "ipv6-address")

                                self.vrf_name = YLeaf(YType.str, "vrf-name")
                                self._segment_path = lambda: "ipv6-address-and-vrf"

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, ['ipv6_address', 'vrf_name'], name, value)


                    class TrafficMirroringParameters(Entity):
                        """
                        Traffic mirroring parameters (deprecated by
                        Attachment)
                        
                        .. attribute:: acl_name
                        
                        	ACL name
                        	**type**\:  str
                        
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
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self._child_container_classes = {}
                            self._child_list_classes = {}

                            self.acl_name = YLeaf(YType.str, "acl-name")

                            self.is_acl_enabled = YLeaf(YType.boolean, "is-acl-enabled")

                            self.mirror_bytes = YLeaf(YType.uint32, "mirror-bytes")

                            self.mirror_interval = YLeaf(YType.enumeration, "mirror-interval")

                            self.port_level = YLeaf(YType.boolean, "port-level")

                            self.traffic_direction = YLeaf(YType.enumeration, "traffic-direction")
                            self._segment_path = lambda: "traffic-mirroring-parameters"

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, ['acl_name', 'is_acl_enabled', 'mirror_bytes', 'mirror_interval', 'port_level', 'traffic_direction'], name, value)

    def clone_ptr(self):
        self._top_entity = SpanMonitorSession()
        return self._top_entity

