""" Cisco_IOS_XR_perf_meas_oper 

This module contains a collection of YANG definitions
for Cisco IOS\-XR perf\-meas package operational data.

This module contains definitions
for the following management objects\:
  performance\-measurement\: Performance Measurement operational
    data
  performance\-measurement\-responder\: performance measurement
    responder

Copyright (c) 2013\-2018 by Cisco Systems, Inc.
All rights reserved.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class PmAdvertReason(Enum):
    """
    PmAdvertReason (Enum Class)

    PM advertisement reason

    .. data:: periodic_timer_expired_no_advertisements = 0

    	Periodic timer expired. No advertisements have

    	occured

    .. data:: periodic_advertisement_threshold_average = 1

    	Periodic timer expired. Average value threshold

    	crossed

    .. data:: periodic_advertisement_threshold_minimum = 2

    	Periodic timer expired. Minimum value threshold

    	crossed

    .. data:: periodic_advertisement_threshold_maximum = 3

    	Periodic timer expired. Maximum value threshold

    	crossed

    .. data:: periodic_advertisement_threshold_variance = 4

    	Periodic timer expired. Variance value

    	threshold crossed

    .. data:: accelerated_advertisement_threshold_minimum = 5

    	Accelerated minimum value threshold crossed

    .. data:: accelerated_advertisement_upper_bound_minimum = 6

    	Accelerated minimum value upper bound crossed

    .. data:: advertisement_enabled = 7

    	Advertisement enabled

    .. data:: advertisement_disabled = 8

    	Advertisement disabled

    .. data:: session_unconfigured = 9

    	Session unconfigured

    .. data:: clear_cli_command = 10

    	Session cleared via CLI

    .. data:: advertise_delay_config = 11

    	Advertise delay config

    .. data:: advertise_delay_unconfig = 12

    	Advertise delay unconfig

    .. data:: received_control_code_error = 13

    	Recevied control code error, as per RFC 6374,

    	from the responder

    """

    periodic_timer_expired_no_advertisements = Enum.YLeaf(0, "periodic-timer-expired-no-advertisements")

    periodic_advertisement_threshold_average = Enum.YLeaf(1, "periodic-advertisement-threshold-average")

    periodic_advertisement_threshold_minimum = Enum.YLeaf(2, "periodic-advertisement-threshold-minimum")

    periodic_advertisement_threshold_maximum = Enum.YLeaf(3, "periodic-advertisement-threshold-maximum")

    periodic_advertisement_threshold_variance = Enum.YLeaf(4, "periodic-advertisement-threshold-variance")

    accelerated_advertisement_threshold_minimum = Enum.YLeaf(5, "accelerated-advertisement-threshold-minimum")

    accelerated_advertisement_upper_bound_minimum = Enum.YLeaf(6, "accelerated-advertisement-upper-bound-minimum")

    advertisement_enabled = Enum.YLeaf(7, "advertisement-enabled")

    advertisement_disabled = Enum.YLeaf(8, "advertisement-disabled")

    session_unconfigured = Enum.YLeaf(9, "session-unconfigured")

    clear_cli_command = Enum.YLeaf(10, "clear-cli-command")

    advertise_delay_config = Enum.YLeaf(11, "advertise-delay-config")

    advertise_delay_unconfig = Enum.YLeaf(12, "advertise-delay-unconfig")

    received_control_code_error = Enum.YLeaf(13, "received-control-code-error")


class PmDelayMode(Enum):
    """
    PmDelayMode (Enum Class)

    PM Delay Mode Type

    .. data:: delay_mode_one_way = 0

    	One-way delay-measurement mode

    .. data:: delay_mode_two_way = 1

    	Two-way delay-measurement mode

    """

    delay_mode_one_way = Enum.YLeaf(0, "delay-mode-one-way")

    delay_mode_two_way = Enum.YLeaf(1, "delay-mode-two-way")


class PmMeasurement(Enum):
    """
    PmMeasurement (Enum Class)

    PM Measurement Type

    .. data:: delay_measurement_type = 0

    	Delay Measurement Type

    """

    delay_measurement_type = Enum.YLeaf(0, "delay-measurement-type")


class PmProbeNotRunningReason(Enum):
    """
    PmProbeNotRunningReason (Enum Class)

    PM probe not running reason

    .. data:: probe_is_running = 0

    	Probe is running

    .. data:: platform_not_supported = 1

    	Measurement is not supported on this plaftorm

    .. data:: nonv1_active_node = 2

    	Node is not V1 active

    .. data:: control_code_error = 3

    	An uncleared control code error was received

    .. data:: interface_admin_down = 4

    	Interface admin down

    .. data:: interface_down = 5

    	Interface down

    .. data:: mpls_capability_not_present = 6

    	MPLS is not enabled on interface

    .. data:: interface_not_present = 7

    	Interface not present or preconfigured

    .. data:: ip_address_not_configured = 8

    	IP address is not present on interface

    """

    probe_is_running = Enum.YLeaf(0, "probe-is-running")

    platform_not_supported = Enum.YLeaf(1, "platform-not-supported")

    nonv1_active_node = Enum.YLeaf(2, "nonv1-active-node")

    control_code_error = Enum.YLeaf(3, "control-code-error")

    interface_admin_down = Enum.YLeaf(4, "interface-admin-down")

    interface_down = Enum.YLeaf(5, "interface-down")

    mpls_capability_not_present = Enum.YLeaf(6, "mpls-capability-not-present")

    interface_not_present = Enum.YLeaf(7, "interface-not-present")

    ip_address_not_configured = Enum.YLeaf(8, "ip-address-not-configured")


class PmTransport(Enum):
    """
    PmTransport (Enum Class)

    PM Transport Type

    .. data:: interface_transport_type = 0

    	Interface transport type

    .. data:: rsvpte_transport_type = 1

    	RSVP-TE tunnel transport type

    .. data:: sr_policy_transport_type = 2

    	SR Policy transport type

    """

    interface_transport_type = Enum.YLeaf(0, "interface-transport-type")

    rsvpte_transport_type = Enum.YLeaf(1, "rsvpte-transport-type")

    sr_policy_transport_type = Enum.YLeaf(2, "sr-policy-transport-type")



class PerformanceMeasurement(Entity):
    """
    Performance Measurement operational data
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes>`
    
    

    """

    _prefix = 'perf-meas-oper'
    _revision = '2017-10-17'

    def __init__(self):
        super(PerformanceMeasurement, self).__init__()
        self._top_entity = None

        self.yang_name = "performance-measurement"
        self.yang_parent_name = "Cisco-IOS-XR-perf-meas-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PerformanceMeasurement.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PerformanceMeasurement.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PerformanceMeasurement, [], name, value)


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node>`
        
        

        """

        _prefix = 'perf-meas-oper'
        _revision = '2017-10-17'

        def __init__(self):
            super(PerformanceMeasurement.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "performance-measurement"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PerformanceMeasurement.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerformanceMeasurement.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	Summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary>`
            
            .. attribute:: interfaces
            
            	Interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'perf-meas-oper'
            _revision = '2017-10-17'

            def __init__(self):
                super(PerformanceMeasurement.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("summary", ("summary", PerformanceMeasurement.Nodes.Node.Summary)), ("interfaces", ("interfaces", PerformanceMeasurement.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.summary = PerformanceMeasurement.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.interfaces = PerformanceMeasurement.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerformanceMeasurement.Nodes.Node, ['node'], name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: delay_summary
                
                	Delay summary
                	**type**\:  :py:class:`DelaySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary>`
                
                .. attribute:: total_interfaces
                
                	Number of delay measurement interfaces enabled
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'perf-meas-oper'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("delay-summary", ("delay_summary", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary))])
                    self._leafs = OrderedDict([
                        ('total_interfaces', (YLeaf(YType.uint32, 'total-interfaces'), ['int'])),
                    ])
                    self.total_interfaces = None

                    self.delay_summary = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary()
                    self.delay_summary.parent = self
                    self._children_name_map["delay_summary"] = "delay-summary"
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary, ['total_interfaces'], name, value)


                class DelaySummary(Entity):
                    """
                    Delay summary
                    
                    .. attribute:: interface_delay_summary
                    
                    	Interface delay summary
                    	**type**\:  :py:class:`InterfaceDelaySummary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary>`
                    
                    .. attribute:: delay_global_counters
                    
                    	PM delay global counters
                    	**type**\:  :py:class:`DelayGlobalCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.DelayGlobalCounters>`
                    
                    

                    """

                    _prefix = 'perf-meas-oper'
                    _revision = '2017-10-17'

                    def __init__(self):
                        super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary, self).__init__()

                        self.yang_name = "delay-summary"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-delay-summary", ("interface_delay_summary", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary)), ("delay-global-counters", ("delay_global_counters", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.DelayGlobalCounters))])
                        self._leafs = OrderedDict()

                        self.interface_delay_summary = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary()
                        self.interface_delay_summary.parent = self
                        self._children_name_map["interface_delay_summary"] = "interface-delay-summary"

                        self.delay_global_counters = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.DelayGlobalCounters()
                        self.delay_global_counters.parent = self
                        self._children_name_map["delay_global_counters"] = "delay-global-counters"
                        self._segment_path = lambda: "delay-summary"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary, [], name, value)


                    class InterfaceDelaySummary(Entity):
                        """
                        Interface delay summary
                        
                        .. attribute:: delay_profile
                        
                        	Delay profile
                        	**type**\:  :py:class:`DelayProfile <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayProfile>`
                        
                        .. attribute:: delay_transport_counters
                        
                        	PM delay counters for a transport types
                        	**type**\:  :py:class:`DelayTransportCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters>`
                        
                        .. attribute:: total_delay_sessions
                        
                        	Number of delay measurement sessions enabled
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary, self).__init__()

                            self.yang_name = "interface-delay-summary"
                            self.yang_parent_name = "delay-summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("delay-profile", ("delay_profile", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayProfile)), ("delay-transport-counters", ("delay_transport_counters", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters))])
                            self._leafs = OrderedDict([
                                ('total_delay_sessions', (YLeaf(YType.uint32, 'total-delay-sessions'), ['int'])),
                            ])
                            self.total_delay_sessions = None

                            self.delay_profile = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayProfile()
                            self.delay_profile.parent = self
                            self._children_name_map["delay_profile"] = "delay-profile"

                            self.delay_transport_counters = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters()
                            self.delay_transport_counters.parent = self
                            self._children_name_map["delay_transport_counters"] = "delay-transport-counters"
                            self._segment_path = lambda: "interface-delay-summary"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary, ['total_delay_sessions'], name, value)


                        class DelayProfile(Entity):
                            """
                            Delay profile
                            
                            .. attribute:: probe_interval
                            
                            	Probe Interval (sec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: burst_interval
                            
                            	Burst Interval (msec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: burst_count
                            
                            	Burst Count
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: delay_measurement_mode
                            
                            	Delay Measurement Mode Type
                            	**type**\:  :py:class:`PmDelayMode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmDelayMode>`
                            
                            .. attribute:: periodic_advertisement_enabled
                            
                            	Advertisement Periodic Enabled
                            	**type**\: bool
                            
                            .. attribute:: periodic_advertisement_interval
                            
                            	Advertisement Periodic Interval (sec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: effective_periodic_advertisement_interval
                            
                            	Advertisement Periodic Effective (sec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: periodic_advertisement_threshold
                            
                            	Advertisement Periodic Threshold (%)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: periodic_advertisement_minimum_change
                            
                            	Advertisement Periodic Minimum Change (uSec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accelerated_advertisement_threshold
                            
                            	Advertisement Accelerated Threshold (%)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accelerated_advertisement_minimum_change
                            
                            	Advertisement Accelerated Minimum Change (uSec)
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: accelerated_advertisement_enabled
                            
                            	Advertisement Accelerated Enabled
                            	**type**\: bool
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayProfile, self).__init__()

                                self.yang_name = "delay-profile"
                                self.yang_parent_name = "interface-delay-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([])
                                self._leafs = OrderedDict([
                                    ('probe_interval', (YLeaf(YType.uint32, 'probe-interval'), ['int'])),
                                    ('burst_interval', (YLeaf(YType.uint32, 'burst-interval'), ['int'])),
                                    ('burst_count', (YLeaf(YType.uint32, 'burst-count'), ['int'])),
                                    ('delay_measurement_mode', (YLeaf(YType.enumeration, 'delay-measurement-mode'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmDelayMode', '')])),
                                    ('periodic_advertisement_enabled', (YLeaf(YType.boolean, 'periodic-advertisement-enabled'), ['bool'])),
                                    ('periodic_advertisement_interval', (YLeaf(YType.uint32, 'periodic-advertisement-interval'), ['int'])),
                                    ('effective_periodic_advertisement_interval', (YLeaf(YType.uint32, 'effective-periodic-advertisement-interval'), ['int'])),
                                    ('periodic_advertisement_threshold', (YLeaf(YType.uint32, 'periodic-advertisement-threshold'), ['int'])),
                                    ('periodic_advertisement_minimum_change', (YLeaf(YType.uint32, 'periodic-advertisement-minimum-change'), ['int'])),
                                    ('accelerated_advertisement_threshold', (YLeaf(YType.uint32, 'accelerated-advertisement-threshold'), ['int'])),
                                    ('accelerated_advertisement_minimum_change', (YLeaf(YType.uint32, 'accelerated-advertisement-minimum-change'), ['int'])),
                                    ('accelerated_advertisement_enabled', (YLeaf(YType.boolean, 'accelerated-advertisement-enabled'), ['bool'])),
                                ])
                                self.probe_interval = None
                                self.burst_interval = None
                                self.burst_count = None
                                self.delay_measurement_mode = None
                                self.periodic_advertisement_enabled = None
                                self.periodic_advertisement_interval = None
                                self.effective_periodic_advertisement_interval = None
                                self.periodic_advertisement_threshold = None
                                self.periodic_advertisement_minimum_change = None
                                self.accelerated_advertisement_threshold = None
                                self.accelerated_advertisement_minimum_change = None
                                self.accelerated_advertisement_enabled = None
                                self._segment_path = lambda: "delay-profile"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayProfile, ['probe_interval', 'burst_interval', 'burst_count', 'delay_measurement_mode', 'periodic_advertisement_enabled', 'periodic_advertisement_interval', 'effective_periodic_advertisement_interval', 'periodic_advertisement_threshold', 'periodic_advertisement_minimum_change', 'accelerated_advertisement_threshold', 'accelerated_advertisement_minimum_change', 'accelerated_advertisement_enabled'], name, value)


                        class DelayTransportCounters(Entity):
                            """
                            PM delay counters for a transport types
                            
                            .. attribute:: generic_counters
                            
                            	Generic counters for a PM interface instance
                            	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.GenericCounters>`
                            
                            .. attribute:: exclusive_counters
                            
                            	Exclusive counters for a PM interface instance
                            	**type**\:  :py:class:`ExclusiveCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters, self).__init__()

                                self.yang_name = "delay-transport-counters"
                                self.yang_parent_name = "interface-delay-summary"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("generic-counters", ("generic_counters", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.GenericCounters)), ("exclusive-counters", ("exclusive_counters", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters))])
                                self._leafs = OrderedDict()

                                self.generic_counters = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.GenericCounters()
                                self.generic_counters.parent = self
                                self._children_name_map["generic_counters"] = "generic-counters"

                                self.exclusive_counters = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters()
                                self.exclusive_counters.parent = self
                                self._children_name_map["exclusive_counters"] = "exclusive-counters"
                                self._segment_path = lambda: "delay-transport-counters"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters, [], name, value)


                            class GenericCounters(Entity):
                                """
                                Generic counters for a PM interface instance
                                
                                .. attribute:: query_packets_sent
                                
                                	Query packets sent
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: query_packet_sent_errors
                                
                                	Query packets sent error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: query_packet_sent_error_no_ip_address
                                
                                	Query packet sent error, no IP address
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: query_packets_received
                                
                                	Query packets received
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_negative_delay
                                
                                	Received packet error, negative delay
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_delay_exceeds_threshold
                                
                                	Received packet error, delay exceeds threshold
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_missing_tx_timestamp
                                
                                	Received packet error, missing Tx timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_missing_rx_timestamp
                                
                                	Received packet error, missing Rx timestamp
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_probe_full
                                
                                	Received packet error, probe full
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_error_probe_not_started
                                
                                	Received packet error, probe not started
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_control_code_error
                                
                                	Received packet with a control code error
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: received_packet_control_code_notification
                                
                                	Received packet with a control code notification
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: probes_started
                                
                                	Probes started
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: probes_complete
                                
                                	Probes completed
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: probes_incomplete
                                
                                	Probes incomplete
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: advertisement
                                
                                	Advertisements
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.GenericCounters, self).__init__()

                                    self.yang_name = "generic-counters"
                                    self.yang_parent_name = "delay-transport-counters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('query_packets_sent', (YLeaf(YType.uint64, 'query-packets-sent'), ['int'])),
                                        ('query_packet_sent_errors', (YLeaf(YType.uint64, 'query-packet-sent-errors'), ['int'])),
                                        ('query_packet_sent_error_no_ip_address', (YLeaf(YType.uint64, 'query-packet-sent-error-no-ip-address'), ['int'])),
                                        ('query_packets_received', (YLeaf(YType.uint64, 'query-packets-received'), ['int'])),
                                        ('received_packet_error_negative_delay', (YLeaf(YType.uint64, 'received-packet-error-negative-delay'), ['int'])),
                                        ('received_packet_error_delay_exceeds_threshold', (YLeaf(YType.uint64, 'received-packet-error-delay-exceeds-threshold'), ['int'])),
                                        ('received_packet_error_missing_tx_timestamp', (YLeaf(YType.uint64, 'received-packet-error-missing-tx-timestamp'), ['int'])),
                                        ('received_packet_error_missing_rx_timestamp', (YLeaf(YType.uint64, 'received-packet-error-missing-rx-timestamp'), ['int'])),
                                        ('received_packet_error_probe_full', (YLeaf(YType.uint64, 'received-packet-error-probe-full'), ['int'])),
                                        ('received_packet_error_probe_not_started', (YLeaf(YType.uint64, 'received-packet-error-probe-not-started'), ['int'])),
                                        ('received_packet_control_code_error', (YLeaf(YType.uint64, 'received-packet-control-code-error'), ['int'])),
                                        ('received_packet_control_code_notification', (YLeaf(YType.uint64, 'received-packet-control-code-notification'), ['int'])),
                                        ('probes_started', (YLeaf(YType.uint64, 'probes-started'), ['int'])),
                                        ('probes_complete', (YLeaf(YType.uint64, 'probes-complete'), ['int'])),
                                        ('probes_incomplete', (YLeaf(YType.uint64, 'probes-incomplete'), ['int'])),
                                        ('advertisement', (YLeaf(YType.uint64, 'advertisement'), ['int'])),
                                    ])
                                    self.query_packets_sent = None
                                    self.query_packet_sent_errors = None
                                    self.query_packet_sent_error_no_ip_address = None
                                    self.query_packets_received = None
                                    self.received_packet_error_negative_delay = None
                                    self.received_packet_error_delay_exceeds_threshold = None
                                    self.received_packet_error_missing_tx_timestamp = None
                                    self.received_packet_error_missing_rx_timestamp = None
                                    self.received_packet_error_probe_full = None
                                    self.received_packet_error_probe_not_started = None
                                    self.received_packet_control_code_error = None
                                    self.received_packet_control_code_notification = None
                                    self.probes_started = None
                                    self.probes_complete = None
                                    self.probes_incomplete = None
                                    self.advertisement = None
                                    self._segment_path = lambda: "generic-counters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.GenericCounters, ['query_packets_sent', 'query_packet_sent_errors', 'query_packet_sent_error_no_ip_address', 'query_packets_received', 'received_packet_error_negative_delay', 'received_packet_error_delay_exceeds_threshold', 'received_packet_error_missing_tx_timestamp', 'received_packet_error_missing_rx_timestamp', 'received_packet_error_probe_full', 'received_packet_error_probe_not_started', 'received_packet_control_code_error', 'received_packet_control_code_notification', 'probes_started', 'probes_complete', 'probes_incomplete', 'advertisement'], name, value)


                            class ExclusiveCounters(Entity):
                                """
                                Exclusive counters for a PM interface instance
                                
                                .. attribute:: interface_exclusive_counters
                                
                                	Counters Exclusive for interface
                                	**type**\:  :py:class:`InterfaceExclusiveCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters.InterfaceExclusiveCounters>`
                                
                                .. attribute:: type
                                
                                	type
                                	**type**\:  :py:class:`PmTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmTransport>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters, self).__init__()

                                    self.yang_name = "exclusive-counters"
                                    self.yang_parent_name = "delay-transport-counters"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("interface-exclusive-counters", ("interface_exclusive_counters", PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters.InterfaceExclusiveCounters))])
                                    self._leafs = OrderedDict([
                                        ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmTransport', '')])),
                                    ])
                                    self.type = None

                                    self.interface_exclusive_counters = PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters.InterfaceExclusiveCounters()
                                    self.interface_exclusive_counters.parent = self
                                    self._children_name_map["interface_exclusive_counters"] = "interface-exclusive-counters"
                                    self._segment_path = lambda: "exclusive-counters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters, ['type'], name, value)


                                class InterfaceExclusiveCounters(Entity):
                                    """
                                    Counters Exclusive for interface
                                    
                                    .. attribute:: query_packet_sent_error_interface_down
                                    
                                    	Query packet sent error, interface down
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: query_packet_sent_error_no_mpls_caps
                                    
                                    	Query packet sent error, no MPLS caps
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters.InterfaceExclusiveCounters, self).__init__()

                                        self.yang_name = "interface-exclusive-counters"
                                        self.yang_parent_name = "exclusive-counters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('query_packet_sent_error_interface_down', (YLeaf(YType.uint64, 'query-packet-sent-error-interface-down'), ['int'])),
                                            ('query_packet_sent_error_no_mpls_caps', (YLeaf(YType.uint64, 'query-packet-sent-error-no-mpls-caps'), ['int'])),
                                        ])
                                        self.query_packet_sent_error_interface_down = None
                                        self.query_packet_sent_error_no_mpls_caps = None
                                        self._segment_path = lambda: "interface-exclusive-counters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.InterfaceDelaySummary.DelayTransportCounters.ExclusiveCounters.InterfaceExclusiveCounters, ['query_packet_sent_error_interface_down', 'query_packet_sent_error_no_mpls_caps'], name, value)


                    class DelayGlobalCounters(Entity):
                        """
                        PM delay global counters
                        
                        .. attribute:: query_packets_sent
                        
                        	Query packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: query_packets_received
                        
                        	Query packets received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_invalid_session_id
                        
                        	Received packet error, invalid session ID
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_no_session
                        
                        	Received packet error, no session
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.DelayGlobalCounters, self).__init__()

                            self.yang_name = "delay-global-counters"
                            self.yang_parent_name = "delay-summary"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('query_packets_sent', (YLeaf(YType.uint64, 'query-packets-sent'), ['int'])),
                                ('query_packets_received', (YLeaf(YType.uint64, 'query-packets-received'), ['int'])),
                                ('received_packet_error_invalid_session_id', (YLeaf(YType.uint64, 'received-packet-error-invalid-session-id'), ['int'])),
                                ('received_packet_error_no_session', (YLeaf(YType.uint64, 'received-packet-error-no-session'), ['int'])),
                            ])
                            self.query_packets_sent = None
                            self.query_packets_received = None
                            self.received_packet_error_invalid_session_id = None
                            self.received_packet_error_no_session = None
                            self._segment_path = lambda: "delay-global-counters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Summary.DelaySummary.DelayGlobalCounters, ['query_packets_sent', 'query_packets_received', 'received_packet_error_invalid_session_id', 'received_packet_error_no_session'], name, value)


            class Interfaces(Entity):
                """
                Interfaces
                
                .. attribute:: interface_details
                
                	Interface detailed table
                	**type**\:  :py:class:`InterfaceDetails <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails>`
                
                .. attribute:: interface_delay
                
                	Delay\-measurement intformation
                	**type**\:  :py:class:`InterfaceDelay <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay>`
                
                

                """

                _prefix = 'perf-meas-oper'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurement.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface-details", ("interface_details", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails)), ("interface-delay", ("interface_delay", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay))])
                    self._leafs = OrderedDict()

                    self.interface_details = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails()
                    self.interface_details.parent = self
                    self._children_name_map["interface_details"] = "interface-details"

                    self.interface_delay = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay()
                    self.interface_delay.parent = self
                    self._children_name_map["interface_delay"] = "interface-delay"
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces, [], name, value)


                class InterfaceDetails(Entity):
                    """
                    Interface detailed table
                    
                    .. attribute:: interface_detail
                    
                    	Detailed interface information
                    	**type**\: list of  		 :py:class:`InterfaceDetail <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail>`
                    
                    

                    """

                    _prefix = 'perf-meas-oper'
                    _revision = '2017-10-17'

                    def __init__(self):
                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails, self).__init__()

                        self.yang_name = "interface-details"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-detail", ("interface_detail", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail))])
                        self._leafs = OrderedDict()

                        self.interface_detail = YList(self)
                        self._segment_path = lambda: "interface-details"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails, [], name, value)


                    class InterfaceDetail(Entity):
                        """
                        Detailed interface information
                        
                        .. attribute:: interface_name  (key)
                        
                        	Interface name
                        	**type**\: str
                        
                        	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                        
                        .. attribute:: interface_name_xr
                        
                        	Interface name
                        	**type**\: str
                        
                        .. attribute:: interface_handle
                        
                        	Interface handle
                        	**type**\: int
                        
                        	**range:** 0..4294967295
                        
                        .. attribute:: interface_state
                        
                        	Interface state
                        	**type**\: bool
                        
                        .. attribute:: source_address
                        
                        	Source Address
                        	**type**\: str
                        
                        	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_v6_address
                        
                        	Source IPv6 Address
                        	**type**\: str
                        
                        	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                        
                        .. attribute:: source_mac_address
                        
                        	Source Mac address
                        	**type**\: str
                        
                        	**pattern:** [0\-9a\-fA\-F]{2}(\:[0\-9a\-fA\-F]{2}){5}
                        
                        .. attribute:: primary_vlan_tag
                        
                        	Primary VLAN Tag
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: secondary_vlan_tag
                        
                        	Secondary VLAN Tag
                        	**type**\: int
                        
                        	**range:** 0..65535
                        
                        .. attribute:: delay_measurement_session
                        
                        	Delay\-measurement sessions
                        	**type**\: list of  		 :py:class:`DelayMeasurementSession <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail, self).__init__()

                            self.yang_name = "interface-detail"
                            self.yang_parent_name = "interface-details"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = ['interface_name']
                            self._child_classes = OrderedDict([("delay-measurement-session", ("delay_measurement_session", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession))])
                            self._leafs = OrderedDict([
                                ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ('interface_state', (YLeaf(YType.boolean, 'interface-state'), ['bool'])),
                                ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                                ('source_v6_address', (YLeaf(YType.str, 'source-v6-address'), ['str'])),
                                ('source_mac_address', (YLeaf(YType.str, 'source-mac-address'), ['str'])),
                                ('primary_vlan_tag', (YLeaf(YType.uint16, 'primary-vlan-tag'), ['int'])),
                                ('secondary_vlan_tag', (YLeaf(YType.uint16, 'secondary-vlan-tag'), ['int'])),
                            ])
                            self.interface_name = None
                            self.interface_name_xr = None
                            self.interface_handle = None
                            self.interface_state = None
                            self.source_address = None
                            self.source_v6_address = None
                            self.source_mac_address = None
                            self.primary_vlan_tag = None
                            self.secondary_vlan_tag = None

                            self.delay_measurement_session = YList(self)
                            self._segment_path = lambda: "interface-detail" + "[interface-name='" + str(self.interface_name) + "']"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail, ['interface_name', 'interface_name_xr', 'interface_handle', 'interface_state', 'source_address', 'source_v6_address', 'source_mac_address', 'primary_vlan_tag', 'secondary_vlan_tag'], name, value)


                        class DelayMeasurementSession(Entity):
                            """
                            Delay\-measurement sessions
                            
                            .. attribute:: current_probe
                            
                            	Information for the current probe
                            	**type**\:  :py:class:`CurrentProbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe>`
                            
                            .. attribute:: session_counters
                            
                            	Session counters
                            	**type**\:  :py:class:`SessionCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters>`
                            
                            .. attribute:: last_advertisement_information
                            
                            	Last advertisement information
                            	**type**\:  :py:class:`LastAdvertisementInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation>`
                            
                            .. attribute:: next_advertisement_information
                            
                            	Next advertisement information
                            	**type**\:  :py:class:`NextAdvertisementInformation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation>`
                            
                            .. attribute:: last_notification_control_code
                            
                            	Last notifcation control code received
                            	**type**\:  :py:class:`LastNotificationControlCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastNotificationControlCode>`
                            
                            .. attribute:: last_error_control_code
                            
                            	Last error control code received
                            	**type**\:  :py:class:`LastErrorControlCode <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastErrorControlCode>`
                            
                            .. attribute:: session_id
                            
                            	Session ID
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: transport_type
                            
                            	Transport Type
                            	**type**\:  :py:class:`PmTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmTransport>`
                            
                            .. attribute:: measurement_type
                            
                            	Measurement Type
                            	**type**\:  :py:class:`PmMeasurement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmMeasurement>`
                            
                            .. attribute:: periodic_advertisement_interval_in_sec
                            
                            	Periodic advertisement interval in seconds
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            	**units**\: second
                            
                            .. attribute:: probe_history
                            
                            	Current probe history
                            	**type**\: list of  		 :py:class:`ProbeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.ProbeHistory>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession, self).__init__()

                                self.yang_name = "delay-measurement-session"
                                self.yang_parent_name = "interface-detail"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = []
                                self._child_classes = OrderedDict([("current-probe", ("current_probe", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe)), ("session-counters", ("session_counters", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters)), ("last-advertisement-information", ("last_advertisement_information", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation)), ("next-advertisement-information", ("next_advertisement_information", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation)), ("last-notification-control-code", ("last_notification_control_code", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastNotificationControlCode)), ("last-error-control-code", ("last_error_control_code", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastErrorControlCode)), ("probe-history", ("probe_history", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.ProbeHistory))])
                                self._leafs = OrderedDict([
                                    ('session_id', (YLeaf(YType.uint32, 'session-id'), ['int'])),
                                    ('transport_type', (YLeaf(YType.enumeration, 'transport-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmTransport', '')])),
                                    ('measurement_type', (YLeaf(YType.enumeration, 'measurement-type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmMeasurement', '')])),
                                    ('periodic_advertisement_interval_in_sec', (YLeaf(YType.uint32, 'periodic-advertisement-interval-in-sec'), ['int'])),
                                ])
                                self.session_id = None
                                self.transport_type = None
                                self.measurement_type = None
                                self.periodic_advertisement_interval_in_sec = None

                                self.current_probe = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe()
                                self.current_probe.parent = self
                                self._children_name_map["current_probe"] = "current-probe"

                                self.session_counters = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters()
                                self.session_counters.parent = self
                                self._children_name_map["session_counters"] = "session-counters"

                                self.last_advertisement_information = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation()
                                self.last_advertisement_information.parent = self
                                self._children_name_map["last_advertisement_information"] = "last-advertisement-information"

                                self.next_advertisement_information = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation()
                                self.next_advertisement_information.parent = self
                                self._children_name_map["next_advertisement_information"] = "next-advertisement-information"

                                self.last_notification_control_code = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastNotificationControlCode()
                                self.last_notification_control_code.parent = self
                                self._children_name_map["last_notification_control_code"] = "last-notification-control-code"

                                self.last_error_control_code = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastErrorControlCode()
                                self.last_error_control_code.parent = self
                                self._children_name_map["last_error_control_code"] = "last-error-control-code"

                                self.probe_history = YList(self)
                                self._segment_path = lambda: "delay-measurement-session"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession, ['session_id', 'transport_type', 'measurement_type', 'periodic_advertisement_interval_in_sec'], name, value)


                            class CurrentProbe(Entity):
                                """
                                Information for the current probe
                                
                                .. attribute:: probe_results
                                
                                	Summarized  results of the current probe
                                	**type**\:  :py:class:`ProbeResults <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe.ProbeResults>`
                                
                                .. attribute:: probe_start_time_stamp
                                
                                	Timestamp in milliseconds of the current probe start (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: next_probe_start_time_remaining_in_millisec
                                
                                	Time in milliseconds until the next probe starts
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: millisecond
                                
                                .. attribute:: next_packet_sent_time_remaining_in_millisec
                                
                                	Time in milliseconds until the next packet is sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                	**units**\: millisecond
                                
                                .. attribute:: number_of_packets_sent
                                
                                	Number of packets sent in the current probe
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: number_of_packets_received
                                
                                	Number of packets received in the current probe
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: probe_not_running_reason
                                
                                	Reason why probe is not running
                                	**type**\:  :py:class:`PmProbeNotRunningReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmProbeNotRunningReason>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe, self).__init__()

                                    self.yang_name = "current-probe"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("probe-results", ("probe_results", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe.ProbeResults))])
                                    self._leafs = OrderedDict([
                                        ('probe_start_time_stamp', (YLeaf(YType.uint64, 'probe-start-time-stamp'), ['int'])),
                                        ('next_probe_start_time_remaining_in_millisec', (YLeaf(YType.uint32, 'next-probe-start-time-remaining-in-millisec'), ['int'])),
                                        ('next_packet_sent_time_remaining_in_millisec', (YLeaf(YType.uint32, 'next-packet-sent-time-remaining-in-millisec'), ['int'])),
                                        ('number_of_packets_sent', (YLeaf(YType.uint32, 'number-of-packets-sent'), ['int'])),
                                        ('number_of_packets_received', (YLeaf(YType.uint32, 'number-of-packets-received'), ['int'])),
                                        ('probe_not_running_reason', (YLeaf(YType.enumeration, 'probe-not-running-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmProbeNotRunningReason', '')])),
                                    ])
                                    self.probe_start_time_stamp = None
                                    self.next_probe_start_time_remaining_in_millisec = None
                                    self.next_packet_sent_time_remaining_in_millisec = None
                                    self.number_of_packets_sent = None
                                    self.number_of_packets_received = None
                                    self.probe_not_running_reason = None

                                    self.probe_results = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe.ProbeResults()
                                    self.probe_results.parent = self
                                    self._children_name_map["probe_results"] = "probe-results"
                                    self._segment_path = lambda: "current-probe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe, ['probe_start_time_stamp', 'next_probe_start_time_remaining_in_millisec', 'next_packet_sent_time_remaining_in_millisec', 'number_of_packets_sent', 'number_of_packets_received', 'probe_not_running_reason'], name, value)


                                class ProbeResults(Entity):
                                    """
                                    Summarized  results of the current probe
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe.ProbeResults, self).__init__()

                                        self.yang_name = "probe-results"
                                        self.yang_parent_name = "current-probe"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "probe-results"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.CurrentProbe.ProbeResults, ['average', 'minimum', 'maximum', 'variance'], name, value)


                            class SessionCounters(Entity):
                                """
                                Session counters
                                
                                .. attribute:: generic_counters
                                
                                	Generic counters for a PM interface instance
                                	**type**\:  :py:class:`GenericCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.GenericCounters>`
                                
                                .. attribute:: exclusive_counters
                                
                                	Exclusive counters for a PM interface instance
                                	**type**\:  :py:class:`ExclusiveCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters, self).__init__()

                                    self.yang_name = "session-counters"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("generic-counters", ("generic_counters", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.GenericCounters)), ("exclusive-counters", ("exclusive_counters", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters))])
                                    self._leafs = OrderedDict()

                                    self.generic_counters = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.GenericCounters()
                                    self.generic_counters.parent = self
                                    self._children_name_map["generic_counters"] = "generic-counters"

                                    self.exclusive_counters = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters()
                                    self.exclusive_counters.parent = self
                                    self._children_name_map["exclusive_counters"] = "exclusive-counters"
                                    self._segment_path = lambda: "session-counters"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters, [], name, value)


                                class GenericCounters(Entity):
                                    """
                                    Generic counters for a PM interface instance
                                    
                                    .. attribute:: query_packets_sent
                                    
                                    	Query packets sent
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: query_packet_sent_errors
                                    
                                    	Query packets sent error
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: query_packet_sent_error_no_ip_address
                                    
                                    	Query packet sent error, no IP address
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: query_packets_received
                                    
                                    	Query packets received
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_negative_delay
                                    
                                    	Received packet error, negative delay
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_delay_exceeds_threshold
                                    
                                    	Received packet error, delay exceeds threshold
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_missing_tx_timestamp
                                    
                                    	Received packet error, missing Tx timestamp
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_missing_rx_timestamp
                                    
                                    	Received packet error, missing Rx timestamp
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_probe_full
                                    
                                    	Received packet error, probe full
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_error_probe_not_started
                                    
                                    	Received packet error, probe not started
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_control_code_error
                                    
                                    	Received packet with a control code error
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: received_packet_control_code_notification
                                    
                                    	Received packet with a control code notification
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: probes_started
                                    
                                    	Probes started
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: probes_complete
                                    
                                    	Probes completed
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: probes_incomplete
                                    
                                    	Probes incomplete
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    .. attribute:: advertisement
                                    
                                    	Advertisements
                                    	**type**\: int
                                    
                                    	**range:** 0..18446744073709551615
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.GenericCounters, self).__init__()

                                        self.yang_name = "generic-counters"
                                        self.yang_parent_name = "session-counters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('query_packets_sent', (YLeaf(YType.uint64, 'query-packets-sent'), ['int'])),
                                            ('query_packet_sent_errors', (YLeaf(YType.uint64, 'query-packet-sent-errors'), ['int'])),
                                            ('query_packet_sent_error_no_ip_address', (YLeaf(YType.uint64, 'query-packet-sent-error-no-ip-address'), ['int'])),
                                            ('query_packets_received', (YLeaf(YType.uint64, 'query-packets-received'), ['int'])),
                                            ('received_packet_error_negative_delay', (YLeaf(YType.uint64, 'received-packet-error-negative-delay'), ['int'])),
                                            ('received_packet_error_delay_exceeds_threshold', (YLeaf(YType.uint64, 'received-packet-error-delay-exceeds-threshold'), ['int'])),
                                            ('received_packet_error_missing_tx_timestamp', (YLeaf(YType.uint64, 'received-packet-error-missing-tx-timestamp'), ['int'])),
                                            ('received_packet_error_missing_rx_timestamp', (YLeaf(YType.uint64, 'received-packet-error-missing-rx-timestamp'), ['int'])),
                                            ('received_packet_error_probe_full', (YLeaf(YType.uint64, 'received-packet-error-probe-full'), ['int'])),
                                            ('received_packet_error_probe_not_started', (YLeaf(YType.uint64, 'received-packet-error-probe-not-started'), ['int'])),
                                            ('received_packet_control_code_error', (YLeaf(YType.uint64, 'received-packet-control-code-error'), ['int'])),
                                            ('received_packet_control_code_notification', (YLeaf(YType.uint64, 'received-packet-control-code-notification'), ['int'])),
                                            ('probes_started', (YLeaf(YType.uint64, 'probes-started'), ['int'])),
                                            ('probes_complete', (YLeaf(YType.uint64, 'probes-complete'), ['int'])),
                                            ('probes_incomplete', (YLeaf(YType.uint64, 'probes-incomplete'), ['int'])),
                                            ('advertisement', (YLeaf(YType.uint64, 'advertisement'), ['int'])),
                                        ])
                                        self.query_packets_sent = None
                                        self.query_packet_sent_errors = None
                                        self.query_packet_sent_error_no_ip_address = None
                                        self.query_packets_received = None
                                        self.received_packet_error_negative_delay = None
                                        self.received_packet_error_delay_exceeds_threshold = None
                                        self.received_packet_error_missing_tx_timestamp = None
                                        self.received_packet_error_missing_rx_timestamp = None
                                        self.received_packet_error_probe_full = None
                                        self.received_packet_error_probe_not_started = None
                                        self.received_packet_control_code_error = None
                                        self.received_packet_control_code_notification = None
                                        self.probes_started = None
                                        self.probes_complete = None
                                        self.probes_incomplete = None
                                        self.advertisement = None
                                        self._segment_path = lambda: "generic-counters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.GenericCounters, ['query_packets_sent', 'query_packet_sent_errors', 'query_packet_sent_error_no_ip_address', 'query_packets_received', 'received_packet_error_negative_delay', 'received_packet_error_delay_exceeds_threshold', 'received_packet_error_missing_tx_timestamp', 'received_packet_error_missing_rx_timestamp', 'received_packet_error_probe_full', 'received_packet_error_probe_not_started', 'received_packet_control_code_error', 'received_packet_control_code_notification', 'probes_started', 'probes_complete', 'probes_incomplete', 'advertisement'], name, value)


                                class ExclusiveCounters(Entity):
                                    """
                                    Exclusive counters for a PM interface instance
                                    
                                    .. attribute:: interface_exclusive_counters
                                    
                                    	Counters Exclusive for interface
                                    	**type**\:  :py:class:`InterfaceExclusiveCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters.InterfaceExclusiveCounters>`
                                    
                                    .. attribute:: type
                                    
                                    	type
                                    	**type**\:  :py:class:`PmTransport <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmTransport>`
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters, self).__init__()

                                        self.yang_name = "exclusive-counters"
                                        self.yang_parent_name = "session-counters"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([("interface-exclusive-counters", ("interface_exclusive_counters", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters.InterfaceExclusiveCounters))])
                                        self._leafs = OrderedDict([
                                            ('type', (YLeaf(YType.enumeration, 'type'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmTransport', '')])),
                                        ])
                                        self.type = None

                                        self.interface_exclusive_counters = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters.InterfaceExclusiveCounters()
                                        self.interface_exclusive_counters.parent = self
                                        self._children_name_map["interface_exclusive_counters"] = "interface-exclusive-counters"
                                        self._segment_path = lambda: "exclusive-counters"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters, ['type'], name, value)


                                    class InterfaceExclusiveCounters(Entity):
                                        """
                                        Counters Exclusive for interface
                                        
                                        .. attribute:: query_packet_sent_error_interface_down
                                        
                                        	Query packet sent error, interface down
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        .. attribute:: query_packet_sent_error_no_mpls_caps
                                        
                                        	Query packet sent error, no MPLS caps
                                        	**type**\: int
                                        
                                        	**range:** 0..18446744073709551615
                                        
                                        

                                        """

                                        _prefix = 'perf-meas-oper'
                                        _revision = '2017-10-17'

                                        def __init__(self):
                                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters.InterfaceExclusiveCounters, self).__init__()

                                            self.yang_name = "interface-exclusive-counters"
                                            self.yang_parent_name = "exclusive-counters"
                                            self.is_top_level_class = False
                                            self.has_list_ancestor = True
                                            self.ylist_key_names = []
                                            self._child_classes = OrderedDict([])
                                            self._leafs = OrderedDict([
                                                ('query_packet_sent_error_interface_down', (YLeaf(YType.uint64, 'query-packet-sent-error-interface-down'), ['int'])),
                                                ('query_packet_sent_error_no_mpls_caps', (YLeaf(YType.uint64, 'query-packet-sent-error-no-mpls-caps'), ['int'])),
                                            ])
                                            self.query_packet_sent_error_interface_down = None
                                            self.query_packet_sent_error_no_mpls_caps = None
                                            self._segment_path = lambda: "interface-exclusive-counters"
                                            self._is_frozen = True

                                        def __setattr__(self, name, value):
                                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.SessionCounters.ExclusiveCounters.InterfaceExclusiveCounters, ['query_packet_sent_error_interface_down', 'query_packet_sent_error_no_mpls_caps'], name, value)


                            class LastAdvertisementInformation(Entity):
                                """
                                Last advertisement information
                                
                                .. attribute:: advertised_values
                                
                                	Advertised values
                                	**type**\:  :py:class:`AdvertisedValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation.AdvertisedValues>`
                                
                                .. attribute:: time_of_advertisement
                                
                                	Time of the advertisement (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_reason
                                
                                	Reason for advertisement
                                	**type**\:  :py:class:`PmAdvertReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmAdvertReason>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation, self).__init__()

                                    self.yang_name = "last-advertisement-information"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("advertised-values", ("advertised_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation.AdvertisedValues))])
                                    self._leafs = OrderedDict([
                                        ('time_of_advertisement', (YLeaf(YType.uint64, 'time-of-advertisement'), ['int'])),
                                        ('advertisement_reason', (YLeaf(YType.enumeration, 'advertisement-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmAdvertReason', '')])),
                                    ])
                                    self.time_of_advertisement = None
                                    self.advertisement_reason = None

                                    self.advertised_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation.AdvertisedValues()
                                    self.advertised_values.parent = self
                                    self._children_name_map["advertised_values"] = "advertised-values"
                                    self._segment_path = lambda: "last-advertisement-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation, ['time_of_advertisement', 'advertisement_reason'], name, value)


                                class AdvertisedValues(Entity):
                                    """
                                    Advertised values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation.AdvertisedValues, self).__init__()

                                        self.yang_name = "advertised-values"
                                        self.yang_parent_name = "last-advertisement-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "advertised-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastAdvertisementInformation.AdvertisedValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                            class NextAdvertisementInformation(Entity):
                                """
                                Next advertisement information
                                
                                .. attribute:: advertisement_interval_values
                                
                                	Advertisement interval values
                                	**type**\:  :py:class:`AdvertisementIntervalValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation.AdvertisementIntervalValues>`
                                
                                .. attribute:: advertisement_interval_probes_remaining
                                
                                	Probes remaining until next periodic advertisement check
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: rolling_average
                                
                                	Rolling average value (uSec)
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation, self).__init__()

                                    self.yang_name = "next-advertisement-information"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("advertisement-interval-values", ("advertisement_interval_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation.AdvertisementIntervalValues))])
                                    self._leafs = OrderedDict([
                                        ('advertisement_interval_probes_remaining', (YLeaf(YType.uint32, 'advertisement-interval-probes-remaining'), ['int'])),
                                        ('rolling_average', (YLeaf(YType.uint32, 'rolling-average'), ['int'])),
                                    ])
                                    self.advertisement_interval_probes_remaining = None
                                    self.rolling_average = None

                                    self.advertisement_interval_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation.AdvertisementIntervalValues()
                                    self.advertisement_interval_values.parent = self
                                    self._children_name_map["advertisement_interval_values"] = "advertisement-interval-values"
                                    self._segment_path = lambda: "next-advertisement-information"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation, ['advertisement_interval_probes_remaining', 'rolling_average'], name, value)


                                class AdvertisementIntervalValues(Entity):
                                    """
                                    Advertisement interval values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation.AdvertisementIntervalValues, self).__init__()

                                        self.yang_name = "advertisement-interval-values"
                                        self.yang_parent_name = "next-advertisement-information"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "advertisement-interval-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.NextAdvertisementInformation.AdvertisementIntervalValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                            class LastNotificationControlCode(Entity):
                                """
                                Last notifcation control code received
                                
                                .. attribute:: control_code
                                
                                	MPLS PM RFC 6374 control code
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: timestamp
                                
                                	Received timestamp of the control code (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastNotificationControlCode, self).__init__()

                                    self.yang_name = "last-notification-control-code"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('control_code', (YLeaf(YType.uint8, 'control-code'), ['int'])),
                                        ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                                    ])
                                    self.control_code = None
                                    self.timestamp = None
                                    self._segment_path = lambda: "last-notification-control-code"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastNotificationControlCode, ['control_code', 'timestamp'], name, value)


                            class LastErrorControlCode(Entity):
                                """
                                Last error control code received
                                
                                .. attribute:: control_code
                                
                                	MPLS PM RFC 6374 control code
                                	**type**\: int
                                
                                	**range:** 0..255
                                
                                .. attribute:: timestamp
                                
                                	Received timestamp of the control code (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastErrorControlCode, self).__init__()

                                    self.yang_name = "last-error-control-code"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('control_code', (YLeaf(YType.uint8, 'control-code'), ['int'])),
                                        ('timestamp', (YLeaf(YType.uint64, 'timestamp'), ['int'])),
                                    ])
                                    self.control_code = None
                                    self.timestamp = None
                                    self._segment_path = lambda: "last-error-control-code"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.LastErrorControlCode, ['control_code', 'timestamp'], name, value)


                            class ProbeHistory(Entity):
                                """
                                Current probe history
                                
                                .. attribute:: measurement_value
                                
                                	Measurement value (nsec)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                .. attribute:: query_timestamp
                                
                                	Timestamp when the measurement was taken (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.ProbeHistory, self).__init__()

                                    self.yang_name = "probe-history"
                                    self.yang_parent_name = "delay-measurement-session"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([])
                                    self._leafs = OrderedDict([
                                        ('measurement_value', (YLeaf(YType.uint64, 'measurement-value'), ['int'])),
                                        ('query_timestamp', (YLeaf(YType.uint64, 'query-timestamp'), ['int'])),
                                    ])
                                    self.measurement_value = None
                                    self.query_timestamp = None
                                    self._segment_path = lambda: "probe-history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDetails.InterfaceDetail.DelayMeasurementSession.ProbeHistory, ['measurement_value', 'query_timestamp'], name, value)


                class InterfaceDelay(Entity):
                    """
                    Delay\-measurement intformation
                    
                    .. attribute:: interface_last_aggregations
                    
                    	Table of last probe aggregation
                    	**type**\:  :py:class:`InterfaceLastAggregations <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations>`
                    
                    .. attribute:: interface_probe_histories
                    
                    	Table of probe histories
                    	**type**\:  :py:class:`InterfaceProbeHistories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories>`
                    
                    .. attribute:: interface_aggregated_histories
                    
                    	Table of aggregated probe histories
                    	**type**\:  :py:class:`InterfaceAggregatedHistories <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories>`
                    
                    .. attribute:: interface_last_probes
                    
                    	Table of last probes
                    	**type**\:  :py:class:`InterfaceLastProbes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes>`
                    
                    .. attribute:: interface_last_advertisements
                    
                    	Table of last advertisements
                    	**type**\:  :py:class:`InterfaceLastAdvertisements <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements>`
                    
                    

                    """

                    _prefix = 'perf-meas-oper'
                    _revision = '2017-10-17'

                    def __init__(self):
                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay, self).__init__()

                        self.yang_name = "interface-delay"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([("interface-last-aggregations", ("interface_last_aggregations", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations)), ("interface-probe-histories", ("interface_probe_histories", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories)), ("interface-aggregated-histories", ("interface_aggregated_histories", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories)), ("interface-last-probes", ("interface_last_probes", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes)), ("interface-last-advertisements", ("interface_last_advertisements", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements))])
                        self._leafs = OrderedDict()

                        self.interface_last_aggregations = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations()
                        self.interface_last_aggregations.parent = self
                        self._children_name_map["interface_last_aggregations"] = "interface-last-aggregations"

                        self.interface_probe_histories = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories()
                        self.interface_probe_histories.parent = self
                        self._children_name_map["interface_probe_histories"] = "interface-probe-histories"

                        self.interface_aggregated_histories = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories()
                        self.interface_aggregated_histories.parent = self
                        self._children_name_map["interface_aggregated_histories"] = "interface-aggregated-histories"

                        self.interface_last_probes = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes()
                        self.interface_last_probes.parent = self
                        self._children_name_map["interface_last_probes"] = "interface-last-probes"

                        self.interface_last_advertisements = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements()
                        self.interface_last_advertisements.parent = self
                        self._children_name_map["interface_last_advertisements"] = "interface-last-advertisements"
                        self._segment_path = lambda: "interface-delay"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay, [], name, value)


                    class InterfaceLastAggregations(Entity):
                        """
                        Table of last probe aggregation
                        
                        .. attribute:: interface_last_aggregation
                        
                        	Last probe aggregation information
                        	**type**\: list of  		 :py:class:`InterfaceLastAggregation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations, self).__init__()

                            self.yang_name = "interface-last-aggregations"
                            self.yang_parent_name = "interface-delay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-last-aggregation", ("interface_last_aggregation", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation))])
                            self._leafs = OrderedDict()

                            self.interface_last_aggregation = YList(self)
                            self._segment_path = lambda: "interface-last-aggregations"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations, [], name, value)


                        class InterfaceLastAggregation(Entity):
                            """
                            Last probe aggregation information
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: last_aggregation
                            
                            	Last probe aggregation
                            	**type**\:  :py:class:`LastAggregation <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation, self).__init__()

                                self.yang_name = "interface-last-aggregation"
                                self.yang_parent_name = "interface-last-aggregations"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("last-aggregation", ("last_aggregation", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.last_aggregation = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation()
                                self.last_aggregation.parent = self
                                self._children_name_map["last_aggregation"] = "last-aggregation"
                                self._segment_path = lambda: "interface-last-aggregation" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation, ['interface_name'], name, value)


                            class LastAggregation(Entity):
                                """
                                Last probe aggregation
                                
                                .. attribute:: aggregated_probe_values
                                
                                	Aggregated probe values
                                	**type**\:  :py:class:`AggregatedProbeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation.AggregatedProbeValues>`
                                
                                .. attribute:: aggregation_timestamp
                                
                                	Time probe aggregation was done (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: aggregation_action
                                
                                	Action performed with the aggregated values
                                	**type**\:  :py:class:`PmAdvertReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmAdvertReason>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation, self).__init__()

                                    self.yang_name = "last-aggregation"
                                    self.yang_parent_name = "interface-last-aggregation"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated-probe-values", ("aggregated_probe_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation.AggregatedProbeValues))])
                                    self._leafs = OrderedDict([
                                        ('aggregation_timestamp', (YLeaf(YType.uint64, 'aggregation-timestamp'), ['int'])),
                                        ('aggregation_action', (YLeaf(YType.enumeration, 'aggregation-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmAdvertReason', '')])),
                                    ])
                                    self.aggregation_timestamp = None
                                    self.aggregation_action = None

                                    self.aggregated_probe_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation.AggregatedProbeValues()
                                    self.aggregated_probe_values.parent = self
                                    self._children_name_map["aggregated_probe_values"] = "aggregated-probe-values"
                                    self._segment_path = lambda: "last-aggregation"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation, ['aggregation_timestamp', 'aggregation_action'], name, value)


                                class AggregatedProbeValues(Entity):
                                    """
                                    Aggregated probe values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation.AggregatedProbeValues, self).__init__()

                                        self.yang_name = "aggregated-probe-values"
                                        self.yang_parent_name = "last-aggregation"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "aggregated-probe-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAggregations.InterfaceLastAggregation.LastAggregation.AggregatedProbeValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                    class InterfaceProbeHistories(Entity):
                        """
                        Table of probe histories
                        
                        .. attribute:: interface_probe_history
                        
                        	Probe history information
                        	**type**\: list of  		 :py:class:`InterfaceProbeHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories, self).__init__()

                            self.yang_name = "interface-probe-histories"
                            self.yang_parent_name = "interface-delay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-probe-history", ("interface_probe_history", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory))])
                            self._leafs = OrderedDict()

                            self.interface_probe_history = YList(self)
                            self._segment_path = lambda: "interface-probe-histories"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories, [], name, value)


                        class InterfaceProbeHistory(Entity):
                            """
                            Probe history information
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface_name_xr
                            
                            	Interface name
                            	**type**\: str
                            
                            .. attribute:: interface_handle
                            
                            	Interface handle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: history
                            
                            	History of previous probes
                            	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory, self).__init__()

                                self.yang_name = "interface-probe-history"
                                self.yang_parent_name = "interface-probe-histories"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("history", ("history", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ])
                                self.interface_name = None
                                self.interface_name_xr = None
                                self.interface_handle = None

                                self.history = YList(self)
                                self._segment_path = lambda: "interface-probe-history" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory, ['interface_name', 'interface_name_xr', 'interface_handle'], name, value)


                            class History(Entity):
                                """
                                History of previous probes
                                
                                .. attribute:: probe_values
                                
                                	Probe values
                                	**type**\:  :py:class:`ProbeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History.ProbeValues>`
                                
                                .. attribute:: probe_start_timestamp
                                
                                	Time last probe started (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: packets_sent
                                
                                	Packets sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: packets_received
                                
                                	Packets received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History, self).__init__()

                                    self.yang_name = "history"
                                    self.yang_parent_name = "interface-probe-history"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("probe-values", ("probe_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History.ProbeValues))])
                                    self._leafs = OrderedDict([
                                        ('probe_start_timestamp', (YLeaf(YType.uint64, 'probe-start-timestamp'), ['int'])),
                                        ('packets_sent', (YLeaf(YType.uint32, 'packets-sent'), ['int'])),
                                        ('packets_received', (YLeaf(YType.uint32, 'packets-received'), ['int'])),
                                    ])
                                    self.probe_start_timestamp = None
                                    self.packets_sent = None
                                    self.packets_received = None

                                    self.probe_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History.ProbeValues()
                                    self.probe_values.parent = self
                                    self._children_name_map["probe_values"] = "probe-values"
                                    self._segment_path = lambda: "history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History, ['probe_start_timestamp', 'packets_sent', 'packets_received'], name, value)


                                class ProbeValues(Entity):
                                    """
                                    Probe values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History.ProbeValues, self).__init__()

                                        self.yang_name = "probe-values"
                                        self.yang_parent_name = "history"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "probe-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceProbeHistories.InterfaceProbeHistory.History.ProbeValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                    class InterfaceAggregatedHistories(Entity):
                        """
                        Table of aggregated probe histories
                        
                        .. attribute:: interface_aggregated_history
                        
                        	Aggregated probe history information
                        	**type**\: list of  		 :py:class:`InterfaceAggregatedHistory <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories, self).__init__()

                            self.yang_name = "interface-aggregated-histories"
                            self.yang_parent_name = "interface-delay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-aggregated-history", ("interface_aggregated_history", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory))])
                            self._leafs = OrderedDict()

                            self.interface_aggregated_history = YList(self)
                            self._segment_path = lambda: "interface-aggregated-histories"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories, [], name, value)


                        class InterfaceAggregatedHistory(Entity):
                            """
                            Aggregated probe history information
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: interface_name_xr
                            
                            	Interface name
                            	**type**\: str
                            
                            .. attribute:: interface_handle
                            
                            	Interface handle
                            	**type**\: int
                            
                            	**range:** 0..4294967295
                            
                            .. attribute:: history
                            
                            	History of previous probe aggregations
                            	**type**\: list of  		 :py:class:`History <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory, self).__init__()

                                self.yang_name = "interface-aggregated-history"
                                self.yang_parent_name = "interface-aggregated-histories"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("history", ("history", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                    ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                                    ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                                ])
                                self.interface_name = None
                                self.interface_name_xr = None
                                self.interface_handle = None

                                self.history = YList(self)
                                self._segment_path = lambda: "interface-aggregated-history" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory, ['interface_name', 'interface_name_xr', 'interface_handle'], name, value)


                            class History(Entity):
                                """
                                History of previous probe aggregations
                                
                                .. attribute:: aggregated_probe_values
                                
                                	Aggregated probe values
                                	**type**\:  :py:class:`AggregatedProbeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History.AggregatedProbeValues>`
                                
                                .. attribute:: aggregation_timestamp
                                
                                	Time probe aggregation was done (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: aggregation_action
                                
                                	Action performed with the aggregated values
                                	**type**\:  :py:class:`PmAdvertReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmAdvertReason>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History, self).__init__()

                                    self.yang_name = "history"
                                    self.yang_parent_name = "interface-aggregated-history"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("aggregated-probe-values", ("aggregated_probe_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History.AggregatedProbeValues))])
                                    self._leafs = OrderedDict([
                                        ('aggregation_timestamp', (YLeaf(YType.uint64, 'aggregation-timestamp'), ['int'])),
                                        ('aggregation_action', (YLeaf(YType.enumeration, 'aggregation-action'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmAdvertReason', '')])),
                                    ])
                                    self.aggregation_timestamp = None
                                    self.aggregation_action = None

                                    self.aggregated_probe_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History.AggregatedProbeValues()
                                    self.aggregated_probe_values.parent = self
                                    self._children_name_map["aggregated_probe_values"] = "aggregated-probe-values"
                                    self._segment_path = lambda: "history"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History, ['aggregation_timestamp', 'aggregation_action'], name, value)


                                class AggregatedProbeValues(Entity):
                                    """
                                    Aggregated probe values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History.AggregatedProbeValues, self).__init__()

                                        self.yang_name = "aggregated-probe-values"
                                        self.yang_parent_name = "history"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "aggregated-probe-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceAggregatedHistories.InterfaceAggregatedHistory.History.AggregatedProbeValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                    class InterfaceLastProbes(Entity):
                        """
                        Table of last probes
                        
                        .. attribute:: interface_last_probe
                        
                        	Last measurement information
                        	**type**\: list of  		 :py:class:`InterfaceLastProbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes, self).__init__()

                            self.yang_name = "interface-last-probes"
                            self.yang_parent_name = "interface-delay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-last-probe", ("interface_last_probe", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe))])
                            self._leafs = OrderedDict()

                            self.interface_last_probe = YList(self)
                            self._segment_path = lambda: "interface-last-probes"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes, [], name, value)


                        class InterfaceLastProbe(Entity):
                            """
                            Last measurement information
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: last_probe
                            
                            	Last probe
                            	**type**\:  :py:class:`LastProbe <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe, self).__init__()

                                self.yang_name = "interface-last-probe"
                                self.yang_parent_name = "interface-last-probes"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("last-probe", ("last_probe", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.last_probe = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe()
                                self.last_probe.parent = self
                                self._children_name_map["last_probe"] = "last-probe"
                                self._segment_path = lambda: "interface-last-probe" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe, ['interface_name'], name, value)


                            class LastProbe(Entity):
                                """
                                Last probe
                                
                                .. attribute:: probe_values
                                
                                	Probe values
                                	**type**\:  :py:class:`ProbeValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe.ProbeValues>`
                                
                                .. attribute:: probe_start_timestamp
                                
                                	Time last probe started (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: packets_sent
                                
                                	Packets sent
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                .. attribute:: packets_received
                                
                                	Packets received
                                	**type**\: int
                                
                                	**range:** 0..4294967295
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe, self).__init__()

                                    self.yang_name = "last-probe"
                                    self.yang_parent_name = "interface-last-probe"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("probe-values", ("probe_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe.ProbeValues))])
                                    self._leafs = OrderedDict([
                                        ('probe_start_timestamp', (YLeaf(YType.uint64, 'probe-start-timestamp'), ['int'])),
                                        ('packets_sent', (YLeaf(YType.uint32, 'packets-sent'), ['int'])),
                                        ('packets_received', (YLeaf(YType.uint32, 'packets-received'), ['int'])),
                                    ])
                                    self.probe_start_timestamp = None
                                    self.packets_sent = None
                                    self.packets_received = None

                                    self.probe_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe.ProbeValues()
                                    self.probe_values.parent = self
                                    self._children_name_map["probe_values"] = "probe-values"
                                    self._segment_path = lambda: "last-probe"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe, ['probe_start_timestamp', 'packets_sent', 'packets_received'], name, value)


                                class ProbeValues(Entity):
                                    """
                                    Probe values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe.ProbeValues, self).__init__()

                                        self.yang_name = "probe-values"
                                        self.yang_parent_name = "last-probe"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "probe-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastProbes.InterfaceLastProbe.LastProbe.ProbeValues, ['average', 'minimum', 'maximum', 'variance'], name, value)


                    class InterfaceLastAdvertisements(Entity):
                        """
                        Table of last advertisements
                        
                        .. attribute:: interface_last_advertisement
                        
                        	Last advertisement information
                        	**type**\: list of  		 :py:class:`InterfaceLastAdvertisement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement>`
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements, self).__init__()

                            self.yang_name = "interface-last-advertisements"
                            self.yang_parent_name = "interface-delay"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([("interface-last-advertisement", ("interface_last_advertisement", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement))])
                            self._leafs = OrderedDict()

                            self.interface_last_advertisement = YList(self)
                            self._segment_path = lambda: "interface-last-advertisements"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements, [], name, value)


                        class InterfaceLastAdvertisement(Entity):
                            """
                            Last advertisement information
                            
                            .. attribute:: interface_name  (key)
                            
                            	Interface name
                            	**type**\: str
                            
                            	**pattern:** [a\-zA\-Z0\-9.\_/\-]+
                            
                            .. attribute:: last_advertisement
                            
                            	Last advertisement
                            	**type**\:  :py:class:`LastAdvertisement <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement>`
                            
                            

                            """

                            _prefix = 'perf-meas-oper'
                            _revision = '2017-10-17'

                            def __init__(self):
                                super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement, self).__init__()

                                self.yang_name = "interface-last-advertisement"
                                self.yang_parent_name = "interface-last-advertisements"
                                self.is_top_level_class = False
                                self.has_list_ancestor = True
                                self.ylist_key_names = ['interface_name']
                                self._child_classes = OrderedDict([("last-advertisement", ("last_advertisement", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement))])
                                self._leafs = OrderedDict([
                                    ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                                ])
                                self.interface_name = None

                                self.last_advertisement = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement()
                                self.last_advertisement.parent = self
                                self._children_name_map["last_advertisement"] = "last-advertisement"
                                self._segment_path = lambda: "interface-last-advertisement" + "[interface-name='" + str(self.interface_name) + "']"
                                self._is_frozen = True

                            def __setattr__(self, name, value):
                                self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement, ['interface_name'], name, value)


                            class LastAdvertisement(Entity):
                                """
                                Last advertisement
                                
                                .. attribute:: advertised_values
                                
                                	Advertised values
                                	**type**\:  :py:class:`AdvertisedValues <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement.AdvertisedValues>`
                                
                                .. attribute:: time_of_advertisement
                                
                                	Time of the advertisement (milliseconds since Jan. 1, 1970)
                                	**type**\: int
                                
                                	**range:** 0..18446744073709551615
                                
                                	**units**\: millisecond
                                
                                .. attribute:: advertisement_reason
                                
                                	Reason for advertisement
                                	**type**\:  :py:class:`PmAdvertReason <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PmAdvertReason>`
                                
                                

                                """

                                _prefix = 'perf-meas-oper'
                                _revision = '2017-10-17'

                                def __init__(self):
                                    super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement, self).__init__()

                                    self.yang_name = "last-advertisement"
                                    self.yang_parent_name = "interface-last-advertisement"
                                    self.is_top_level_class = False
                                    self.has_list_ancestor = True
                                    self.ylist_key_names = []
                                    self._child_classes = OrderedDict([("advertised-values", ("advertised_values", PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement.AdvertisedValues))])
                                    self._leafs = OrderedDict([
                                        ('time_of_advertisement', (YLeaf(YType.uint64, 'time-of-advertisement'), ['int'])),
                                        ('advertisement_reason', (YLeaf(YType.enumeration, 'advertisement-reason'), [('ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper', 'PmAdvertReason', '')])),
                                    ])
                                    self.time_of_advertisement = None
                                    self.advertisement_reason = None

                                    self.advertised_values = PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement.AdvertisedValues()
                                    self.advertised_values.parent = self
                                    self._children_name_map["advertised_values"] = "advertised-values"
                                    self._segment_path = lambda: "last-advertisement"
                                    self._is_frozen = True

                                def __setattr__(self, name, value):
                                    self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement, ['time_of_advertisement', 'advertisement_reason'], name, value)


                                class AdvertisedValues(Entity):
                                    """
                                    Advertised values
                                    
                                    .. attribute:: average
                                    
                                    	Average value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: minimum
                                    
                                    	Minimum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: maximum
                                    
                                    	Maximum value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    .. attribute:: variance
                                    
                                    	Variance value (uSec)
                                    	**type**\: int
                                    
                                    	**range:** 0..4294967295
                                    
                                    

                                    """

                                    _prefix = 'perf-meas-oper'
                                    _revision = '2017-10-17'

                                    def __init__(self):
                                        super(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement.AdvertisedValues, self).__init__()

                                        self.yang_name = "advertised-values"
                                        self.yang_parent_name = "last-advertisement"
                                        self.is_top_level_class = False
                                        self.has_list_ancestor = True
                                        self.ylist_key_names = []
                                        self._child_classes = OrderedDict([])
                                        self._leafs = OrderedDict([
                                            ('average', (YLeaf(YType.uint32, 'average'), ['int'])),
                                            ('minimum', (YLeaf(YType.uint32, 'minimum'), ['int'])),
                                            ('maximum', (YLeaf(YType.uint32, 'maximum'), ['int'])),
                                            ('variance', (YLeaf(YType.uint32, 'variance'), ['int'])),
                                        ])
                                        self.average = None
                                        self.minimum = None
                                        self.maximum = None
                                        self.variance = None
                                        self._segment_path = lambda: "advertised-values"
                                        self._is_frozen = True

                                    def __setattr__(self, name, value):
                                        self._perform_setattr(PerformanceMeasurement.Nodes.Node.Interfaces.InterfaceDelay.InterfaceLastAdvertisements.InterfaceLastAdvertisement.LastAdvertisement.AdvertisedValues, ['average', 'minimum', 'maximum', 'variance'], name, value)

    def clone_ptr(self):
        self._top_entity = PerformanceMeasurement()
        return self._top_entity

class PerformanceMeasurementResponder(Entity):
    """
    performance measurement responder
    
    .. attribute:: nodes
    
    	Node table for node\-specific operational data
    	**type**\:  :py:class:`Nodes <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes>`
    
    

    """

    _prefix = 'perf-meas-oper'
    _revision = '2017-10-17'

    def __init__(self):
        super(PerformanceMeasurementResponder, self).__init__()
        self._top_entity = None

        self.yang_name = "performance-measurement-responder"
        self.yang_parent_name = "Cisco-IOS-XR-perf-meas-oper"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("nodes", ("nodes", PerformanceMeasurementResponder.Nodes))])
        self._leafs = OrderedDict()

        self.nodes = PerformanceMeasurementResponder.Nodes()
        self.nodes.parent = self
        self._children_name_map["nodes"] = "nodes"
        self._segment_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement-responder"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(PerformanceMeasurementResponder, [], name, value)


    class Nodes(Entity):
        """
        Node table for node\-specific operational data
        
        .. attribute:: node
        
        	Node\-specific data for a particular node
        	**type**\: list of  		 :py:class:`Node <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node>`
        
        

        """

        _prefix = 'perf-meas-oper'
        _revision = '2017-10-17'

        def __init__(self):
            super(PerformanceMeasurementResponder.Nodes, self).__init__()

            self.yang_name = "nodes"
            self.yang_parent_name = "performance-measurement-responder"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("node", ("node", PerformanceMeasurementResponder.Nodes.Node))])
            self._leafs = OrderedDict()

            self.node = YList(self)
            self._segment_path = lambda: "nodes"
            self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement-responder/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(PerformanceMeasurementResponder.Nodes, [], name, value)


        class Node(Entity):
            """
            Node\-specific data for a particular node
            
            .. attribute:: node  (key)
            
            	Node
            	**type**\: str
            
            	**pattern:** ([a\-zA\-Z0\-9\_]\*\\d+/){1,2}([a\-zA\-Z0\-9\_]\*\\d+)
            
            .. attribute:: summary
            
            	Summary
            	**type**\:  :py:class:`Summary <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node.Summary>`
            
            .. attribute:: interfaces
            
            	Table of interfaces
            	**type**\:  :py:class:`Interfaces <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node.Interfaces>`
            
            

            """

            _prefix = 'perf-meas-oper'
            _revision = '2017-10-17'

            def __init__(self):
                super(PerformanceMeasurementResponder.Nodes.Node, self).__init__()

                self.yang_name = "node"
                self.yang_parent_name = "nodes"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['node']
                self._child_classes = OrderedDict([("summary", ("summary", PerformanceMeasurementResponder.Nodes.Node.Summary)), ("interfaces", ("interfaces", PerformanceMeasurementResponder.Nodes.Node.Interfaces))])
                self._leafs = OrderedDict([
                    ('node', (YLeaf(YType.str, 'node'), ['str'])),
                ])
                self.node = None

                self.summary = PerformanceMeasurementResponder.Nodes.Node.Summary()
                self.summary.parent = self
                self._children_name_map["summary"] = "summary"

                self.interfaces = PerformanceMeasurementResponder.Nodes.Node.Interfaces()
                self.interfaces.parent = self
                self._children_name_map["interfaces"] = "interfaces"
                self._segment_path = lambda: "node" + "[node='" + str(self.node) + "']"
                self._absolute_path = lambda: "Cisco-IOS-XR-perf-meas-oper:performance-measurement-responder/nodes/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node, ['node'], name, value)


            class Summary(Entity):
                """
                Summary
                
                .. attribute:: responder_counters
                
                	Global responder counters
                	**type**\:  :py:class:`ResponderCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node.Summary.ResponderCounters>`
                
                .. attribute:: total_interfaces
                
                	Number of interfaces in the responder cache
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_rate
                
                	Global incoming packet rate
                	**type**\: int
                
                	**range:** 0..4294967295
                
                .. attribute:: packet_rate_high_water_mark
                
                	Global incoming packet rate high water mark
                	**type**\: int
                
                	**range:** 0..4294967295
                
                

                """

                _prefix = 'perf-meas-oper'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurementResponder.Nodes.Node.Summary, self).__init__()

                    self.yang_name = "summary"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("responder-counters", ("responder_counters", PerformanceMeasurementResponder.Nodes.Node.Summary.ResponderCounters))])
                    self._leafs = OrderedDict([
                        ('total_interfaces', (YLeaf(YType.uint32, 'total-interfaces'), ['int'])),
                        ('packet_rate', (YLeaf(YType.uint32, 'packet-rate'), ['int'])),
                        ('packet_rate_high_water_mark', (YLeaf(YType.uint32, 'packet-rate-high-water-mark'), ['int'])),
                    ])
                    self.total_interfaces = None
                    self.packet_rate = None
                    self.packet_rate_high_water_mark = None

                    self.responder_counters = PerformanceMeasurementResponder.Nodes.Node.Summary.ResponderCounters()
                    self.responder_counters.parent = self
                    self._children_name_map["responder_counters"] = "responder-counters"
                    self._segment_path = lambda: "summary"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node.Summary, [u'total_interfaces', u'packet_rate', u'packet_rate_high_water_mark'], name, value)


                class ResponderCounters(Entity):
                    """
                    Global responder counters
                    
                    .. attribute:: reply_packet_sent
                    
                    	Response packets sent
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: reply_packet_sent_error
                    
                    	Response packets sent error
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: query_packet_received
                    
                    	Response packets received
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_urotlv_not_present
                    
                    	Received packet error, URO TLV not present
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_invalid_source_port_number
                    
                    	Received packet error, invalid source port number
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_no_source_address
                    
                    	Received packet error, no source address
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_no_return_path
                    
                    	Received packet error, no return path
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_invalid_querier_control_code
                    
                    	Received packet error, invalid querier control code
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_unsupported_timestamp_format
                    
                    	Received packet error, unsupported timestamp format
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_timestamp_not_available
                    
                    	Received packet error, timestamp not available
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_unsupported_mandatory_tlv
                    
                    	Received packet error, unsupported mandatory TLV
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    .. attribute:: received_packet_error_invalid_packet
                    
                    	Received packet error, invalid packet
                    	**type**\: int
                    
                    	**range:** 0..18446744073709551615
                    
                    

                    """

                    _prefix = 'perf-meas-oper'
                    _revision = '2017-10-17'

                    def __init__(self):
                        super(PerformanceMeasurementResponder.Nodes.Node.Summary.ResponderCounters, self).__init__()

                        self.yang_name = "responder-counters"
                        self.yang_parent_name = "summary"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = []
                        self._child_classes = OrderedDict([])
                        self._leafs = OrderedDict([
                            ('reply_packet_sent', (YLeaf(YType.uint64, 'reply-packet-sent'), ['int'])),
                            ('reply_packet_sent_error', (YLeaf(YType.uint64, 'reply-packet-sent-error'), ['int'])),
                            ('query_packet_received', (YLeaf(YType.uint64, 'query-packet-received'), ['int'])),
                            ('received_packet_error_urotlv_not_present', (YLeaf(YType.uint64, 'received-packet-error-urotlv-not-present'), ['int'])),
                            ('received_packet_error_invalid_source_port_number', (YLeaf(YType.uint64, 'received-packet-error-invalid-source-port-number'), ['int'])),
                            ('received_packet_error_no_source_address', (YLeaf(YType.uint64, 'received-packet-error-no-source-address'), ['int'])),
                            ('received_packet_error_no_return_path', (YLeaf(YType.uint64, 'received-packet-error-no-return-path'), ['int'])),
                            ('received_packet_error_invalid_querier_control_code', (YLeaf(YType.uint64, 'received-packet-error-invalid-querier-control-code'), ['int'])),
                            ('received_packet_error_unsupported_timestamp_format', (YLeaf(YType.uint64, 'received-packet-error-unsupported-timestamp-format'), ['int'])),
                            ('received_packet_error_timestamp_not_available', (YLeaf(YType.uint64, 'received-packet-error-timestamp-not-available'), ['int'])),
                            ('received_packet_error_unsupported_mandatory_tlv', (YLeaf(YType.uint64, 'received-packet-error-unsupported-mandatory-tlv'), ['int'])),
                            ('received_packet_error_invalid_packet', (YLeaf(YType.uint64, 'received-packet-error-invalid-packet'), ['int'])),
                        ])
                        self.reply_packet_sent = None
                        self.reply_packet_sent_error = None
                        self.query_packet_received = None
                        self.received_packet_error_urotlv_not_present = None
                        self.received_packet_error_invalid_source_port_number = None
                        self.received_packet_error_no_source_address = None
                        self.received_packet_error_no_return_path = None
                        self.received_packet_error_invalid_querier_control_code = None
                        self.received_packet_error_unsupported_timestamp_format = None
                        self.received_packet_error_timestamp_not_available = None
                        self.received_packet_error_unsupported_mandatory_tlv = None
                        self.received_packet_error_invalid_packet = None
                        self._segment_path = lambda: "responder-counters"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node.Summary.ResponderCounters, [u'reply_packet_sent', u'reply_packet_sent_error', u'query_packet_received', u'received_packet_error_urotlv_not_present', u'received_packet_error_invalid_source_port_number', u'received_packet_error_no_source_address', u'received_packet_error_no_return_path', u'received_packet_error_invalid_querier_control_code', u'received_packet_error_unsupported_timestamp_format', u'received_packet_error_timestamp_not_available', u'received_packet_error_unsupported_mandatory_tlv', u'received_packet_error_invalid_packet'], name, value)


            class Interfaces(Entity):
                """
                Table of interfaces
                
                .. attribute:: interface
                
                	Interface information
                	**type**\: list of  		 :py:class:`Interface <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface>`
                
                

                """

                _prefix = 'perf-meas-oper'
                _revision = '2017-10-17'

                def __init__(self):
                    super(PerformanceMeasurementResponder.Nodes.Node.Interfaces, self).__init__()

                    self.yang_name = "interfaces"
                    self.yang_parent_name = "node"
                    self.is_top_level_class = False
                    self.has_list_ancestor = True
                    self.ylist_key_names = []
                    self._child_classes = OrderedDict([("interface", ("interface", PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface))])
                    self._leafs = OrderedDict()

                    self.interface = YList(self)
                    self._segment_path = lambda: "interfaces"
                    self._is_frozen = True

                def __setattr__(self, name, value):
                    self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node.Interfaces, [], name, value)


                class Interface(Entity):
                    """
                    Interface information
                    
                    .. attribute:: interface_name  (key)
                    
                    	Interface name
                    	**type**\: str
                    
                    	**pattern:** [\\w\\\-\\.\:,\_@#%$\\+=\\\|;]+
                    
                    .. attribute:: interface_counters
                    
                    	Per interface responder counters
                    	**type**\:  :py:class:`InterfaceCounters <ydk.models.cisco_ios_xr.Cisco_IOS_XR_perf_meas_oper.PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface.InterfaceCounters>`
                    
                    .. attribute:: interface_name_xr
                    
                    	Interface name
                    	**type**\: str
                    
                    .. attribute:: interface_handle
                    
                    	Interface handle
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: source_address
                    
                    	Source Address
                    	**type**\: str
                    
                    	**pattern:** (([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])\\.){3}([0\-9]\|[1\-9][0\-9]\|1[0\-9][0\-9]\|2[0\-4][0\-9]\|25[0\-5])(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: source_v6_address
                    
                    	Source V6 Address
                    	**type**\: str
                    
                    	**pattern:** ((\:\|[0\-9a\-fA\-F]{0,4})\:)([0\-9a\-fA\-F]{0,4}\:){0,5}((([0\-9a\-fA\-F]{0,4}\:)?(\:\|[0\-9a\-fA\-F]{0,4}))\|(((25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])\\.){3}(25[0\-5]\|2[0\-4][0\-9]\|[01]?[0\-9]?[0\-9])))(%[\\p{N}\\p{L}]+)?
                    
                    .. attribute:: packet_rate
                    
                    	Incoming packet rate
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: packet_rate_high_water_mark
                    
                    	Incoming packet rate high water mark
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    .. attribute:: cleanup_time_remaining
                    
                    	Seconds until an inactive interface is cleaned up
                    	**type**\: int
                    
                    	**range:** 0..4294967295
                    
                    	**units**\: second
                    
                    

                    """

                    _prefix = 'perf-meas-oper'
                    _revision = '2017-10-17'

                    def __init__(self):
                        super(PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface, self).__init__()

                        self.yang_name = "interface"
                        self.yang_parent_name = "interfaces"
                        self.is_top_level_class = False
                        self.has_list_ancestor = True
                        self.ylist_key_names = ['interface_name']
                        self._child_classes = OrderedDict([("interface-counters", ("interface_counters", PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface.InterfaceCounters))])
                        self._leafs = OrderedDict([
                            ('interface_name', (YLeaf(YType.str, 'interface-name'), ['str'])),
                            ('interface_name_xr', (YLeaf(YType.str, 'interface-name-xr'), ['str'])),
                            ('interface_handle', (YLeaf(YType.uint32, 'interface-handle'), ['int'])),
                            ('source_address', (YLeaf(YType.str, 'source-address'), ['str'])),
                            ('source_v6_address', (YLeaf(YType.str, 'source-v6-address'), ['str'])),
                            ('packet_rate', (YLeaf(YType.uint32, 'packet-rate'), ['int'])),
                            ('packet_rate_high_water_mark', (YLeaf(YType.uint32, 'packet-rate-high-water-mark'), ['int'])),
                            ('cleanup_time_remaining', (YLeaf(YType.uint32, 'cleanup-time-remaining'), ['int'])),
                        ])
                        self.interface_name = None
                        self.interface_name_xr = None
                        self.interface_handle = None
                        self.source_address = None
                        self.source_v6_address = None
                        self.packet_rate = None
                        self.packet_rate_high_water_mark = None
                        self.cleanup_time_remaining = None

                        self.interface_counters = PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface.InterfaceCounters()
                        self.interface_counters.parent = self
                        self._children_name_map["interface_counters"] = "interface-counters"
                        self._segment_path = lambda: "interface" + "[interface-name='" + str(self.interface_name) + "']"
                        self._is_frozen = True

                    def __setattr__(self, name, value):
                        self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface, ['interface_name', u'interface_name_xr', u'interface_handle', u'source_address', u'source_v6_address', u'packet_rate', u'packet_rate_high_water_mark', u'cleanup_time_remaining'], name, value)


                    class InterfaceCounters(Entity):
                        """
                        Per interface responder counters
                        
                        .. attribute:: reply_packet_sent
                        
                        	Response packets sent
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: reply_packet_sent_error
                        
                        	Response packets sent error
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: query_packet_received
                        
                        	Response packets received
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_urotlv_not_present
                        
                        	Received packet error, URO TLV not present
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_invalid_source_port_number
                        
                        	Received packet error, invalid source port number
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_no_source_address
                        
                        	Received packet error, no source address
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_no_return_path
                        
                        	Received packet error, no return path
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_invalid_querier_control_code
                        
                        	Received packet error, invalid querier control code
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_unsupported_timestamp_format
                        
                        	Received packet error, unsupported timestamp format
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_timestamp_not_available
                        
                        	Received packet error, timestamp not available
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_unsupported_mandatory_tlv
                        
                        	Received packet error, unsupported mandatory TLV
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        .. attribute:: received_packet_error_invalid_packet
                        
                        	Received packet error, invalid packet
                        	**type**\: int
                        
                        	**range:** 0..18446744073709551615
                        
                        

                        """

                        _prefix = 'perf-meas-oper'
                        _revision = '2017-10-17'

                        def __init__(self):
                            super(PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface.InterfaceCounters, self).__init__()

                            self.yang_name = "interface-counters"
                            self.yang_parent_name = "interface"
                            self.is_top_level_class = False
                            self.has_list_ancestor = True
                            self.ylist_key_names = []
                            self._child_classes = OrderedDict([])
                            self._leafs = OrderedDict([
                                ('reply_packet_sent', (YLeaf(YType.uint64, 'reply-packet-sent'), ['int'])),
                                ('reply_packet_sent_error', (YLeaf(YType.uint64, 'reply-packet-sent-error'), ['int'])),
                                ('query_packet_received', (YLeaf(YType.uint64, 'query-packet-received'), ['int'])),
                                ('received_packet_error_urotlv_not_present', (YLeaf(YType.uint64, 'received-packet-error-urotlv-not-present'), ['int'])),
                                ('received_packet_error_invalid_source_port_number', (YLeaf(YType.uint64, 'received-packet-error-invalid-source-port-number'), ['int'])),
                                ('received_packet_error_no_source_address', (YLeaf(YType.uint64, 'received-packet-error-no-source-address'), ['int'])),
                                ('received_packet_error_no_return_path', (YLeaf(YType.uint64, 'received-packet-error-no-return-path'), ['int'])),
                                ('received_packet_error_invalid_querier_control_code', (YLeaf(YType.uint64, 'received-packet-error-invalid-querier-control-code'), ['int'])),
                                ('received_packet_error_unsupported_timestamp_format', (YLeaf(YType.uint64, 'received-packet-error-unsupported-timestamp-format'), ['int'])),
                                ('received_packet_error_timestamp_not_available', (YLeaf(YType.uint64, 'received-packet-error-timestamp-not-available'), ['int'])),
                                ('received_packet_error_unsupported_mandatory_tlv', (YLeaf(YType.uint64, 'received-packet-error-unsupported-mandatory-tlv'), ['int'])),
                                ('received_packet_error_invalid_packet', (YLeaf(YType.uint64, 'received-packet-error-invalid-packet'), ['int'])),
                            ])
                            self.reply_packet_sent = None
                            self.reply_packet_sent_error = None
                            self.query_packet_received = None
                            self.received_packet_error_urotlv_not_present = None
                            self.received_packet_error_invalid_source_port_number = None
                            self.received_packet_error_no_source_address = None
                            self.received_packet_error_no_return_path = None
                            self.received_packet_error_invalid_querier_control_code = None
                            self.received_packet_error_unsupported_timestamp_format = None
                            self.received_packet_error_timestamp_not_available = None
                            self.received_packet_error_unsupported_mandatory_tlv = None
                            self.received_packet_error_invalid_packet = None
                            self._segment_path = lambda: "interface-counters"
                            self._is_frozen = True

                        def __setattr__(self, name, value):
                            self._perform_setattr(PerformanceMeasurementResponder.Nodes.Node.Interfaces.Interface.InterfaceCounters, [u'reply_packet_sent', u'reply_packet_sent_error', u'query_packet_received', u'received_packet_error_urotlv_not_present', u'received_packet_error_invalid_source_port_number', u'received_packet_error_no_source_address', u'received_packet_error_no_return_path', u'received_packet_error_invalid_querier_control_code', u'received_packet_error_unsupported_timestamp_format', u'received_packet_error_timestamp_not_available', u'received_packet_error_unsupported_mandatory_tlv', u'received_packet_error_invalid_packet'], name, value)

    def clone_ptr(self):
        self._top_entity = PerformanceMeasurementResponder()
        return self._top_entity

