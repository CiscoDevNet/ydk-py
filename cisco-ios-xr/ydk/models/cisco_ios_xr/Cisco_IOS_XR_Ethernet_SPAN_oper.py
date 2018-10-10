""" Cisco_IOS_XR_Ethernet_SPAN_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR Ethernet\-SPAN package operational data.

This module contains definitions
for the following management objects\:
  span\-monitor\-session\: Monitor Session operational data

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class DestinationClass(Enum):
    """
    DestinationClass (Enum Class)

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
    ImStateEnum (Enum Class)

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
    MirrorInterval (Enum Class)

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
    SessionClass (Enum Class)

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
    TrafficDirection (Enum Class)

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
    	**type**\:  :py:class:`Global <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global>`
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes>`
    
    

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
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("global", ("global_", SpanMonitorSession.Global)), ("nodes", ("nodes", SpanMonitorSession.Nodes))])
        self._leafs = OrderedDict()

        self.global_ = SpanMonitorSession.Global()
        self.global_.parent = self
        self._children_name_map["global_"] = "global"

        self.nodes = SpanMonitorSession.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(SpanMonitorSession, [], name, value)


    class Global(Entity):
        """
        Global operational data
        
        .. attribute:: statistics
        
        	Table of statistics for source interfaces
        	**type**\:  :py:class:`Statistics <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.Statistics>`
        
        .. attribute:: global_sessions
        
        	Global Monitor Sessions table
        	**type**\:  :py:class:`GlobalSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Global, self).__init__()

            self.yang_name = "global"
            self.yang_parent_name = "span-monitor-session"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("statistics", ("statistics", SpanMonitorSession.Global.Statistics)), ("global-sessions", ("global_sessions", SpanMonitorSession.Global.GlobalSessions))])
            self._leafs = OrderedDict()

            self.statistics = SpanMonitorSession.Global.Statistics()
            self.statistics.parent = self
            self._children_name_map["statistics"] = "statistics"

            self.global_sessions = SpanMonitorSession.Global.GlobalSessions()
            self.global_sessions.parent = self
            self._children_name_map["global_sessions"] = "global-sessions"
            self._segment_path = lambda: "global"
            self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SpanMonitorSession.Global, [], name, value)


        class Statistics(Entity):
            """
            Table of statistics for source interfaces
            
            .. attribute:: statistic
            
            	Statistics for a particular source interface
            	**type**\: list of  		 :py:class:`Statistic <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.Statistics.Statistic>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Global.Statistics, self).__init__()

                self.yang_name = "statistics"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("statistic", ("statistic", SpanMonitorSession.Global.Statistics.Statistic))])
                self._leafs = OrderedDict()

                self.statistic = YList(self)
                self._segment_path = lambda: "statistics"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Global.Statistics, [], name, value)


            class Statistic(Entity):
                """
                Statistics for a particular source interface
                
                .. attribute:: session  (key)
                
                	Session Name
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: interface  (key)
                
                	Interface
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: rx_packets_mirrored
                
                	RX Packets Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: rx_octets_mirrored
                
                	RX Octets Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_packets_mirrored
                
                	TX Packets Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: tx_octets_mirrored
                
                	TX Octets Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: packets_not_mirrored
                
                	Packets Not Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                .. attribute:: octets_not_mirrored
                
                	Octets Not Mirrored
                	**type**\: int
                
                	**range:** 0..18446744073709551615
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Global.Statistics.Statistic, self).__init__()

                    self.yang_name = "statistic"
                    self.yang_parent_name = "statistics"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['session','interface']
                    self._child_classes = OrderedDict([])
                    self._leafs = OrderedDict([
                        ('session', (YLeaf(YType.str, 'session'), ['str'])),
                        ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                        ('rx_packets_mirrored', (YLeaf(YType.uint64, 'rx-packets-mirrored'), ['int'])),
                        ('rx_octets_mirrored', (YLeaf(YType.uint64, 'rx-octets-mirrored'), ['int'])),
                        ('tx_packets_mirrored', (YLeaf(YType.uint64, 'tx-packets-mirrored'), ['int'])),
                        ('tx_octets_mirrored', (YLeaf(YType.uint64, 'tx-octets-mirrored'), ['int'])),
                        ('packets_not_mirrored', (YLeaf(YType.uint64, 'packets-not-mirrored'), ['int'])),
                        ('octets_not_mirrored', (YLeaf(YType.uint64, 'octets-not-mirrored'), ['int'])),
                    ])
                    self.session = None
                    self.interface = None
                    self.rx_packets_mirrored = None
                    self.rx_octets_mirrored = None
                    self.tx_packets_mirrored = None
                    self.tx_octets_mirrored = None
                    self.packets_not_mirrored = None
                    self.octets_not_mirrored = None
                    self._segment_path = lambda: "statistic" + "[session='" + str(self.session) + "']" + "[interface='" + str(self.interface) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/statistics/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Global.Statistics.Statistic, ['session', 'interface', 'rx_packets_mirrored', 'rx_octets_mirrored', 'tx_packets_mirrored', 'tx_octets_mirrored', 'packets_not_mirrored', 'octets_not_mirrored'], name, value)


        class GlobalSessions(Entity):
            """
            Global Monitor Sessions table
            
            .. attribute:: global_session
            
            	Information about a globally\-configured monitor session
            	**type**\: list of  		 :py:class:`GlobalSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Global.GlobalSessions, self).__init__()

                self.yang_name = "global-sessions"
                self.yang_parent_name = "global"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = []
                self._child_classes = OrderedDict([("global-session", ("global_session", SpanMonitorSession.Global.GlobalSessions.GlobalSession))])
                self._leafs = OrderedDict()

                self.global_session = YList(self)
                self._segment_path = lambda: "global-sessions"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Global.GlobalSessions, [], name, value)


            class GlobalSession(Entity):
                """
                Information about a globally\-configured
                monitor session
                
                .. attribute:: session  (key)
                
                	Session Name
                	**type**\: str
                
                	**length:** 1..79
                
                .. attribute:: destination_data
                
                	Destination data
                	**type**\:  :py:class:`DestinationData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData>`
                
                .. attribute:: destination_id
                
                	Destination ID
                	**type**\:  :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId>`
                
                .. attribute:: inject_interface
                
                	Inject interface data
                	**type**\:  :py:class:`InjectInterface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.InjectInterface>`
                
                .. attribute:: name
                
                	Session Name
                	**type**\: str
                
                .. attribute:: session_class
                
                	Session class
                	**type**\:  :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                
                .. attribute:: id
                
                	Numerical ID assigned to session
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_error
                
                	Last error observed for the destination 
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: destination_interface_name
                
                	Destination interface name (deprecated by DestinationData, invalid for pseudowires)
                	**type**\: str
                
                .. attribute:: destination_interface_handle
                
                	Destination interface handle (deprecated by DestinationID, invalid for pseudowires)
                	**type**\: str
                
                	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                
                .. attribute:: interface_error
                
                	Last error observed for the destination interface (deprecated by DestinationError)
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Global.GlobalSessions.GlobalSession, self).__init__()

                    self.yang_name = "global-session"
                    self.yang_parent_name = "global-sessions"
                    self.is_top_level_class = False
                    self.has_list_ancestor = False
                    self.ylist_key_names = ['session']
                    self._child_classes = OrderedDict([("destination-data", ("destination_data", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData)), ("destination-id", ("destination_id", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId)), ("inject-interface", ("inject_interface", SpanMonitorSession.Global.GlobalSessions.GlobalSession.InjectInterface))])
                    self._leafs = OrderedDict([
                        ('session', (YLeaf(YType.str, 'session'), ['str'])),
                        ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ('session_class', (YLeaf(YType.enumeration, 'session-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClass', '')])),
                        ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                        ('destination_error', (YLeaf(YType.uint32, 'destination-error'), ['int'])),
                        ('destination_interface_name', (YLeaf(YType.str, 'destination-interface-name'), ['str'])),
                        ('destination_interface_handle', (YLeaf(YType.str, 'destination-interface-handle'), ['str'])),
                        ('interface_error', (YLeaf(YType.uint32, 'interface-error'), ['int'])),
                    ])
                    self.session = None
                    self.name = None
                    self.session_class = None
                    self.id = None
                    self.destination_error = None
                    self.destination_interface_name = None
                    self.destination_interface_handle = None
                    self.interface_error = None

                    self.destination_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData()
                    self.destination_data.parent = self
                    self._children_name_map["destination_data"] = "destination-data"

                    self.destination_id = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId()
                    self.destination_id.parent = self
                    self._children_name_map["destination_id"] = "destination-id"

                    self.inject_interface = SpanMonitorSession.Global.GlobalSessions.GlobalSession.InjectInterface()
                    self.inject_interface.parent = self
                    self._children_name_map["inject_interface"] = "inject-interface"
                    self._segment_path = lambda: "global-session" + "[session='" + str(self.session) + "']"
                    self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/global/global-sessions/%s" % self._segment_path()
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession, ['session', u'name', u'session_class', u'id', u'destination_error', u'destination_interface_name', u'destination_interface_handle', u'interface_error'], name, value)


                class DestinationData(Entity):
                    """
                    Destination data
                    
                    .. attribute:: interface_data
                    
                    	Interface data
                    	**type**\:  :py:class:`InterfaceData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData>`
                    
                    .. attribute:: pseudowire_data
                    
                    	Pseudowire data
                    	**type**\:  :py:class:`PseudowireData <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData>`
                    
                    .. attribute:: next_hop_ipv4_data
                    
                    	Next\-hop IPv4 data
                    	**type**\:  :py:class:`NextHopIpv4Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data>`
                    
                    .. attribute:: next_hop_ipv6_data
                    
                    	Next\-hop IPv6 data
                    	**type**\:  :py:class:`NextHopIpv6Data <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data>`
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData, self).__init__()

                        self.yang_name = "destination-data"
                        self.yang_parent_name = "global-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-data", ("interface_data", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData)), ("pseudowire-data", ("pseudowire_data", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData)), ("next-hop-ipv4-data", ("next_hop_ipv4_data", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data)), ("next-hop-ipv6-data", ("next_hop_ipv6_data", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data))])
                        self._leafs = OrderedDict([
                            ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                            ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                        ])
                        self.destination_class = None
                        self.invalid_value = None

                        self.interface_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData()
                        self.interface_data.parent = self
                        self._children_name_map["interface_data"] = "interface-data"

                        self.pseudowire_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData()
                        self.pseudowire_data.parent = self
                        self._children_name_map["pseudowire_data"] = "pseudowire-data"

                        self.next_hop_ipv4_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data()
                        self.next_hop_ipv4_data.parent = self
                        self._children_name_map["next_hop_ipv4_data"] = "next-hop-ipv4-data"

                        self.next_hop_ipv6_data = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data()
                        self.next_hop_ipv6_data.parent = self
                        self._children_name_map["next_hop_ipv6_data"] = "next-hop-ipv6-data"
                        self._segment_path = lambda: "destination-data"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData, [u'destination_class', u'invalid_value'], name, value)


                    class InterfaceData(Entity):
                        """
                        Interface data
                        
                        .. attribute:: interface_name
                        
                        	Interface Name
                        	**type**\: str
                        
                        .. attribute:: interface_state
                        
                        	Interface State
                        	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnum>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData, self).__init__()

                            self.yang_name = "interface-data"
                            self.yang_parent_name = "destination-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_state', (YLeaf(YType.enumeration, 'interface-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnum', '')])),
                            ])
                            self.interface_name = None
                            self.interface_state = None
                            self._segment_path = lambda: "interface-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.InterfaceData, [u'interface_name', u'interface_state'], name, value)


                    class PseudowireData(Entity):
                        """
                        Pseudowire data
                        
                        .. attribute:: pseudowire_name
                        
                        	Pseudowire Name
                        	**type**\: str
                        
                        .. attribute:: pseudowire_is_up
                        
                        	Pseudowire State
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData, self).__init__()

                            self.yang_name = "pseudowire-data"
                            self.yang_parent_name = "destination-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('pseudowire_name', (YLeaf(YType.str, 'pseudowire-name'), ['str'])),
                                ('pseudowire_is_up', (YLeaf(YType.boolean, 'pseudowire-is-up'), ['bool'])),
                            ])
                            self.pseudowire_name = None
                            self.pseudowire_is_up = None
                            self._segment_path = lambda: "pseudowire-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.PseudowireData, [u'pseudowire_name', u'pseudowire_is_up'], name, value)


                    class NextHopIpv4Data(Entity):
                        """
                        Next\-hop IPv4 data
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, self).__init__()

                            self.yang_name = "next-hop-ipv4-data"
                            self.yang_parent_name = "destination-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('address_is_reachable', (YLeaf(YType.boolean, 'address-is-reachable'), ['bool'])),
                            ])
                            self.ipv4_address = None
                            self.vrf_name = None
                            self.address_is_reachable = None
                            self._segment_path = lambda: "next-hop-ipv4-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv4Data, [u'ipv4_address', u'vrf_name', u'address_is_reachable'], name, value)


                    class NextHopIpv6Data(Entity):
                        """
                        Next\-hop IPv6 data
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF name
                        	**type**\: str
                        
                        .. attribute:: address_is_reachable
                        
                        	Address is reachable
                        	**type**\: bool
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, self).__init__()

                            self.yang_name = "next-hop-ipv6-data"
                            self.yang_parent_name = "destination-data"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ('address_is_reachable', (YLeaf(YType.boolean, 'address-is-reachable'), ['bool'])),
                            ])
                            self.ipv6_address = None
                            self.vrf_name = None
                            self.address_is_reachable = None
                            self._segment_path = lambda: "next-hop-ipv6-data"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationData.NextHopIpv6Data, [u'ipv6_address', u'vrf_name', u'address_is_reachable'], name, value)


                class DestinationId(Entity):
                    """
                    Destination ID
                    
                    .. attribute:: ipv4_address_and_vrf
                    
                    	IPv4 address
                    	**type**\:  :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf>`
                    
                    .. attribute:: ipv6_address_and_vrf
                    
                    	IPv6 address
                    	**type**\:  :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf>`
                    
                    .. attribute:: destination_class
                    
                    	DestinationClass
                    	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                    
                    .. attribute:: interface
                    
                    	Interface Handle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: pseudowire_id
                    
                    	Pseudowire XCID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: invalid_value
                    
                    	Invalid Parameter
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId, self).__init__()

                        self.yang_name = "destination-id"
                        self.yang_parent_name = "global-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("ipv4-address-and-vrf", ("ipv4_address_and_vrf", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf)), ("ipv6-address-and-vrf", ("ipv6_address_and_vrf", SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf))])
                        self._leafs = OrderedDict([
                            ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('pseudowire_id', (YLeaf(YType.uint32, 'pseudowire-id'), ['int'])),
                            ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                        ])
                        self.destination_class = None
                        self.interface = None
                        self.pseudowire_id = None
                        self.invalid_value = None

                        self.ipv4_address_and_vrf = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf()
                        self.ipv4_address_and_vrf.parent = self
                        self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"

                        self.ipv6_address_and_vrf = SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf()
                        self.ipv6_address_and_vrf.parent = self
                        self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                        self._segment_path = lambda: "destination-id"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId, [u'destination_class', u'interface', u'pseudowire_id', u'invalid_value'], name, value)


                    class Ipv4AddressAndVrf(Entity):
                        """
                        IPv4 address
                        
                        .. attribute:: ipv4_address
                        
                        	IPv4 address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, self).__init__()

                            self.yang_name = "ipv4-address-and-vrf"
                            self.yang_parent_name = "destination-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.ipv4_address = None
                            self.vrf_name = None
                            self._segment_path = lambda: "ipv4-address-and-vrf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv4AddressAndVrf, [u'ipv4_address', u'vrf_name'], name, value)


                    class Ipv6AddressAndVrf(Entity):
                        """
                        IPv6 address
                        
                        .. attribute:: ipv6_address
                        
                        	IPv6 address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: vrf_name
                        
                        	VRF
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, self).__init__()

                            self.yang_name = "ipv6-address-and-vrf"
                            self.yang_parent_name = "destination-id"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                            ])
                            self.ipv6_address = None
                            self.vrf_name = None
                            self._segment_path = lambda: "ipv6-address-and-vrf"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.DestinationId.Ipv6AddressAndVrf, [u'ipv6_address', u'vrf_name'], name, value)


                class InjectInterface(Entity):
                    """
                    Inject interface data
                    
                    .. attribute:: name
                    
                    	Interface Name
                    	**type**\: str
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Global.GlobalSessions.GlobalSession.InjectInterface, self).__init__()

                        self.yang_name = "inject-interface"
                        self.yang_parent_name = "global-session"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                        ])
                        self.name = None
                        self._segment_path = lambda: "inject-interface"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Global.GlobalSessions.GlobalSession.InjectInterface, [u'name'], name, value)


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node>`
        
        

        """

        _prefix = 'ethernet-span-oper'
        _revision = '2015-11-09'

        def __init__(self):
            super(SpanMonitorSession.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "span-monitor-session"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", SpanMonitorSession.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(SpanMonitorSession.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: attachments
            
            	Table of source interfaces configured as attached to a session
            	**type**\:  :py:class:`Attachments <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments>`
            
            .. attribute:: hardware_sessions
            
            	Table of sessions set up in the hardware.  When all sessions are operating correctly the entries in this table should match those entries in GlobalSessionTable that have a destination configured
            	**type**\:  :py:class:`HardwareSessions <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions>`
            
            .. attribute:: interfaces
            
            	Table of source interfaces set up in the hardware.  The entries in this table should match the entries in AttachmentTable when all sessions are operating correctly
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'ethernet-span-oper'
            _revision = '2015-11-09'

            def __init__(self):
                super(SpanMonitorSession.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("attachments", ("attachments", SpanMonitorSession.Nodes.Node.Attachments)), ("hardware-sessions", ("hardware_sessions", SpanMonitorSession.Nodes.Node.HardwareSessions)), ("interfaces", ("interfaces", SpanMonitorSession.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.attachments = SpanMonitorSession.Nodes.Node.Attachments()
                self.attachments.parent = self
                self._children_name_map["attachments"] = "attachments"

                self.hardware_sessions = SpanMonitorSession.Nodes.Node.HardwareSessions()
                self.hardware_sessions.parent = self
                self._children_name_map["hardware_sessions"] = "hardware-sessions"

                self.interfaces = SpanMonitorSession.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-Ethernet-SPAN-oper:span-monitor-session/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(SpanMonitorSession.Nodes.Node, ['node'], name, value)


            class Attachments(Entity):
                """
                Table of source interfaces configured as
                attached to a session
                
                .. attribute:: attachment
                
                	Information about a particular source interface configured as attached to monitor session
                	**type**\: list of  		 :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.Attachments, self).__init__()

                    self.yang_name = "attachments"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("attachment", ("attachment", SpanMonitorSession.Nodes.Node.Attachments.Attachment))])
                    self._leafs = OrderedDict()

                    self.attachment = YList(self)
                    self._segment_path = lambda: "attachments"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments, [], name, value)


                class Attachment(Entity):
                    """
                    Information about a particular source
                    interface configured as attached to monitor
                    session
                    
                    .. attribute:: session  (key)
                    
                    	Session Name
                    	**type**\: str
                    
                    	**length:** 1..79
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: traffic_parameters
                    
                    	Traffic mirroring parameters
                    	**type**\:  :py:class:`TrafficParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters>`
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:  :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId>`
                    
                    .. attribute:: name
                    
                    	Session Name
                    	**type**\: str
                    
                    .. attribute:: local_class
                    
                    	Local attachment class
                    	**type**\:  :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: id
                    
                    	Numerical ID assigned to session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: global_class
                    
                    	Global session class
                    	**type**\:  :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: session_is_configured
                    
                    	The Session is configured globally
                    	**type**\: bool
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: source_interface_state
                    
                    	Source interface state
                    	**type**\:  :py:class:`ImStateEnum <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.ImStateEnum>`
                    
                    .. attribute:: pfi_error
                    
                    	Last error returned from PFI for this interface
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: dest_pw_type_not_supported
                    
                    	The destination PW type is not supported
                    	**type**\: bool
                    
                    .. attribute:: source_interface_is_a_destination
                    
                    	This source interface is a destination for another monitor\-session
                    	**type**\: bool
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by TrafficParameters)
                    	**type**\:  :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.Attachments.Attachment, self).__init__()

                        self.yang_name = "attachment"
                        self.yang_parent_name = "attachments"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['session','interface']
                        self._child_classes = OrderedDict([("traffic-parameters", ("traffic_parameters", SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters)), ("destination-id", ("destination_id", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId))])
                        self._leafs = OrderedDict([
                            ('session', (YLeaf(YType.str, 'session'), ['str'])),
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('local_class', (YLeaf(YType.enumeration, 'local-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClass', '')])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('global_class', (YLeaf(YType.enumeration, 'global-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClass', '')])),
                            ('session_is_configured', (YLeaf(YType.boolean, 'session-is-configured'), ['bool'])),
                            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                            ('source_interface_state', (YLeaf(YType.enumeration, 'source-interface-state'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'ImStateEnum', '')])),
                            ('pfi_error', (YLeaf(YType.uint32, 'pfi-error'), ['int'])),
                            ('dest_pw_type_not_supported', (YLeaf(YType.boolean, 'dest-pw-type-not-supported'), ['bool'])),
                            ('source_interface_is_a_destination', (YLeaf(YType.boolean, 'source-interface-is-a-destination'), ['bool'])),
                            ('destination_interface', (YLeaf(YType.str, 'destination-interface'), ['str'])),
                            ('traffic_direction', (YLeaf(YType.enumeration, 'traffic-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirection', '')])),
                        ])
                        self.session = None
                        self.interface = None
                        self.name = None
                        self.local_class = None
                        self.id = None
                        self.global_class = None
                        self.session_is_configured = None
                        self.source_interface = None
                        self.source_interface_state = None
                        self.pfi_error = None
                        self.dest_pw_type_not_supported = None
                        self.source_interface_is_a_destination = None
                        self.destination_interface = None
                        self.traffic_direction = None

                        self.traffic_parameters = SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters()
                        self.traffic_parameters.parent = self
                        self._children_name_map["traffic_parameters"] = "traffic-parameters"

                        self.destination_id = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"
                        self._segment_path = lambda: "attachment" + "[session='" + str(self.session) + "']" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment, ['session', 'interface', 'name', 'local_class', 'id', 'global_class', 'session_is_configured', 'source_interface', 'source_interface_state', 'pfi_error', 'dest_pw_type_not_supported', 'source_interface_is_a_destination', 'destination_interface', 'traffic_direction'], name, value)


                    class TrafficParameters(Entity):
                        """
                        Traffic mirroring parameters
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:  :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\: bool
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\: bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:  :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                        
                        .. attribute:: acl_name
                        
                        	ACL name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, self).__init__()

                            self.yang_name = "traffic-parameters"
                            self.yang_parent_name = "attachment"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('traffic_direction', (YLeaf(YType.enumeration, 'traffic-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirection', '')])),
                                ('port_level', (YLeaf(YType.boolean, 'port-level'), ['bool'])),
                                ('is_acl_enabled', (YLeaf(YType.boolean, 'is-acl-enabled'), ['bool'])),
                                ('mirror_bytes', (YLeaf(YType.uint32, 'mirror-bytes'), ['int'])),
                                ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorInterval', '')])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.traffic_direction = None
                            self.port_level = None
                            self.is_acl_enabled = None
                            self.mirror_bytes = None
                            self.mirror_interval = None
                            self.acl_name = None
                            self._segment_path = lambda: "traffic-parameters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.TrafficParameters, [u'traffic_direction', u'port_level', u'is_acl_enabled', u'mirror_bytes', u'mirror_interval', u'acl_name'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:  :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:  :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4-address-and-vrf", ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf)), ("ipv6-address-and-vrf", ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf))])
                            self._leafs = OrderedDict([
                                ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('pseudowire_id', (YLeaf(YType.uint32, 'pseudowire-id'), ['int'])),
                                ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                            ])
                            self.destination_class = None
                            self.interface = None
                            self.pseudowire_id = None
                            self.invalid_value = None

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._segment_path = lambda: "destination-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId, [u'destination_class', u'interface', u'pseudowire_id', u'invalid_value'], name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv4_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv4-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv4AddressAndVrf, [u'ipv4_address', u'vrf_name'], name, value)


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv6_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv6-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Attachments.Attachment.DestinationId.Ipv6AddressAndVrf, [u'ipv6_address', u'vrf_name'], name, value)


            class HardwareSessions(Entity):
                """
                Table of sessions set up in the hardware. 
                When all sessions are operating correctly the
                entries in this table should match those
                entries in GlobalSessionTable that have a
                destination configured
                
                .. attribute:: hardware_session
                
                	Information about a particular session that is set up in the hardware
                	**type**\: list of  		 :py:class:`HardwareSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.HardwareSessions, self).__init__()

                    self.yang_name = "hardware-sessions"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("hardware-session", ("hardware_session", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession))])
                    self._leafs = OrderedDict()

                    self.hardware_session = YList(self)
                    self._segment_path = lambda: "hardware-sessions"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions, [], name, value)


                class HardwareSession(Entity):
                    """
                    Information about a particular session that
                    is set up in the hardware
                    
                    .. attribute:: session_class
                    
                    	Sesssion class
                    	**type**\:  :py:class:`SpanSessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes.SpanSessionClass>`
                    
                    .. attribute:: session_id
                    
                    	Session ID
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_id
                    
                    	Destination ID
                    	**type**\:  :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId>`
                    
                    .. attribute:: id
                    
                    	Assigned numerical ID for this session
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: name
                    
                    	Configured Session Name
                    	**type**\: str
                    
                    .. attribute:: session_class_xr
                    
                    	Session class
                    	**type**\:  :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by DestinationID, invalid for pseudowires)
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this session while programming the hardware
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: inject_interface_ifh
                    
                    	Inject Interface ifhandle
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: inject_interface_mac
                    
                    	Inject Interface MAC address
                    	**type**\: str
                    
                    	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                    
                    .. attribute:: inject_interface_invalid
                    
                    	An inject interface is flagged as invalid on a particular node if the interface exists on that node, and there is no attachment interface config for it
                    	**type**\: bool
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, self).__init__()

                        self.yang_name = "hardware-session"
                        self.yang_parent_name = "hardware-sessions"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("destination-id", ("destination_id", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId))])
                        self._leafs = OrderedDict([
                            ('session_class', (YLeaf(YType.enumeration, 'session-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_datatypes', 'SpanSessionClass', '')])),
                            ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                            ('id', (YLeaf(YType.uint32, 'id'), ['int'])),
                            ('name', (YLeaf(YType.str, 'name'), ['str'])),
                            ('session_class_xr', (YLeaf(YType.enumeration, 'session-class-xr'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClass', '')])),
                            ('destination_interface', (YLeaf(YType.str, 'destination-interface'), ['str'])),
                            ('platform_error', (YLeaf(YType.uint32, 'platform-error'), ['int'])),
                            ('inject_interface_ifh', (YLeaf(YType.str, 'inject-interface-ifh'), ['str'])),
                            ('inject_interface_mac', (YLeaf(YType.str, 'inject-interface-mac'), ['str'])),
                            ('inject_interface_invalid', (YLeaf(YType.boolean, 'inject-interface-invalid'), ['bool'])),
                        ])
                        self.session_class = None
                        self.session_id = None
                        self.id = None
                        self.name = None
                        self.session_class_xr = None
                        self.destination_interface = None
                        self.platform_error = None
                        self.inject_interface_ifh = None
                        self.inject_interface_mac = None
                        self.inject_interface_invalid = None

                        self.destination_id = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"
                        self._segment_path = lambda: "hardware-session"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession, ['session_class', 'session_id', u'id', u'name', u'session_class_xr', u'destination_interface', u'platform_error', u'inject_interface_ifh', u'inject_interface_mac', u'inject_interface_invalid'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:  :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:  :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4-address-and-vrf", ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf)), ("ipv6-address-and-vrf", ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf))])
                            self._leafs = OrderedDict([
                                ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('pseudowire_id', (YLeaf(YType.uint32, 'pseudowire-id'), ['int'])),
                                ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                            ])
                            self.destination_class = None
                            self.interface = None
                            self.pseudowire_id = None
                            self.invalid_value = None

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._segment_path = lambda: "destination-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId, [u'destination_class', u'interface', u'pseudowire_id', u'invalid_value'], name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv4_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv4-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv4AddressAndVrf, [u'ipv4_address', u'vrf_name'], name, value)


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv6_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv6-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.HardwareSessions.HardwareSession.DestinationId.Ipv6AddressAndVrf, [u'ipv6_address', u'vrf_name'], name, value)


            class Interfaces(Entity):
                """
                Table of source interfaces set up in the
                hardware.  The entries in this table should
                match the entries in AttachmentTable when all
                sessions are operating correctly
                
                .. attribute:: interface
                
                	Information about a particular interface that is set up in the hardware
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'ethernet-span-oper'
                _revision = '2015-11-09'

                def __init__(self):
                    super(SpanMonitorSession.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", SpanMonitorSession.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Information about a particular interface that
                    is set up in the hardware
                    
                    .. attribute:: interface  (key)
                    
                    	Interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: destination_id
                    
                    	Destination ID (deprecated by Attachment)
                    	**type**\:  :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId>`
                    
                    .. attribute:: traffic_mirroring_parameters
                    
                    	Traffic mirroring parameters (deprecated by Attachment)
                    	**type**\:  :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters>`
                    
                    .. attribute:: source_interface
                    
                    	Source interface
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: platform_error
                    
                    	Last error observed for this interface while programming the hardware
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: destination_interface
                    
                    	Destination interface (deprecated by Attachment)
                    	**type**\: str
                    
                    	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                    
                    .. attribute:: traffic_direction
                    
                    	Traffic mirroring direction (deprecated by Attachment)
                    	**type**\:  :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                    
                    .. attribute:: attachment
                    
                    	Attachment information
                    	**type**\: list of  		 :py:class:`Attachment <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment>`
                    
                    

                    """

                    _prefix = 'ethernet-span-oper'
                    _revision = '2015-11-09'

                    def __init__(self):
                        super(SpanMonitorSession.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface']
                        self._child_classes = OrderedDict([("destination-id", ("destination_id", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId)), ("traffic-mirroring-parameters", ("traffic_mirroring_parameters", SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters)), ("attachment", ("attachment", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment))])
                        self._leafs = OrderedDict([
                            ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                            ('source_interface', (YLeaf(YType.str, 'source-interface'), ['str'])),
                            ('platform_error', (YLeaf(YType.uint32, 'platform-error'), ['int'])),
                            ('destination_interface', (YLeaf(YType.str, 'destination-interface'), ['str'])),
                            ('traffic_direction', (YLeaf(YType.enumeration, 'traffic-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirection', '')])),
                        ])
                        self.interface = None
                        self.source_interface = None
                        self.platform_error = None
                        self.destination_interface = None
                        self.traffic_direction = None

                        self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId()
                        self.destination_id.parent = self
                        self._children_name_map["destination_id"] = "destination-id"

                        self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters()
                        self.traffic_mirroring_parameters.parent = self
                        self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"

                        self.attachment = YList(self)
                        self._segment_path = lambda: "interface" + "[interface='" + str(self.interface) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface, ['interface', u'source_interface', u'platform_error', u'destination_interface', u'traffic_direction'], name, value)


                    class DestinationId(Entity):
                        """
                        Destination ID (deprecated by Attachment)
                        
                        .. attribute:: ipv4_address_and_vrf
                        
                        	IPv4 address
                        	**type**\:  :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf>`
                        
                        .. attribute:: ipv6_address_and_vrf
                        
                        	IPv6 address
                        	**type**\:  :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf>`
                        
                        .. attribute:: destination_class
                        
                        	DestinationClass
                        	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                        
                        .. attribute:: interface
                        
                        	Interface Handle
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: pseudowire_id
                        
                        	Pseudowire XCID
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: invalid_value
                        
                        	Invalid Parameter
                        	**type**\: int
                        
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
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("ipv4-address-and-vrf", ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf)), ("ipv6-address-and-vrf", ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf))])
                            self._leafs = OrderedDict([
                                ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                                ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                ('pseudowire_id', (YLeaf(YType.uint32, 'pseudowire-id'), ['int'])),
                                ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                            ])
                            self.destination_class = None
                            self.interface = None
                            self.pseudowire_id = None
                            self.invalid_value = None

                            self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf()
                            self.ipv4_address_and_vrf.parent = self
                            self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"

                            self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf()
                            self.ipv6_address_and_vrf.parent = self
                            self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                            self._segment_path = lambda: "destination-id"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId, [u'destination_class', u'interface', u'pseudowire_id', u'invalid_value'], name, value)


                        class Ipv4AddressAndVrf(Entity):
                            """
                            IPv4 address
                            
                            .. attribute:: ipv4_address
                            
                            	IPv4 address
                            	**type**\: str
                            
                            	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                self.yang_name = "ipv4-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv4_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv4-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv4AddressAndVrf, [u'ipv4_address', u'vrf_name'], name, value)


                        class Ipv6AddressAndVrf(Entity):
                            """
                            IPv6 address
                            
                            .. attribute:: ipv6_address
                            
                            	IPv6 address
                            	**type**\: str
                            
                            	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                            
                            .. attribute:: vrf_name
                            
                            	VRF
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                self.yang_name = "ipv6-address-and-vrf"
                                self.yang_parent_name = "destination-id"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                    ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                ])
                                self.ipv6_address = None
                                self.vrf_name = None
                                self._segment_path = lambda: "ipv6-address-and-vrf"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.DestinationId.Ipv6AddressAndVrf, [u'ipv6_address', u'vrf_name'], name, value)


                    class TrafficMirroringParameters(Entity):
                        """
                        Traffic mirroring parameters (deprecated by
                        Attachment)
                        
                        .. attribute:: traffic_direction
                        
                        	Direction
                        	**type**\:  :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                        
                        .. attribute:: port_level
                        
                        	Port level mirroring
                        	**type**\: bool
                        
                        .. attribute:: is_acl_enabled
                        
                        	ACL enabled
                        	**type**\: bool
                        
                        .. attribute:: mirror_bytes
                        
                        	Number of bytes to mirror
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        	**units**\: byte
                        
                        .. attribute:: mirror_interval
                        
                        	Interval between mirrored packets
                        	**type**\:  :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                        
                        .. attribute:: acl_name
                        
                        	ACL name
                        	**type**\: str
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, self).__init__()

                            self.yang_name = "traffic-mirroring-parameters"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('traffic_direction', (YLeaf(YType.enumeration, 'traffic-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirection', '')])),
                                ('port_level', (YLeaf(YType.boolean, 'port-level'), ['bool'])),
                                ('is_acl_enabled', (YLeaf(YType.boolean, 'is-acl-enabled'), ['bool'])),
                                ('mirror_bytes', (YLeaf(YType.uint32, 'mirror-bytes'), ['int'])),
                                ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorInterval', '')])),
                                ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                            ])
                            self.traffic_direction = None
                            self.port_level = None
                            self.is_acl_enabled = None
                            self.mirror_bytes = None
                            self.mirror_interval = None
                            self.acl_name = None
                            self._segment_path = lambda: "traffic-mirroring-parameters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.TrafficMirroringParameters, [u'traffic_direction', u'port_level', u'is_acl_enabled', u'mirror_bytes', u'mirror_interval', u'acl_name'], name, value)


                    class Attachment(Entity):
                        """
                        Attachment information
                        
                        .. attribute:: destination_id
                        
                        	Destination ID
                        	**type**\:  :py:class:`DestinationId <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId>`
                        
                        .. attribute:: traffic_mirroring_parameters
                        
                        	Traffic mirroring parameters
                        	**type**\:  :py:class:`TrafficMirroringParameters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters>`
                        
                        .. attribute:: class_
                        
                        	Attachment class
                        	**type**\:  :py:class:`SessionClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SessionClass>`
                        
                        

                        """

                        _prefix = 'ethernet-span-oper'
                        _revision = '2015-11-09'

                        def __init__(self):
                            super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, self).__init__()

                            self.yang_name = "attachment"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("destination-id", ("destination_id", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId)), ("traffic-mirroring-parameters", ("traffic_mirroring_parameters", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters))])
                            self._leafs = OrderedDict([
                                ('class_', (YLeaf(YType.enumeration, 'class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'SessionClass', '')])),
                            ])
                            self.class_ = None

                            self.destination_id = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId()
                            self.destination_id.parent = self
                            self._children_name_map["destination_id"] = "destination-id"

                            self.traffic_mirroring_parameters = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters()
                            self.traffic_mirroring_parameters.parent = self
                            self._children_name_map["traffic_mirroring_parameters"] = "traffic-mirroring-parameters"
                            self._segment_path = lambda: "attachment"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment, [u'class_'], name, value)


                        class DestinationId(Entity):
                            """
                            Destination ID
                            
                            .. attribute:: ipv4_address_and_vrf
                            
                            	IPv4 address
                            	**type**\:  :py:class:`Ipv4AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf>`
                            
                            .. attribute:: ipv6_address_and_vrf
                            
                            	IPv6 address
                            	**type**\:  :py:class:`Ipv6AddressAndVrf <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf>`
                            
                            .. attribute:: destination_class
                            
                            	DestinationClass
                            	**type**\:  :py:class:`DestinationClass <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.DestinationClass>`
                            
                            .. attribute:: interface
                            
                            	Interface Handle
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: pseudowire_id
                            
                            	Pseudowire XCID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: invalid_value
                            
                            	Invalid Parameter
                            	**type**\: int
                            
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
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("ipv4-address-and-vrf", ("ipv4_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf)), ("ipv6-address-and-vrf", ("ipv6_address_and_vrf", SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf))])
                                self._leafs = OrderedDict([
                                    ('destination_class', (YLeaf(YType.enumeration, 'destination-class'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'DestinationClass', '')])),
                                    ('interface', (YLeaf(YType.str, 'interface'), ['str'])),
                                    ('pseudowire_id', (YLeaf(YType.uint32, 'pseudowire-id'), ['int'])),
                                    ('invalid_value', (YLeaf(YType.uint32, 'invalid-value'), ['int'])),
                                ])
                                self.destination_class = None
                                self.interface = None
                                self.pseudowire_id = None
                                self.invalid_value = None

                                self.ipv4_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf()
                                self.ipv4_address_and_vrf.parent = self
                                self._children_name_map["ipv4_address_and_vrf"] = "ipv4-address-and-vrf"

                                self.ipv6_address_and_vrf = SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf()
                                self.ipv6_address_and_vrf.parent = self
                                self._children_name_map["ipv6_address_and_vrf"] = "ipv6-address-and-vrf"
                                self._segment_path = lambda: "destination-id"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId, [u'destination_class', u'interface', u'pseudowire_id', u'invalid_value'], name, value)


                            class Ipv4AddressAndVrf(Entity):
                                """
                                IPv4 address
                                
                                .. attribute:: ipv4_address
                                
                                	IPv4 address
                                	**type**\: str
                                
                                	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, self).__init__()

                                    self.yang_name = "ipv4-address-and-vrf"
                                    self.yang_parent_name = "destination-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv4_address', (YLeaf(YType.str, 'ipv4-address'), ['str'])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.ipv4_address = None
                                    self.vrf_name = None
                                    self._segment_path = lambda: "ipv4-address-and-vrf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv4AddressAndVrf, [u'ipv4_address', u'vrf_name'], name, value)


                            class Ipv6AddressAndVrf(Entity):
                                """
                                IPv6 address
                                
                                .. attribute:: ipv6_address
                                
                                	IPv6 address
                                	**type**\: str
                                
                                	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                                
                                .. attribute:: vrf_name
                                
                                	VRF
                                	**type**\: str
                                
                                

                                """

                                _prefix = 'ethernet-span-oper'
                                _revision = '2015-11-09'

                                def __init__(self):
                                    super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, self).__init__()

                                    self.yang_name = "ipv6-address-and-vrf"
                                    self.yang_parent_name = "destination-id"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('ipv6_address', (YLeaf(YType.str, 'ipv6-address'), ['str'])),
                                        ('vrf_name', (YLeaf(YType.str, 'vrf-name'), ['str'])),
                                    ])
                                    self.ipv6_address = None
                                    self.vrf_name = None
                                    self._segment_path = lambda: "ipv6-address-and-vrf"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.DestinationId.Ipv6AddressAndVrf, [u'ipv6_address', u'vrf_name'], name, value)


                        class TrafficMirroringParameters(Entity):
                            """
                            Traffic mirroring parameters
                            
                            .. attribute:: traffic_direction
                            
                            	Direction
                            	**type**\:  :py:class:`TrafficDirection <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.TrafficDirection>`
                            
                            .. attribute:: port_level
                            
                            	Port level mirroring
                            	**type**\: bool
                            
                            .. attribute:: is_acl_enabled
                            
                            	ACL enabled
                            	**type**\: bool
                            
                            .. attribute:: mirror_bytes
                            
                            	Number of bytes to mirror
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: byte
                            
                            .. attribute:: mirror_interval
                            
                            	Interval between mirrored packets
                            	**type**\:  :py:class:`MirrorInterval <ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper.MirrorInterval>`
                            
                            .. attribute:: acl_name
                            
                            	ACL name
                            	**type**\: str
                            
                            

                            """

                            _prefix = 'ethernet-span-oper'
                            _revision = '2015-11-09'

                            def __init__(self):
                                super(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, self).__init__()

                                self.yang_name = "traffic-mirroring-parameters"
                                self.yang_parent_name = "attachment"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('traffic_direction', (YLeaf(YType.enumeration, 'traffic-direction'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'TrafficDirection', '')])),
                                    ('port_level', (YLeaf(YType.boolean, 'port-level'), ['bool'])),
                                    ('is_acl_enabled', (YLeaf(YType.boolean, 'is-acl-enabled'), ['bool'])),
                                    ('mirror_bytes', (YLeaf(YType.uint32, 'mirror-bytes'), ['int'])),
                                    ('mirror_interval', (YLeaf(YType.enumeration, 'mirror-interval'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_Ethernet_SPAN_oper', 'MirrorInterval', '')])),
                                    ('acl_name', (YLeaf(YType.str, 'acl-name'), ['str'])),
                                ])
                                self.traffic_direction = None
                                self.port_level = None
                                self.is_acl_enabled = None
                                self.mirror_bytes = None
                                self.mirror_interval = None
                                self.acl_name = None
                                self._segment_path = lambda: "traffic-mirroring-parameters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(SpanMonitorSession.Nodes.Node.Interfaces.Interface.Attachment.TrafficMirroringParameters, [u'traffic_direction', u'port_level', u'is_acl_enabled', u'mirror_bytes', u'mirror_interval', u'acl_name'], name, value)

    def clone_ptr(self):
        self._top_entity = SpanMonitorSession()
        return self._top_entity

